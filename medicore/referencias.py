"""Registro das fontes efetivamente consultadas na auditoria de 19/10/2026.

Regra do projeto: nenhuma recomendação clínica aparece no aplicativo sem pelo menos uma
referência deste registro. O campo ``acesso`` declara, com honestidade, o quanto de cada
fonte foi realmente lido — inclusive quando só foi possível ler um resumo ou o sumário.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Acesso(str, Enum):
    TEXTO_INTEGRAL = "texto integral lido"
    PARCIAL = "documento lido parcialmente"
    RESUMO_RECOMENDACOES = "lista de recomendações lida; texto integral não acessado"
    RESUMO_SECUNDARIO = "resumo secundário (não emitido pela instituição autora)"
    SOMENTE_IDENTIFICACAO = "apenas identificação/sumário; seção relevante NÃO lida"


@dataclass(frozen=True)
class Referencia:
    id: str
    instituicao: str
    titulo: str
    ano: str
    versao: str
    url: str
    secao: str
    acesso: Acesso
    doi: str = ""
    observacao: str = ""
    consultado_em: str = "2026-10-19"

    def citacao_curta(self) -> str:
        return f"{self.instituicao} — {self.titulo} ({self.ano})"


_LISTA: tuple[Referencia, ...] = (
    # ------------------------------------------------------------------ Ressuscitação
    Referencia(
        id="aha2025_als",
        instituicao="American Heart Association (AHA)",
        titulo="Part 9: Adult Advanced Life Support — 2025 AHA Guidelines for CPR and ECC",
        ano="2025",
        versao="Diretrizes AHA 2025 para RCP e ACE (publicadas em Circulation)",
        doi="10.1161/CIR.0000000000001376",
        url="https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-advanced-life-support",
        secao="Seções 5 (desfibrilação), 9 (acesso vascular), 10 (vasopressores) e 11 (não vasopressores)",
        acesso=Acesso.PARCIAL,
        observacao="Página oficial lida até cerca de 86% do texto (limite técnico); todas as recomendações citadas estavam no trecho lido.",
    ),
    Referencia(
        id="aha2025_algoritmo_pcr",
        instituicao="American Heart Association (AHA)",
        titulo="Adult Cardiac Arrest Algorithm — descrição textual",
        ano="2025",
        versao="Algorithm-ACLS-CA-LngDscrp-250725",
        url="https://cpr.heart.org/-/media/CPR-Files/CPR-Guidelines-Files/2025-Accessible/Algorithm-ACLS-CA-LngDscrp-250725-Ed.pdf",
        secao="Algoritmo completo: qualidade da RCP, energia do choque, fármacos e causas reversíveis",
        acesso=Acesso.TEXTO_INTEGRAL,
    ),
    Referencia(
        id="rcuk_abcde",
        instituicao="Resuscitation Council UK",
        titulo="The ABCDE Approach",
        ano="2024",
        versao="Publicado em 10/2015, revisado em 05/2021 e atualizado em 07/2024",
        url="https://resus.org.uk/node/123",
        secao="Princípios e avaliação A, B, C, D e E",
        acesso=Acesso.TEXTO_INTEGRAL,
    ),
    # ------------------------------------------------------------------ Sepse
    Referencia(
        id="ssc2026",
        instituicao="Society of Critical Care Medicine (SCCM) e European Society of Intensive Care Medicine (ESICM)",
        titulo="Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2026",
        ano="2026",
        versao="Prescott HC, Antonelli M, et al. Crit Care Med, publicado em 23/03/2026",
        doi="10.1097/CCM.0000000000007075",
        url="https://www.sccm.org/clinical-resources/guidelines/guidelines/surviving-sepsis-campaign-international-guidelines-for-management-of-sepsis-and-septic-shock-2026",
        secao="Recomendações de rastreio, lactato, hemoculturas, antimicrobianos, fluidos, PAM, vasopressores, corticoide e betalactâmicos",
        acesso=Acesso.RESUMO_RECOMENDACOES,
        observacao=(
            "Recomendações conferidas na página oficial da SCCM e no resumo da Guideline Central "
            "(https://www.guidelinecentral.com/guideline/5149062). O texto integral da editora não abriu: "
            "dose de hidrocortisona e limiar de noradrenalina para associar vasopressina NÃO foram verificados."
        ),
    ),
    Referencia(
        id="fda_vasostrict",
        instituicao="Par Pharmaceutical — rótulo aprovado pela FDA (EUA)",
        titulo="VASOSTRICT (vasopressin injection) — Prescribing Information",
        ano="2023",
        versao="Revisão 2/2023",
        url="https://drugs.com/pro/vasostrict.html",
        secao="2 — Dosage and Administration",
        acesso=Acesso.PARCIAL,
        observacao="Reprodução do rótulo em site de consulta. A bula brasileira de vasopressina não foi consultada.",
    ),
    # ------------------------------------------------------------------ Anafilaxia
    Referencia(
        id="rcuk2021_anafilaxia",
        instituicao="Resuscitation Council UK",
        titulo="Emergency treatment of anaphylaxis: Guidelines for healthcare providers",
        ano="2021",
        versao="Maio/2021 (página oficial indicava ser a versão mais recente em 19/10/2026)",
        url="https://www.resus.org.uk/library/additional-guidance/guidance-anaphylaxis/emergency-treatment",
        secao="Adrenalina IM por idade, anafilaxia refratária, fluidos, anti-histamínicos, corticoides e observação",
        acesso=Acesso.TEXTO_INTEGRAL,
        observacao="PDF lido: https://resus.org.uk/media/337/download (data de revisão prevista: maio/2026).",
    ),
    Referencia(
        id="wao2011_anafilaxia",
        instituicao="World Allergy Organization (WAO)",
        titulo="WAO Guidelines for the Assessment and Management of Anaphylaxis — Tabela 5",
        ano="2011",
        versao="World Allergy Organization Journal, 2011",
        doi="10.1097/WOX.0b013e318211496c",
        url="https://waojournal.biomedcentral.com/articles/10.1097/WOX.0b013e318211496c/tables/5",
        secao="Tabela 5 — tratamento inicial (adrenalina IM)",
        acesso=Acesso.PARCIAL,
        observacao="A atualização WAO 2020 não foi acessada nesta revisão.",
    ),
    # ------------------------------------------------------------------ Via aérea
    Referencia(
        id="sccm2023_sri",
        instituicao="Society of Critical Care Medicine (SCCM)",
        titulo="Clinical Practice Guidelines for Rapid Sequence Intubation in the Critically Ill Adult Patient — Executive Summary",
        ano="2023",
        versao="Acquisto NM et al. Crit Care Med 2023;51(10):1407-1410",
        doi="10.1097/CCM.0000000000005999",
        url="https://guidelinecentral.com/guideline/3250007",
        secao="Recomendações 1 a 5",
        acesso=Acesso.RESUMO_RECOMENDACOES,
        observacao="Página da SCCM: https://www.sccm.org/clinical-resources/guidelines/guidelines/guidelines-rapid-sequence-intubation",
    ),
    Referencia(
        id="das2018_uti",
        instituicao="Difficult Airway Society, Intensive Care Society, FICM e Royal College of Anaesthetists",
        titulo="Guidelines for the management of tracheal intubation in critically ill adults — algoritmo",
        ano="2018",
        versao="Higgs A et al. Br J Anaesth 2018 (algoritmo oficial)",
        url="https://database.das.uk.com/files/2017/page/DAS_ICU_guidelines.pdf",
        secao="Algoritmo: planos A a D, acesso cirúrgico frontal do pescoço e cuidados pós-intubação",
        acesso=Acesso.PARCIAL,
        observacao="Lido o algoritmo oficial; o texto integral do artigo não foi acessado.",
    ),
    Referencia(
        id="das2025",
        instituicao="Difficult Airway Society (DAS)",
        titulo="DAS 2025 guidelines for management of unanticipated difficult tracheal intubation in adults",
        ano="2025",
        versao="Ahmad I et al. Br J Anaesth, publicado online em 07/11/2025 (PMID 41203471)",
        url="https://nysora.com/education-news/difficult-airway-society-das-2025-update/",
        secao="Planos A–D e videolaringoscopia (segundo resumo da NYSORA)",
        acesso=Acesso.RESUMO_SECUNDARIO,
        observacao="Texto da diretriz não acessado.",
    ),
    # ------------------------------------------------------------------ Hipertensão
    Referencia(
        id="esc2019_has",
        instituicao="European Society of Cardiology — Council on Hypertension",
        titulo="ESC Council on hypertension position document on the management of hypertensive emergencies",
        ano="2019",
        versao="van den Born BJH et al. Eur Heart J Cardiovasc Pharmacother 2019;5:37-46",
        doi="10.1093/ehjcvp/pvy032",
        url="https://www.eshonline.org/esh-content/uploads/2019/07/3.-ESC-Council-on-hypertension-position-document-on-the-management-of-hypertensive-emergencies.pdf",
        secao="Definições, 'urgência hipertensiva' e Tabela 3 (metas por apresentação)",
        acesso=Acesso.TEXTO_INTEGRAL,
        observacao=(
            "A Tabela 4 (doses IV) desta versão tem erros de unidade, corrigidos por errata "
            "(doi:10.1093/ehjcvp/pvy040) não acessada — por isso nenhuma dose IV foi usada."
        ),
    ),
    Referencia(
        id="sbc2025_has",
        instituicao="Sociedade Brasileira de Cardiologia, Sociedade Brasileira de Hipertensão e Sociedade Brasileira de Nefrologia",
        titulo="Diretriz Brasileira de Hipertensão Arterial – 2025",
        ano="2025",
        versao="Brandão AA et al. Arq Bras Cardiol 2025;122(9):e20250624",
        doi="10.36660/abc.20250624",
        url="https://abccardiol.org/wp-content/uploads/2025/09/2025-0624_Diretriz_Hipertensao_2025_port.x66747.pdf",
        secao="Capítulo 11 — Crise Hipertensiva (págs. 98-105)",
        acesso=Acesso.SOMENTE_IDENTIFICACAO,
        observacao="Só foi possível ler o sumário e os capítulos iniciais (limite técnico). O capítulo 11 NÃO foi verificado.",
    ),
    # ------------------------------------------------------------------ Eletrólitos
    Referencia(
        id="sps2024_hipocalemia",
        instituicao="NHS Specialist Pharmacy Service",
        titulo="Hypokalaemia",
        ano="2024",
        versao="Publicado em 14/08/2024",
        url="https://sps.nhs.uk/articles/hypokalaemia/",
        secao="Definição, gravidade, reposição, concentração e velocidade máximas",
        acesso=Acesso.TEXTO_INTEGRAL,
    ),
    Referencia(
        id="smpc_kcl",
        instituicao="B. Braun Melsungen — SmPC aprovado no Reino Unido",
        titulo="Sterile Potassium Chloride concentrate (15% w/v) — Summary of Product Characteristics",
        ano="2019",
        versao="Seção 10: 18/12/2019 (página atualizada em 26/10/2023)",
        url="https://www.medicines.org.uk/emc/product/15218/smpc/print",
        secao="4.2 (posologia), 4.3 (contraindicações) e 4.4 (advertências)",
        acesso=Acesso.TEXTO_INTEGRAL,
    ),
    Referencia(
        id="bula_kcl_blau",
        instituicao="Blau Farmacêutica",
        titulo="Cloreto de potássio 19,1% solução injetável — bula do paciente",
        ano="2025",
        versao="Registro MS 1.1637.0090; texto atualizado em 30/07/2025 no site de consulta",
        url="https://bula.com.br/original/cloreto-de-potassio-injetavel-191",
        secao="Composição, modo de uso e advertências",
        acesso=Acesso.TEXTO_INTEGRAL,
        observacao="É a bula do paciente: não traz velocidades máximas nem concentração após diluição.",
    ),
    Referencia(
        id="ukka_hipercalemia",
        instituicao="UK Kidney Association",
        titulo="Clinical Practice Guidelines: Treatment of Acute Hyperkalaemia in Adults",
        ano="2026",
        versao="Original 07/2020; atualizações 10/2023 e 07/2026",
        url="https://www.ukkidney.org/sites/default/files/documents/FINAL%20VERSION%20-%20UKKA%20CLINICAL%20PRACTICE%20GUIDELINE%20-%20MANAGEMENT%20OF%20HYPERKALAEMIA%20IN%20ADULTS%20-%20UPDATED%20JULY%202026_0.pdf",
        secao="Definição e gravidade; diretrizes 14.1-14.2 (ECG e monitorização); 16.2-16.4 (tratamento de emergência)",
        acesso=Acesso.PARCIAL,
    ),
    # ------------------------------------------------------------------ Queimados
    Referencia(
        id="aba2023_queimados",
        instituicao="American Burn Association (ABA)",
        titulo="American Burn Association Clinical Practice Guidelines on Burn Shock Resuscitation",
        ano="2023",
        versao="Cartotto R et al. J Burn Care Res (publicação online 2023)",
        doi="10.1093/jbcr/irad125",
        url="https://achpccg.com/wp-content/uploads/2024/02/Cartotto-et-al_2023_American-Burn-Association-CLinical-Practice-Guidelines-on-Burn-Shock-Resuscitation.pdf",
        secao="População (adultos com ≥ 20% SCQ) e estimativa inicial de 2 mL/kg/%SCQ",
        acesso=Acesso.TEXTO_INTEGRAL,
        observacao="Cópia do artigo hospedada por terceiro.",
    ),
    Referencia(
        id="aafp2025_aba",
        instituicao="American Academy of Family Physicians (AAFP)",
        titulo="Resuscitation of Patients With Burns: Guidelines From the American Burn Association",
        ano="2025",
        versao="Am Fam Physician 2025;112(2):219-220",
        url="https://www.aafp.org/afp/2025/0800/practice-guidelines-resuscitation-patients-burns",
        secao="Resumo das recomendações da ABA",
        acesso=Acesso.RESUMO_SECUNDARIO,
    ),
    Referencia(
        id="msd_parkland",
        instituicao="MSD Manuals (calculadora EBMcalc)",
        titulo="Burn Injury Fluid Resuscitation, Adult (Parkland crystalloid estimate)",
        ano="s/d",
        versao="Versão on-line consultada em 19/10/2026",
        url="https://msdmanuals.com/medical-calculators/BurnInjuryFluidParkland-en.htm",
        secao="Equações (total em 24 h; taxa nas primeiras 8 h e nas 16 h seguintes)",
        acesso=Acesso.RESUMO_SECUNDARIO,
    ),
    # ------------------------------------------------------------------ Fórmulas
    Referencia(
        id="cockcroft1976",
        instituicao="Nephron (Karger)",
        titulo="Prediction of creatinine clearance from serum creatinine",
        ano="1976",
        versao="Cockcroft DW, Gault H. Nephron 1976;16(1):31-41 (autoria conforme página da editora)",
        doi="10.1159/000180580",
        url="https://karger.com/nef/article/16/1/31/828833",
        secao="Resumo (fórmula, fator feminino e população do estudo)",
        acesso=Acesso.PARCIAL,
        observacao="Lido o resumo; o texto integral é pago.",
    ),
    Referencia(
        id="mosteller1987",
        instituicao="New England Journal of Medicine",
        titulo="Simplified calculation of body-surface area",
        ano="1987",
        versao="Mosteller RD. N Engl J Med 1987;317:1098",
        url="https://www.rxlist.com/body_surface_area/definition.htm",
        secao="Fórmula",
        acesso=Acesso.RESUMO_SECUNDARIO,
        observacao="Fórmula conferida em fonte secundária (RxList) que cita o artigo original.",
    ),
    Referencia(
        id="dubois1916",
        instituicao="Archives of Internal Medicine",
        titulo="A formula to estimate the approximate surface area if height and weight be known",
        ano="1916",
        versao="Du Bois D, Du Bois EF. Arch Intern Med 1916;17:863-871",
        url="https://msdmanuals.com/medical-calculators/BodySurfaceArea-en.htm",
        secao="Fórmula",
        acesso=Acesso.RESUMO_SECUNDARIO,
        observacao="Fórmula conferida em fonte secundária (MSD Manuals/EBMcalc) que cita o artigo original.",
    ),
    # ------------------------------------------------------------------ Bulas e rótulos
    Referencia(
        id="bula_hyponor",
        instituicao="Hypofarma — Instituto de Hypodermia e Farmácia",
        titulo="Hyponor (hemitartarato de norepinefrina) solução injetável — bula",
        ano="2025",
        versao="Registro MS 1.0387.0030; texto atualizado em 30/07/2025 no site de consulta",
        url="https://bula.com.br/original/hyponor",
        secao="Composição, indicações, contraindicações, posologia, advertências e interações",
        acesso=Acesso.TEXTO_INTEGRAL,
        observacao=(
            "Reprodução da bula em site de consulta (não é o Bulário Eletrônico da Anvisa). A dose inicial "
            "da bula tem inconsistência de unidade ('2 a 6 mg'); por isso a dose inicial exibida é a do rótulo "
            "norte-americano."
        ),
    ),
    Referencia(
        id="fda_levophed",
        instituicao="Pfizer — rótulo aprovado pela FDA (EUA)",
        titulo="LEVOPHED (norepinephrine bitartrate injection) — Prescribing Information",
        ano="s/d",
        versao="Seção 2 do rótulo publicado pelo fabricante",
        url="https://www.pfizermedical.com/levophed-1/dosage-admin",
        secao="2 — Dosage and Administration",
        acesso=Acesso.PARCIAL,
    ),
    Referencia(
        id="bula_epinefrina",
        instituicao="Hypofarma — Instituto de Hypodermia e Farmácia",
        titulo="Epinefrina 1 mg/mL solução injetável — bula",
        ano="2025",
        versao="Registro MS 1.0387.0078; texto atualizado em 05/08/2025 no site de consulta",
        url="https://bula.com.br/original/epinefrina",
        secao="Composição, indicações, contraindicações, advertências e interações",
        acesso=Acesso.TEXTO_INTEGRAL,
        observacao="A bula não traz doses para anafilaxia nem para parada cardíaca.",
    ),
    Referencia(
        id="bula_amiodarona",
        instituicao="Hipolabor Farmacêutica (registro: Sanval)",
        titulo="Cloridrato de amiodarona 50 mg/mL solução injetável — bula",
        ano="2025",
        versao="Registro MS 1.0714.0254; texto atualizado em 05/08/2025 no site de consulta",
        url="https://bula.com.br/original/cloridrato-de-amiodarona-injetavel-50-mgml",
        secao="Composição, indicações, contraindicações, posologia, advertências, interações e populações especiais",
        acesso=Acesso.TEXTO_INTEGRAL,
    ),
    Referencia(
        id="fda_nexterone",
        instituicao="Baxter — rótulo aprovado pela FDA (EUA)",
        titulo="NEXTERONE (amiodarone HCl) premixed injection — Prescribing Information",
        ano="2025",
        versao="Revisão 2/2025",
        url="https://www.drugs.com/pro/nexterone.html",
        secao="2.1, 2.2 (Tabela 1), 5.2 e 5.12",
        acesso=Acesso.TEXTO_INTEGRAL,
        observacao="Reprodução do rótulo em site de consulta.",
    ),
    Referencia(
        id="bula_ceftriaxona",
        instituicao="Laboratório Teuto Brasileiro",
        titulo="Ceftriaxona dissódica intravenosa 500 mg e 1 g — bula",
        ano="2025",
        versao="Registro MS 1.0370.0712; texto atualizado em 30/07/2025 no site de consulta",
        url="https://bula.com.br/original/ceftriaxona-dissodica-intravenoso-500-mg-e-1-g",
        secao="Contraindicações, posologia, administração, interação com cálcio e populações especiais",
        acesso=Acesso.TEXTO_INTEGRAL,
    ),
    Referencia(
        id="bula_meronem",
        instituicao="Meronem IV — detentor do registro não exibido no trecho lido",
        titulo="Meronem IV (meropeném) — bula, seção de posologia",
        ano="s/d",
        versao="Seção 'Como usar' do site de consulta",
        url="https://bula.com.br/meronem-iv/posologia-como-usar",
        secao="Posologia, ajuste renal, populações especiais e preparo",
        acesso=Acesso.PARCIAL,
    ),
    Referencia(
        id="bula_meropenem_fk",
        instituicao="Fresenius Kabi Brasil",
        titulo="Meropeném pó para solução injetável — bula (minibula)",
        ano="s/d",
        versao="Registro MS 1.0041.0207",
        url="https://fresenius-kabi.com/br/documents/Meropenem-minibula.pdf",
        secao="Contraindicações, advertências, interações, ajuste renal e administração",
        acesso=Acesso.TEXTO_INTEGRAL,
    ),
    Referencia(
        id="bula_ketamin",
        instituicao="Cristália Produtos Químicos Farmacêuticos",
        titulo="Ketamin e Ketamin NP (cloridrato de escetamina 50 mg/mL) — bula profissional",
        ano="2026",
        versao="Registro MS 1.0298.0213; bulas aprovadas pela Anvisa em 14/08/2026 (R_0213_07) e 25/06/2026 (R_0213_06)",
        url="https://cristalia.com.br/produto/112/bula-profissional",
        secao="Composição, indicações, contraindicações, posologia, advertências e interações",
        acesso=Acesso.TEXTO_INTEGRAL,
        observacao="Também publicada em https://cristalia.com.br/produto/341/bula-profissional",
    ),
    Referencia(
        id="bula_cetamina_biochimico",
        instituicao="Instituto Biochimico (fabricante: Hameln Pharmaceuticals)",
        titulo="Cloridrato de cetamina 50 mg/mL — bula",
        ano="s/d",
        versao="Registro MS 1.0063.0237",
        url="https://bula.com.br/cloridrato-de-cetamina-biochimico",
        secao="Composição, posologia e contraindicações",
        acesso=Acesso.PARCIAL,
        observacao="A bula acessada não informa se a cetamina é racêmica.",
    ),
    Referencia(
        id="asra2018_cetamina",
        instituicao="ASRA, AAPM e ASA",
        titulo="Consensus guidelines on the use of intravenous ketamine infusions for acute pain management",
        ano="2018",
        versao="Schwenk ES et al. Reg Anesth Pain Med 2018;43(5):456-466",
        doi="10.1097/AAP.0000000000000806",
        url="https://asra.com/news-publications/asra-newsletter/newsletter-item/asra-news/2018/11/09/intravenous-ketamine-guidelines-for-pain-management",
        secao="Limites de bolus e infusão e ambiente monitorizado",
        acesso=Acesso.RESUMO_SECUNDARIO,
        observacao="Resumo publicado na ASRA News; refere-se à cetamina usada nos EUA, não à escetamina.",
    ),
    Referencia(
        id="bula_fentanest",
        instituicao="Cristália Produtos Químicos Farmacêuticos",
        titulo="Fentanest (citrato de fentanila 0,05 mg/mL) — bula",
        ano="2001",
        versao="Registro MS 1.0298.0081; texto 'revisado em 21/09/01' (página atualizada em 30/07/2025)",
        url="https://bula.com.br/original/fentanest-005mgml-25fr10ml",
        secao="Composição, indicações, posologia, advertências e antídoto",
        acesso=Acesso.TEXTO_INTEGRAL,
        observacao="Revisão antiga: conferir a versão vigente no Bulário Eletrônico da Anvisa.",
    ),
    Referencia(
        id="bula_midazolam",
        instituicao="Fresenius Kabi Brasil",
        titulo="Cloridrato de midazolam solução injetável — bula do profissional de saúde",
        ano="2026",
        versao="Registro MS 1.0041.0212; conforme bula padrão aprovada pela Anvisa em 05/02/2026",
        url="https://www.fresenius-kabi.com/content/dam/fresenius-kabi/br/documents/bulas/medicamentos/Cloridrato%20de%20Midazolam%20-%20Bula%20Profissional%20da%20Sa%C3%BAde.pdf.coredownload.inline.pdf",
        secao="Apresentações, posologia, populações especiais, advertências, interações e antídoto",
        acesso=Acesso.TEXTO_INTEGRAL,
        observacao="O extrator apontou células desalinhadas nas tabelas pediátricas; doses pediátricas não foram usadas.",
    ),
    Referencia(
        id="aes2016_status",
        instituicao="American Epilepsy Society (AES)",
        titulo="Diretriz da AES para tratamento do estado de mal epiléptico convulsivo (Epilepsy Currents)",
        ano="2016",
        versao="Glauser T et al. Epilepsy Curr 2016",
        url="https://www.reliasmedia.com/blogs/new-guideline-issued-for-emergency-treatment-of-status-epilepticus",
        secao="Fases do tratamento e classes de fármacos",
        acesso=Acesso.RESUMO_SECUNDARIO,
        observacao="O resumo acessado não traz doses.",
    ),
)

REFERENCIAS: dict[str, Referencia] = {ref.id: ref for ref in _LISTA}

# Rótulos curtos exibidos ao lado de cada item no aplicativo.
ROTULOS: dict[str, str] = {
    "aha2025_als": "AHA 2025",
    "aha2025_algoritmo_pcr": "AHA 2025 — algoritmo",
    "rcuk_abcde": "RCUK ABCDE 2024",
    "ssc2026": "SSC 2026",
    "fda_vasostrict": "Rótulo FDA vasopressina",
    "rcuk2021_anafilaxia": "RCUK 2021",
    "wao2011_anafilaxia": "WAO 2011",
    "sccm2023_sri": "SCCM 2023",
    "das2018_uti": "DAS 2018",
    "das2025": "DAS 2025 (resumo)",
    "esc2019_has": "ESC 2019",
    "sbc2025_has": "SBC 2025",
    "sps2024_hipocalemia": "NHS SPS 2024",
    "smpc_kcl": "SmPC KCl",
    "bula_kcl_blau": "Bula KCl 19,1%",
    "ukka_hipercalemia": "UKKA 2026",
    "aba2023_queimados": "ABA 2023",
    "aafp2025_aba": "AAFP 2025 (resumo)",
    "msd_parkland": "MSD Manuals",
    "cockcroft1976": "Cockcroft-Gault 1976",
    "mosteller1987": "Mosteller 1987",
    "dubois1916": "DuBois 1916",
    "bula_hyponor": "Bula noradrenalina",
    "fda_levophed": "Rótulo FDA noradrenalina",
    "bula_epinefrina": "Bula epinefrina",
    "bula_amiodarona": "Bula amiodarona",
    "fda_nexterone": "Rótulo FDA amiodarona",
    "bula_ceftriaxona": "Bula ceftriaxona",
    "bula_meronem": "Bula Meronem",
    "bula_meropenem_fk": "Bula meropeném",
    "bula_ketamin": "Bula Ketamin (escetamina)",
    "bula_cetamina_biochimico": "Bula cetamina",
    "asra2018_cetamina": "ASRA 2018 (resumo)",
    "bula_fentanest": "Bula Fentanest",
    "bula_midazolam": "Bula midazolam",
    "aes2016_status": "AES 2016 (resumo)",
}


def rotulo(ref_id: str) -> str:
    return ROTULOS.get(ref_id, ref_id)

if len(REFERENCIAS) != len(_LISTA):  # pragma: no cover - proteção contra IDs duplicados
    raise RuntimeError("Há referências com ID duplicado em medicore/referencias.py")


def obter(ref_id: str) -> Referencia:
    try:
        return REFERENCIAS[ref_id]
    except KeyError as exc:  # pragma: no cover - coberto pelos testes de integridade
        raise KeyError(f"Referência desconhecida: {ref_id}") from exc
