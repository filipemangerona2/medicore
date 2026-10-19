# Legado — versões anteriores preservadas

Esta pasta guarda, **apenas para consulta**, as versões do MediCore que existiam antes da
auditoria de 19/10/2026. Os arquivos têm extensão `.txt` de propósito: não são executados
pelo Streamlit nem pelos testes.

| Arquivo | Origem | Observação |
|---|---|---|
| `app_original_1292114.txt` | commit `1292114` (281 linhas) | Versão original completa. Não executava: tinha o cabeçalho do e-mail (SyntaxError) e perdeu toda a indentação (IndentationError). As 6 linhas do cabeçalho do e-mail foram omitidas nesta cópia por privacidade. |
| `app_intermediario_b161d85.txt` | commit `b161d85` (125 linhas) | Versão intermediária com Midazolam, fluxograma de sepse e aba de raciocínio clínico. Também sem indentação. |
| `app_esqueleto_35f2e67.txt` | commit `35f2e67` (23 linhas) | Último `app.py` antes da auditoria: executava, mas com quase todas as funções desligadas. |
| `README_do_zip_medicore_corrigido.md` | `medicore_corrigido.zip` | Único conteúdo do .zip que não era cópia idêntica de outro arquivo. O .zip também tinha um `app.py` idêntico ao `35f2e67` e um `.pyc` compilado no ambiente do ChatGPT; o .zip foi removido do repositório. |

Backup integral: a branch `backup/pre-auditoria-2026-10-19` aponta para o estado exato do
repositório antes desta auditoria (commit `97a3063`, que contém o último `app.py` — `35f2e67` —
e a pasta `.devcontainer` adicionada depois).

O texto clínico original de cada fármaco e fluxograma também foi preservado campo a campo em
`medicore/farmacos.py` e `medicore/fluxogramas.py` (atributos `original`), junto com o
registro de cada alteração e o motivo. O relatório completo está em `docs/AUDITORIA.md`.
