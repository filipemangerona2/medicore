"""Guia de fármacos — conteúdo auditado em 19/10/2026.

Todos os itens estão PENDENTES DE REVISÃO CLÍNICA. O texto original de cada fármaco foi
preservado em ``original``; trechos sem fonte verificável ficaram em ``bloqueados``.
"""

from __future__ import annotations

from .conteudo import Alteracao, Farmaco, I, ItemBloqueado, Secao
from .status import Status

ORIGEM_1292114 = "commit 1292114 (versão original de 281 linhas)"
ORIGEM_B161D85 = "commit b161d85 (versão intermediária)"

# --------------------------------------------------------------------------- Noradrenalina

NORADRENALINA = Farmaco(
    id="noradrenalina",
    nome="Noradrenalina (norepinefrina)",
    classe="Vasopressor — amina simpatomimética",
    status=Status.PENDENTE,
    alertas_principais=(
        "Confirme se a dose e a concentração estão em norepinefrina BASE ou em sal (hemitartarato): a diferença é de 2 vezes.",
        "Não existe concentração universal: calcule a vazão com a concentração real da bolsa.",
    ),
    secoes=(
        Secao(
            "Apresentação e concentração",
            (
                I(
                    "A bula brasileira consultada descreve ampola de 4 mL com 8 mg de hemitartarato de norepinefrina, "
                    "equivalente a 4 mg de norepinefrina base (2 mg/mL do sal = 1 mg/mL de base).",
                    "bula_hyponor",
                ),
                I(
                    "Sempre registre se a dose e a concentração estão expressas em base ou em sal: confundir as duas "
                    "formas dobra ou reduz pela metade a dose real.",
                    "bula_hyponor",
                    alerta=True,
                ),
                I("O rótulo norte-americano descreve frasco de 4 mg em 4 mL.", "fda_levophed"),
            ),
        ),
        Secao(
            "Indicações",
            (
                I(
                    "Bula: estados hipotensivos agudos e coadjuvante no tratamento da parada cardíaca e da hipotensão profunda.",
                    "bula_hyponor",
                ),
                I("Choque séptico: vasopressor de primeira linha (recomendação forte, SSC 2026).", "ssc2026"),
                I(
                    "Choque séptico: meta inicial de PAM de 65 mmHg (forte); a partir de 65 anos, faixa inicial de "
                    "60–65 mmHg (condicional).",
                    "ssc2026",
                ),
            ),
        ),
        Secao(
            "Contraindicações (bula)",
            (
                I("Hipersensibilidade a qualquer componente da fórmula.", "bula_hyponor"),
                I(
                    "Hipotensão por déficit de volume sanguíneo, exceto como medida de emergência até a reposição volêmica.",
                    "bula_hyponor",
                ),
                I(
                    "Trombose vascular mesentérica ou periférica, salvo se o uso for considerado indispensável para salvar a vida.",
                    "bula_hyponor",
                ),
                I("Anestesia com ciclopropano ou halotano (risco de taquicardia ou fibrilação ventricular).", "bula_hyponor"),
            ),
        ),
        Secao(
            "Dose e titulação",
            (
                I(
                    "Rótulo norte-americano: dose inicial de 8 a 12 mcg/min por infusão IV e manutenção típica de 2 a "
                    "4 mcg/min, ajustando para manter o efeito hemodinâmico desejado.",
                    "fda_levophed",
                ),
                I(
                    "A bula brasileira traz a mesma manutenção (2 a 4 mcg/min de base). Ela titula pela pressão "
                    "sistólica (cerca de 80 a 100 mmHg; em hipertensos prévios, até 40 mmHg abaixo da sistólica prévia); "
                    "no choque séptico, a SSC 2026 usa a meta de PAM descrita acima.",
                    "bula_hyponor",
                    "ssc2026",
                ),
                I(
                    "A dose inicial impressa na bula consultada ('2 a 6 mg') é incompatível com a própria diluição "
                    "descrita — provável erro de unidade. Confira a bula do produto em uso.",
                    "bula_hyponor",
                    alerta=True,
                ),
                I("Ao suspender, reduzir a infusão gradualmente (bula).", "bula_hyponor"),
                I(
                    "No rótulo norte-americano, a pressão é verificada a cada 2 minutos até atingir o efeito desejado.",
                    "fda_levophed",
                ),
            ),
        ),
        Secao(
            "Diluição",
            (
                I(
                    "Bula: diluir em glicose 5%. Exemplo da bula: 1 ampola (4 mg de base) em 1.000 mL = 4 mcg/mL de "
                    "base, estável por 24 h protegida da luz e do calor.",
                    "bula_hyponor",
                ),
                I(
                    "Rótulo norte-americano: glicose 5% ou soro fisiológico com glicose 5%; administração em solução "
                    "salina isolada não é recomendada.",
                    "fda_levophed",
                    alerta=True,
                ),
                I(
                    "Concentrações mais altas (como 4 a 8 mg em 250 mL) dependem do protocolo institucional e não "
                    "constam nas fontes verificadas: use a calculadora com a concentração real.",
                    "bula_hyponor",
                    "fda_levophed",
                ),
            ),
        ),
        Secao(
            "Via de administração",
            (
                I(
                    "Choque séptico: a SSC 2026 sugere iniciar o vasopressor por via periférica em vez de atrasar até "
                    "obter acesso central (condicional, certeza muito baixa).",
                    "ssc2026",
                ),
                I(
                    "Preferir veia de grosso calibre (ex.: antecubital); evitar veias da perna em idosos e em doença "
                    "vascular oclusiva.",
                    "bula_hyponor",
                    "fda_levophed",
                ),
                I(
                    "Extravasamento pode causar necrose: vigie o local continuamente. A bula cita a fentolamina como antídoto.",
                    "bula_hyponor",
                    alerta=True,
                ),
            ),
        ),
        Secao(
            "Função renal e hepática",
            (
                I(
                    "A bula consultada não aborda ajuste em insuficiência renal ou hepática; a dose é titulada pelo efeito hemodinâmico.",
                    "bula_hyponor",
                ),
            ),
        ),
        Secao(
            "Populações especiais",
            (
                I("Idosos (> 65 anos): usar com cautela, por maior sensibilidade.", "bula_hyponor"),
                I("Crianças: segurança e eficácia não estabelecidas na bula.", "bula_hyponor"),
                I("Gestação: usar somente se absolutamente necessário.", "bula_hyponor"),
            ),
        ),
        Secao(
            "Interações e efeitos adversos",
            (
                I("IMAO e antidepressivos tricíclicos: risco de hipertensão grave e prolongada.", "bula_hyponor"),
                I(
                    "Contém bissulfito de sódio: pode causar reações alérgicas, inclusive anafilaxia, sobretudo em asmáticos.",
                    "bula_hyponor",
                ),
                I(
                    "Superdose: cefaleia pode indicar hipertensão; pode ocorrer bradicardia reflexa.",
                    "bula_hyponor",
                ),
            ),
        ),
        Secao(
            "Monitorização",
            (
                I(
                    "Pressão arterial e velocidade de infusão de forma contínua; local da infusão; pressão venosa central em doses altas.",
                    "bula_hyponor",
                ),
                I(
                    "Manter a reposição volêmica: infusão sem volume adequado pode causar vasoconstrição grave, hipóxia "
                    "tecidual e acidose láctica.",
                    "bula_hyponor",
                ),
            ),
        ),
    ),
    bloqueados=(
        ItemBloqueado(
            "Dose inicial por peso",
            "Iniciar com 0,05 a 0,1 mcg/kg/min, titulando conforme PAM.",
            ORIGEM_1292114 + " — posologia",
            "Dose inicial em mcg/kg/min não encontrada nas fontes verificadas (bula e rótulo usam mcg/min).",
        ),
        ItemBloqueado(
            "Diluente soro fisiológico isolado",
            "Diluir 4 mg a 8 mg em 250 mL de SG 5% ou SF 0,9%.",
            ORIGEM_1292114 + " — posologia",
            "O rótulo norte-americano não recomenda solução salina isolada e a bula brasileira cita glicose 5%; "
            "a faixa de 4 a 8 mg em 250 mL não consta nas fontes verificadas.",
        ),
        ItemBloqueado(
            "Indicações específicas de choque cardiogênico e anafilático",
            "Choque séptico, cardiogênico ou anafilático refratário a volume; Hipotensão grave (PAM < 65 mmHg).",
            ORIGEM_1292114 + " — indicações",
            "As fontes verificadas citam estados hipotensivos agudos (bula) e choque séptico (SSC 2026); as "
            "indicações específicas de choque cardiogênico e anafilático não foram verificadas.",
        ),
    ),
    alteracoes=(
        Alteracao(
            "Apresentação",
            "Ampola 4 mg / 4 mL (1 mg/mL)",
            "Ampola de 4 mL = 8 mg de hemitartarato = 4 mg de base; explicitar sempre sal × base",
            "Evitar erro de fator 2 entre sal e base.",
            ("bula_hyponor",),
        ),
        Alteracao(
            "Diluente",
            "SG 5% ou SF 0,9%",
            "Glicose 5% (bula); solução salina isolada não recomendada (rótulo norte-americano)",
            "Divergência com as fontes verificadas.",
            ("bula_hyponor", "fda_levophed"),
        ),
        Alteracao(
            "Dose inicial",
            "0,05 a 0,1 mcg/kg/min",
            "8 a 12 mcg/min inicial; 2 a 4 mcg/min de manutenção",
            "Única dose verificada é a do rótulo/bula, em mcg/min.",
            ("fda_levophed", "bula_hyponor"),
        ),
        Alteracao(
            "Ajuste renal",
            "Não requer ajuste na insuficiência renal.",
            "A bula não aborda ajuste renal ou hepático",
            "A afirmação original não foi encontrada nas fontes.",
            ("bula_hyponor",),
        ),
        Alteracao(
            "Acesso venoso",
            "Infusão preferencialmente em acesso venoso central.",
            "SSC 2026: iniciar por via periférica em vez de atrasar; veia de grosso calibre; vigiar extravasamento",
            "Recomendação atual da SSC 2026 para choque séptico.",
            ("ssc2026", "bula_hyponor"),
        ),
        Alteracao(
            "Contraindicações",
            "Hipotensão decorrente de hipovolemia não corrigida.",
            "Lista completa da bula (hipersensibilidade, déficit de volume, trombose mesentérica/periférica, ciclopropano/halotano)",
            "Completar com a bula.",
            ("bula_hyponor",),
        ),
    ),
    original={
        "classe": "Vasoativo / Amina Simpatomimética",
        "apresentacao": "Ampola 4 mg / 4 mL (1 mg/mL)",
        "indicacoes": "Choque séptico, cardiogênico ou anafilático refratário a volume; Hipotensão grave (PAM < 65 mmHg).",
        "contraindicacoes": "Hipotensão decorrente de hipovolemia não corrigida.",
        "posologia": "Diluir 4 mg a 8 mg em 250 mL de SG 5% ou SF 0,9%. Iniciar com 0,05 a 0,1 mcg/kg/min, titulando conforme PAM.",
        "ajuste_renal": "Não requer ajuste na insuficiência renal.",
        "cuidados": "Infusão preferencialmente em Acesso Venoso Central (AVC). Alto risco de necrose por extravasamento periférico.",
    },
    origem_original=ORIGEM_1292114,
    pendencias=(
        "Confirmar, na bula do produto padronizado na instituição, se a concentração é expressa em base ou em sal.",
        "Definir as concentrações padrão institucionais e, se adotada, a dose inicial por peso (com fonte).",
        "Conferir com o fabricante a dose inicial da bula brasileira (inconsistência de unidade).",
        "Verificar a bula no Bulário Eletrônico da Anvisa (a consultada é reprodução em site de consulta).",
    ),
)

# --------------------------------------------------------------------------- Adrenalina

ADRENALINA = Farmaco(
    id="adrenalina",
    nome="Adrenalina (epinefrina)",
    classe="Agonista adrenérgico — vasopressor, inotrópico e broncodilatador",
    status=Status.PENDENTE,
    alertas_principais=(
        "Anafilaxia: via INTRAMUSCULAR (coxa); bolus IV apenas na parada cardíaca.",
        "Mesma ampola de 1 mg/mL serve à PCR (IV/IO) e à anafilaxia (IM): confira via e dose antes de aplicar.",
    ),
    secoes=(
        Secao(
            "Apresentação",
            (I("Solução 1 mg/mL (1:1.000), ampola de 1 mL; contém bissulfito de sódio.", "bula_epinefrina"),),
        ),
        Secao(
            "Indicações (bula)",
            (
                I(
                    "Suporte hemodinâmico na parada cardiorrespiratória ou no choque; anafilaxia e choque anafilático; "
                    "crise asmática grave sem resposta às medidas habituais; também hemorragias cutâneas pequenas e "
                    "associação a anestésicos locais.",
                    "bula_epinefrina",
                ),
            ),
        ),
        Secao(
            "Contraindicações e precauções",
            (
                I(
                    "Hipersensibilidade a componentes da fórmula. A bula afirma que, em emergências, qualquer "
                    "contraindicação é relativa.",
                    "bula_epinefrina",
                ),
                I(
                    "A bula cita risco de hipertensão grave e hemorragia cerebral em pacientes em uso de betabloqueadores.",
                    "bula_epinefrina",
                    alerta=True,
                ),
                I("Não administrar na mesma via que bicarbonato.", "bula_epinefrina"),
                I(
                    "Precauções da bula: trabalho de parto (não recomendada), angina e asma de longa duração.",
                    "bula_epinefrina",
                ),
            ),
        ),
        Secao(
            "Parada cardiorrespiratória (adulto)",
            (
                I("1 mg IV/IO a cada 3 a 5 minutos (AHA 2025, classe 2a).", "aha2025_als", "aha2025_algoritmo_pcr"),
                I(
                    "Ritmo não chocável: o mais cedo possível. Ritmo chocável: após falha das tentativas iniciais de "
                    "desfibrilação — no algoritmo, depois do 2º choque.",
                    "aha2025_als",
                    "aha2025_algoritmo_pcr",
                ),
                I("Tentar acesso IV primeiro; IO se o IV falhar ou não for viável (AHA 2025).", "aha2025_als"),
                I("Epinefrina em dose alta não é recomendada de rotina (AHA 2025).", "aha2025_als"),
            ),
        ),
        Secao(
            "Anafilaxia",
            (
                I(
                    "Via IM na face anterolateral do terço médio da coxa, solução 1 mg/mL: adultos e maiores de 12 "
                    "anos, 500 mcg (0,5 mL); 6 a 12 anos, 300 mcg (0,3 mL); 6 meses a 6 anos, 150 mcg (0,15 mL); "
                    "menores de 6 meses, 100 a 150 mcg (0,1 a 0,15 mL).",
                    "rcuk2021_anafilaxia",
                ),
                I(
                    "Alternativa por peso (WAO): 0,01 mg/kg da solução 1 mg/mL, máximo de 0,5 mg no adulto e 0,3 mg na criança pré-púbere.",
                    "wao2011_anafilaxia",
                ),
                I(
                    "Repetir após 5 minutos se persistirem problemas de via aérea, respiração ou circulação (RCUK); a WAO cita intervalo de 5 a 15 minutos.",
                    "rcuk2021_anafilaxia",
                    "wao2011_anafilaxia",
                ),
                I(
                    "Anafilaxia refratária (sem resposta a 2 doses IM), em adultos e crianças: infusão IV em dose baixa — "
                    "1 mg em 100 mL de NaCl 0,9% (10 mcg/mL), iniciando a 0,5 mL/kg/h (moderada) ou 1,0 mL/kg/h "
                    "(grave, com hipotensão ou hipóxia), com apoio de terapia intensiva. Bolus IV não são "
                    "recomendados fora da parada cardíaca.",
                    "rcuk2021_anafilaxia",
                    alerta=True,
                ),
            ),
        ),
        Secao(
            "Função renal e hepática",
            (I("A bula consultada não traz orientação específica.", "bula_epinefrina"),),
        ),
        Secao(
            "Efeitos adversos e interações",
            (
                I(
                    "Comuns: ansiedade, tremor, cefaleia, palpitação, taquicardia, arritmias e hiperglicemia. Em doses "
                    "altas: arritmias graves, hipertensão súbita, hemorragia cerebral, edema pulmonar e isquemia.",
                    "bula_epinefrina",
                ),
                I(
                    "Potente causador de isquemia de extremidades; a bula cita a fentolamina para reverter o efeito.",
                    "bula_epinefrina",
                ),
                I("Uso prévio de cocaína: a bula orienta não administrar, pelo risco cardíaco.", "bula_epinefrina"),
            ),
        ),
        Secao(
            "Monitorização",
            (
                I(
                    "No paciente grave, monitorização precoce com oxímetro de pulso, ECG e pressão não invasiva (abordagem ABCDE).",
                    "rcuk_abcde",
                ),
            ),
        ),
    ),
    bloqueados=(
        ItemBloqueado(
            "Contraindicações listadas na versão original",
            "Taquiarritmias ventriculares não tratadas, glaucoma de ângulo fechado.",
            ORIGEM_1292114 + " — contraindicações",
            "Não constam na bula consultada, que considera relativas todas as contraindicações em emergências.",
        ),
        ItemBloqueado(
            "Faixa de infusão contínua",
            "Infusão: 0,05 - 1 mcg/kg/min.",
            ORIGEM_1292114 + " — posologia",
            "Faixa não verificada. O único esquema de infusão verificado é o da anafilaxia refratária (RCUK 2021).",
        ),
    ),
    alteracoes=(
        Alteracao(
            "Anafilaxia (IM)",
            "0,01 mg/kg (máx 0,5 mg) na coxa; a versão intermediária trazia 0,3 a 0,5 mg IM",
            "Doses por faixa etária (RCUK 2021) e alternativa por peso (WAO), repetição após 5 min",
            "Completar com as fontes; a WAO limita a 0,3 mg na criança pré-púbere.",
            ("rcuk2021_anafilaxia", "wao2011_anafilaxia"),
        ),
        Alteracao(
            "PCR",
            "1 mg IV/IO a cada 3-5 minutos",
            "Mantido, com momento por ritmo e preferência do acesso IV (AHA 2025)",
            "Atualização para a AHA 2025.",
            ("aha2025_als", "aha2025_algoritmo_pcr"),
        ),
        Alteracao(
            "Anafilaxia refratária",
            "(ausente)",
            "Infusão IV em dose baixa conforme RCUK 2021",
            "Escalonamento previsto na diretriz verificada.",
            ("rcuk2021_anafilaxia",),
        ),
    ),
    original={
        "classe": "Vasoativo / Inotrópico / Broncodilatador",
        "apresentacao": "Ampola 1 mg / 1 mL (1:1.000)",
        "indicacoes": "Parada cardiorrespiratória (PCR), Choque Anafilático grave, Asma grave refratária.",
        "contraindicacoes": "Taquiarritmias ventriculares não tratadas, glaucoma de ângulo fechado.",
        "posologia": "PCR: 1 mg IV/IO a cada 3-5 minutos. Anafilaxia (IM): 0,01 mg/kg (máx 0,5 mg) na coxa. Infusão: 0,05 - 1 mcg/kg/min.",
        "ajuste_renal": "Não requer ajuste renal.",
        "cuidados": "Monitorização rigorosa de ECG e FC; potencial arritmogênico elevado.",
    },
    origem_original=ORIGEM_1292114,
    pendencias=(
        "Definir protocolo institucional de infusão contínua de adrenalina fora da anafilaxia (com fonte).",
        "Verificar a atualização WAO 2020 e diretrizes brasileiras de anafilaxia (não acessadas).",
        "Confirmar a bula vigente no Bulário Eletrônico da Anvisa.",
    ),
)

# --------------------------------------------------------------------------- Amiodarona

AMIODARONA = Farmaco(
    id="amiodarona",
    nome="Amiodarona",
    classe="Antiarrítmico classe III",
    status=Status.PENDENTE,
    alertas_principais=(
        "Diluir somente em glicose 5%.",
        "Os esquemas da bula brasileira (mg/kg/dia) e do rótulo norte-americano (mg/min) são diferentes: não misture etapas.",
    ),
    secoes=(
        Secao(
            "Apresentação",
            (
                I(
                    "Cloridrato de amiodarona 50 mg/mL, ampola de 3 mL (150 mg); contém álcool benzílico e polissorbato 80.",
                    "bula_amiodarona",
                ),
            ),
        ),
        Secao(
            "Indicações",
            (
                I(
                    "Bula: distúrbios graves do ritmo, inclusive resistentes a outras terapias; taquicardia ventricular e "
                    "supraventricular sintomáticas; arritmias da síndrome de Wolff-Parkinson-White.",
                    "bula_amiodarona",
                ),
                I(
                    "PCR com FV/TV sem pulso refratária ao choque: amiodarona ou lidocaína podem ser consideradas (AHA 2025, classe 2b).",
                    "aha2025_als",
                ),
            ),
        ),
        Secao(
            "Contraindicações (bula)",
            (
                I(
                    "Hipersensibilidade ao iodo ou à amiodarona; bradicardia sinusal, bloqueio sinoatrial, doença do nó "
                    "sinusal e distúrbios graves de condução AV sem marca-passo; bloqueios bi ou trifasciculares sem "
                    "marca-passo; hipotensão grave e colapso circulatório; doença tireoidiana; associação com fármacos "
                    "que induzem torsade de pointes; gravidez (salvo exceções) e lactação.",
                    "bula_amiodarona",
                ),
                I(
                    "Essas contraindicações não se aplicam ao uso de emergência na fibrilação ventricular refratária ao choque.",
                    "bula_amiodarona",
                ),
            ),
        ),
        Secao(
            "Parada cardiorrespiratória",
            (
                I(
                    "AHA 2025: 300 mg IV/IO em bolus; segunda dose de 150 mg. No algoritmo, o antiarrítmico entra após o 3º choque.",
                    "aha2025_algoritmo_pcr",
                ),
                I(
                    "Bula brasileira: 300 mg (ou 5 mg/kg) diluídos em 20 mL de glicose 5%, em bolus; considerar 150 mg "
                    "(ou 2,5 mg/kg) adicionais se a fibrilação persistir.",
                    "bula_amiodarona",
                ),
            ),
        ),
        Secao(
            "Arritmias com pulso — dois esquemas de bula",
            (
                I(
                    "Bula brasileira: ataque de 5 mg/kg em 250 mL de glicose 5%, em 20 min a 2 h (pode repetir 2 a 3 "
                    "vezes em 24 h); manutenção de 10 a 20 mg/kg/dia (em geral 600 a 800 mg/24 h, até 1.200 mg/24 h) em "
                    "250 mL de glicose 5%.",
                    "bula_amiodarona",
                ),
                I(
                    "Rótulo norte-americano (Nexterone): 150 mg em 10 min; 360 mg nas 6 h seguintes (1 mg/min); 540 mg "
                    "nas 18 h restantes (0,5 mg/min); depois 0,5 mg/min (720 mg/24 h); bolus suplementar de 150 mg em "
                    "10 min para FV ou TV instável recorrente.",
                    "fda_nexterone",
                ),
                I(
                    "Siga o esquema adotado pelo protocolo institucional e não misture etapas de esquemas diferentes.",
                    "bula_amiodarona",
                    "fda_nexterone",
                    alerta=True,
                ),
                I(
                    "Bolus IV fora da PCR: a bula o reserva para emergências, em UTI, com ECG e PA contínuos — injeção em "
                    "no mínimo 3 minutos, sem repetir antes de 15 minutos.",
                    "bula_amiodarona",
                ),
            ),
        ),
        Secao(
            "Diluição e administração",
            (
                I(
                    "Diluir exclusivamente em glicose 5%; não usar concentração inferior a 600 mg/L; proteger da luz; "
                    "administrar em até 24 h.",
                    "bula_amiodarona",
                ),
                I(
                    "Preferir via venosa central. No rótulo norte-americano, concentrações acima de 3 mg/mL associaram-se "
                    "a flebite periférica frequente.",
                    "bula_amiodarona",
                    "fda_nexterone",
                ),
                I("Usar equipos sem DEHP; não misturar outros fármacos na mesma seringa ou linha.", "bula_amiodarona"),
            ),
        ),
        Secao(
            "Função renal e hepática",
            (
                I("Insuficiência renal: posologia habitual; não é removida por diálise.", "bula_amiodarona"),
                I(
                    "Hepatotoxicidade: dosar transaminases no início e periodicamente; reduzir ou suspender se passarem de 3 vezes o normal.",
                    "bula_amiodarona",
                ),
            ),
        ),
        Secao(
            "Populações especiais",
            (
                I(
                    "Crianças: uso não recomendado pela bula (álcool benzílico — risco de síndrome fatal em neonatos).",
                    "bula_amiodarona",
                    alerta=True,
                ),
                I("Idosos: a redução da frequência cardíaca pode ser mais acentuada.", "bula_amiodarona"),
                I("Gravidez e lactação: contraindicadas, salvo circunstâncias excepcionais na gravidez.", "bula_amiodarona"),
            ),
        ),
        Secao(
            "Interações e efeitos adversos",
            (
                I(
                    "Interações: varfarina (monitorar INR), digoxina (nível sérico e ECG), estatinas metabolizadas pelo "
                    "CYP3A4 (risco muscular), fármacos que prolongam o QT, betabloqueadores, verapamil e diltiazem "
                    "(bradicardia), fenitoína, e sofosbuvir associado a outros antivirais (bradicardia grave).",
                    "bula_amiodarona",
                ),
                I(
                    "Efeitos: hipotensão, bradicardia, bloqueios, arritmias novas, flebite, hepatotoxicidade, alterações "
                    "tireoidianas e pneumonite (rara no uso IV).",
                    "bula_amiodarona",
                ),
            ),
        ),
        Secao(
            "Monitorização",
            (
                I(
                    "ECG e pressão arterial contínuos durante o uso IV; intervalo QT e eletrólitos (sobretudo potássio); transaminases.",
                    "bula_amiodarona",
                ),
            ),
        ),
    ),
    bloqueados=(),
    alteracoes=(
        Alteracao(
            "Dose na PCR",
            "300 mg IV em bolus rápido (pode repetir 150 mg após 3-5 min)",
            "300 mg; segunda dose de 150 mg, no ciclo seguinte do algoritmo (após o 3º choque)",
            "O intervalo de 3-5 min para a 2ª dose não consta no algoritmo AHA 2025.",
            ("aha2025_algoritmo_pcr",),
        ),
        Alteracao(
            "Manutenção",
            "Manutenção: 1 mg/min por 6h",
            "Esquemas completos da bula brasileira e do rótulo norte-americano",
            "O texto original estava incompleto (omitia a fase seguinte de 0,5 mg/min por 18 h do esquema norte-americano).",
            ("bula_amiodarona", "fda_nexterone"),
        ),
        Alteracao(
            "Contraindicações",
            "Choque cardiogênico grave, bradicardia sinusal severa, BAV de alto grau sem marca-passo.",
            "Lista completa da bula e exceção para FV refratária",
            "Completar com a bula.",
            ("bula_amiodarona",),
        ),
    ),
    original={
        "classe": "Antiarrítmico Classe III",
        "apresentacao": "Ampola 150 mg / 3 mL",
        "indicacoes": "PCR por FV/TV sem pulso refratária; Taquiarritmias ventriculares e supraventriculares instáveis.",
        "contraindicacoes": "Choque cardiogênico grave, bradicardia sinusal severa, BAV de alto grau sem marca-passo.",
        "posologia": "PCR (FV/TV): 300 mg IV em bolus rápido (pode repetir 150 mg após 3-5 min). Manutenção: 1 mg/min por 6h.",
        "ajuste_renal": "Não requer ajuste renal.",
        "cuidados": "Risco de hipotensão severa e bradicardia em infusões rápidas fora de parada.",
    },
    origem_original=ORIGEM_1292114,
    pendencias=(
        "Definir qual esquema de manutenção (bula brasileira ou rótulo norte-americano) o protocolo institucional adota.",
        "Comparar com as diretrizes ERC 2025 e SBC (não comparadas em detalhe nesta revisão).",
    ),
)

# --------------------------------------------------------------------------- Ceftriaxona

CEFTRIAXONA = Farmaco(
    id="ceftriaxona",
    nome="Ceftriaxona",
    classe="Antibiótico — cefalosporina de 3ª geração",
    status=Status.PENDENTE,
    alertas_principais=(
        "Nunca diluir em solução com cálcio (Ringer, Ringer lactato/Hartmann).",
        "Neonatos: contraindicada com soluções IV que contêm cálcio.",
    ),
    secoes=(
        Secao(
            "Apresentação",
            (I("Ceftriaxona dissódica, frasco-ampola de 500 mg e 1 g (em ceftriaxona).", "bula_ceftriaxona"),),
        ),
        Secao(
            "Indicações",
            (
                I(
                    "A bula consultada descreve infecções causadas por microrganismos sensíveis à ceftriaxona, com "
                    "posologia específica para meningite em lactentes e crianças.",
                    "bula_ceftriaxona",
                ),
            ),
        ),
        Secao(
            "Contraindicações (bula)",
            (
                I("Alergia à ceftriaxona, a excipientes ou a qualquer cefalosporina.", "bula_ceftriaxona"),
                I(
                    "Neonatos prematuros até 41 semanas de idade pós-menstrual; recém-nascidos com icterícia; neonatos "
                    "(≤ 28 dias) que recebam ou devam receber soluções IV com cálcio, inclusive nutrição parenteral.",
                    "bula_ceftriaxona",
                    alerta=True,
                ),
                I(
                    "Alergia a penicilinas: não é contraindicação formal na bula consultada, mas aumenta o risco de hipersensibilidade.",
                    "bula_ceftriaxona",
                ),
                I("Soluções preparadas com lidocaína nunca devem ser administradas por via IV.", "bula_ceftriaxona", alerta=True),
            ),
        ),
        Secao(
            "Posologia (bula)",
            (
                I(
                    "Adultos e maiores de 12 anos: 1 a 2 g uma vez ao dia; em casos graves, até 4 g uma vez ao dia.",
                    "bula_ceftriaxona",
                ),
                I(
                    "Crianças de 15 dias a 12 anos: 20 a 80 mg/kg uma vez ao dia; a partir de 50 kg, dose de adulto.",
                    "bula_ceftriaxona",
                ),
                I("Recém-nascidos (abaixo de 14 dias): 20 a 50 mg/kg uma vez ao dia, sem ultrapassar 50 mg/kg.", "bula_ceftriaxona"),
                I(
                    "Meningite em lactentes e crianças: 100 mg/kg uma vez ao dia (máximo de 4 g).",
                    "bula_ceftriaxona",
                ),
            ),
        ),
        Secao(
            "Administração e compatibilidade",
            (
                I(
                    "IV lenta em 2 a 4 minutos (500 mg em 5 mL ou 1 g em 10 mL de água para injetáveis) ou infusão de "
                    "pelo menos 30 minutos; em neonatos, infusão em 60 minutos.",
                    "bula_ceftriaxona",
                ),
                I(
                    "Infusão de 2 g: dissolver em 40 mL de solução sem cálcio (NaCl 0,9%, glicose 5% ou 10%, entre outras).",
                    "bula_ceftriaxona",
                ),
                I(
                    "Adultos: não administrar simultaneamente com soluções que contêm cálcio, nem em Y; uso sequencial só "
                    "com lavagem completa da linha.",
                    "bula_ceftriaxona",
                    alerta=True,
                ),
            ),
        ),
        Secao(
            "Função renal e hepática",
            (
                I(
                    "Insuficiência renal com função hepática preservada: sem redução; com ClCr < 10 mL/min, até 2 g/dia.",
                    "bula_ceftriaxona",
                ),
                I(
                    "Insuficiência hepática com função renal preservada: sem redução. Se ambas estiverem graves: monitorar segurança e eficácia.",
                    "bula_ceftriaxona",
                ),
                I("Idosos: a bula não exige alterar as doses de adulto.", "bula_ceftriaxona"),
            ),
        ),
        Secao(
            "Advertências e monitorização",
            (
                I(
                    "Reações de hipersensibilidade graves, anemia hemolítica, colite por C. difficile, precipitados de "
                    "ceftriaxona-cálcio na vesícula (podem simular cálculos) e pancreatite.",
                    "bula_ceftriaxona",
                ),
                I(
                    "Hemograma periódico em tratamentos prolongados; com aminoglicosídeos, monitorar níveis e função renal.",
                    "bula_ceftriaxona",
                ),
            ),
        ),
    ),
    bloqueados=(
        ItemBloqueado(
            "Dose de meningite em adultos",
            "Meningite: 2 g IV de 12/12h.",
            ORIGEM_1292114 + " — posologia",
            "Dose para adultos com meningite não consta na bula consultada e a diretriz de meningite não foi acessada.",
        ),
        ItemBloqueado(
            "Lista de indicações específicas",
            "Infecções graves (pneumonia comunitária, sepse, meningite bacteriana, pielonefrite).",
            ORIGEM_1292114 + " — indicações",
            "Lista não conferida na bula acessada, que descreve infecções por microrganismos sensíveis.",
        ),
    ),
    alteracoes=(
        Alteracao(
            "Intervalo",
            "1 g a 2 g IV a cada 12 a 24 horas (máx 4 g/dia)",
            "1 a 2 g uma vez ao dia; casos graves até 4 g uma vez ao dia",
            "Conforme a bula.",
            ("bula_ceftriaxona",),
        ),
        Alteracao(
            "Cálcio",
            "Incompatível com soluções com cálcio (Ringer Lactato) em neonatos.",
            "Nunca diluir com cálcio em qualquer idade; em adultos, uso sequencial só com lavagem da linha; em neonatos, contraindicada",
            "A incompatibilidade não se limita aos neonatos.",
            ("bula_ceftriaxona",),
        ),
        Alteracao(
            "Penicilinas",
            "Contraindicação: hipersensibilidade a cefalosporinas/penicilinas",
            "Contraindicada na alergia a cefalosporinas; alergia a penicilinas = maior risco",
            "Conforme a bula consultada.",
            ("bula_ceftriaxona",),
        ),
        Alteracao(
            "Ajuste renal",
            "Não requer ajuste na insuficiência renal isolada (excreção mista biliar/renal).",
            "Sem redução se a função hepática estiver preservada; ClCr < 10 mL/min: até 2 g/dia",
            "Completar com a bula.",
            ("bula_ceftriaxona",),
        ),
    ),
    original={
        "classe": "Antibiótico / Cefalosporina de 3ª Geração",
        "apresentacao": "Frasco-ampola 1 g",
        "indicacoes": "Infecções graves (pneumonia comunitária, sepse, meningite bacteriana, pielonefrite).",
        "contraindicacoes": "Hipersensibilidade a cefalosporinas/penicilinas; neonatos com hiperbilirrubinemia.",
        "posologia": "Adultos: 1 g a 2 g IV a cada 12 a 24 horas (máx 4 g/dia). Meningite: 2 g IV de 12/12h.",
        "ajuste_renal": "Não requer ajuste na insuficiência renal isolada (excreção mista biliar/renal).",
        "cuidados": "Incompatível com soluções com cálcio (Ringer Lactato) em neonatos.",
    },
    origem_original=ORIGEM_1292114,
    pendencias=(
        "Definir a dose de meningite em adultos com base em diretriz verificada (ex.: Ministério da Saúde ou sociedade de infectologia).",
        "Confirmar a bula vigente no Bulário Eletrônico da Anvisa.",
    ),
)

# --------------------------------------------------------------------------- Meropeném

MEROPENEM = Farmaco(
    id="meropenem",
    nome="Meropeném",
    classe="Antibiótico — carbapenêmico",
    status=Status.PENDENTE,
    alertas_principais=(
        "Ajustar pela função renal quando ClCr < 51 mL/min (tabela abaixo e calculadora renal).",
        "Uso com ácido valproico/valproato não é recomendado.",
    ),
    secoes=(
        Secao(
            "Apresentação",
            (I("Frasco-ampola de 500 mg ou 1 g; reconstituído com 10 mL ou 20 mL resulta em cerca de 50 mg/mL.", "bula_meronem"),),
        ),
        Secao(
            "Posologia em adultos (bula)",
            (
                I("Dose usual: 500 mg a 1 g IV a cada 8 h (1,5 a 6 g/dia), conforme tipo e gravidade da infecção.", "bula_meronem"),
                I("Neutropenia febril: 1 g a cada 8 h.", "bula_meronem", "bula_meropenem_fk"),
                I("Meningite (ou fibrose cística): 2 g a cada 8 h.", "bula_meronem", "bula_meropenem_fk"),
                I("Pseudomonas aeruginosa: pelo menos 1 g a cada 8 h, até 6 g/dia.", "bula_meronem"),
            ),
        ),
        Secao(
            "Administração",
            (
                I("Bula: bolus IV em cerca de 5 minutos ou infusão de 15 a 30 minutos.", "bula_meronem", "bula_meropenem_fk"),
                I(
                    "Sepse e choque séptico: a SSC 2026 recomenda infusão prolongada de betalactâmicos na manutenção, "
                    "após dose de ataque (forte, certeza moderada). A duração da infusão deve seguir o protocolo institucional.",
                    "ssc2026",
                ),
            ),
        ),
        Secao(
            "Ajuste renal (bula)",
            (
                I(
                    "Ajustar quando ClCr < 51 mL/min, sobre a 'unidade de dose' (500 mg a 2 g a cada 8 h): ClCr 26–50 → "
                    "1 unidade a cada 12 h; ClCr 10–25 → ½ unidade a cada 12 h; ClCr < 10 → ½ unidade a cada 24 h.",
                    "bula_meronem",
                    "bula_meropenem_fk",
                    alerta=True,
                ),
                I("Hemodiálise e hemofiltração removem o fármaco: reiniciar a dose ao fim da sessão.", "bula_meronem"),
            ),
        ),
        Secao(
            "Função hepática e populações especiais",
            (
                I(
                    "Insuficiência hepática: sem ajuste de dose (bula); monitorar a função hepática se houver doença hepática prévia.",
                    "bula_meronem",
                    "bula_meropenem_fk",
                ),
                I("Idosos: sem ajuste se ClCr > 50 mL/min.", "bula_meronem"),
                I(
                    "Crianças de 3 meses a 12 anos: 10 a 40 mg/kg a cada 8 h; meningite, 40 mg/kg a cada 8 h; acima de 50 kg, dose de adulto.",
                    "bula_meronem",
                ),
            ),
        ),
        Secao(
            "Contraindicações, advertências e interações",
            (
                I(
                    "Contraindicado na hipersensibilidade ao meropeném ou ao carbonato de sódio; cautela se houver alergia "
                    "a carbapenêmicos, penicilinas ou outros betalactâmicos.",
                    "bula_meropenem_fk",
                ),
                I(
                    "Convulsões relatadas, mais frequentes com doença do SNC, meningite bacteriana ou insuficiência renal.",
                    "bula_meropenem_fk",
                ),
                I("Colite pseudomembranosa: considerar diante de diarreia durante o uso.", "bula_meropenem_fk"),
                I("Ácido valproico/valproato: uso concomitante não recomendado.", "bula_meropenem_fk", alerta=True),
                I("Probenecida: coadministração não recomendada.", "bula_meropenem_fk"),
            ),
        ),
    ),
    bloqueados=(
        ItemBloqueado(
            "Duração da infusão estendida",
            "1 g IV de 8/8 horas (infusão estendida em 3 horas para sepse grave).",
            ORIGEM_1292114 + " — posologia",
            "A SSC 2026 recomenda infusão prolongada, mas a duração de 3 h não foi verificada nas fontes acessadas.",
        ),
        ItemBloqueado(
            "Indicações gerais da versão original",
            "Infecções graves por multirresistentes, sepse hospitalar, neutropenia febril, meningite.",
            ORIGEM_1292114 + " — indicações",
            "Substituídas pelas indicações com dose descritas na bula; as demais não foram verificadas.",
        ),
    ),
    alteracoes=(
        Alteracao(
            "Ajuste renal",
            "Obrigatório ajustar dose se ClCr < 50 mL/min.",
            "Tabela completa da bula (ajuste quando ClCr < 51 mL/min)",
            "Completar com as faixas e doses da bula.",
            ("bula_meronem", "bula_meropenem_fk"),
        ),
        Alteracao(
            "Interações",
            "(ausente)",
            "Ácido valproico/valproato e probenecida: não recomendados",
            "Interações relevantes descritas na bula.",
            ("bula_meropenem_fk",),
        ),
        Alteracao(
            "SNC",
            "SNC: 2 g IV de 8/8h (removido na versão 0272b4a)",
            "Meningite: 2 g a cada 8 h (bula)",
            "Recuperado e confirmado na bula.",
            ("bula_meronem",),
        ),
    ),
    original={
        "classe": "Antibiótico / Carbapenêmico de Amplo Espectro",
        "apresentacao": "Frasco-ampola 500 mg e 1 g",
        "indicacoes": "Infecções graves por multirresistentes, sepse hospitalar, neutropenia febril, meningite.",
        "contraindicacoes": "Hipersensibilidade severa a carbapenêmicos.",
        "posologia": "1 g IV de 8/8 horas (infusão estendida em 3 horas para sepse grave). SNC: 2 g IV de 8/8h.",
        "ajuste_renal": "Obrigatório ajustar dose se Clearance de Creatinina (ClCr) < 50 mL/min.",
        "cuidados": "Reduz limiar convulsivo; monitorar pacientes com histórico neurológico.",
    },
    origem_original=ORIGEM_1292114,
    pendencias=(
        "Definir a duração da infusão prolongada e a dose de ataque conforme protocolo institucional (com fonte).",
        "Confirmar o detentor do registro e a versão da bula do Meronem consultada.",
    ),
)

# --------------------------------------------------------------------------- Cetamina / escetamina

CETAMINA = Farmaco(
    id="cetamina",
    nome="Cetamina / escetamina",
    classe="Anestésico dissociativo",
    status=Status.PENDENTE,
    alertas_principais=(
        "No Brasil há escetamina (S+) e cetamina com o mesmo rótulo de 50 mg/mL: confira o princípio ativo na embalagem.",
        "As bulas consultadas trazem a mesma faixa em mg/kg para os dois produtos; a equivalência de potência não foi verificada.",
    ),
    secoes=(
        Secao(
            "Apresentações verificadas",
            (
                I(
                    "Ketamin e Ketamin NP (Cristália): cloridrato de ESCETAMINA equivalente a 50 mg/mL de escetamina — "
                    "frasco de 10 mL e ampola de 2 mL sem conservante.",
                    "bula_ketamin",
                ),
                I(
                    "Cloridrato de cetamina (Instituto Biochimico/Hameln): 50 mg/mL de cetamina base, ampola de 10 mL; "
                    "a bula acessada não informa se é racêmica.",
                    "bula_cetamina_biochimico",
                ),
                I(
                    "Confira o princípio ativo antes de usar doses de outra fonte.",
                    "bula_ketamin",
                    "bula_cetamina_biochimico",
                    alerta=True,
                ),
            ),
        ),
        Secao(
            "Indicações (bula Cristália)",
            (
                I(
                    "Anestésico único em procedimentos sem necessidade de relaxamento muscular, indução anestésica, "
                    "adjuvante anestésico e outras situações listadas na bula.",
                    "bula_ketamin",
                ),
            ),
        ),
        Secao(
            "Contraindicações",
            (
                I("Absolutas (Cristália): hipersensibilidade à cetamina e porfiria.", "bula_ketamin"),
                I(
                    "Pacientes em que a elevação da pressão arterial represente risco grave (ambas as bulas).",
                    "bula_ketamin",
                    "bula_cetamina_biochimico",
                ),
                I(
                    "Relativas (Cristália): hipertensão arterial, antecedente de AVC e insuficiência cardíaca grave.",
                    "bula_ketamin",
                ),
                I(
                    "Precaução com pressão do líquor elevada (bula Cristália).",
                    "bula_ketamin",
                ),
            ),
        ),
        Secao(
            "Dose (bulas)",
            (
                I(
                    "Indução IV: 1 a 4,5 mg/kg (média de 2 mg/kg para 5 a 10 minutos de anestesia), injetada em 60 segundos.",
                    "bula_ketamin",
                    "bula_cetamina_biochimico",
                ),
                I("Indução IM: 6,5 a 13 mg/kg.", "bula_ketamin", "bula_cetamina_biochimico"),
                I("Manutenção: cada dose adicional deve ser metade da dose de indução.", "bula_ketamin"),
                I(
                    "Analgesia (consenso ASRA/AAPM/ASA 2018, por resumo secundário): bolus acima de 0,35 mg/kg ou "
                    "infusão acima de 1 mg/kg/h exigem ambiente monitorizado. Refere-se à cetamina dos EUA, não à escetamina.",
                    "asra2018_cetamina",
                ),
            ),
        ),
        Secao(
            "Advertências (bula Cristália)",
            (
                I(
                    "Reações de emergência (geralmente duram poucas horas); podem ser reduzidas com benzodiazepínico e "
                    "pouca estimulação na recuperação.",
                    "bula_ketamin",
                ),
                I(
                    "Reflexos laríngeos costumam ser mantidos, mas há risco de laringoespasmo; secreções aumentadas "
                    "(considerar antissialagogo antes da indução).",
                    "bula_ketamin",
                ),
                I("Depressão respiratória com doses altas ou injeção rápida; elevação da pressão intraocular (rara).", "bula_ketamin"),
                I("Potencial de abuso e dependência.", "bula_ketamin"),
            ),
        ),
        Secao(
            "Função renal e hepática; populações especiais",
            (
                I(
                    "As bulas consultadas não trazem ajuste renal ou hepático; o metabolismo é hepático (norcetamina).",
                    "bula_ketamin",
                ),
                I(
                    "Idosos: sem ajuste específico; menor incidência de reações de emergência acima de 65 anos.",
                    "bula_ketamin",
                ),
                I("Pediatria: estudos com 9 a 13 mg/kg IM citados na bula.", "bula_ketamin"),
            ),
        ),
        Secao(
            "Interações e monitorização",
            (
                I(
                    "Potencializa bloqueadores neuromusculares; prolonga a recuperação com anestésicos halogenados; "
                    "anti-hipertensivos e depressores do SNC aumentam o risco de hipotensão e depressão respiratória; "
                    "hormônios tireoidianos aumentam o risco de hipertensão e taquicardia.",
                    "bula_ketamin",
                ),
                I(
                    "Não misturar com diazepam ou barbitúricos na mesma seringa (precipitação/potencialização).",
                    "bula_ketamin",
                ),
                I(
                    "Monitorar sinais vitais e função cardíaca em pacientes de risco; manter equipamento de ressuscitação disponível.",
                    "bula_ketamin",
                ),
            ),
        ),
    ),
    bloqueados=(
        ItemBloqueado(
            "Contraindicações da versão original",
            "Hipertensão intracraniana grave, aneurismas, eclâmpsia grave, psicose ativa.",
            ORIGEM_1292114 + " — contraindicações",
            "Lista não confere com as bulas consultadas (que trazem porfiria, hipertensão, AVC prévio e IC grave).",
        ),
        ItemBloqueado(
            "Dose analgésica da versão original",
            "Analgesia: 0,2 a 0,5 mg/kg IV.",
            ORIGEM_1292114 + " — posologia",
            "Não verificada; o limite de bolus fora de ambiente monitorizado no consenso ASRA é 0,35 mg/kg.",
        ),
    ),
    alteracoes=(
        Alteracao(
            "Apresentação",
            "Ampola 50 mg / mL (10 mL)",
            "Distinguir escetamina (Ketamin/Ketamin NP) de cetamina",
            "Isômeros diferentes no mercado brasileiro com a mesma concentração rotulada.",
            ("bula_ketamin", "bula_cetamina_biochimico"),
        ),
        Alteracao(
            "Indução para SRI",
            "Indução SRI: 1,0 a 2,0 mg/kg IV em bolus",
            "Faixa de bula 1 a 4,5 mg/kg (média 2 mg/kg), em 60 s",
            "A faixa original está contida na faixa de bula, mas não há fonte verificada específica para SRI.",
            ("bula_ketamin", "bula_cetamina_biochimico"),
        ),
    ),
    original={
        "classe": "Anestésico / Analgésico Dissociativo",
        "apresentacao": "Ampola 50 mg / mL (10 mL)",
        "indicacoes": "Indução em Sequência Rápida de Intubação (SRI), especialmente em asmáticos ou chocados.",
        "contraindicacoes": "Hipertensão intracraniana grave, aneurismas, eclâmpsia grave, psicose ativa.",
        "posologia": "Indução SRI: 1,0 a 2,0 mg/kg IV em bolus. Analgesia: 0,2 a 0,5 mg/kg IV.",
        "ajuste_renal": "Sem alterações farmacocinéticas importantes na insuficiência renal.",
        "cuidados": "Mantém tônus simpático (aumenta PA/FC), mas pode causar sialorreia e confusão no despertar.",
    },
    origem_original=ORIGEM_1292114,
    pendencias=(
        "Farmacêutico/anestesiologista: confirmar a equivalência de dose entre escetamina e cetamina racêmica para os produtos padronizados.",
        "Definir dose para SRI e analgesia com fonte primária verificada.",
        "Verificar se a indicação 'asmáticos ou chocados' tem respaldo em diretriz.",
    ),
)

# --------------------------------------------------------------------------- Fentanil

FENTANIL = Farmaco(
    id="fentanil",
    nome="Fentanil (fentanila)",
    classe="Analgésico opioide",
    status=Status.PENDENTE,
    alertas_principais=(
        "Rigidez torácica está ligada à velocidade de injeção: aplicar lentamente.",
        "Bula consultada é de 2001: conferir a versão vigente.",
    ),
    secoes=(
        Secao(
            "Apresentação",
            (
                I(
                    "Citrato de fentanila equivalente a 0,05 mg/mL (50 mcg/mL) de fentanila base; ampolas e frascos (Fentanest).",
                    "bula_fentanest",
                ),
            ),
        ),
        Secao(
            "Indicações (bula)",
            (
                I(
                    "Analgesia de curta duração na anestesia (pré-medicação, indução e manutenção) e no pós-operatório "
                    "imediato; componente analgésico da anestesia geral; suplemento da anestesia regional.",
                    "bula_fentanest",
                ),
            ),
        ),
        Secao(
            "Contraindicações",
            (I("Intolerância conhecida ao fármaco ou aos componentes da fórmula.", "bula_fentanest"),),
        ),
        Secao(
            "Dose (bula, contexto anestésico)",
            (
                I("Pré-medicação: 50 a 100 mcg IM, 30 a 60 minutos antes da cirurgia.", "bula_fentanest"),
                I(
                    "Adjuvante da anestesia geral: dose baixa de 2 mcg/kg; moderada de 2 a 20 mcg/kg (exige ventilação "
                    "assistida ou controlada); alta de 20 a 50 mcg/kg.",
                    "bula_fentanest",
                ),
                I("Idosos e debilitados: reduzir a dose inicial.", "bula_fentanest"),
                I("Crianças de 2 a 12 anos: dose reduzida de 20 a 30 mcg para cada 10 a 12 kg.", "bula_fentanest"),
            ),
        ),
        Secao(
            "Advertências (bula)",
            (
                I(
                    "A depressão respiratória pode durar mais que a analgesia; reduzir doses subsequentes de outros opioides.",
                    "bula_fentanest",
                    alerta=True,
                ),
                I(
                    "Rigidez muscular relacionada à velocidade de injeção: injetar lentamente; se ocorrer, ventilar e "
                    "considerar bloqueador neuromuscular.",
                    "bula_fentanest",
                ),
                I(
                    "IMAO: potencialização imprevisível — suspender 2 semanas antes. Cautela em TCE, tumor cerebral, DPOC e bradiarritmias.",
                    "bula_fentanest",
                ),
            ),
        ),
        Secao(
            "Função renal e hepática",
            (
                I(
                    "Insuficiência renal ou hepática: administrar com cuidado; a bula não traz ajuste numérico.",
                    "bula_fentanest",
                ),
            ),
        ),
        Secao(
            "Interações, antídoto e monitorização",
            (
                I("Droperidol: pode causar hipotensão.", "bula_fentanest"),
                I("O fentanil aumentou em 1,5 vez a exposição ao midazolam (bula do midazolam).", "bula_midazolam"),
                I("Antídoto: naloxona.", "bula_fentanest"),
                I(
                    "Vigilância médica adequada, equipamento de ressuscitação e antagonista disponíveis.",
                    "bula_fentanest",
                ),
            ),
        ),
    ),
    bloqueados=(
        ItemBloqueado(
            "Dose para analgesia/intubação",
            "Analgesia/Intubação: 1 a 3 mcg/kg IV em bolus lento. (versão intermediária: 1 a 2 mcg/kg)",
            ORIGEM_1292114 + " e " + ORIGEM_B161D85 + " — posologia",
            "Faixa não encontrada nas fontes verificadas; a bula descreve doses para o contexto anestésico.",
        ),
        ItemBloqueado(
            "Infusão em UTI",
            "UTI: 1 a 3 mcg/kg/h.",
            ORIGEM_1292114 + " — posologia",
            "A bula não aborda infusão contínua em UTI e a diretriz de sedação/analgesia não foi acessada.",
        ),
        ItemBloqueado(
            "Ajuste renal por metabólitos",
            "Ajustar em insuficiência renal crônica grave pelo acúmulo de metabólitos.",
            ORIGEM_1292114 + " — ajuste renal",
            "A justificativa não consta nas fontes verificadas; a bula orienta apenas cautela.",
        ),
    ),
    alteracoes=(
        Alteracao(
            "Rigidez torácica",
            "Risco de rigidez torácica se infundido rapidamente em altas doses.",
            "Mantido, com conduta da bula (injeção lenta; ventilar e considerar bloqueador neuromuscular)",
            "Confirmado na bula.",
            ("bula_fentanest",),
        ),
    ),
    original={
        "classe": "Analgésico Opióide de Ação Rápida",
        "apresentacao": "Ampola 50 mcg / mL (2 mL ou 10 mL)",
        "indicacoes": "Analgesia em procedimentos de emergência, indução anestésica, suporte ventilatório em UTI.",
        "contraindicacoes": "Depressão respiratória aguda sem via aérea garantida.",
        "posologia": "Analgesia/Intubação: 1 a 3 mcg/kg IV em bolus lento. UTI: 1 a 3 mcg/kg/h.",
        "ajuste_renal": "Ajustar em insuficiência renal crônica grave pelo acúmulo de metabólitos.",
        "cuidados": "Risco de rigidez torácica ('tórax lenhoso') se infundido rapidamente em altas doses.",
    },
    origem_original=ORIGEM_1292114,
    pendencias=(
        "Obter bula vigente (a consultada é de 2001) e diretriz de analgesia/sedação em UTI para doses de infusão.",
        "Definir doses para analgesia de procedimento e intubação com fonte verificada.",
    ),
)

# --------------------------------------------------------------------------- Midazolam

MIDAZOLAM = Farmaco(
    id="midazolam",
    nome="Midazolam",
    classe="Benzodiazepínico — sedativo, hipnótico e amnésico",
    status=Status.PENDENTE,
    alertas_principais=(
        "Há ampolas de 1 mg/mL e de 5 mg/mL: confira a concentração antes de aspirar.",
        "Idosos e pacientes críticos recebem doses bem menores (ver tabela).",
    ),
    secoes=(
        Secao(
            "Apresentações (bula Fresenius Kabi)",
            (
                I("1 mg/mL (ampola de 5 mL) e 5 mg/mL (ampolas de 3 mL e 10 mL); vias IV, IM e retal.", "bula_midazolam"),
                I(
                    "A existência de duas concentrações é fonte de erro de 5 vezes na dose: identifique a ampola.",
                    "bula_midazolam",
                    alerta=True,
                ),
            ),
        ),
        Secao(
            "Indicações (bula)",
            (
                I(
                    "Sedação consciente em procedimentos; pré-medicação; indução anestésica (adultos); componente "
                    "sedativo da anestesia; sedação em UTI.",
                    "bula_midazolam",
                ),
                I(
                    "Estado de mal epiléptico: a AES 2016 inclui benzodiazepínicos (entre eles midazolam IM) na terapia "
                    "inicial e midazolam em dose anestésica na fase refratária — doses não verificadas nesta revisão.",
                    "aes2016_status",
                ),
            ),
        ),
        Secao(
            "Contraindicação",
            (I("Hipersensibilidade a benzodiazepínicos ou a excipientes.", "bula_midazolam"),),
        ),
        Secao(
            "Doses em adultos (bula)",
            (
                I(
                    "Sedação consciente IV: até 60 anos, 2 a 2,5 mg iniciais, titular com 1 mg (total 3,5 a 7,5 mg); "
                    "60 anos ou mais, debilitados ou alto risco, 0,5 a 1 mg iniciais (total < 3,5 mg). Velocidade de "
                    "cerca de 1 mg a cada 30 segundos.",
                    "bula_midazolam",
                ),
                I(
                    "Indução anestésica IV (em 20 a 30 segundos): até 60 anos, 0,2 mg/kg em pré-medicados e até 0,3 a "
                    "0,35 mg/kg sem pré-medicação; 60 anos ou mais, críticos ou alto risco, 0,05 a 0,15 mg/kg em "
                    "pré-medicados e 0,15 a 0,2 mg/kg sem pré-medicação.",
                    "bula_midazolam",
                ),
                I(
                    "Sedação em UTI: ataque de 0,03 a 0,3 mg/kg em incrementos de 1 a 2,5 mg a cada 2 minutos; "
                    "manutenção de 0,03 a 0,2 mg/kg/h.",
                    "bula_midazolam",
                ),
            ),
        ),
        Secao(
            "Função renal e hepática",
            (
                I(
                    "Insuficiência renal grave: sedação mais intensa e prolongada por acúmulo do metabólito "
                    "1'-hidroximidazolam glicuronídeo; titular com cuidado.",
                    "bula_midazolam",
                ),
                I("Insuficiência hepática: efeitos mais intensos e prolongados; pode ser preciso reduzir a dose.", "bula_midazolam"),
            ),
        ),
        Secao(
            "Advertências",
            (
                I(
                    "Depressão respiratória, apneia e parada cardiorrespiratória, sobretudo com injeção rápida, dose alta, "
                    "idosos ou doença cardiorrespiratória. Usar apenas com material de ressuscitação disponível.",
                    "bula_midazolam",
                    alerta=True,
                ),
                I("Reações paradoxais (agitação, agressividade), mais comuns em crianças e idosos.", "bula_midazolam"),
                I(
                    "Uso prolongado em UTI: dependência e abstinência — reduzir a dose gradualmente.",
                    "bula_midazolam",
                ),
            ),
        ),
        Secao(
            "Interações e antídoto",
            (
                I(
                    "Inibidores do CYP3A4 aumentam o efeito (cetoconazol cerca de 5 vezes; voriconazol 3 a 4 vezes; "
                    "ritonavir/lopinavir 5,4 vezes; eritromicina, claritromicina, diltiazem, verapamil).",
                    "bula_midazolam",
                ),
                I(
                    "Indutores do CYP3A4 reduzem o efeito (rifampicina reduziu a concentração IV em cerca de 60%; carbamazepina, fenitoína).",
                    "bula_midazolam",
                ),
                I("Opioides e outros depressores do SNC somam sedação; o fentanil aumentou a exposição em 1,5 vez.", "bula_midazolam"),
                I(
                    "Antídoto: flumazenil, com monitorização após a reversão (meia-vida curta, cerca de 1 hora).",
                    "bula_midazolam",
                ),
            ),
        ),
    ),
    bloqueados=(
        ItemBloqueado(
            "Uso em crise convulsiva refratária (dose)",
            "Indicação Principal: Sedação para IOT, controle de crise convulsiva refratária.",
            ORIGEM_B161D85 + " — indicação",
            "A indicação aparece na AES 2016 (resumo secundário), mas nenhuma dose para crises foi verificada.",
        ),
    ),
    alteracoes=(
        Alteracao(
            "Posologia",
            "0,05 a 0,15 mg/kg IV",
            "Faixa de indução da bula para ≥ 60 anos, críticos ou alto risco (com pré-medicação); tabela completa por faixa",
            "A faixa original corresponde a apenas um subgrupo da bula.",
            ("bula_midazolam",),
        ),
    ),
    original={
        "classe": "Benzodiazepínico sedativo / Hipnótico / Amnésico",
        "indicacoes": "Sedação para IOT, controle de crise convulsiva refratária.",
        "posologia": "0,05 a 0,15 mg/kg IV.",
    },
    origem_original=ORIGEM_B161D85,
    pendencias=(
        "Definir doses para crise convulsiva/estado de mal com diretriz primária verificada.",
        "Conferir as doses pediátricas na bula impressa (tabelas com células desalinhadas na extração).",
    ),
)

FARMACOS: tuple[Farmaco, ...] = (
    NORADRENALINA,
    ADRENALINA,
    AMIODARONA,
    CEFTRIAXONA,
    MEROPENEM,
    CETAMINA,
    FENTANIL,
    MIDAZOLAM,
)

FARMACOS_POR_ID: dict[str, Farmaco] = {f.id: f for f in FARMACOS}
