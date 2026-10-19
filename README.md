# MediCore Urgent Pro

![Testes](https://github.com/filipemangerona2/medicore/actions/workflows/testes.yml/badge.svg)

Protótipo em Python/Streamlit para consulta rápida em urgência: guia de fármacos,
calculadoras e fluxogramas, com fonte rastreável em cada informação clínica.

> ⚠️ **Todo o conteúdo está PENDENTE DE REVISÃO CLÍNICA.** Não use para prescrição nem para
> decisão assistencial. Confira sempre a bula vigente e o protocolo da sua instituição.

Aplicativo publicado: https://medicore-pro.streamlit.app/

## Situação após a auditoria de 19/10/2026

- **Recuperado:** 8 fármacos (noradrenalina, adrenalina, amiodarona, ceftriaxona, meropeném,
  cetamina/escetamina, fentanil, midazolam), 6 fluxogramas (PCR, intubação em sequência rápida,
  crise hipertensiva, anafilaxia, sepse, ABCDE) e 5 calculadoras (infusão, clearance de
  creatinina, superfície corporal, queimados, potássio). A antiga aba "RAG", que era simulada,
  virou uma busca real no conteúdo.
- **Critérios de liberação:** nada está VALIDADO (falta revisão de profissional habilitado).
  Itens conferidos com fonte estão PENDENTES; trechos sem fonte verificável ou com risco estão
  BLOQUEADOS e não aparecem como orientação.
- **Relatório completo:** [docs/AUDITORIA.md](docs/AUDITORIA.md) — texto original de cada
  módulo, cada correção com motivo e fonte, trechos bloqueados, pendências e todas as
  referências com o nível de acesso real a cada uma.
- **Versões antigas:** preservadas em [legado/](legado/) e na branch
  `backup/pre-auditoria-2026-10-19`.

## Estrutura

```
app.py                      ponto de entrada (só monta a página)
medicore/
  calculos.py               calculadoras como funções puras, com validação de unidades e limites
  unidades.py, formatacao.py conversões (massas molares) e números no padrão brasileiro
  farmacos.py               guia de fármacos (texto revisado + original + alterações + bloqueios)
  fluxogramas.py            fluxogramas (mesma estrutura)
  calculadoras_info.py      fórmula, fontes e histórico de cada calculadora
  referencias.py            registro de todas as fontes consultadas
  status.py                 critérios VALIDADO / PENDENTE / BLOQUEADO
  busca.py                  busca textual no conteúdo
  auditoria.py, relatorio.py registro da auditoria e gerador de docs/AUDITORIA.md
  ui/                       telas Streamlit (sem lógica clínica)
tests/                      testes automatizados (cálculos, conteúdo, busca e interface)
legado/                     versões anteriores, só para consulta
.streamlit/config.toml      tema escuro
.github/workflows/          testes automáticos no GitHub a cada atualização
```

## Executar no computador

```bash
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Testes

```bash
pip install -r requirements.txt -r requirements-dev.txt
pytest
```

Os testes também rodam sozinhos no GitHub (aba **Actions**) a cada atualização, em Python 3.11,
3.12 e 3.13, incluindo a execução real do app com o Streamlit e a subida do servidor.

## Publicar no Streamlit Community Cloud

Configuração do app: repositório `filipemangerona2/medicore`, branch `main`, arquivo principal
`app.py`. Cada atualização da branch `main` é publicada automaticamente; se o app não
atualizar, use **Manage app → Reboot app**.

## Como um profissional valida um conteúdo

1. Revise o módulo e as fontes em `docs/AUDITORIA.md`, resolvendo as pendências listadas.
2. No arquivo do módulo (ex.: `medicore/farmacos.py`), mude `status=Status.PENDENTE` para
   `status=Status.VALIDADO` e preencha
   `revisao=RevisaoClinica(revisor="Nome", registro_profissional="CRM-UF 0000", data="AAAA-MM-DD")`.
3. Gere o relatório (`python -m medicore.relatorio`) e rode `pytest`. Os testes recusam
   conteúdo VALIDADO sem revisão completa e qualquer informação clínica sem fonte registrada.
