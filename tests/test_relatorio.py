from medicore.relatorio import CAMINHO, gerar_relatorio


def test_relatorio_sincronizado_com_o_codigo():
    assert CAMINHO.exists(), "Gere o relatório com: python -m medicore.relatorio"
    atual = CAMINHO.read_text(encoding="utf-8")
    assert atual == gerar_relatorio(), "docs/AUDITORIA.md desatualizado: rode python -m medicore.relatorio"


def test_relatorio_contem_todas_as_secoes():
    texto = gerar_relatorio()
    for secao in (
        "## Critérios de liberação",
        "## Limitações desta auditoria",
        "## Problemas técnicos corrigidos",
        "## Fármacos",
        "## Fluxogramas",
        "## Calculadoras",
        "## Testes automatizados",
        "## Referências consultadas",
        "## Fontes procuradas e não acessadas",
    ):
        assert secao in texto
