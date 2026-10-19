"""Registro da auditoria de 19/10/2026: problemas técnicos corrigidos, limitações e fontes não acessadas."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProblemaTecnico:
    problema: str
    onde: str
    correcao: str


PROBLEMAS_TECNICOS: tuple[ProblemaTecnico, ...] = (
    ProblemaTecnico(
        "Cabeçalho de e-mail colado no código (nome, endereço, horário e 'para mim') → SyntaxError.",
        "commit 1292114, linhas 1-6",
        "Código reconstruído a partir do conteúdo; cabeçalho omitido da cópia em legado/.",
    ),
    ProblemaTecnico(
        "Indentação perdida ao copiar e colar → IndentationError.",
        "commits 1292114, 0272b4a, df1ecf4, 030cc1f e b161d85",
        "Código reescrito em módulos e entregue como arquivos, sem copiar e colar.",
    ),
    ProblemaTecnico(
        "O Gmail transformou 'st.info' em link (https://www.google.com/url?q=http://st.info...) → SyntaxError.",
        "commit 0272b4a (3 ocorrências)",
        "Eliminado na reconstrução.",
    ),
    ProblemaTecnico(
        "Funcionalidades apagadas a cada tentativa de correção (281 → 23 linhas).",
        "commits 0272b4a a 35f2e67",
        "Todas as funcionalidades recuperadas e testadas; textos originais preservados.",
    ),
    ProblemaTecnico(
        "Arquivo único misturando dados, cálculos e interface; nenhum teste.",
        "app.py",
        "Pacote medicore/ (cálculos puros, conteúdo, fontes, interface) e suíte de testes automatizados.",
    ),
    ProblemaTecnico(
        ".zip no repositório com cópia idêntica do app.py e um .pyc compilado em outro ambiente.",
        "medicore_corrigido.zip",
        "Removido; o README dele foi preservado em legado/ e o .gitignore impede novos .pyc.",
    ),
    ProblemaTecnico(
        "Aba 'RAG' simulada: qualquer pergunta devolvia o mesmo texto com 'relevância 99,2%' inventada.",
        "commit 1292114, aba 3",
        "Substituída por busca textual real no conteúdo do app, sem pontuação inventada.",
    ),
    ProblemaTecnico(
        "Alegações sem base na interface: 'Validação Automática Ativa', 'Sem Erros', 'Padrão Whitebook revisada'.",
        "commit 1292114",
        "Removidas; status de cada conteúdo exibido conforme os critérios de liberação.",
    ),
    ProblemaTecnico(
        "CSS injetado via HTML (unsafe_allow_html) com seletores frágeis.",
        "commit 1292114",
        "Tema escuro equivalente definido em .streamlit/config.toml, sem HTML injetado.",
    ),
    ProblemaTecnico(
        "Valores padrão silenciosos (peso 70 kg, creatinina 1,0, concentração 16 mcg/mL) usados nos cálculos.",
        "todas as versões",
        "Campos começam vazios; nenhuma conta é feita com valor presumido.",
    ),
)

LIMITACOES: tuple[str, ...] = (
    "A auditoria foi feita por um assistente de IA. Não substitui a revisão por profissional habilitado: por isso nada está VALIDADO.",
    "Só foram usadas fontes efetivamente abertas nesta sessão; o nível de acesso de cada uma está declarado no registro de referências.",
    "Várias bulas foram lidas em sites de consulta que reproduzem o texto; o Bulário Eletrônico da Anvisa não pôde ser acessado.",
    "O aplicativo publicado (medicore-pro.streamlit.app) não pôde ser aberto a partir do ambiente da auditoria. A "
    "execução foi testada localmente com o Streamlit 1.66.0 montado a partir do código-fonte oficial, e o GitHub "
    "Actions repete todos os testes a cada atualização do repositório.",
)

FONTES_NAO_ACESSADAS: tuple[tuple[str, str], ...] = (
    ("Diretriz Brasileira de Hipertensão Arterial 2025 — capítulo 11 (Crise Hipertensiva)", "Documento muito extenso para a ferramenta de leitura; só o sumário foi lido."),
    ("Surviving Sepsis Campaign 2026 — texto integral", "Site da editora não abriu; usadas a página oficial da SCCM e o resumo da Guideline Central."),
    ("SCCM 2023 (intubação em sequência rápida) — texto integral", "Site da editora não abriu; usado o resumo das recomendações."),
    ("DAS 2025 — texto integral", "Não acessado; usado apenas resumo secundário."),
    ("ESC 2024 e AHA/ACC 2025 — seções de crise hipertensiva", "Não acessadas nesta revisão."),
    ("ERC 2025 — suporte avançado de vida (detalhes)", "Localizada, mas não comparada em detalhe."),
    ("SBC — diretriz de ressuscitação cardiopulmonar (2019, a mais recente localizada)", "Não lida nesta revisão."),
    ("WAO 2020 (anafilaxia) e material da ASBAI", "Não acessados; usada a WAO 2011 e a RCUK 2021."),
    ("ATLS, ACLS e PALS — manuais", "Material licenciado; usados apenas documentos públicos da AHA."),
    ("Diretriz de meningite bacteriana (IDSA/Ministério da Saúde)", "Não acessada; dose de ceftriaxona para meningite em adultos ficou bloqueada."),
    ("Diretriz de analgesia e sedação em UTI (SCCM PADIS)", "Não acessada; doses de infusão de fentanil ficaram bloqueadas."),
    ("Bula brasileira da vasopressina", "Não consultada; usado o rótulo norte-americano."),
    ("Bulário Eletrônico da Anvisa", "Não acessível a partir do ambiente da auditoria."),
)
