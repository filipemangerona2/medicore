"""Fluxogramas de urgência — conteúdo auditado em 19/10/2026.

Todos PENDENTES DE REVISÃO CLÍNICA. O texto original de cada fluxograma está em
``original``; trechos sem fonte verificável ou contrários às fontes estão em ``bloqueados``.
"""

from __future__ import annotations

from .conteudo import Alteracao, Etapa, Fluxograma, I, ItemBloqueado
from .status import Status

O_1292114 = "commit 1292114 (versão original)"
O_B161D85 = "commit b161d85 (versão intermediária)"

# --------------------------------------------------------------------------- PCR

PCR = Fluxograma(
    id="pcr",
    titulo="Parada cardiorrespiratória — adulto (ACLS)",
    publico="Adultos",
    status=Status.PENDENTE,
    etapas=(
        Etapa(
            "1. RCP de alta qualidade",
            (
                I(
                    "Compressões de pelo menos 5 cm, 100 a 120 por minuto, com retorno total do tórax e mínimo de interrupções.",
                    "aha2025_algoritmo_pcr",
                ),
                I(
                    "Sem via aérea avançada: 30 compressões para 2 ventilações. Com via aérea avançada: 1 ventilação a "
                    "cada 6 segundos (10/min) com compressões contínuas. Evitar ventilação excessiva.",
                    "aha2025_algoritmo_pcr",
                ),
                I(
                    "Trocar quem comprime a cada 2 minutos (ou antes, se cansado); usar capnografia em forma de onda; "
                    "oxigênio e monitor/desfibrilador.",
                    "aha2025_algoritmo_pcr",
                ),
            ),
        ),
        Etapa(
            "2. Checar o ritmo",
            (I("Chocável (FV/TV sem pulso) → etapa 3A. Não chocável (assistolia/AESP) → etapa 3B.", "aha2025_algoritmo_pcr"),),
        ),
        Etapa(
            "3A. Ritmo chocável (FV/TV sem pulso)",
            (
                I(
                    "Choque: bifásico na dose do fabricante (ex.: 120 a 200 J; se desconhecida, a máxima disponível); monofásico 360 J.",
                    "aha2025_algoritmo_pcr",
                ),
                I("RCP por 2 minutos e acesso IV; IO se o IV falhar ou não for viável.", "aha2025_algoritmo_pcr", "aha2025_als"),
                I(
                    "Se persistir chocável: choque → RCP 2 min → epinefrina 1 mg a cada 3 a 5 minutos (a 1ª dose após o 2º choque); considerar via aérea avançada e capnografia.",
                    "aha2025_algoritmo_pcr",
                ),
                I(
                    "Se ainda chocável: choque → RCP 2 min → amiodarona 300 mg (2ª dose 150 mg) ou lidocaína 1 a 1,5 mg/kg "
                    "(2ª dose 0,5 a 0,75 mg/kg), após o 3º choque → tratar causas reversíveis.",
                    "aha2025_algoritmo_pcr",
                    "aha2025_als",
                ),
            ),
        ),
        Etapa(
            "3B. Ritmo não chocável (assistolia/AESP)",
            (
                I("Epinefrina 1 mg o mais cedo possível; depois a cada 3 a 5 minutos.", "aha2025_algoritmo_pcr", "aha2025_als"),
                I(
                    "RCP por 2 minutos, acesso IV/IO, considerar via aérea avançada e capnografia; checar o ritmo — se "
                    "tornar-se chocável, seguir a etapa 3A.",
                    "aha2025_algoritmo_pcr",
                ),
            ),
        ),
        Etapa(
            "4. Causas reversíveis",
            (
                I(
                    "Hipovolemia, hipóxia, íon hidrogênio (acidose), hipo/hipercalemia, hipotermia, pneumotórax "
                    "hipertensivo, tamponamento cardíaco, toxinas, trombose pulmonar e trombose coronária.",
                    "aha2025_algoritmo_pcr",
                ),
            ),
        ),
        Etapa(
            "5. O que NÃO fazer de rotina (AHA 2025)",
            (
                I("Cálcio, bicarbonato de sódio e magnésio de rotina: sem benefício.", "aha2025_als", alerta=True),
                I("Vasopressina, isolada ou com epinefrina: sem vantagem sobre a epinefrina isolada.", "aha2025_als"),
                I("Epinefrina em dose alta: não recomendada de rotina.", "aha2025_als"),
                I("Corticoide: benefício incerto (classe 2b).", "aha2025_als"),
            ),
        ),
        Etapa(
            "6. Retorno da circulação espontânea",
            (I("Com retorno da circulação, iniciar os cuidados pós-parada.", "aha2025_algoritmo_pcr"),),
        ),
    ),
    bloqueados=(
        ItemBloqueado(
            "Limite superior de profundidade",
            "Iniciar RCP de Alta Qualidade: 100-120 bpm, profundidade 5-6 cm, retorno total do tórax.",
            O_B161D85,
            "O algoritmo AHA 2025 consultado indica 'pelo menos 5 cm'; o limite superior de 6 cm não foi verificado.",
        ),
        ItemBloqueado(
            "Momento da amiodarona",
            "FV / TV sem pulso: Choque imediato ➔ RCP por 2 min ➔ Adrenalina a cada 3-5 min ➔ Amiodarona no 2º choque.",
            O_B161D85,
            "Contraria o algoritmo AHA 2025: a epinefrina entra após o 2º choque e o antiarrítmico após o 3º.",
        ),
    ),
    alteracoes=(
        Alteracao(
            "Frequência das compressões",
            "100-120 bpm",
            "100 a 120 compressões por minuto",
            "'bpm' (batimentos por minuto) é unidade de frequência cardíaca, não de compressões.",
            ("aha2025_algoritmo_pcr",),
        ),
        Alteracao(
            "Sequência do ritmo chocável",
            "Amiodarona no 2º choque",
            "Epinefrina após o 2º choque; amiodarona ou lidocaína após o 3º",
            "Alinhar ao algoritmo AHA 2025.",
            ("aha2025_algoritmo_pcr",),
        ),
        Alteracao(
            "Acesso vascular",
            "Adrenalina 1 mg IV/IO",
            "Tentar IV primeiro; IO se o IV falhar ou não for viável",
            "Recomendação AHA 2025 (classe 1).",
            ("aha2025_als",),
        ),
        Alteracao(
            "Itens novos",
            "(ausentes)",
            "Energia do choque, lidocaína como alternativa, causas reversíveis por extenso e o que não fazer de rotina",
            "Completar o fluxo com o algoritmo e as recomendações AHA 2025.",
            ("aha2025_algoritmo_pcr", "aha2025_als"),
        ),
    ),
    original=(
        "1292114: 1. Iniciar RCP de alta qualidade imediata (100-120 bpm). 2. Checar ritmo: Chocável (FV/TV) vs Não "
        "Chocável (AESP/Assistolia). 3. Adrenalina 1 mg IV/IO a cada 3-5 minutos. 4. Investigar 5 H's e 5 T's. | "
        "b161d85: 1. Checar Segurança e Responsividade -> Chamar ajuda / Trazer desfibrilador. 2. Iniciar RCP de Alta "
        "Qualidade: 100-120 bpm, profundidade 5-6 cm, retorno total do tórax. 3. Checar Ritmo: FV/TV sem pulso: Choque "
        "imediato ➔ RCP por 2 min ➔ Adrenalina a cada 3-5 min ➔ Amiodarona no 2º choque. Asistolia/AESP: RCP imediata ➔ "
        "Adrenalina precoce ➔ Investigar 5 Hs e 5 Ts."
    ),
    origem_original=f"{O_1292114} e {O_B161D85}",
    pendencias=(
        "Comparar com as diretrizes ERC 2025 e com a diretriz brasileira de RCP (SBC 2019, a mais recente localizada).",
        "Incluir cuidados pós-parada (AHA 2025, Parte 11) após verificação.",
    ),
    divergencias=(
        "Adotada a AHA 2025 como referência principal (base do curso ACLS). A ERC 2025 não foi comparada em detalhe nesta revisão.",
    ),
)

# --------------------------------------------------------------------------- SRI

SRI = Fluxograma(
    id="sri",
    titulo="Intubação em sequência rápida — adulto crítico",
    publico="Adultos",
    status=Status.PENDENTE,
    etapas=(
        Etapa(
            "1. Preparação",
            (
                I("Usar checklist e compartilhar com a equipe o plano para falha da intubação.", "das2018_uti"),
                I("Otimizar o sistema cardiovascular antes da indução.", "das2018_uti"),
            ),
        ),
        Etapa(
            "2. Pré-oxigenação",
            (
                I("Máscara facial, CPAP, VNI ou oxigênio nasal; cabeceira elevada se possível.", "das2018_uti"),
                I(
                    "Cateter nasal de alto fluxo quando a laringoscopia for prevista como difícil (SCCM, condicional).",
                    "sccm2023_sri",
                ),
                I("Ventilação não invasiva se PaO₂/FiO₂ < 150 (SCCM, condicional).", "sccm2023_sri"),
            ),
        ),
        Etapa(
            "3. Indução e bloqueio neuromuscular",
            (
                I(
                    "Administrar bloqueador neuromuscular sempre que usar indutor sedativo-hipnótico (SCCM, forte).",
                    "sccm2023_sri",
                ),
                I(
                    "Sem diferença entre etomidato e outros indutores em mortalidade, hipotensão ou uso de vasopressor (SCCM, condicional).",
                    "sccm2023_sri",
                ),
                I(
                    "Rocurônio ou succinilcolina, se não houver contraindicação à succinilcolina (SCCM, condicional).",
                    "sccm2023_sri",
                ),
                I(
                    "Doses dos indutores: ver o guia de fármacos (cetamina/escetamina, midazolam, fentanil). Doses de "
                    "bloqueadores neuromusculares não foram verificadas nesta revisão.",
                    "bula_ketamin",
                    "bula_midazolam",
                    alerta=True,
                ),
            ),
        ),
        Etapa(
            "4. Laringoscopia (Plano A)",
            (
                I(
                    "Vídeo ou laringoscopia direta, com ou sem bougie/estilete; manipulação laríngea externa; retirar a "
                    "pressão cricoide, se aplicada, diante de dificuldade.",
                    "das2018_uti",
                ),
                I(
                    "Entre as tentativas, manter a oxigenação (oxigênio nasal contínuo e ventilação com máscara).",
                    "das2018_uti",
                ),
                I(
                    "No máximo 3 tentativas, trocando dispositivo, tamanho ou operador; 1 tentativa extra por especialista, se apropriado.",
                    "das2018_uti",
                    alerta=True,
                ),
                I(
                    "A DAS 2025 indica videolaringoscopia como primeira escolha onde disponível (segundo resumo secundário).",
                    "das2025",
                ),
            ),
        ),
        Etapa(
            "5. Confirmar a posição do tubo",
            (I("Confirmar com capnografia em forma de onda.", "das2018_uti", "aha2025_algoritmo_pcr"),),
        ),
        Etapa(
            "6. Falha — Planos B, C e D",
            (
                I(
                    "Planos B/C: dispositivo supraglótico de 2ª geração ou ventilação com máscara a duas pessoas com "
                    "adjuntos, mantendo a oxigenação.",
                    "das2018_uti",
                ),
                I(
                    "Plano D — 'não intubo, não oxigeno': declarar a situação, pedir ajuda, estender o pescoço, garantir "
                    "bloqueio neuromuscular e fazer acesso cirúrgico frontal do pescoço sem demora.",
                    "das2018_uti",
                    "das2025",
                    alerta=True,
                ),
                I(
                    "Técnica bisturi-bougie-tubo: lâmina larga (nº 10 ou 20), bougie de até 14 Fr e tubo com balonete "
                    "de 5,0 a 6,0 mm; confirmar com capnografia.",
                    "das2018_uti",
                ),
            ),
        ),
        Etapa(
            "7. Pós-intubação",
            (
                I(
                    "Aspiração traqueal, manobra de recrutamento se estável, radiografia de tórax, vigiar complicações, "
                    "documentar e registrar alerta de via aérea.",
                    "das2018_uti",
                ),
            ),
        ),
    ),
    bloqueados=(
        ItemBloqueado(
            "Pré-medicação como etapa de rotina",
            "Os 7 Ps da SRI: Preparo, Pré-oxigenação, Premedicação, Paralisação com Indução (Ex: Cetamina + Rocurônio), "
            "Posicionamento, Passagem do Tubo e Pós-intubação.",
            O_1292114,
            "A pré-medicação de rotina não aparece nas fontes verificadas (SCCM 2023, DAS 2018); a etapa foi retirada até revisão.",
        ),
    ),
    alteracoes=(
        Alteracao(
            "Estrutura",
            "7 Ps (mnemônico sem fonte citada)",
            "Etapas da DAS 2018 para o paciente crítico, com recomendações da SCCM 2023",
            "Organizar o fluxo por diretrizes verificadas, incluindo o caminho de falha (planos B a D).",
            ("das2018_uti", "sccm2023_sri"),
        ),
        Alteracao(
            "Indução",
            "Ex: Cetamina + Rocurônio",
            "Indutor + bloqueador neuromuscular obrigatório; sem diferença entre etomidato e outros indutores; rocurônio ou succinilcolina",
            "Recomendações SCCM 2023.",
            ("sccm2023_sri",),
        ),
    ),
    original=(
        "1292114: Os 7 Ps da SRI: Preparo, Pré-oxigenação, Premedicação, Paralisação com Indução (Ex: Cetamina + "
        "Rocurônio), Posicionamento, Passagem do Tubo e Pós-intubação."
    ),
    origem_original=O_1292114,
    pendencias=(
        "Definir doses de bloqueadores neuromusculares e indutores com bula/diretriz verificada.",
        "Ler o texto integral da DAS 2025 e da SCCM 2023 (apenas resumos foram acessados).",
        "Verificar recomendações brasileiras (SBA/ABRAMEDE) não consultadas.",
    ),
)

# --------------------------------------------------------------------------- Crise hipertensiva

CRISE_HIPERTENSIVA = Fluxograma(
    id="crise_hipertensiva",
    titulo="Pressão arterial muito elevada (crise hipertensiva)",
    publico="Adultos",
    status=Status.PENDENTE,
    etapas=(
        Etapa(
            "1. Procurar lesão aguda de órgão-alvo",
            (
                I(
                    "A emergência hipertensiva é definida pela lesão aguda de órgão-alvo (coração, retina, cérebro, rins, "
                    "grandes artérias), não por um valor isolado de PA.",
                    "esc2019_has",
                ),
                I(
                    "A Diretriz Brasileira de Hipertensão Arterial 2025 tem capítulo próprio sobre crise hipertensiva, que "
                    "NÃO pôde ser lido nesta revisão: confira-o antes de usar este fluxograma.",
                    "sbc2025_has",
                    alerta=True,
                ),
            ),
        ),
        Etapa(
            "2A. Sem lesão aguda de órgão-alvo",
            (
                I(
                    "A ESC 2019 desaconselha o termo 'urgência hipertensiva': tratar com anti-hipertensivo oral ou ajustar o "
                    "esquema, com observação breve.",
                    "esc2019_has",
                ),
                I("Não reduzir a PA rapidamente; não usar nifedipino de ação curta.", "esc2019_has", alerta=True),
                I("Se for acrescentado medicamento, observar por pelo menos 2 horas.", "esc2019_has"),
            ),
        ),
        Etapa(
            "2B. Com lesão aguda (emergência hipertensiva)",
            (
                I(
                    "Redução imediata, porém controlada, em ambiente monitorizado, com fármacos IV. Quedas da PAM acima "
                    "de 50% associaram-se a AVC isquêmico e morte.",
                    "esc2019_has",
                    alerta=True,
                ),
            ),
        ),
        Etapa(
            "3. Metas por apresentação (ESC 2019, Tabela 3)",
            (
                I(
                    "Hipertensão maligna (com ou sem microangiopatia trombótica ou insuficiência renal aguda): reduzir a PAM em 20–25% em várias horas.",
                    "esc2019_has",
                ),
                I("Encefalopatia hipertensiva: reduzir a PAM em 20–25% imediatamente.", "esc2019_has"),
                I(
                    "AVC isquêmico com PA > 220/120 mmHg: reduzir a PAM em 15% em 1 h. Com indicação de trombólise: PA < 185/110 mmHg antes da trombólise.",
                    "esc2019_has",
                ),
                I("AVC hemorrágico com PAS > 180 mmHg: PAS entre 130 e 180 mmHg, imediatamente.", "esc2019_has"),
                I("Síndrome coronariana aguda: PAS < 140 mmHg, imediatamente (1ª escolha: nitroglicerina).", "esc2019_has"),
                I(
                    "Edema agudo de pulmão cardiogênico: PAS < 140 mmHg, imediatamente (nitroprussiato ou nitroglicerina com diurético de alça).",
                    "esc2019_has",
                ),
                I(
                    "Doença aguda da aorta: PAS < 120 mmHg e FC < 60 bpm, imediatamente (esmolol associado a vasodilatador).",
                    "esc2019_has",
                    alerta=True,
                ),
                I(
                    "Eclâmpsia, pré-eclâmpsia grave ou HELLP: PA < 160/105 mmHg, imediatamente (com sulfato de magnésio).",
                    "esc2019_has",
                ),
            ),
        ),
    ),
    bloqueados=(
        ItemBloqueado(
            "Prazo de redução e monitorização invasiva",
            "Urgência: Redução gradual da PA ao longo de 24-48h com medicação oral. Emergência: Internação em UTI, "
            "monitorização invasiva e uso de drogas vasoativas endovenosas (ex: Nitroprussiato ou Nitroglicerina).",
            O_B161D85,
            "O prazo de 24–48 h e a monitorização invasiva de rotina não constam na fonte verificada; a escolha do "
            "fármaco IV depende da apresentação (ver metas).",
        ),
        ItemBloqueado(
            "Doses de anti-hipertensivos IV",
            "(não havia doses na versão original)",
            "auditoria",
            "A tabela de doses da fonte verificada tem erros de unidade corrigidos por errata não acessada: nenhuma dose foi incluída.",
        ),
    ),
    alteracoes=(
        Alteracao(
            "Terminologia",
            "Urgência × Emergência hipertensiva",
            "Elevação grave sem lesão aguda × emergência hipertensiva (a ESC 2019 desaconselha o termo 'urgência')",
            "Alinhar à fonte verificada.",
            ("esc2019_has",),
        ),
        Alteracao(
            "Metas",
            "(ausentes)",
            "Metas e prazos por apresentação clínica",
            "Pontos de decisão objetivos.",
            ("esc2019_has",),
        ),
    ),
    original=(
        "1292114: Crise Hipertensiva: Distinguir Urgência (sem lesão de órgão-alvo, tratamento oral gradual) de Emergência "
        "(com lesão de órgão-alvo aguda, internação em UTI e drogas venosas). | b161d85: 1. Diferenciar: Urgência "
        "Hipertensiva vs. Emergência Hipertensiva (presença de lesão de órgão-alvo aguda). 2. Urgência: Redução gradual da PA "
        "ao longo de 24-48h com medicação oral. 3. Emergência: Internação em UTI, monitorização invasiva e uso de drogas "
        "vasoativas endovenosas (ex: Nitroprussiato ou Nitroglicerina)."
    ),
    origem_original=f"{O_1292114} e {O_B161D85}",
    pendencias=(
        "PRIORITÁRIO: conciliar com o capítulo 11 da Diretriz Brasileira de Hipertensão Arterial 2025 (SBC/SBH/SBN), que não pôde ser lido.",
        "Conferir com as diretrizes ESC 2024 e AHA/ACC 2025, mais recentes que a fonte usada (2019).",
        "Definir fármacos IV e doses disponíveis no Brasil com bula vigente.",
    ),
    divergencias=(
        "A fonte verificada é de 2019; existem diretrizes mais recentes (SBC 2025, ESC 2024, AHA/ACC 2025) cujas seções de crise hipertensiva não foram lidas.",
        "Na própria fonte, o texto diz que a redução da PA no AVC isquêmico em geral é evitada, enquanto a Tabela 3 "
        "prevê redução de 15% se PA > 220/120 mmHg: o revisor clínico deve conciliar.",
    ),
)

# --------------------------------------------------------------------------- Anafilaxia

ANAFILAXIA = Fluxograma(
    id="anafilaxia",
    titulo="Anafilaxia",
    publico="Adultos e crianças",
    status=Status.PENDENTE,
    etapas=(
        Etapa(
            "1. Adrenalina IM imediatamente",
            (
                I(
                    "Face anterolateral do terço médio da coxa, solução 1 mg/mL: adultos e maiores de 12 anos 500 mcg "
                    "(0,5 mL); 6 a 12 anos 300 mcg (0,3 mL); 6 meses a 6 anos 150 mcg (0,15 mL); menores de 6 meses "
                    "100 a 150 mcg (0,1 a 0,15 mL).",
                    "rcuk2021_anafilaxia",
                    alerta=True,
                ),
                I(
                    "Alternativa por peso: 0,01 mg/kg, máximo 0,5 mg no adulto e 0,3 mg na criança pré-púbere.",
                    "wao2011_anafilaxia",
                ),
            ),
        ),
        Etapa(
            "2. Repetir se não houver melhora",
            (
                I(
                    "Repetir a adrenalina IM após 5 minutos se persistirem problemas de via aérea, respiração ou "
                    "circulação (RCUK); a WAO cita 5 a 15 minutos.",
                    "rcuk2021_anafilaxia",
                    "wao2011_anafilaxia",
                ),
            ),
        ),
        Etapa(
            "3. Medidas de suporte",
            (
                I(
                    "Avaliação ABCDE, oxigênio e acesso venoso. Fluidos: adultos 500 a 1.000 mL (até 3 a 5 L no choque "
                    "grave); crianças 10 mL/kg; usar cristaloide sem glicose com sódio de 130 a 154 mmol/L.",
                    "rcuk2021_anafilaxia",
                ),
            ),
        ),
        Etapa(
            "4. Anafilaxia refratária (sem resposta a 2 doses IM)",
            (
                I("Chamar suporte de terapia intensiva e ajuda especializada precocemente.", "rcuk2021_anafilaxia"),
                I(
                    "Infusão IV de adrenalina em dose baixa: 1 mg em 100 mL de NaCl 0,9% (10 mcg/mL), iniciando a "
                    "0,5 mL/kg/h (moderada) ou 1,0 mL/kg/h (grave, com hipotensão ou hipóxia). Se não for possível "
                    "infundir com segurança, repetir a dose IM a cada 5 minutos.",
                    "rcuk2021_anafilaxia",
                ),
                I("Bolus IV de adrenalina: apenas na parada cardíaca.", "rcuk2021_anafilaxia", alerta=True),
            ),
        ),
        Etapa(
            "5. Tratamentos que NÃO são de primeira linha",
            (
                I(
                    "Anti-histamínicos não fazem parte do tratamento inicial e não podem atrasar a adrenalina; corticoide de rotina não é aconselhado.",
                    "rcuk2021_anafilaxia",
                ),
            ),
        ),
        Etapa(
            "6. Observação",
            (
                I(
                    "Alta precoce (2 h após a resolução) só com boa resposta a 1 dose e demais critérios do RCUK; pelo "
                    "menos 6 h se forem necessárias 2 doses ou houver reação bifásica prévia; pelo menos 12 h em reações "
                    "graves, com mais de 2 doses ou comprometimento respiratório grave.",
                    "rcuk2021_anafilaxia",
                ),
            ),
        ),
    ),
    bloqueados=(),
    alteracoes=(
        Alteracao(
            "Dose de adrenalina",
            "Adrenalina IM imediata (0,01 mg/kg, máx 0,5 mg) na coxa anterolateral",
            "Mantida (WAO) e complementada com doses por idade (RCUK 2021)",
            "A dose por peso tem limite de 0,3 mg na criança pré-púbere.",
            ("wao2011_anafilaxia", "rcuk2021_anafilaxia"),
        ),
        Alteracao(
            "Repetição",
            "Repetir a cada 5-15 min",
            "Repetir após 5 min se persistirem problemas A/B/C (RCUK); WAO 5 a 15 min",
            "Detalhar o critério de repetição.",
            ("rcuk2021_anafilaxia", "wao2011_anafilaxia"),
        ),
        Alteracao(
            "Fluidos",
            "Acesso venoso calibroso e expansão volêmica com cristaloides",
            "Volumes de bolus para adultos e crianças (RCUK)",
            "Critério objetivo de volume.",
            ("rcuk2021_anafilaxia",),
        ),
        Alteracao(
            "Escalonamento",
            "(ausente)",
            "Anafilaxia refratária, papel dos anti-histamínicos/corticoides e observação",
            "Caminho de falha terapêutica.",
            ("rcuk2021_anafilaxia",),
        ),
    ),
    original=(
        "1292114: Choque Anafilático: Adrenalina IM imediata (0,01 mg/kg, máx 0,5 mg) na coxa anterolateral. Repetir a "
        "cada 5-15 min. Acesso venoso calibroso e expansão volêmica com cristaloides."
    ),
    origem_original=O_1292114,
    pendencias=(
        "Conferir a atualização WAO 2020 e o material da ASBAI (não acessados).",
        "A RCUK previa revisão da diretriz em maio/2026: confirmar se há versão nova.",
    ),
    divergencias=(
        "Intervalo de repetição: RCUK 5 min × WAO 5 a 15 min. Exibidos os dois; o RCUK é mais recente (2021).",
    ),
)

# --------------------------------------------------------------------------- Sepse

SEPSE = Fluxograma(
    id="sepse",
    titulo="Sepse e choque séptico — adulto",
    publico="Adultos",
    status=Status.PENDENTE,
    etapas=(
        Etapa(
            "1. Rastreio",
            (
                I(
                    "Em pacientes internados, usar NEWS, NEWS2, MEWS ou SIRS — e não o qSOFA isolado — como ferramenta de rastreio (forte).",
                    "ssc2026",
                ),
            ),
        ),
        Etapa(
            "2. Exames iniciais",
            (
                I("Dosar lactato sérico (condicional).", "ssc2026"),
                I("Hemoculturas o mais cedo possível, idealmente antes dos antimicrobianos (forte).", "ssc2026"),
            ),
        ),
        Etapa(
            "3. Antimicrobianos",
            (
                I(
                    "Choque séptico ou sepse provável/definida: iniciar imediatamente, idealmente em até 1 hora do reconhecimento (forte).",
                    "ssc2026",
                    alerta=True,
                ),
                I(
                    "Sepse possível sem choque: investigação rápida e limitada no tempo; se a suspeita persistir, iniciar em até 3 horas (condicional).",
                    "ssc2026",
                ),
                I(
                    "Betalactâmicos: infusão prolongada na manutenção, após dose de ataque (forte).",
                    "ssc2026",
                ),
            ),
        ),
        Etapa(
            "4. Fluidos",
            (
                I(
                    "Hipoperfusão induzida por sepse ou choque séptico: pelo menos 30 mL/kg de cristaloide IV nas primeiras "
                    "3 horas, individualizando (condicional). Com IMC > 30 kg/m², usar peso ajustado ou ideal.",
                    "ssc2026",
                ),
                I(
                    "Preferir cristaloide balanceado ao soro fisiológico (condicional; exceção: lesão cerebral traumática). "
                    "Não usar amidos (forte) nem gelatinas (condicional).",
                    "ssc2026",
                ),
            ),
        ),
        Etapa(
            "5. Vasopressor",
            (
                I("Noradrenalina como primeira escolha (forte).", "ssc2026"),
                I(
                    "Pode ser iniciada por via periférica em vez de atrasar até obter acesso central (condicional).",
                    "ssc2026",
                ),
                I(
                    "Meta inicial de PAM 65 mmHg (forte); a partir de 65 anos, faixa de 60–65 mmHg (condicional).",
                    "ssc2026",
                ),
            ),
        ),
        Etapa(
            "6. Escalonamento (choque refratário)",
            (
                I("Com doses crescentes de noradrenalina: associar vasopressina (condicional, certeza moderada).", "ssc2026"),
                I(
                    "Vasopressina — rótulo norte-americano: iniciar com 0,01 UI/min e titular 0,005 UI/min a cada 10 a 15 "
                    "min, na faixa de 0,01 a 0,07 UI/min. A bula brasileira não foi consultada.",
                    "fda_vasostrict",
                ),
                I(
                    "PAM inadequada com noradrenalina + vasopressina: associar adrenalina (condicional).",
                    "ssc2026",
                ),
                I(
                    "Disfunção cardíaca com hipoperfusão persistente: inotrópico (dobutamina + noradrenalina ou adrenalina isolada) (condicional).",
                    "ssc2026",
                ),
                I(
                    "Choque séptico: corticoide IV sugerido (condicional, baixa certeza). Dose e critério de início não "
                    "verificados nesta revisão — seguir protocolo institucional.",
                    "ssc2026",
                    alerta=True,
                ),
            ),
        ),
        Etapa(
            "7. Reavaliação",
            (
                I("Lactato seriado para guiar a ressuscitação (condicional).", "ssc2026"),
                I("Tempo de enchimento capilar como adjunto de outras medidas de perfusão (condicional).", "ssc2026"),
            ),
        ),
    ),
    bloqueados=(
        ItemBloqueado(
            "qSOFA como critério de reconhecimento",
            "Reconhecimento Imediato: Avaliar critérios qSOFA ou SOFA e sinais de hipoperfusão (lactato > 2 mmol/L).",
            O_B161D85,
            "A SSC 2026 recomenda NÃO usar o qSOFA isolado como ferramenta de rastreio; o limiar de lactato > 2 mmol/L não foi verificado.",
        ),
        ItemBloqueado(
            "Hemoculturas — limite de tempo",
            "Hemoculturas (antes do antibiótico se não atrasar > 45 min)",
            O_B161D85,
            "O limite de 45 minutos não foi verificado na SSC 2026, que recomenda coletar o mais cedo possível, idealmente antes do antimicrobiano.",
        ),
        ItemBloqueado(
            "Critério de lactato para volume",
            "30 mL/kg de cristaloide em caso de hipotensão ou lactato ≥ 4.",
            O_B161D85,
            "A SSC 2026 usa 'hipoperfusão induzida por sepse ou choque séptico'; o limiar de lactato ≥ 4 não foi verificado.",
        ),
        ItemBloqueado(
            "Vasopressina em dose fixa e limiar de noradrenalina",
            "PAM < 65 mmHg apesar de volume adequado (30 mL/kg) e Noradrenalina > 0.25 mcg/kg/min: Adicionar Vasopressina (0.04 UI/min fixo).",
            "commit 1292114 — aba 'RAG' (texto fixo)",
            "O limiar de noradrenalina não foi verificado; o rótulo verificado prevê vasopressina titulada a partir de 0,01 UI/min, não dose fixa.",
        ),
        ItemBloqueado(
            "Dose de hidrocortisona",
            "Avaliar corticoterapia de suporte (Hidrocortisona 200 mg/dia).",
            "commit 1292114 — aba 'RAG' (texto fixo)",
            "A SSC 2026 sugere corticoide, mas a dose não constava nos trechos verificados.",
        ),
    ),
    alteracoes=(
        Alteracao(
            "Rastreio",
            "qSOFA ou SOFA",
            "NEWS/NEWS2/MEWS ou SIRS, não qSOFA isolado",
            "Recomendação forte da SSC 2026.",
            ("ssc2026",),
        ),
        Alteracao(
            "Antimicrobiano",
            "Na primeira hora",
            "1 h no choque/sepse provável; até 3 h na sepse possível sem choque",
            "Estratificação da SSC 2026.",
            ("ssc2026",),
        ),
        Alteracao(
            "Escalonamento",
            "Texto fixo da aba 'RAG' com relevância fictícia de 99,2%",
            "Escalonamento com recomendações SSC 2026 e rótulo da vasopressina",
            "A aba 'RAG' era simulada; o conteúdo foi incorporado a este fluxograma com fontes.",
            ("ssc2026", "fda_vasostrict"),
        ),
        Alteracao(
            "Meta de PAM em idosos",
            "(ausente)",
            "60–65 mmHg a partir de 65 anos",
            "Recomendação nova da SSC 2026.",
            ("ssc2026",),
        ),
    ),
    original=(
        "b161d85: 1. Reconhecimento Imediato: Avaliar critérios qSOFA ou SOFA e sinais de hipoperfusão (lactato > 2 "
        "mmol/L). 2. Coleta de Exames: Lactato sérico, hemoculturas (antes do antibiótico se não atrasar > 45 min), "
        "hemograma, função renal, coagulograma. 3. Antibioticoterapia Precoce: Administrar antibiótico de largo espectro na "
        "primeira hora. 4. Reposição Volêmica: 30 mL/kg de cristaloide em caso de hipotensão ou lactato ≥ 4. 5. Drogas "
        "Vasoativas: Se persistir PAM < 65 mmHg após volume, iniciar Noradrenalina como primeira escolha. | 1292114 (aba "
        "RAG, texto fixo): Critério: PAM < 65 mmHg apesar de volume adequado (30 mL/kg) e Noradrenalina > 0.25 "
        "mcg/kg/min. Conduta Imediata: Adicionar Vasopressina (0.04 UI/min fixo) e avaliar corticoterapia de suporte "
        "(Hidrocortisona 200 mg/dia)."
    ),
    origem_original=f"{O_B161D85} e {O_1292114}",
    pendencias=(
        "Ler o texto integral da SSC 2026 para dose/critério do corticoide e limiar de noradrenalina para vasopressina.",
        "Consultar a bula brasileira de vasopressina.",
        "Comparar com protocolos brasileiros (ILAS/AMIB), não consultados.",
    ),
)

# --------------------------------------------------------------------------- ABCDE

ABCDE = Fluxograma(
    id="abcde",
    titulo="Avaliação ABCDE do paciente grave",
    publico="Adultos",
    status=Status.PENDENTE,
    etapas=(
        Etapa(
            "Princípios",
            (
                I(
                    "Avaliação inicial completa e reavaliação frequente; tratar o que ameaça a vida antes de passar à "
                    "etapa seguinte; avaliar o efeito de cada tratamento; pedir ajuda cedo; dividir tarefas na equipe.",
                    "rcuk_abcde",
                ),
                I(
                    "Paciente sem resposta e sem respiração normal: iniciar RCP (ver fluxograma de PCR).",
                    "rcuk_abcde",
                    alerta=True,
                ),
                I(
                    "Monitorizar cedo: oxímetro de pulso, ECG e pressão não invasiva; acesso venoso.",
                    "rcuk_abcde",
                ),
            ),
        ),
        Etapa(
            "A — Via aérea",
            (
                I("Obstrução de via aérea é emergência: pedir ajuda especializada imediatamente.", "rcuk_abcde"),
                I(
                    "Oxigênio em alta concentração; alvo de SpO₂ 94–98% na insuficiência respiratória aguda, ou 88–92% "
                    "se houver risco de insuficiência respiratória hipercápnica.",
                    "rcuk_abcde",
                ),
            ),
        ),
        Etapa(
            "B — Respiração",
            (
                I(
                    "Frequência respiratória normal de 12 a 20/min; acima de 25/min ou em elevação indica gravidade. A "
                    "oximetria não detecta hipercapnia.",
                    "rcuk_abcde",
                ),
                I("Ventilação com bolsa-máscara se a respiração for inadequada.", "rcuk_abcde"),
            ),
        ),
        Etapa(
            "C — Circulação",
            (
                I(
                    "Considerar hipovolemia como causa de choque até prova em contrário. Tempo de enchimento capilar "
                    "normal < 2 s; débito urinário < 0,5 mL/kg/h sugere baixo débito.",
                    "rcuk_abcde",
                ),
                I(
                    "Hipotensão: bolus de 500 mL de cristaloide em menos de 15 minutos (250 mL se insuficiência cardíaca "
                    "ou trauma); reavaliar FC e PA a cada 5 minutos; se a PA habitual for desconhecida, buscar PAS > 100 mmHg.",
                    "rcuk_abcde",
                ),
                I("Suspender ou reduzir fluidos se surgirem sinais de insuficiência cardíaca.", "rcuk_abcde", alerta=True),
            ),
        ),
        Etapa(
            "D — Neurológico",
            (
                I("Avaliar pupilas e nível de consciência (ACVPU ou Glasgow).", "rcuk_abcde"),
                I(
                    "Glicemia < 4,0 mmol/L (≈ 72 mg/dL) no paciente inconsciente: 50 mL de glicose 10% IV, repetindo se "
                    "necessário até 250 mL no total.",
                    "rcuk_abcde",
                    alerta=True,
                ),
                I("Inconsciente com via aérea desprotegida: posição lateral.", "rcuk_abcde"),
            ),
        ),
        Etapa(
            "E — Exposição",
            (I("Expor o paciente para o exame, preservando a dignidade e evitando perda de calor.", "rcuk_abcde"),),
        ),
    ),
    bloqueados=(
        ItemBloqueado(
            "Checagem de alergias e interações",
            "Segurança do Paciente: Checar sempre alergias medicamentosas graves e interações antes de infundir drogas de alta vigilância.",
            O_B161D85,
            "Orientação sem fonte verificada nesta revisão (não consta no material ABCDE consultado).",
        ),
        ItemBloqueado(
            "Intervalo de reavaliação",
            "Reavaliação Contínua: Resposta hemodinâmica à volemia e drogas vasoativas a cada 5 a 15 minutos em pacientes instáveis.",
            O_B161D85,
            "A fonte verificada indica reavaliar FC e PA a cada 5 minutos durante a prova de volume; o intervalo de 5 a 15 min não foi verificado.",
        ),
    ),
    alteracoes=(
        Alteracao(
            "Conteúdo",
            "Lista das letras ABCDE",
            "Ações e critérios objetivos por etapa (RCUK)",
            "Critérios objetivos para cada conduta.",
            ("rcuk_abcde",),
        ),
        Alteracao(
            "Unidade da glicemia",
            "(ausente)",
            "4,0 mmol/L convertido para ≈ 72 mg/dL (massa molar da glicose 180,16 g/mol)",
            "O Brasil usa mg/dL.",
            ("rcuk_abcde",),
        ),
    ),
    original=(
        "b161d85 (aba Raciocínio Clínico): Avaliação Primária (ABCDE): Vias aéreas, Respiração, Circulação, Incapacidade "
        "(neurológica), Exposição. Segurança do Paciente: Checar sempre alergias medicamentosas graves e interações antes "
        "de infundir drogas de alta vigilância. Reavaliação Contínua: Resposta hemodinâmica à volemia e drogas vasoativas a "
        "cada 5 a 15 minutos em pacientes instáveis."
    ),
    origem_original=O_B161D85,
    pendencias=(
        "Comparar com o ATLS (xABCDE para trauma), não consultado por restrição de licença.",
    ),
)

FLUXOGRAMAS: tuple[Fluxograma, ...] = (PCR, SRI, CRISE_HIPERTENSIVA, ANAFILAXIA, SEPSE, ABCDE)
FLUXOGRAMAS_POR_ID: dict[str, Fluxograma] = {f.id: f for f in FLUXOGRAMAS}
