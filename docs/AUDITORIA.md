# Relatório de auditoria — MediCore Urgent Pro

> Gerado automaticamente a partir do código (`python -m medicore.relatorio`). Não edite à mão: altere o conteúdo em `medicore/` e gere de novo.

- **Data da auditoria:** 2026-10-19 · **Versão do app:** 2.0.0
- **Módulos:** 8 fármacos, 6 fluxogramas, 5 calculadoras
- **Itens clínicos com fonte rastreável:** 249
- **VALIDADOS:** 0 · **Trechos BLOQUEADOS:** 28 · **Pendências para revisão humana:** 40
- **Fontes registradas:** 36

## Critérios de liberação

- **🟢 VALIDADO** — Conferido com fontes verificáveis, cálculos testados quando aplicável e revisão clínica concluída por profissional habilitado.
- **🟡 PENDENTE DE REVISÃO CLÍNICA** — Revisado tecnicamente, com fonte rastreável, mas ainda sem aprovação de profissional habilitado. Não usar para decisão assistencial.
- **🔴 BLOQUEADO** — Erro relevante, informação insuficiente ou potencial de dano. Indisponível no aplicativo até correção e aprovação.

Conteúdo recuperado nunca vira VALIDADO automaticamente: o status exige um registro de revisão clínica (`RevisaoClinica`: revisor, registro profissional e data), conferido pelos testes automatizados.

## Limitações desta auditoria

- A auditoria foi feita por um assistente de IA. Não substitui a revisão por profissional habilitado: por isso nada está VALIDADO.
- Só foram usadas fontes efetivamente abertas nesta sessão; o nível de acesso de cada uma está declarado no registro de referências.
- Várias bulas foram lidas em sites de consulta que reproduzem o texto; o Bulário Eletrônico da Anvisa não pôde ser acessado.
- O aplicativo publicado (medicore-pro.streamlit.app) não pôde ser aberto a partir do ambiente da auditoria. A execução foi testada localmente com o Streamlit 1.66.0 montado a partir do código-fonte oficial, e o GitHub Actions repete todos os testes a cada atualização do repositório.

## Problemas técnicos corrigidos

| Problema | Onde | Correção |
|---|---|---|
| Cabeçalho de e-mail colado no código (nome, endereço, horário e 'para mim') → SyntaxError. | commit 1292114, linhas 1-6 | Código reconstruído a partir do conteúdo; cabeçalho omitido da cópia em legado/. |
| Indentação perdida ao copiar e colar → IndentationError. | commits 1292114, 0272b4a, df1ecf4, 030cc1f e b161d85 | Código reescrito em módulos e entregue como arquivos, sem copiar e colar. |
| O Gmail transformou 'st.info' em link (https://www.google.com/url?q=http://st.info...) → SyntaxError. | commit 0272b4a (3 ocorrências) | Eliminado na reconstrução. |
| Funcionalidades apagadas a cada tentativa de correção (281 → 23 linhas). | commits 0272b4a a 35f2e67 | Todas as funcionalidades recuperadas e testadas; textos originais preservados. |
| Arquivo único misturando dados, cálculos e interface; nenhum teste. | app.py | Pacote medicore/ (cálculos puros, conteúdo, fontes, interface) e suíte de testes automatizados. |
| .zip no repositório com cópia idêntica do app.py e um .pyc compilado em outro ambiente. | medicore_corrigido.zip | Removido; o README dele foi preservado em legado/ e o .gitignore impede novos .pyc. |
| Aba 'RAG' simulada: qualquer pergunta devolvia o mesmo texto com 'relevância 99,2%' inventada. | commit 1292114, aba 3 | Substituída por busca textual real no conteúdo do app, sem pontuação inventada. |
| Alegações sem base na interface: 'Validação Automática Ativa', 'Sem Erros', 'Padrão Whitebook revisada'. | commit 1292114 | Removidas; status de cada conteúdo exibido conforme os critérios de liberação. |
| CSS injetado via HTML (unsafe_allow_html) com seletores frágeis. | commit 1292114 | Tema escuro equivalente definido em .streamlit/config.toml, sem HTML injetado. |
| Valores padrão silenciosos (peso 70 kg, creatinina 1,0, concentração 16 mcg/mL) usados nos cálculos. | todas as versões | Campos começam vazios; nenhuma conta é feita com valor presumido. |

## Resumo por módulo

| Tipo | Módulo | Status | Itens com fonte | Bloqueados | Pendências |
|---|---|---|---|---|---|
| Fármaco | Noradrenalina (norepinefrina) | 🟡 PENDENTE DE REVISÃO CLÍNICA | 30 | 3 | 4 |
| Fármaco | Adrenalina (epinefrina) | 🟡 PENDENTE DE REVISÃO CLÍNICA | 19 | 2 | 3 |
| Fármaco | Amiodarona | 🟡 PENDENTE DE REVISÃO CLÍNICA | 22 | 0 | 2 |
| Fármaco | Ceftriaxona | 🟡 PENDENTE DE REVISÃO CLÍNICA | 18 | 2 | 2 |
| Fármaco | Meropeném | 🟡 PENDENTE DE REVISÃO CLÍNICA | 17 | 2 | 2 |
| Fármaco | Cetamina / escetamina | 🟡 PENDENTE DE REVISÃO CLÍNICA | 22 | 2 | 3 |
| Fármaco | Fentanil (fentanila) | 🟡 PENDENTE DE REVISÃO CLÍNICA | 15 | 3 | 2 |
| Fármaco | Midazolam | 🟡 PENDENTE DE REVISÃO CLÍNICA | 17 | 1 | 2 |
| Fluxograma | Parada cardiorrespiratória — adulto (ACLS) | 🟡 PENDENTE DE REVISÃO CLÍNICA | 16 | 2 | 2 |
| Fluxograma | Intubação em sequência rápida — adulto crítico | 🟡 PENDENTE DE REVISÃO CLÍNICA | 18 | 1 | 3 |
| Fluxograma | Pressão arterial muito elevada (crise hipertensiva) | 🟡 PENDENTE DE REVISÃO CLÍNICA | 14 | 2 | 3 |
| Fluxograma | Anafilaxia | 🟡 PENDENTE DE REVISÃO CLÍNICA | 9 | 0 | 2 |
| Fluxograma | Sepse e choque séptico — adulto | 🟡 PENDENTE DE REVISÃO CLÍNICA | 18 | 5 | 3 |
| Fluxograma | Avaliação ABCDE do paciente grave | 🟡 PENDENTE DE REVISÃO CLÍNICA | 14 | 2 | 1 |
| Calculadora | Infusão contínua (vazão em mL/h) | 🟡 PENDENTE DE REVISÃO CLÍNICA | — | 0 | 1 |
| Calculadora | Clearance de creatinina (Cockcroft-Gault) | 🟡 PENDENTE DE REVISÃO CLÍNICA | — | 0 | 1 |
| Calculadora | Superfície corporal (Mosteller e DuBois) | 🟡 PENDENTE DE REVISÃO CLÍNICA | — | 0 | 0 |
| Calculadora | Reposição volêmica no grande queimado | 🟡 PENDENTE DE REVISÃO CLÍNICA | — | 1 | 2 |
| Calculadora | Potássio: classificação e conferência de infusão | 🟡 PENDENTE DE REVISÃO CLÍNICA | — | 0 | 2 |

## Fármacos

### Noradrenalina (norepinefrina)

*Vasopressor — amina simpatomimética* · fontes: Bula noradrenalina; Rótulo FDA noradrenalina; SSC 2026

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA

**Texto original preservado** (commit 1292114 (versão original de 281 linhas)):

| Campo | Texto original |
|---|---|
| classe | Vasoativo / Amina Simpatomimética |
| apresentacao | Ampola 4 mg / 4 mL (1 mg/mL) |
| indicacoes | Choque séptico, cardiogênico ou anafilático refratário a volume; Hipotensão grave (PAM < 65 mmHg). |
| contraindicacoes | Hipotensão decorrente de hipovolemia não corrigida. |
| posologia | Diluir 4 mg a 8 mg em 250 mL de SG 5% ou SF 0,9%. Iniciar com 0,05 a 0,1 mcg/kg/min, titulando conforme PAM. |
| ajuste_renal | Não requer ajuste na insuficiência renal. |
| cuidados | Infusão preferencialmente em Acesso Venoso Central (AVC). Alto risco de necrose por extravasamento periférico. |

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Apresentação | Ampola 4 mg / 4 mL (1 mg/mL) | Ampola de 4 mL = 8 mg de hemitartarato = 4 mg de base; explicitar sempre sal × base | Evitar erro de fator 2 entre sal e base. | Bula noradrenalina |
| Diluente | SG 5% ou SF 0,9% | Glicose 5% (bula); solução salina isolada não recomendada (rótulo norte-americano) | Divergência com as fontes verificadas. | Bula noradrenalina; Rótulo FDA noradrenalina |
| Dose inicial | 0,05 a 0,1 mcg/kg/min | 8 a 12 mcg/min inicial; 2 a 4 mcg/min de manutenção | Única dose verificada é a do rótulo/bula, em mcg/min. | Rótulo FDA noradrenalina; Bula noradrenalina |
| Ajuste renal | Não requer ajuste na insuficiência renal. | A bula não aborda ajuste renal ou hepático | A afirmação original não foi encontrada nas fontes. | Bula noradrenalina |
| Acesso venoso | Infusão preferencialmente em acesso venoso central. | SSC 2026: iniciar por via periférica em vez de atrasar; veia de grosso calibre; vigiar extravasamento | Recomendação atual da SSC 2026 para choque séptico. | SSC 2026; Bula noradrenalina |
| Contraindicações | Hipotensão decorrente de hipovolemia não corrigida. | Lista completa da bula (hipersensibilidade, déficit de volume, trombose mesentérica/periférica, ciclopropano/halotano) | Completar com a bula. | Bula noradrenalina |

**Trechos BLOQUEADOS (não exibidos como orientação no aplicativo):**

| Trecho | Texto original | Origem | Motivo |
|---|---|---|---|
| Dose inicial por peso | Iniciar com 0,05 a 0,1 mcg/kg/min, titulando conforme PAM. | commit 1292114 (versão original de 281 linhas) — posologia | Dose inicial em mcg/kg/min não encontrada nas fontes verificadas (bula e rótulo usam mcg/min). |
| Diluente soro fisiológico isolado | Diluir 4 mg a 8 mg em 250 mL de SG 5% ou SF 0,9%. | commit 1292114 (versão original de 281 linhas) — posologia | O rótulo norte-americano não recomenda solução salina isolada e a bula brasileira cita glicose 5%; a faixa de 4 a 8 mg em 250 mL não consta nas fontes verificadas. |
| Indicações específicas de choque cardiogênico e anafilático | Choque séptico, cardiogênico ou anafilático refratário a volume; Hipotensão grave (PAM < 65 mmHg). | commit 1292114 (versão original de 281 linhas) — indicações | As fontes verificadas citam estados hipotensivos agudos (bula) e choque séptico (SSC 2026); as indicações específicas de choque cardiogênico e anafilático não foram verificadas. |

**Pendências que exigem revisão humana:**

- [ ] Confirmar, na bula do produto padronizado na instituição, se a concentração é expressa em base ou em sal.
- [ ] Definir as concentrações padrão institucionais e, se adotada, a dose inicial por peso (com fonte).
- [ ] Conferir com o fabricante a dose inicial da bula brasileira (inconsistência de unidade).
- [ ] Verificar a bula no Bulário Eletrônico da Anvisa (a consultada é reprodução em site de consulta).

### Adrenalina (epinefrina)

*Agonista adrenérgico — vasopressor, inotrópico e broncodilatador* · fontes: Bula epinefrina; AHA 2025; AHA 2025 — algoritmo; RCUK 2021; WAO 2011; RCUK ABCDE 2024

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA

**Texto original preservado** (commit 1292114 (versão original de 281 linhas)):

| Campo | Texto original |
|---|---|
| classe | Vasoativo / Inotrópico / Broncodilatador |
| apresentacao | Ampola 1 mg / 1 mL (1:1.000) |
| indicacoes | Parada cardiorrespiratória (PCR), Choque Anafilático grave, Asma grave refratária. |
| contraindicacoes | Taquiarritmias ventriculares não tratadas, glaucoma de ângulo fechado. |
| posologia | PCR: 1 mg IV/IO a cada 3-5 minutos. Anafilaxia (IM): 0,01 mg/kg (máx 0,5 mg) na coxa. Infusão: 0,05 - 1 mcg/kg/min. |
| ajuste_renal | Não requer ajuste renal. |
| cuidados | Monitorização rigorosa de ECG e FC; potencial arritmogênico elevado. |

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Anafilaxia (IM) | 0,01 mg/kg (máx 0,5 mg) na coxa; a versão intermediária trazia 0,3 a 0,5 mg IM | Doses por faixa etária (RCUK 2021) e alternativa por peso (WAO), repetição após 5 min | Completar com as fontes; a WAO limita a 0,3 mg na criança pré-púbere. | RCUK 2021; WAO 2011 |
| PCR | 1 mg IV/IO a cada 3-5 minutos | Mantido, com momento por ritmo e preferência do acesso IV (AHA 2025) | Atualização para a AHA 2025. | AHA 2025; AHA 2025 — algoritmo |
| Anafilaxia refratária | (ausente) | Infusão IV em dose baixa conforme RCUK 2021 | Escalonamento previsto na diretriz verificada. | RCUK 2021 |

**Trechos BLOQUEADOS (não exibidos como orientação no aplicativo):**

| Trecho | Texto original | Origem | Motivo |
|---|---|---|---|
| Contraindicações listadas na versão original | Taquiarritmias ventriculares não tratadas, glaucoma de ângulo fechado. | commit 1292114 (versão original de 281 linhas) — contraindicações | Não constam na bula consultada, que considera relativas todas as contraindicações em emergências. |
| Faixa de infusão contínua | Infusão: 0,05 - 1 mcg/kg/min. | commit 1292114 (versão original de 281 linhas) — posologia | Faixa não verificada. O único esquema de infusão verificado é o da anafilaxia refratária (RCUK 2021). |

**Pendências que exigem revisão humana:**

- [ ] Definir protocolo institucional de infusão contínua de adrenalina fora da anafilaxia (com fonte).
- [ ] Verificar a atualização WAO 2020 e diretrizes brasileiras de anafilaxia (não acessadas).
- [ ] Confirmar a bula vigente no Bulário Eletrônico da Anvisa.

### Amiodarona

*Antiarrítmico classe III* · fontes: Bula amiodarona; AHA 2025; AHA 2025 — algoritmo; Rótulo FDA amiodarona

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA

**Texto original preservado** (commit 1292114 (versão original de 281 linhas)):

| Campo | Texto original |
|---|---|
| classe | Antiarrítmico Classe III |
| apresentacao | Ampola 150 mg / 3 mL |
| indicacoes | PCR por FV/TV sem pulso refratária; Taquiarritmias ventriculares e supraventriculares instáveis. |
| contraindicacoes | Choque cardiogênico grave, bradicardia sinusal severa, BAV de alto grau sem marca-passo. |
| posologia | PCR (FV/TV): 300 mg IV em bolus rápido (pode repetir 150 mg após 3-5 min). Manutenção: 1 mg/min por 6h. |
| ajuste_renal | Não requer ajuste renal. |
| cuidados | Risco de hipotensão severa e bradicardia em infusões rápidas fora de parada. |

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Dose na PCR | 300 mg IV em bolus rápido (pode repetir 150 mg após 3-5 min) | 300 mg; segunda dose de 150 mg, no ciclo seguinte do algoritmo (após o 3º choque) | O intervalo de 3-5 min para a 2ª dose não consta no algoritmo AHA 2025. | AHA 2025 — algoritmo |
| Manutenção | Manutenção: 1 mg/min por 6h | Esquemas completos da bula brasileira e do rótulo norte-americano | O texto original estava incompleto (omitia a fase seguinte de 0,5 mg/min por 18 h do esquema norte-americano). | Bula amiodarona; Rótulo FDA amiodarona |
| Contraindicações | Choque cardiogênico grave, bradicardia sinusal severa, BAV de alto grau sem marca-passo. | Lista completa da bula e exceção para FV refratária | Completar com a bula. | Bula amiodarona |

**Pendências que exigem revisão humana:**

- [ ] Definir qual esquema de manutenção (bula brasileira ou rótulo norte-americano) o protocolo institucional adota.
- [ ] Comparar com as diretrizes ERC 2025 e SBC (não comparadas em detalhe nesta revisão).

### Ceftriaxona

*Antibiótico — cefalosporina de 3ª geração* · fontes: Bula ceftriaxona

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA

**Texto original preservado** (commit 1292114 (versão original de 281 linhas)):

| Campo | Texto original |
|---|---|
| classe | Antibiótico / Cefalosporina de 3ª Geração |
| apresentacao | Frasco-ampola 1 g |
| indicacoes | Infecções graves (pneumonia comunitária, sepse, meningite bacteriana, pielonefrite). |
| contraindicacoes | Hipersensibilidade a cefalosporinas/penicilinas; neonatos com hiperbilirrubinemia. |
| posologia | Adultos: 1 g a 2 g IV a cada 12 a 24 horas (máx 4 g/dia). Meningite: 2 g IV de 12/12h. |
| ajuste_renal | Não requer ajuste na insuficiência renal isolada (excreção mista biliar/renal). |
| cuidados | Incompatível com soluções com cálcio (Ringer Lactato) em neonatos. |

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Intervalo | 1 g a 2 g IV a cada 12 a 24 horas (máx 4 g/dia) | 1 a 2 g uma vez ao dia; casos graves até 4 g uma vez ao dia | Conforme a bula. | Bula ceftriaxona |
| Cálcio | Incompatível com soluções com cálcio (Ringer Lactato) em neonatos. | Nunca diluir com cálcio em qualquer idade; em adultos, uso sequencial só com lavagem da linha; em neonatos, contraindicada | A incompatibilidade não se limita aos neonatos. | Bula ceftriaxona |
| Penicilinas | Contraindicação: hipersensibilidade a cefalosporinas/penicilinas | Contraindicada na alergia a cefalosporinas; alergia a penicilinas = maior risco | Conforme a bula consultada. | Bula ceftriaxona |
| Ajuste renal | Não requer ajuste na insuficiência renal isolada (excreção mista biliar/renal). | Sem redução se a função hepática estiver preservada; ClCr < 10 mL/min: até 2 g/dia | Completar com a bula. | Bula ceftriaxona |

**Trechos BLOQUEADOS (não exibidos como orientação no aplicativo):**

| Trecho | Texto original | Origem | Motivo |
|---|---|---|---|
| Dose de meningite em adultos | Meningite: 2 g IV de 12/12h. | commit 1292114 (versão original de 281 linhas) — posologia | Dose para adultos com meningite não consta na bula consultada e a diretriz de meningite não foi acessada. |
| Lista de indicações específicas | Infecções graves (pneumonia comunitária, sepse, meningite bacteriana, pielonefrite). | commit 1292114 (versão original de 281 linhas) — indicações | Lista não conferida na bula acessada, que descreve infecções por microrganismos sensíveis. |

**Pendências que exigem revisão humana:**

- [ ] Definir a dose de meningite em adultos com base em diretriz verificada (ex.: Ministério da Saúde ou sociedade de infectologia).
- [ ] Confirmar a bula vigente no Bulário Eletrônico da Anvisa.

### Meropeném

*Antibiótico — carbapenêmico* · fontes: Bula Meronem; Bula meropeném; SSC 2026

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA

**Texto original preservado** (commit 1292114 (versão original de 281 linhas)):

| Campo | Texto original |
|---|---|
| classe | Antibiótico / Carbapenêmico de Amplo Espectro |
| apresentacao | Frasco-ampola 500 mg e 1 g |
| indicacoes | Infecções graves por multirresistentes, sepse hospitalar, neutropenia febril, meningite. |
| contraindicacoes | Hipersensibilidade severa a carbapenêmicos. |
| posologia | 1 g IV de 8/8 horas (infusão estendida em 3 horas para sepse grave). SNC: 2 g IV de 8/8h. |
| ajuste_renal | Obrigatório ajustar dose se Clearance de Creatinina (ClCr) < 50 mL/min. |
| cuidados | Reduz limiar convulsivo; monitorar pacientes com histórico neurológico. |

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Ajuste renal | Obrigatório ajustar dose se ClCr < 50 mL/min. | Tabela completa da bula (ajuste quando ClCr < 51 mL/min) | Completar com as faixas e doses da bula. | Bula Meronem; Bula meropeném |
| Interações | (ausente) | Ácido valproico/valproato e probenecida: não recomendados | Interações relevantes descritas na bula. | Bula meropeném |
| SNC | SNC: 2 g IV de 8/8h (removido na versão 0272b4a) | Meningite: 2 g a cada 8 h (bula) | Recuperado e confirmado na bula. | Bula Meronem |

**Trechos BLOQUEADOS (não exibidos como orientação no aplicativo):**

| Trecho | Texto original | Origem | Motivo |
|---|---|---|---|
| Duração da infusão estendida | 1 g IV de 8/8 horas (infusão estendida em 3 horas para sepse grave). | commit 1292114 (versão original de 281 linhas) — posologia | A SSC 2026 recomenda infusão prolongada, mas a duração de 3 h não foi verificada nas fontes acessadas. |
| Indicações gerais da versão original | Infecções graves por multirresistentes, sepse hospitalar, neutropenia febril, meningite. | commit 1292114 (versão original de 281 linhas) — indicações | Substituídas pelas indicações com dose descritas na bula; as demais não foram verificadas. |

**Pendências que exigem revisão humana:**

- [ ] Definir a duração da infusão prolongada e a dose de ataque conforme protocolo institucional (com fonte).
- [ ] Confirmar o detentor do registro e a versão da bula do Meronem consultada.

### Cetamina / escetamina

*Anestésico dissociativo* · fontes: Bula Ketamin (escetamina); Bula cetamina; ASRA 2018 (resumo)

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA

**Texto original preservado** (commit 1292114 (versão original de 281 linhas)):

| Campo | Texto original |
|---|---|
| classe | Anestésico / Analgésico Dissociativo |
| apresentacao | Ampola 50 mg / mL (10 mL) |
| indicacoes | Indução em Sequência Rápida de Intubação (SRI), especialmente em asmáticos ou chocados. |
| contraindicacoes | Hipertensão intracraniana grave, aneurismas, eclâmpsia grave, psicose ativa. |
| posologia | Indução SRI: 1,0 a 2,0 mg/kg IV em bolus. Analgesia: 0,2 a 0,5 mg/kg IV. |
| ajuste_renal | Sem alterações farmacocinéticas importantes na insuficiência renal. |
| cuidados | Mantém tônus simpático (aumenta PA/FC), mas pode causar sialorreia e confusão no despertar. |

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Apresentação | Ampola 50 mg / mL (10 mL) | Distinguir escetamina (Ketamin/Ketamin NP) de cetamina | Isômeros diferentes no mercado brasileiro com a mesma concentração rotulada. | Bula Ketamin (escetamina); Bula cetamina |
| Indução para SRI | Indução SRI: 1,0 a 2,0 mg/kg IV em bolus | Faixa de bula 1 a 4,5 mg/kg (média 2 mg/kg), em 60 s | A faixa original está contida na faixa de bula, mas não há fonte verificada específica para SRI. | Bula Ketamin (escetamina); Bula cetamina |

**Trechos BLOQUEADOS (não exibidos como orientação no aplicativo):**

| Trecho | Texto original | Origem | Motivo |
|---|---|---|---|
| Contraindicações da versão original | Hipertensão intracraniana grave, aneurismas, eclâmpsia grave, psicose ativa. | commit 1292114 (versão original de 281 linhas) — contraindicações | Lista não confere com as bulas consultadas (que trazem porfiria, hipertensão, AVC prévio e IC grave). |
| Dose analgésica da versão original | Analgesia: 0,2 a 0,5 mg/kg IV. | commit 1292114 (versão original de 281 linhas) — posologia | Não verificada; o limite de bolus fora de ambiente monitorizado no consenso ASRA é 0,35 mg/kg. |

**Pendências que exigem revisão humana:**

- [ ] Farmacêutico/anestesiologista: confirmar a equivalência de dose entre escetamina e cetamina racêmica para os produtos padronizados.
- [ ] Definir dose para SRI e analgesia com fonte primária verificada.
- [ ] Verificar se a indicação 'asmáticos ou chocados' tem respaldo em diretriz.

### Fentanil (fentanila)

*Analgésico opioide* · fontes: Bula Fentanest; Bula midazolam

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA

**Texto original preservado** (commit 1292114 (versão original de 281 linhas)):

| Campo | Texto original |
|---|---|
| classe | Analgésico Opióide de Ação Rápida |
| apresentacao | Ampola 50 mcg / mL (2 mL ou 10 mL) |
| indicacoes | Analgesia em procedimentos de emergência, indução anestésica, suporte ventilatório em UTI. |
| contraindicacoes | Depressão respiratória aguda sem via aérea garantida. |
| posologia | Analgesia/Intubação: 1 a 3 mcg/kg IV em bolus lento. UTI: 1 a 3 mcg/kg/h. |
| ajuste_renal | Ajustar em insuficiência renal crônica grave pelo acúmulo de metabólitos. |
| cuidados | Risco de rigidez torácica ('tórax lenhoso') se infundido rapidamente em altas doses. |

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Rigidez torácica | Risco de rigidez torácica se infundido rapidamente em altas doses. | Mantido, com conduta da bula (injeção lenta; ventilar e considerar bloqueador neuromuscular) | Confirmado na bula. | Bula Fentanest |

**Trechos BLOQUEADOS (não exibidos como orientação no aplicativo):**

| Trecho | Texto original | Origem | Motivo |
|---|---|---|---|
| Dose para analgesia/intubação | Analgesia/Intubação: 1 a 3 mcg/kg IV em bolus lento. (versão intermediária: 1 a 2 mcg/kg) | commit 1292114 (versão original de 281 linhas) e commit b161d85 (versão intermediária) — posologia | Faixa não encontrada nas fontes verificadas; a bula descreve doses para o contexto anestésico. |
| Infusão em UTI | UTI: 1 a 3 mcg/kg/h. | commit 1292114 (versão original de 281 linhas) — posologia | A bula não aborda infusão contínua em UTI e a diretriz de sedação/analgesia não foi acessada. |
| Ajuste renal por metabólitos | Ajustar em insuficiência renal crônica grave pelo acúmulo de metabólitos. | commit 1292114 (versão original de 281 linhas) — ajuste renal | A justificativa não consta nas fontes verificadas; a bula orienta apenas cautela. |

**Pendências que exigem revisão humana:**

- [ ] Obter bula vigente (a consultada é de 2001) e diretriz de analgesia/sedação em UTI para doses de infusão.
- [ ] Definir doses para analgesia de procedimento e intubação com fonte verificada.

### Midazolam

*Benzodiazepínico — sedativo, hipnótico e amnésico* · fontes: Bula midazolam; AES 2016 (resumo)

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA

**Texto original preservado** (commit b161d85 (versão intermediária)):

| Campo | Texto original |
|---|---|
| classe | Benzodiazepínico sedativo / Hipnótico / Amnésico |
| indicacoes | Sedação para IOT, controle de crise convulsiva refratária. |
| posologia | 0,05 a 0,15 mg/kg IV. |

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Posologia | 0,05 a 0,15 mg/kg IV | Faixa de indução da bula para ≥ 60 anos, críticos ou alto risco (com pré-medicação); tabela completa por faixa | A faixa original corresponde a apenas um subgrupo da bula. | Bula midazolam |

**Trechos BLOQUEADOS (não exibidos como orientação no aplicativo):**

| Trecho | Texto original | Origem | Motivo |
|---|---|---|---|
| Uso em crise convulsiva refratária (dose) | Indicação Principal: Sedação para IOT, controle de crise convulsiva refratária. | commit b161d85 (versão intermediária) — indicação | A indicação aparece na AES 2016 (resumo secundário), mas nenhuma dose para crises foi verificada. |

**Pendências que exigem revisão humana:**

- [ ] Definir doses para crise convulsiva/estado de mal com diretriz primária verificada.
- [ ] Conferir as doses pediátricas na bula impressa (tabelas com células desalinhadas na extração).

## Fluxogramas

### Parada cardiorrespiratória — adulto (ACLS)

Público: Adultos · fontes: AHA 2025 — algoritmo; AHA 2025

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA

**Texto original preservado** (commit 1292114 (versão original) e commit b161d85 (versão intermediária)):

> 1292114: 1. Iniciar RCP de alta qualidade imediata (100-120 bpm). 2. Checar ritmo: Chocável (FV/TV) vs Não Chocável (AESP/Assistolia). 3. Adrenalina 1 mg IV/IO a cada 3-5 minutos. 4. Investigar 5 H's e 5 T's. \| b161d85: 1. Checar Segurança e Responsividade -> Chamar ajuda / Trazer desfibrilador. 2. Iniciar RCP de Alta Qualidade: 100-120 bpm, profundidade 5-6 cm, retorno total do tórax. 3. Checar Ritmo: FV/TV sem pulso: Choque imediato ➔ RCP por 2 min ➔ Adrenalina a cada 3-5 min ➔ Amiodarona no 2º choque. Asistolia/AESP: RCP imediata ➔ Adrenalina precoce ➔ Investigar 5 Hs e 5 Ts.

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Frequência das compressões | 100-120 bpm | 100 a 120 compressões por minuto | 'bpm' (batimentos por minuto) é unidade de frequência cardíaca, não de compressões. | AHA 2025 — algoritmo |
| Sequência do ritmo chocável | Amiodarona no 2º choque | Epinefrina após o 2º choque; amiodarona ou lidocaína após o 3º | Alinhar ao algoritmo AHA 2025. | AHA 2025 — algoritmo |
| Acesso vascular | Adrenalina 1 mg IV/IO | Tentar IV primeiro; IO se o IV falhar ou não for viável | Recomendação AHA 2025 (classe 1). | AHA 2025 |
| Itens novos | (ausentes) | Energia do choque, lidocaína como alternativa, causas reversíveis por extenso e o que não fazer de rotina | Completar o fluxo com o algoritmo e as recomendações AHA 2025. | AHA 2025 — algoritmo; AHA 2025 |

**Trechos BLOQUEADOS (não exibidos como orientação no aplicativo):**

| Trecho | Texto original | Origem | Motivo |
|---|---|---|---|
| Limite superior de profundidade | Iniciar RCP de Alta Qualidade: 100-120 bpm, profundidade 5-6 cm, retorno total do tórax. | commit b161d85 (versão intermediária) | O algoritmo AHA 2025 consultado indica 'pelo menos 5 cm'; o limite superior de 6 cm não foi verificado. |
| Momento da amiodarona | FV / TV sem pulso: Choque imediato ➔ RCP por 2 min ➔ Adrenalina a cada 3-5 min ➔ Amiodarona no 2º choque. | commit b161d85 (versão intermediária) | Contraria o algoritmo AHA 2025: a epinefrina entra após o 2º choque e o antiarrítmico após o 3º. |

**Divergências entre fontes e escolha adotada:**

- Adotada a AHA 2025 como referência principal (base do curso ACLS). A ERC 2025 não foi comparada em detalhe nesta revisão.

**Pendências que exigem revisão humana:**

- [ ] Comparar com as diretrizes ERC 2025 e com a diretriz brasileira de RCP (SBC 2019, a mais recente localizada).
- [ ] Incluir cuidados pós-parada (AHA 2025, Parte 11) após verificação.

### Intubação em sequência rápida — adulto crítico

Público: Adultos · fontes: DAS 2018; SCCM 2023; Bula Ketamin (escetamina); Bula midazolam; DAS 2025 (resumo); AHA 2025 — algoritmo

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA

**Texto original preservado** (commit 1292114 (versão original)):

> 1292114: Os 7 Ps da SRI: Preparo, Pré-oxigenação, Premedicação, Paralisação com Indução (Ex: Cetamina + Rocurônio), Posicionamento, Passagem do Tubo e Pós-intubação.

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Estrutura | 7 Ps (mnemônico sem fonte citada) | Etapas da DAS 2018 para o paciente crítico, com recomendações da SCCM 2023 | Organizar o fluxo por diretrizes verificadas, incluindo o caminho de falha (planos B a D). | DAS 2018; SCCM 2023 |
| Indução | Ex: Cetamina + Rocurônio | Indutor + bloqueador neuromuscular obrigatório; sem diferença entre etomidato e outros indutores; rocurônio ou succinilcolina | Recomendações SCCM 2023. | SCCM 2023 |

**Trechos BLOQUEADOS (não exibidos como orientação no aplicativo):**

| Trecho | Texto original | Origem | Motivo |
|---|---|---|---|
| Pré-medicação como etapa de rotina | Os 7 Ps da SRI: Preparo, Pré-oxigenação, Premedicação, Paralisação com Indução (Ex: Cetamina + Rocurônio), Posicionamento, Passagem do Tubo e Pós-intubação. | commit 1292114 (versão original) | A pré-medicação de rotina não aparece nas fontes verificadas (SCCM 2023, DAS 2018); a etapa foi retirada até revisão. |

**Pendências que exigem revisão humana:**

- [ ] Definir doses de bloqueadores neuromusculares e indutores com bula/diretriz verificada.
- [ ] Ler o texto integral da DAS 2025 e da SCCM 2023 (apenas resumos foram acessados).
- [ ] Verificar recomendações brasileiras (SBA/ABRAMEDE) não consultadas.

### Pressão arterial muito elevada (crise hipertensiva)

Público: Adultos · fontes: ESC 2019; SBC 2025

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA

**Texto original preservado** (commit 1292114 (versão original) e commit b161d85 (versão intermediária)):

> 1292114: Crise Hipertensiva: Distinguir Urgência (sem lesão de órgão-alvo, tratamento oral gradual) de Emergência (com lesão de órgão-alvo aguda, internação em UTI e drogas venosas). \| b161d85: 1. Diferenciar: Urgência Hipertensiva vs. Emergência Hipertensiva (presença de lesão de órgão-alvo aguda). 2. Urgência: Redução gradual da PA ao longo de 24-48h com medicação oral. 3. Emergência: Internação em UTI, monitorização invasiva e uso de drogas vasoativas endovenosas (ex: Nitroprussiato ou Nitroglicerina).

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Terminologia | Urgência × Emergência hipertensiva | Elevação grave sem lesão aguda × emergência hipertensiva (a ESC 2019 desaconselha o termo 'urgência') | Alinhar à fonte verificada. | ESC 2019 |
| Metas | (ausentes) | Metas e prazos por apresentação clínica | Pontos de decisão objetivos. | ESC 2019 |

**Trechos BLOQUEADOS (não exibidos como orientação no aplicativo):**

| Trecho | Texto original | Origem | Motivo |
|---|---|---|---|
| Prazo de redução e monitorização invasiva | Urgência: Redução gradual da PA ao longo de 24-48h com medicação oral. Emergência: Internação em UTI, monitorização invasiva e uso de drogas vasoativas endovenosas (ex: Nitroprussiato ou Nitroglicerina). | commit b161d85 (versão intermediária) | O prazo de 24–48 h e a monitorização invasiva de rotina não constam na fonte verificada; a escolha do fármaco IV depende da apresentação (ver metas). |
| Doses de anti-hipertensivos IV | (não havia doses na versão original) | auditoria | A tabela de doses da fonte verificada tem erros de unidade corrigidos por errata não acessada: nenhuma dose foi incluída. |

**Divergências entre fontes e escolha adotada:**

- A fonte verificada é de 2019; existem diretrizes mais recentes (SBC 2025, ESC 2024, AHA/ACC 2025) cujas seções de crise hipertensiva não foram lidas.
- Na própria fonte, o texto diz que a redução da PA no AVC isquêmico em geral é evitada, enquanto a Tabela 3 prevê redução de 15% se PA > 220/120 mmHg: o revisor clínico deve conciliar.

**Pendências que exigem revisão humana:**

- [ ] PRIORITÁRIO: conciliar com o capítulo 11 da Diretriz Brasileira de Hipertensão Arterial 2025 (SBC/SBH/SBN), que não pôde ser lido.
- [ ] Conferir com as diretrizes ESC 2024 e AHA/ACC 2025, mais recentes que a fonte usada (2019).
- [ ] Definir fármacos IV e doses disponíveis no Brasil com bula vigente.

### Anafilaxia

Público: Adultos e crianças · fontes: RCUK 2021; WAO 2011

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA

**Texto original preservado** (commit 1292114 (versão original)):

> 1292114: Choque Anafilático: Adrenalina IM imediata (0,01 mg/kg, máx 0,5 mg) na coxa anterolateral. Repetir a cada 5-15 min. Acesso venoso calibroso e expansão volêmica com cristaloides.

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Dose de adrenalina | Adrenalina IM imediata (0,01 mg/kg, máx 0,5 mg) na coxa anterolateral | Mantida (WAO) e complementada com doses por idade (RCUK 2021) | A dose por peso tem limite de 0,3 mg na criança pré-púbere. | WAO 2011; RCUK 2021 |
| Repetição | Repetir a cada 5-15 min | Repetir após 5 min se persistirem problemas A/B/C (RCUK); WAO 5 a 15 min | Detalhar o critério de repetição. | RCUK 2021; WAO 2011 |
| Fluidos | Acesso venoso calibroso e expansão volêmica com cristaloides | Volumes de bolus para adultos e crianças (RCUK) | Critério objetivo de volume. | RCUK 2021 |
| Escalonamento | (ausente) | Anafilaxia refratária, papel dos anti-histamínicos/corticoides e observação | Caminho de falha terapêutica. | RCUK 2021 |

**Divergências entre fontes e escolha adotada:**

- Intervalo de repetição: RCUK 5 min × WAO 5 a 15 min. Exibidos os dois; o RCUK é mais recente (2021).

**Pendências que exigem revisão humana:**

- [ ] Conferir a atualização WAO 2020 e o material da ASBAI (não acessados).
- [ ] A RCUK previa revisão da diretriz em maio/2026: confirmar se há versão nova.

### Sepse e choque séptico — adulto

Público: Adultos · fontes: SSC 2026; Rótulo FDA vasopressina

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA

**Texto original preservado** (commit b161d85 (versão intermediária) e commit 1292114 (versão original)):

> b161d85: 1. Reconhecimento Imediato: Avaliar critérios qSOFA ou SOFA e sinais de hipoperfusão (lactato > 2 mmol/L). 2. Coleta de Exames: Lactato sérico, hemoculturas (antes do antibiótico se não atrasar > 45 min), hemograma, função renal, coagulograma. 3. Antibioticoterapia Precoce: Administrar antibiótico de largo espectro na primeira hora. 4. Reposição Volêmica: 30 mL/kg de cristaloide em caso de hipotensão ou lactato ≥ 4. 5. Drogas Vasoativas: Se persistir PAM < 65 mmHg após volume, iniciar Noradrenalina como primeira escolha. \| 1292114 (aba RAG, texto fixo): Critério: PAM < 65 mmHg apesar de volume adequado (30 mL/kg) e Noradrenalina > 0.25 mcg/kg/min. Conduta Imediata: Adicionar Vasopressina (0.04 UI/min fixo) e avaliar corticoterapia de suporte (Hidrocortisona 200 mg/dia).

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Rastreio | qSOFA ou SOFA | NEWS/NEWS2/MEWS ou SIRS, não qSOFA isolado | Recomendação forte da SSC 2026. | SSC 2026 |
| Antimicrobiano | Na primeira hora | 1 h no choque/sepse provável; até 3 h na sepse possível sem choque | Estratificação da SSC 2026. | SSC 2026 |
| Escalonamento | Texto fixo da aba 'RAG' com relevância fictícia de 99,2% | Escalonamento com recomendações SSC 2026 e rótulo da vasopressina | A aba 'RAG' era simulada; o conteúdo foi incorporado a este fluxograma com fontes. | SSC 2026; Rótulo FDA vasopressina |
| Meta de PAM em idosos | (ausente) | 60–65 mmHg a partir de 65 anos | Recomendação nova da SSC 2026. | SSC 2026 |

**Trechos BLOQUEADOS (não exibidos como orientação no aplicativo):**

| Trecho | Texto original | Origem | Motivo |
|---|---|---|---|
| qSOFA como critério de reconhecimento | Reconhecimento Imediato: Avaliar critérios qSOFA ou SOFA e sinais de hipoperfusão (lactato > 2 mmol/L). | commit b161d85 (versão intermediária) | A SSC 2026 recomenda NÃO usar o qSOFA isolado como ferramenta de rastreio; o limiar de lactato > 2 mmol/L não foi verificado. |
| Hemoculturas — limite de tempo | Hemoculturas (antes do antibiótico se não atrasar > 45 min) | commit b161d85 (versão intermediária) | O limite de 45 minutos não foi verificado na SSC 2026, que recomenda coletar o mais cedo possível, idealmente antes do antimicrobiano. |
| Critério de lactato para volume | 30 mL/kg de cristaloide em caso de hipotensão ou lactato ≥ 4. | commit b161d85 (versão intermediária) | A SSC 2026 usa 'hipoperfusão induzida por sepse ou choque séptico'; o limiar de lactato ≥ 4 não foi verificado. |
| Vasopressina em dose fixa e limiar de noradrenalina | PAM < 65 mmHg apesar de volume adequado (30 mL/kg) e Noradrenalina > 0.25 mcg/kg/min: Adicionar Vasopressina (0.04 UI/min fixo). | commit 1292114 — aba 'RAG' (texto fixo) | O limiar de noradrenalina não foi verificado; o rótulo verificado prevê vasopressina titulada a partir de 0,01 UI/min, não dose fixa. |
| Dose de hidrocortisona | Avaliar corticoterapia de suporte (Hidrocortisona 200 mg/dia). | commit 1292114 — aba 'RAG' (texto fixo) | A SSC 2026 sugere corticoide, mas a dose não constava nos trechos verificados. |

**Pendências que exigem revisão humana:**

- [ ] Ler o texto integral da SSC 2026 para dose/critério do corticoide e limiar de noradrenalina para vasopressina.
- [ ] Consultar a bula brasileira de vasopressina.
- [ ] Comparar com protocolos brasileiros (ILAS/AMIB), não consultados.

### Avaliação ABCDE do paciente grave

Público: Adultos · fontes: RCUK ABCDE 2024

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA

**Texto original preservado** (commit b161d85 (versão intermediária)):

> b161d85 (aba Raciocínio Clínico): Avaliação Primária (ABCDE): Vias aéreas, Respiração, Circulação, Incapacidade (neurológica), Exposição. Segurança do Paciente: Checar sempre alergias medicamentosas graves e interações antes de infundir drogas de alta vigilância. Reavaliação Contínua: Resposta hemodinâmica à volemia e drogas vasoativas a cada 5 a 15 minutos em pacientes instáveis.

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Conteúdo | Lista das letras ABCDE | Ações e critérios objetivos por etapa (RCUK) | Critérios objetivos para cada conduta. | RCUK ABCDE 2024 |
| Unidade da glicemia | (ausente) | 4,0 mmol/L convertido para ≈ 72 mg/dL (massa molar da glicose 180,16 g/mol) | O Brasil usa mg/dL. | RCUK ABCDE 2024 |

**Trechos BLOQUEADOS (não exibidos como orientação no aplicativo):**

| Trecho | Texto original | Origem | Motivo |
|---|---|---|---|
| Checagem de alergias e interações | Segurança do Paciente: Checar sempre alergias medicamentosas graves e interações antes de infundir drogas de alta vigilância. | commit b161d85 (versão intermediária) | Orientação sem fonte verificada nesta revisão (não consta no material ABCDE consultado). |
| Intervalo de reavaliação | Reavaliação Contínua: Resposta hemodinâmica à volemia e drogas vasoativas a cada 5 a 15 minutos em pacientes instáveis. | commit b161d85 (versão intermediária) | A fonte verificada indica reavaliar FC e PA a cada 5 minutos durante a prova de volume; o intervalo de 5 a 15 min não foi verificado. |

**Pendências que exigem revisão humana:**

- [ ] Comparar com o ATLS (xABCDE para trauma), não consultado por restrição de licença.

## Calculadoras

### Infusão contínua (vazão em mL/h)

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA · fontes: Bula noradrenalina

**Fórmula:** `vazão (mL/h) = dose por hora na unidade-base ÷ concentração (unidade-base/mL)`

**Versão original:** vazao = (dose_val * peso_kg * 60.0) / 16.0  — concentração fixa de 16 mcg/mL (4 mg/250 mL); a droga escolhida não alterava o cálculo.

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Concentração | Fixa em 16 mcg/mL | Informada pelo usuário (quantidade + volume final, ou valor direto); sem valor padrão | Não existe concentração universal; com 8 mg/250 mL a vazão exibida seria o dobro da correta. | Bula noradrenalina |
| Unidades | Somente mcg/kg/min | mcg/kg/min, mcg/kg/h, mcg/min, mcg/h, mg/kg/min, mg/kg/h, mg/min, mg/h, UI/kg/h, UI/min, UI/h, com bloqueio de combinações incompatíveis | Permitir os fármacos do guia (ex.: amiodarona em mg/min, vasopressina em UI/min). | — |
| Sal × base | (ausente) | Conversor de hemitartarato de norepinefrina para base (8 mg de sal = 4 mg de base, conforme bula) | Evitar erro de fator 2. | Bula noradrenalina |
| Cálculo inverso e passos | (ausente) | Dose a partir da vazão e exibição de cada passo da análise dimensional | Permitir conferência humana do cálculo. | — |

**Pendências que exigem revisão humana:**

- [ ] Definir concentrações padrão institucionais, se desejado, com fonte e aprovação.

### Clearance de creatinina (Cockcroft-Gault)

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA · fontes: Cockcroft-Gault 1976; Bula Meronem; Bula meropeném; Bula ceftriaxona

**Fórmula:** `ClCr (mL/min) = (140 − idade) × peso (kg) ÷ (72 × creatinina em mg/dL); × 0,85 se sexo feminino`

**Versão original:** clcr = max(0, ((140 - idade) * peso * fator_sexo) / (72 * creatinina)); idade de 0 a 120 anos; alerta genérico 'ClCr < 50: ajuste para antimicrobianos'.

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Idade | 0 a 120 anos | 18 a 120 anos, com aviso acima de 92 anos (faixa do estudo original: 18 a 92 anos) | A fórmula foi derivada em adultos. | Cockcroft-Gault 1976 |
| Unidade da creatinina | Somente mg/dL | mg/dL ou µmol/L (1 mg/dL = 88,40 µmol/L), com alerta de unidade provavelmente trocada | Evitar erro de fator 88. | — |
| Alerta renal | ClCr < 50: necessário ajuste para antimicrobianos | Faixas de ajuste das bulas de meropeném e ceftriaxona e orientações de amiodarona, midazolam e fentanil | Substituir o alerta genérico por orientação específica com fonte. | Bula Meronem; Bula meropeném; Bula ceftriaxona; Bula amiodarona; Bula midazolam; Bula Fentanest |

**Pendências que exigem revisão humana:**

- [ ] Definir qual peso usar em obesidade (real, ideal ou ajustado) conforme protocolo institucional.

### Superfície corporal (Mosteller e DuBois)

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA · fontes: Mosteller 1987; DuBois 1916

**Fórmula:** `Mosteller: √(altura cm × peso kg ÷ 3600)  |  DuBois: 0,007184 × peso^0,425 × altura^0,725`

**Versão original:** sc_val = (peso_kg ** 0.425) * (altura_cm ** 0.725) * 0.007184, rotulado como 'Mosteller'.

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Rótulo da fórmula | Fórmula de DuBois rotulada como Mosteller | As duas fórmulas, cada uma com o nome correto | Erro de identificação; os valores diferem até cerca de 6% em obesos. | Mosteller 1987; DuBois 1916 |

### Reposição volêmica no grande queimado

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA · fontes: ABA 2023; MSD Manuals; AAFP 2025 (resumo)

**Fórmula:** `volume 24 h = fator (mL) × peso (kg) × %SCQ; metade nas primeiras 8 h e metade nas 16 h seguintes`

**Versão original:** vol_tot = 4 * peso_kg * pct_scq; metade em 8 h e metade em 16 h; calculava para qualquer %SCQ.

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Fator | Somente 4 mL/kg/%SCQ | 4 mL (Parkland) ou 2 mL (estimativa inicial recomendada pela ABA 2023 para adultos com ≥ 20% SCQ) | A ABA 2023 recomenda iniciar com 2 mL/kg/%SCQ em adultos. | ABA 2023; AAFP 2025 (resumo) |
| Avisos | (ausentes) | Não contar queimaduras superficiais; titular pela resposta clínica; população da ABA | Uso correto da estimativa. | MSD Manuals; ABA 2023 |

**Trechos BLOQUEADOS:**

| Trecho | Texto original | Origem | Motivo |
|---|---|---|---|
| Início da contagem das 8 horas | Primeiras 8h: metade do volume | auditoria | Não foi confirmado em fonte primária acessível se as 8 h contam a partir da queimadura ou da chegada; o aplicativo não ajusta pelo tempo decorrido. |

**Pendências que exigem revisão humana:**

- [ ] Definir o momento zero (queimadura × admissão) e a meta de débito urinário com fonte primária.
- [ ] Definir limiar de %SCQ para reposição formal e regras pediátricas.

### Potássio: classificação e conferência de infusão

**Status:** 🟡 PENDENTE DE REVISÃO CLÍNICA · fontes: NHS SPS 2024; SmPC KCl; UKKA 2026; Bula KCl 19,1%

**Fórmula:** `concentração (mmol/L) = mmol ÷ volume (L); velocidade (mmol/h) = concentração × vazão (mL/h) ÷ 1000`

**Versão original:** K < 3,5: 'Hipocalemia Crítica — periférica máx 10 mEq/h; central 20 mEq/h'; K ≥ 3,5: '✅ Potássio dentro da faixa segura' (inclusive valores de hipercalemia até 7,0).

**Problemas encontrados e correções:**

| Campo | Antes | Depois | Motivo | Fontes |
|---|---|---|---|---|
| Hipercalemia | Qualquer K ≥ 3,5 exibido como 'faixa segura' | Classificação de hipercalemia leve, moderada e grave com condutas de monitorização (UKKA) | Erro grave: falsa tranquilização diante de hipercalemia. | UKKA 2026 |
| Gravidade da hipocalemia | 3,4 mmol/L rotulado como 'crítica' | Leve 3,0–3,4; moderada 2,5–2,9; grave < 2,5 (SPS) | Classificação verificada. | NHS SPS 2024 |
| Velocidade de reposição | Periférica 10 mEq/h; central 20 mEq/h | Usual até 10 mmol/h; até 20 mmol/h na deficiência grave sintomática; > 20 mmol/h só com monitorização (e, pelo SmPC, K < 2 com ECG contínuo); concentração periférica até 40 mmol/L | As fontes definem a velocidade pela gravidade e pela monitorização, não pelo tipo de acesso. | NHS SPS 2024; SmPC KCl |

**Pendências que exigem revisão humana:**

- [ ] Adaptar à concentração de KCl padronizada na instituição (ex.: 19,1% ≈ 2,56 mmol/mL, por cálculo).
- [ ] Incluir protocolo de reposição pediátrica, se desejado, com fonte.

## Testes automatizados

Executar: `pip install -r requirements.txt -r requirements-dev.txt` e depois `pytest`.

- `tests/test_calculos_*.py` — cada fórmula com valores de referência calculados de forma independente (inclusive exemplos das próprias bulas e rótulos), limites mínimos e máximos, valores intermediários, ida e volta aleatória com semente fixa e entradas inválidas (zero, negativos, NaN, infinito, texto, booleanos, unidades incompatíveis).
- `tests/test_unidades_e_formatacao.py` — fatores de conversão derivados de massas molares e formatação pt-BR.
- `tests/test_conteudo.py` — toda informação clínica tem fonte registrada; nada VALIDADO sem revisão clínica; texto original preservado campo a campo e comparado com a versão de 281 linhas; nada bloqueado aparece no texto exibido.
- `tests/test_busca.py` — busca real, acentos, consultas vazias ou malformadas, ausência de pontuação inventada.
- `tests/test_app.py` — executa o `app.py` com o Streamlit real (AppTest): inicialização, declaração de ciência, todos os fármacos e fluxogramas, cada calculadora com valores conferidos, mensagens de erro e ausência de conteúdo bloqueado na tela.
- `tests/test_relatorio.py` — este relatório precisa estar sincronizado com o código.

## Referências consultadas

| Rótulo | Instituição | Título | Ano | Versão | DOI | Seção | Acesso | Link |
|---|---|---|---|---|---|---|---|---|
| AHA 2025 | American Heart Association (AHA) | Part 9: Adult Advanced Life Support — 2025 AHA Guidelines for CPR and ECC | 2025 | Diretrizes AHA 2025 para RCP e ACE (publicadas em Circulation) | 10.1161/CIR.0000000000001376 | Seções 5 (desfibrilação), 9 (acesso vascular), 10 (vasopressores) e 11 (não vasopressores) | documento lido parcialmente | https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-advanced-life-support |
| AHA 2025 — algoritmo | American Heart Association (AHA) | Adult Cardiac Arrest Algorithm — descrição textual | 2025 | Algorithm-ACLS-CA-LngDscrp-250725 | — | Algoritmo completo: qualidade da RCP, energia do choque, fármacos e causas reversíveis | texto integral lido | https://cpr.heart.org/-/media/CPR-Files/CPR-Guidelines-Files/2025-Accessible/Algorithm-ACLS-CA-LngDscrp-250725-Ed.pdf |
| RCUK ABCDE 2024 | Resuscitation Council UK | The ABCDE Approach | 2024 | Publicado em 10/2015, revisado em 05/2021 e atualizado em 07/2024 | — | Princípios e avaliação A, B, C, D e E | texto integral lido | https://resus.org.uk/node/123 |
| SSC 2026 | Society of Critical Care Medicine (SCCM) e European Society of Intensive Care Medicine (ESICM) | Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2026 | 2026 | Prescott HC, Antonelli M, et al. Crit Care Med, publicado em 23/03/2026 | 10.1097/CCM.0000000000007075 | Recomendações de rastreio, lactato, hemoculturas, antimicrobianos, fluidos, PAM, vasopressores, corticoide e betalactâmicos | lista de recomendações lida; texto integral não acessado | https://www.sccm.org/clinical-resources/guidelines/guidelines/surviving-sepsis-campaign-international-guidelines-for-management-of-sepsis-and-septic-shock-2026 |
| Rótulo FDA vasopressina | Par Pharmaceutical — rótulo aprovado pela FDA (EUA) | VASOSTRICT (vasopressin injection) — Prescribing Information | 2023 | Revisão 2/2023 | — | 2 — Dosage and Administration | documento lido parcialmente | https://drugs.com/pro/vasostrict.html |
| RCUK 2021 | Resuscitation Council UK | Emergency treatment of anaphylaxis: Guidelines for healthcare providers | 2021 | Maio/2021 (página oficial indicava ser a versão mais recente em 19/10/2026) | — | Adrenalina IM por idade, anafilaxia refratária, fluidos, anti-histamínicos, corticoides e observação | texto integral lido | https://www.resus.org.uk/library/additional-guidance/guidance-anaphylaxis/emergency-treatment |
| WAO 2011 | World Allergy Organization (WAO) | WAO Guidelines for the Assessment and Management of Anaphylaxis — Tabela 5 | 2011 | World Allergy Organization Journal, 2011 | 10.1097/WOX.0b013e318211496c | Tabela 5 — tratamento inicial (adrenalina IM) | documento lido parcialmente | https://waojournal.biomedcentral.com/articles/10.1097/WOX.0b013e318211496c/tables/5 |
| SCCM 2023 | Society of Critical Care Medicine (SCCM) | Clinical Practice Guidelines for Rapid Sequence Intubation in the Critically Ill Adult Patient — Executive Summary | 2023 | Acquisto NM et al. Crit Care Med 2023;51(10):1407-1410 | 10.1097/CCM.0000000000005999 | Recomendações 1 a 5 | lista de recomendações lida; texto integral não acessado | https://guidelinecentral.com/guideline/3250007 |
| DAS 2018 | Difficult Airway Society, Intensive Care Society, FICM e Royal College of Anaesthetists | Guidelines for the management of tracheal intubation in critically ill adults — algoritmo | 2018 | Higgs A et al. Br J Anaesth 2018 (algoritmo oficial) | — | Algoritmo: planos A a D, acesso cirúrgico frontal do pescoço e cuidados pós-intubação | documento lido parcialmente | https://database.das.uk.com/files/2017/page/DAS_ICU_guidelines.pdf |
| DAS 2025 (resumo) | Difficult Airway Society (DAS) | DAS 2025 guidelines for management of unanticipated difficult tracheal intubation in adults | 2025 | Ahmad I et al. Br J Anaesth, publicado online em 07/11/2025 (PMID 41203471) | — | Planos A–D e videolaringoscopia (segundo resumo da NYSORA) | resumo secundário (não emitido pela instituição autora) | https://nysora.com/education-news/difficult-airway-society-das-2025-update/ |
| ESC 2019 | European Society of Cardiology — Council on Hypertension | ESC Council on hypertension position document on the management of hypertensive emergencies | 2019 | van den Born BJH et al. Eur Heart J Cardiovasc Pharmacother 2019;5:37-46 | 10.1093/ehjcvp/pvy032 | Definições, 'urgência hipertensiva' e Tabela 3 (metas por apresentação) | texto integral lido | https://www.eshonline.org/esh-content/uploads/2019/07/3.-ESC-Council-on-hypertension-position-document-on-the-management-of-hypertensive-emergencies.pdf |
| SBC 2025 | Sociedade Brasileira de Cardiologia, Sociedade Brasileira de Hipertensão e Sociedade Brasileira de Nefrologia | Diretriz Brasileira de Hipertensão Arterial – 2025 | 2025 | Brandão AA et al. Arq Bras Cardiol 2025;122(9):e20250624 | 10.36660/abc.20250624 | Capítulo 11 — Crise Hipertensiva (págs. 98-105) | apenas identificação/sumário; seção relevante NÃO lida | https://abccardiol.org/wp-content/uploads/2025/09/2025-0624_Diretriz_Hipertensao_2025_port.x66747.pdf |
| NHS SPS 2024 | NHS Specialist Pharmacy Service | Hypokalaemia | 2024 | Publicado em 14/08/2024 | — | Definição, gravidade, reposição, concentração e velocidade máximas | texto integral lido | https://sps.nhs.uk/articles/hypokalaemia/ |
| SmPC KCl | B. Braun Melsungen — SmPC aprovado no Reino Unido | Sterile Potassium Chloride concentrate (15% w/v) — Summary of Product Characteristics | 2019 | Seção 10: 18/12/2019 (página atualizada em 26/10/2023) | — | 4.2 (posologia), 4.3 (contraindicações) e 4.4 (advertências) | texto integral lido | https://www.medicines.org.uk/emc/product/15218/smpc/print |
| Bula KCl 19,1% | Blau Farmacêutica | Cloreto de potássio 19,1% solução injetável — bula do paciente | 2025 | Registro MS 1.1637.0090; texto atualizado em 30/07/2025 no site de consulta | — | Composição, modo de uso e advertências | texto integral lido | https://bula.com.br/original/cloreto-de-potassio-injetavel-191 |
| UKKA 2026 | UK Kidney Association | Clinical Practice Guidelines: Treatment of Acute Hyperkalaemia in Adults | 2026 | Original 07/2020; atualizações 10/2023 e 07/2026 | — | Definição e gravidade; diretrizes 14.1-14.2 (ECG e monitorização); 16.2-16.4 (tratamento de emergência) | documento lido parcialmente | https://www.ukkidney.org/sites/default/files/documents/FINAL%20VERSION%20-%20UKKA%20CLINICAL%20PRACTICE%20GUIDELINE%20-%20MANAGEMENT%20OF%20HYPERKALAEMIA%20IN%20ADULTS%20-%20UPDATED%20JULY%202026_0.pdf |
| ABA 2023 | American Burn Association (ABA) | American Burn Association Clinical Practice Guidelines on Burn Shock Resuscitation | 2023 | Cartotto R et al. J Burn Care Res (publicação online 2023) | 10.1093/jbcr/irad125 | População (adultos com ≥ 20% SCQ) e estimativa inicial de 2 mL/kg/%SCQ | texto integral lido | https://achpccg.com/wp-content/uploads/2024/02/Cartotto-et-al_2023_American-Burn-Association-CLinical-Practice-Guidelines-on-Burn-Shock-Resuscitation.pdf |
| AAFP 2025 (resumo) | American Academy of Family Physicians (AAFP) | Resuscitation of Patients With Burns: Guidelines From the American Burn Association | 2025 | Am Fam Physician 2025;112(2):219-220 | — | Resumo das recomendações da ABA | resumo secundário (não emitido pela instituição autora) | https://www.aafp.org/afp/2025/0800/practice-guidelines-resuscitation-patients-burns |
| MSD Manuals | MSD Manuals (calculadora EBMcalc) | Burn Injury Fluid Resuscitation, Adult (Parkland crystalloid estimate) | s/d | Versão on-line consultada em 19/10/2026 | — | Equações (total em 24 h; taxa nas primeiras 8 h e nas 16 h seguintes) | resumo secundário (não emitido pela instituição autora) | https://msdmanuals.com/medical-calculators/BurnInjuryFluidParkland-en.htm |
| Cockcroft-Gault 1976 | Nephron (Karger) | Prediction of creatinine clearance from serum creatinine | 1976 | Cockcroft DW, Gault H. Nephron 1976;16(1):31-41 (autoria conforme página da editora) | 10.1159/000180580 | Resumo (fórmula, fator feminino e população do estudo) | documento lido parcialmente | https://karger.com/nef/article/16/1/31/828833 |
| Mosteller 1987 | New England Journal of Medicine | Simplified calculation of body-surface area | 1987 | Mosteller RD. N Engl J Med 1987;317:1098 | — | Fórmula | resumo secundário (não emitido pela instituição autora) | https://www.rxlist.com/body_surface_area/definition.htm |
| DuBois 1916 | Archives of Internal Medicine | A formula to estimate the approximate surface area if height and weight be known | 1916 | Du Bois D, Du Bois EF. Arch Intern Med 1916;17:863-871 | — | Fórmula | resumo secundário (não emitido pela instituição autora) | https://msdmanuals.com/medical-calculators/BodySurfaceArea-en.htm |
| Bula noradrenalina | Hypofarma — Instituto de Hypodermia e Farmácia | Hyponor (hemitartarato de norepinefrina) solução injetável — bula | 2025 | Registro MS 1.0387.0030; texto atualizado em 30/07/2025 no site de consulta | — | Composição, indicações, contraindicações, posologia, advertências e interações | texto integral lido | https://bula.com.br/original/hyponor |
| Rótulo FDA noradrenalina | Pfizer — rótulo aprovado pela FDA (EUA) | LEVOPHED (norepinephrine bitartrate injection) — Prescribing Information | s/d | Seção 2 do rótulo publicado pelo fabricante | — | 2 — Dosage and Administration | documento lido parcialmente | https://www.pfizermedical.com/levophed-1/dosage-admin |
| Bula epinefrina | Hypofarma — Instituto de Hypodermia e Farmácia | Epinefrina 1 mg/mL solução injetável — bula | 2025 | Registro MS 1.0387.0078; texto atualizado em 05/08/2025 no site de consulta | — | Composição, indicações, contraindicações, advertências e interações | texto integral lido | https://bula.com.br/original/epinefrina |
| Bula amiodarona | Hipolabor Farmacêutica (registro: Sanval) | Cloridrato de amiodarona 50 mg/mL solução injetável — bula | 2025 | Registro MS 1.0714.0254; texto atualizado em 05/08/2025 no site de consulta | — | Composição, indicações, contraindicações, posologia, advertências, interações e populações especiais | texto integral lido | https://bula.com.br/original/cloridrato-de-amiodarona-injetavel-50-mgml |
| Rótulo FDA amiodarona | Baxter — rótulo aprovado pela FDA (EUA) | NEXTERONE (amiodarone HCl) premixed injection — Prescribing Information | 2025 | Revisão 2/2025 | — | 2.1, 2.2 (Tabela 1), 5.2 e 5.12 | texto integral lido | https://www.drugs.com/pro/nexterone.html |
| Bula ceftriaxona | Laboratório Teuto Brasileiro | Ceftriaxona dissódica intravenosa 500 mg e 1 g — bula | 2025 | Registro MS 1.0370.0712; texto atualizado em 30/07/2025 no site de consulta | — | Contraindicações, posologia, administração, interação com cálcio e populações especiais | texto integral lido | https://bula.com.br/original/ceftriaxona-dissodica-intravenoso-500-mg-e-1-g |
| Bula Meronem | Meronem IV — detentor do registro não exibido no trecho lido | Meronem IV (meropeném) — bula, seção de posologia | s/d | Seção 'Como usar' do site de consulta | — | Posologia, ajuste renal, populações especiais e preparo | documento lido parcialmente | https://bula.com.br/meronem-iv/posologia-como-usar |
| Bula meropeném | Fresenius Kabi Brasil | Meropeném pó para solução injetável — bula (minibula) | s/d | Registro MS 1.0041.0207 | — | Contraindicações, advertências, interações, ajuste renal e administração | texto integral lido | https://fresenius-kabi.com/br/documents/Meropenem-minibula.pdf |
| Bula Ketamin (escetamina) | Cristália Produtos Químicos Farmacêuticos | Ketamin e Ketamin NP (cloridrato de escetamina 50 mg/mL) — bula profissional | 2026 | Registro MS 1.0298.0213; bulas aprovadas pela Anvisa em 14/08/2026 (R_0213_07) e 25/06/2026 (R_0213_06) | — | Composição, indicações, contraindicações, posologia, advertências e interações | texto integral lido | https://cristalia.com.br/produto/112/bula-profissional |
| Bula cetamina | Instituto Biochimico (fabricante: Hameln Pharmaceuticals) | Cloridrato de cetamina 50 mg/mL — bula | s/d | Registro MS 1.0063.0237 | — | Composição, posologia e contraindicações | documento lido parcialmente | https://bula.com.br/cloridrato-de-cetamina-biochimico |
| ASRA 2018 (resumo) | ASRA, AAPM e ASA | Consensus guidelines on the use of intravenous ketamine infusions for acute pain management | 2018 | Schwenk ES et al. Reg Anesth Pain Med 2018;43(5):456-466 | 10.1097/AAP.0000000000000806 | Limites de bolus e infusão e ambiente monitorizado | resumo secundário (não emitido pela instituição autora) | https://asra.com/news-publications/asra-newsletter/newsletter-item/asra-news/2018/11/09/intravenous-ketamine-guidelines-for-pain-management |
| Bula Fentanest | Cristália Produtos Químicos Farmacêuticos | Fentanest (citrato de fentanila 0,05 mg/mL) — bula | 2001 | Registro MS 1.0298.0081; texto 'revisado em 21/09/01' (página atualizada em 30/07/2025) | — | Composição, indicações, posologia, advertências e antídoto | texto integral lido | https://bula.com.br/original/fentanest-005mgml-25fr10ml |
| Bula midazolam | Fresenius Kabi Brasil | Cloridrato de midazolam solução injetável — bula do profissional de saúde | 2026 | Registro MS 1.0041.0212; conforme bula padrão aprovada pela Anvisa em 05/02/2026 | — | Apresentações, posologia, populações especiais, advertências, interações e antídoto | texto integral lido | https://www.fresenius-kabi.com/content/dam/fresenius-kabi/br/documents/bulas/medicamentos/Cloridrato%20de%20Midazolam%20-%20Bula%20Profissional%20da%20Sa%C3%BAde.pdf.coredownload.inline.pdf |
| AES 2016 (resumo) | American Epilepsy Society (AES) | Diretriz da AES para tratamento do estado de mal epiléptico convulsivo (Epilepsy Currents) | 2016 | Glauser T et al. Epilepsy Curr 2016 | — | Fases do tratamento e classes de fármacos | resumo secundário (não emitido pela instituição autora) | https://www.reliasmedia.com/blogs/new-guideline-issued-for-emergency-treatment-of-status-epilepticus |

Todas consultadas em 19/10/2026. Observações por fonte:

- **AHA 2025:** Página oficial lida até cerca de 86% do texto (limite técnico); todas as recomendações citadas estavam no trecho lido.
- **SSC 2026:** Recomendações conferidas na página oficial da SCCM e no resumo da Guideline Central (https://www.guidelinecentral.com/guideline/5149062). O texto integral da editora não abriu: dose de hidrocortisona e limiar de noradrenalina para associar vasopressina NÃO foram verificados.
- **Rótulo FDA vasopressina:** Reprodução do rótulo em site de consulta. A bula brasileira de vasopressina não foi consultada.
- **RCUK 2021:** PDF lido: https://resus.org.uk/media/337/download (data de revisão prevista: maio/2026).
- **WAO 2011:** A atualização WAO 2020 não foi acessada nesta revisão.
- **SCCM 2023:** Página da SCCM: https://www.sccm.org/clinical-resources/guidelines/guidelines/guidelines-rapid-sequence-intubation
- **DAS 2018:** Lido o algoritmo oficial; o texto integral do artigo não foi acessado.
- **DAS 2025 (resumo):** Texto da diretriz não acessado.
- **ESC 2019:** A Tabela 4 (doses IV) desta versão tem erros de unidade, corrigidos por errata (doi:10.1093/ehjcvp/pvy040) não acessada — por isso nenhuma dose IV foi usada.
- **SBC 2025:** Só foi possível ler o sumário e os capítulos iniciais (limite técnico). O capítulo 11 NÃO foi verificado.
- **Bula KCl 19,1%:** É a bula do paciente: não traz velocidades máximas nem concentração após diluição.
- **ABA 2023:** Cópia do artigo hospedada por terceiro.
- **Cockcroft-Gault 1976:** Lido o resumo; o texto integral é pago.
- **Mosteller 1987:** Fórmula conferida em fonte secundária (RxList) que cita o artigo original.
- **DuBois 1916:** Fórmula conferida em fonte secundária (MSD Manuals/EBMcalc) que cita o artigo original.
- **Bula noradrenalina:** Reprodução da bula em site de consulta (não é o Bulário Eletrônico da Anvisa). A dose inicial da bula tem inconsistência de unidade ('2 a 6 mg'); por isso a dose inicial exibida é a do rótulo norte-americano.
- **Bula epinefrina:** A bula não traz doses para anafilaxia nem para parada cardíaca.
- **Rótulo FDA amiodarona:** Reprodução do rótulo em site de consulta.
- **Bula Ketamin (escetamina):** Também publicada em https://cristalia.com.br/produto/341/bula-profissional
- **Bula cetamina:** A bula acessada não informa se a cetamina é racêmica.
- **ASRA 2018 (resumo):** Resumo publicado na ASRA News; refere-se à cetamina usada nos EUA, não à escetamina.
- **Bula Fentanest:** Revisão antiga: conferir a versão vigente no Bulário Eletrônico da Anvisa.
- **Bula midazolam:** O extrator apontou células desalinhadas nas tabelas pediátricas; doses pediátricas não foram usadas.
- **AES 2016 (resumo):** O resumo acessado não traz doses.

## Fontes procuradas e não acessadas

- **Diretriz Brasileira de Hipertensão Arterial 2025 — capítulo 11 (Crise Hipertensiva):** Documento muito extenso para a ferramenta de leitura; só o sumário foi lido.
- **Surviving Sepsis Campaign 2026 — texto integral:** Site da editora não abriu; usadas a página oficial da SCCM e o resumo da Guideline Central.
- **SCCM 2023 (intubação em sequência rápida) — texto integral:** Site da editora não abriu; usado o resumo das recomendações.
- **DAS 2025 — texto integral:** Não acessado; usado apenas resumo secundário.
- **ESC 2024 e AHA/ACC 2025 — seções de crise hipertensiva:** Não acessadas nesta revisão.
- **ERC 2025 — suporte avançado de vida (detalhes):** Localizada, mas não comparada em detalhe.
- **SBC — diretriz de ressuscitação cardiopulmonar (2019, a mais recente localizada):** Não lida nesta revisão.
- **WAO 2020 (anafilaxia) e material da ASBAI:** Não acessados; usada a WAO 2011 e a RCUK 2021.
- **ATLS, ACLS e PALS — manuais:** Material licenciado; usados apenas documentos públicos da AHA.
- **Diretriz de meningite bacteriana (IDSA/Ministério da Saúde):** Não acessada; dose de ceftriaxona para meningite em adultos ficou bloqueada.
- **Diretriz de analgesia e sedação em UTI (SCCM PADIS):** Não acessada; doses de infusão de fentanil ficaram bloqueadas.
- **Bula brasileira da vasopressina:** Não consultada; usado o rótulo norte-americano.
- **Bulário Eletrônico da Anvisa:** Não acessível a partir do ambiente da auditoria.
