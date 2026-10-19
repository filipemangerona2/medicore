"""Gera docs/AUDITORIA.md a partir dos próprios dados do aplicativo.

Uso:  python -m medicore.relatorio

O relatório é derivado do código (fonte única): um teste automatizado falha se o arquivo
em docs/ estiver desatualizado em relação ao conteúdo do aplicativo.
"""

from __future__ import annotations

from pathlib import Path

from . import DATA_AUDITORIA, __version__
from .auditoria import FONTES_NAO_ACESSADAS, LIMITACOES, PROBLEMAS_TECNICOS
from .calculadoras_info import CALCULADORAS
from .farmacos import FARMACOS
from .fluxogramas import FLUXOGRAMAS
from .referencias import REFERENCIAS, rotulo
from .status import DESCRICAO_STATUS, Status, rotulo_status

CAMINHO = Path(__file__).resolve().parent.parent / "docs" / "AUDITORIA.md"


def _celula(texto: str) -> str:
    return str(texto).replace("|", "\\|").replace("\n", " ").strip() or "—"


def _tabela(cabecalho: tuple[str, ...], linhas: list[tuple]) -> list[str]:
    saida = ["| " + " | ".join(cabecalho) + " |", "|" + "|".join("---" for _ in cabecalho) + "|"]
    for linha in linhas:
        saida.append("| " + " | ".join(_celula(c) for c in linha) + " |")
    return saida


def _fontes(ids) -> str:
    return "; ".join(rotulo(i) for i in ids) if ids else "—"


def _bloco_modulo(modulo, original_como_tabela: bool) -> list[str]:
    linhas: list[str] = [f"**Status:** {rotulo_status(modulo.status)}", ""]
    linhas.append(f"**Texto original preservado** ({modulo.origem_original}):")
    linhas.append("")
    if original_como_tabela:
        linhas += _tabela(("Campo", "Texto original"), list(modulo.original.items()))
    else:
        linhas.append(f"> {_celula(modulo.original)}")
    linhas.append("")
    if modulo.alteracoes:
        linhas.append("**Problemas encontrados e correções:**")
        linhas.append("")
        linhas += _tabela(
            ("Campo", "Antes", "Depois", "Motivo", "Fontes"),
            [(a.campo, a.antes, a.depois, a.motivo, _fontes(a.refs)) for a in modulo.alteracoes],
        )
        linhas.append("")
    if modulo.bloqueados:
        linhas.append("**Trechos BLOQUEADOS (não exibidos como orientação no aplicativo):**")
        linhas.append("")
        linhas += _tabela(
            ("Trecho", "Texto original", "Origem", "Motivo"),
            [(b.titulo, b.texto_original, b.origem, b.motivo) for b in modulo.bloqueados],
        )
        linhas.append("")
    if getattr(modulo, "divergencias", ()):
        linhas.append("**Divergências entre fontes e escolha adotada:**")
        linhas.append("")
        linhas += [f"- {d}" for d in modulo.divergencias]
        linhas.append("")
    if modulo.pendencias:
        linhas.append("**Pendências que exigem revisão humana:**")
        linhas.append("")
        linhas += [f"- [ ] {p}" for p in modulo.pendencias]
        linhas.append("")
    return linhas


def gerar_relatorio() -> str:
    modulos = list(FARMACOS) + list(FLUXOGRAMAS)
    total_itens = sum(len(m.itens()) for m in modulos)
    total_bloq = sum(len(m.bloqueados) for m in modulos) + sum(len(c.bloqueados) for c in CALCULADORAS)
    total_pend = sum(len(m.pendencias) for m in modulos) + sum(len(c.pendencias) for c in CALCULADORAS)
    validados = sum(1 for m in modulos + list(CALCULADORAS) if m.status is Status.VALIDADO)

    l: list[str] = [
        "# Relatório de auditoria — MediCore Urgent Pro",
        "",
        "> Gerado automaticamente a partir do código (`python -m medicore.relatorio`). Não edite à mão: altere o "
        "conteúdo em `medicore/` e gere de novo.",
        "",
        f"- **Data da auditoria:** {DATA_AUDITORIA} · **Versão do app:** {__version__}",
        f"- **Módulos:** {len(FARMACOS)} fármacos, {len(FLUXOGRAMAS)} fluxogramas, {len(CALCULADORAS)} calculadoras",
        f"- **Itens clínicos com fonte rastreável:** {total_itens}",
        f"- **VALIDADOS:** {validados} · **Trechos BLOQUEADOS:** {total_bloq} · **Pendências para revisão humana:** {total_pend}",
        f"- **Fontes registradas:** {len(REFERENCIAS)}",
        "",
        "## Critérios de liberação",
        "",
    ]
    l += [f"- **{rotulo_status(s)}** — {DESCRICAO_STATUS[s]}" for s in Status]
    l += [
        "",
        "Conteúdo recuperado nunca vira VALIDADO automaticamente: o status exige um registro de revisão clínica "
        "(`RevisaoClinica`: revisor, registro profissional e data), conferido pelos testes automatizados.",
        "",
        "## Limitações desta auditoria",
        "",
    ]
    l += [f"- {texto}" for texto in LIMITACOES]
    l += ["", "## Problemas técnicos corrigidos", ""]
    l += _tabela(("Problema", "Onde", "Correção"), [(p.problema, p.onde, p.correcao) for p in PROBLEMAS_TECNICOS])
    l += ["", "## Resumo por módulo", ""]
    resumo = [("Fármaco", f.nome, rotulo_status(f.status), len(f.itens()), len(f.bloqueados), len(f.pendencias)) for f in FARMACOS]
    resumo += [("Fluxograma", f.titulo, rotulo_status(f.status), len(f.itens()), len(f.bloqueados), len(f.pendencias)) for f in FLUXOGRAMAS]
    resumo += [("Calculadora", c.titulo, rotulo_status(c.status), "—", len(c.bloqueados), len(c.pendencias)) for c in CALCULADORAS]
    l += _tabela(("Tipo", "Módulo", "Status", "Itens com fonte", "Bloqueados", "Pendências"), resumo)

    l += ["", "## Fármacos", ""]
    for f in FARMACOS:
        l += [f"### {f.nome}", "", f"*{f.classe}* · fontes: {_fontes(f.referencias_usadas())}", ""]
        l += _bloco_modulo(f, original_como_tabela=True)

    l += ["## Fluxogramas", ""]
    for f in FLUXOGRAMAS:
        l += [f"### {f.titulo}", "", f"Público: {f.publico} · fontes: {_fontes(f.referencias_usadas())}", ""]
        l += _bloco_modulo(f, original_como_tabela=False)

    l += ["## Calculadoras", ""]
    for c in CALCULADORAS:
        l += [
            f"### {c.titulo}",
            "",
            f"**Status:** {rotulo_status(c.status)} · fontes: {_fontes(c.refs)}",
            "",
            f"**Fórmula:** `{c.formula}`",
            "",
            f"**Versão original:** {_celula(c.original)}",
            "",
        ]
        if c.alteracoes:
            l += ["**Problemas encontrados e correções:**", ""]
            l += _tabela(
                ("Campo", "Antes", "Depois", "Motivo", "Fontes"),
                [(a.campo, a.antes, a.depois, a.motivo, _fontes(a.refs)) for a in c.alteracoes],
            )
            l.append("")
        if c.bloqueados:
            l += ["**Trechos BLOQUEADOS:**", ""]
            l += _tabela(("Trecho", "Texto original", "Origem", "Motivo"), [(b.titulo, b.texto_original, b.origem, b.motivo) for b in c.bloqueados])
            l.append("")
        if c.pendencias:
            l += ["**Pendências que exigem revisão humana:**", ""]
            l += [f"- [ ] {p}" for p in c.pendencias]
            l.append("")

    l += [
        "## Testes automatizados",
        "",
        "Executar: `pip install -r requirements.txt -r requirements-dev.txt` e depois `pytest`.",
        "",
        "- `tests/test_calculos_*.py` — cada fórmula com valores de referência calculados de forma independente "
        "(inclusive exemplos das próprias bulas e rótulos), limites mínimos e máximos, valores intermediários, ida e "
        "volta aleatória com semente fixa e entradas inválidas (zero, negativos, NaN, infinito, texto, booleanos, "
        "unidades incompatíveis).",
        "- `tests/test_unidades_e_formatacao.py` — fatores de conversão derivados de massas molares e formatação pt-BR.",
        "- `tests/test_conteudo.py` — toda informação clínica tem fonte registrada; nada VALIDADO sem revisão clínica; "
        "texto original preservado campo a campo e comparado com a versão de 281 linhas; nada bloqueado aparece no texto exibido.",
        "- `tests/test_busca.py` — busca real, acentos, consultas vazias ou malformadas, ausência de pontuação inventada.",
        "- `tests/test_app.py` — executa o `app.py` com o Streamlit real (AppTest): inicialização, declaração de ciência, "
        "todos os fármacos e fluxogramas, cada calculadora com valores conferidos, mensagens de erro e ausência de "
        "conteúdo bloqueado na tela.",
        "- `tests/test_relatorio.py` — este relatório precisa estar sincronizado com o código.",
        "",
        "## Referências consultadas",
        "",
    ]
    l += _tabela(
        ("Rótulo", "Instituição", "Título", "Ano", "Versão", "DOI", "Seção", "Acesso", "Link"),
        [
            (rotulo(r.id), r.instituicao, r.titulo, r.ano, r.versao, r.doi or "—", r.secao, r.acesso.value, r.url)
            for r in REFERENCIAS.values()
        ],
    )
    l += ["", "Todas consultadas em 19/10/2026. Observações por fonte:", ""]
    l += [f"- **{rotulo(r.id)}:** {r.observacao}" for r in REFERENCIAS.values() if r.observacao]
    l += ["", "## Fontes procuradas e não acessadas", ""]
    l += [f"- **{fonte}:** {motivo}" for fonte, motivo in FONTES_NAO_ACESSADAS]
    l.append("")
    return "\n".join(l)


def main() -> None:
    CAMINHO.parent.mkdir(parents=True, exist_ok=True)
    CAMINHO.write_text(gerar_relatorio(), encoding="utf-8")
    print(f"Relatório gerado em {CAMINHO}")


if __name__ == "__main__":
    main()
