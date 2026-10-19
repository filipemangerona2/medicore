"""Busca textual real no conteúdo do aplicativo (substitui a aba 'RAG' simulada).

A versão original devolvia sempre o mesmo texto com uma "relevância" inventada de 99,2%.
Esta busca percorre de fato fármacos, fluxogramas, calculadoras e referências, ignora
acentos e maiúsculas, e informa apenas quantos termos da pergunta foram encontrados.
Trechos bloqueados aparecem só com o motivo do bloqueio, nunca com o texto original.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from functools import lru_cache

from .calculadoras_info import CALCULADORAS
from .farmacos import FARMACOS
from .fluxogramas import FLUXOGRAMAS
from .referencias import REFERENCIAS
from .status import Status

PALAVRAS_VAZIAS = frozenset(
    "a o as os de da do das dos e em no na nos nas um uma para por com sem que se ao aos ou".split()
)
LIMITE_CONSULTA = 200  # caracteres


def normalizar(texto: str) -> str:
    """Minúsculas, sem acentos e só com letras/números separados por espaço."""
    decomposto = unicodedata.normalize("NFKD", texto)
    sem_acento = "".join(c for c in decomposto if not unicodedata.combining(c))
    return re.sub(r"[^0-9a-z]+", " ", sem_acento.lower()).strip()


def termos_da_consulta(consulta: str) -> tuple[str, ...]:
    termos = []
    for termo in normalizar(consulta[:LIMITE_CONSULTA]).split():
        if termo in PALAVRAS_VAZIAS:
            continue
        if len(termo) < 2 and not termo.isdigit():
            continue
        if termo not in termos:
            termos.append(termo)
    return tuple(termos)


@dataclass(frozen=True)
class Documento:
    id: str
    tipo: str  # Fármaco, Fluxograma, Calculadora, Referência, Bloqueado
    titulo: str
    onde: str  # aba onde o conteúdo aparece
    texto: str
    status: Status


@dataclass(frozen=True)
class ResultadoBusca:
    documento: Documento
    termos_encontrados: tuple[str, ...]
    total_termos: int
    trecho: str


@lru_cache(maxsize=1)
def indice() -> tuple[Documento, ...]:
    docs: list[Documento] = []
    for f in FARMACOS:
        for secao in f.secoes:
            texto = " ".join(item.texto for item in secao.itens)
            docs.append(Documento(f"farmaco:{f.id}:{secao.titulo}", "Fármaco", f"{f.nome} — {secao.titulo}", "Fármacos", texto, f.status))
        for alerta in f.alertas_principais:
            docs.append(Documento(f"farmaco:{f.id}:alerta", "Fármaco", f"{f.nome} — alerta", "Fármacos", alerta, f.status))
        for b in f.bloqueados:
            docs.append(
                Documento(f"bloqueado:{f.id}:{b.titulo}", "Bloqueado", f"{f.nome} — {b.titulo}", "Auditoria", b.motivo, Status.BLOQUEADO)
            )
    for fl in FLUXOGRAMAS:
        for etapa in fl.etapas:
            texto = " ".join(item.texto for item in etapa.itens)
            docs.append(Documento(f"fluxo:{fl.id}:{etapa.titulo}", "Fluxograma", f"{fl.titulo} — {etapa.titulo}", "Fluxogramas", texto, fl.status))
        for b in fl.bloqueados:
            docs.append(
                Documento(f"bloqueado:{fl.id}:{b.titulo}", "Bloqueado", f"{fl.titulo} — {b.titulo}", "Auditoria", b.motivo, Status.BLOQUEADO)
            )
    for c in CALCULADORAS:
        docs.append(Documento(f"calc:{c.id}", "Calculadora", c.titulo, "Calculadoras", f"{c.descricao} {c.formula}", c.status))
    for r in REFERENCIAS.values():
        texto = f"{r.instituicao} {r.titulo} {r.ano} {r.versao} {r.secao}"
        docs.append(Documento(f"ref:{r.id}", "Referência", r.titulo, "Auditoria", texto, Status.PENDENTE))
    return tuple(docs)


def _palavras(texto_normalizado: str) -> tuple[str, ...]:
    return tuple(texto_normalizado.split())


def _casa(termo: str, palavras: tuple[str, ...]) -> int:
    """Conta palavras que começam com o termo (busca por prefixo: 'adrenal' acha 'adrenalina')."""
    return sum(1 for p in palavras if p.startswith(termo))


def _trecho(texto: str, termos: tuple[str, ...], tamanho: int = 180) -> str:
    norm = normalizar(texto)
    posicao = -1
    for termo in termos:
        achado = re.search(r"\b" + re.escape(termo), norm)
        if achado:
            posicao = achado.start()
            break
    if posicao <= 0 or len(texto) <= tamanho:
        return texto[:tamanho] + ("…" if len(texto) > tamanho else "")
    # A normalização preserva aproximadamente as posições; recuar um pouco para dar contexto.
    inicio = max(0, posicao - 40)
    fim = min(len(texto), inicio + tamanho)
    return ("…" if inicio > 0 else "") + texto[inicio:fim] + ("…" if fim < len(texto) else "")


def buscar(consulta: str, limite: int = 20) -> tuple[ResultadoBusca, ...]:
    """Retorna documentos que contêm os termos, ordenados por termos encontrados e ocorrências.

    Mostra primeiro os documentos com todos os termos; se nenhum tiver todos, mostra os que
    têm pelo menos um. Nunca inventa pontuação de relevância.
    """
    if not isinstance(consulta, str):
        return ()
    termos = termos_da_consulta(consulta)
    if not termos:
        return ()
    candidatos = []
    for doc in indice():
        palavras_titulo = _palavras(normalizar(doc.titulo))
        palavras_texto = _palavras(normalizar(doc.texto))
        encontrados = []
        ocorrencias = 0
        no_titulo = 0
        for termo in termos:
            n_titulo = _casa(termo, palavras_titulo)
            n_texto = _casa(termo, palavras_texto)
            if n_titulo or n_texto:
                encontrados.append(termo)
                ocorrencias += n_titulo + n_texto
                no_titulo += n_titulo
        if encontrados:
            candidatos.append((len(encontrados), no_titulo, ocorrencias, doc, tuple(encontrados)))
    if not candidatos:
        return ()
    completos = [c for c in candidatos if c[0] == len(termos)]
    escolhidos = completos if completos else candidatos
    # Conteúdo clínico antes de fontes; trechos bloqueados por último.
    prioridade = {"Fármaco": 0, "Fluxograma": 0, "Calculadora": 0, "Referência": 1, "Bloqueado": 2}
    escolhidos.sort(key=lambda c: (-c[0], prioridade.get(c[3].tipo, 1), -c[1], -c[2], c[3].titulo))
    return tuple(
        ResultadoBusca(doc, encontrados, len(termos), _trecho(doc.texto, encontrados))
        for _, _, _, doc, encontrados in escolhidos[: max(1, int(limite))]
    )
