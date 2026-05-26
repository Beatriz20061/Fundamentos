import streamlit as st

# Tentar importar módulos gráficos com proteção para falhas de cloud
try:
    import numpy as np
    import matplotlib.pyplot as plt
    GRAFICOS_ATIVOS = True
except ImportError:
    GRAFICOS_ATIVOS = False

# Configuração da plataforma web para alto impacto visual e responsividade
st.set_page_config(page_title="MathXplore - ISCTE Sintra", layout="wide", page_icon="🔢")

# ---- NOMES EXATOS DOS TEUS FICHEIROS DE IMAGEM ----
IMG_MODULO_1 = "Designer.png"
IMG_MODULO_2 = "3656235 (1).jpg"
IMG_MODULO_3 = "one_to_nine_numbers_hand_drawn (1).jpg"
IMG_MODULO_4 = "v979-007a.jpg"
IMG_MODULO_5 = "8375253.jpg"

# Injeção de CSS para colocar a foto com fórmulas por trás e criar a moldura retangular
st.markdown("""
    <style>
    /* Aplica a foto de fórmulas matemáticas por trás de todo o site */
    .stApp {
        background-image: linear-gradient(rgba(248, 250, 252, 0.85), rgba(248, 250, 252, 0.85)), 
                          url('https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Configuração dos botões interativos */
    .stButton>button {
        border-radius: 12px;
        background: linear-gradient(135deg, #4f46e5 0%, #3730a3 100%);
        color: white;
        border: none;
        padding: 12px 28px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.4);
    }
    
    /* Retângulo do Módulo com Borda Arredondada e Sombra Superior/Inferior */
    .modulo-caixa-moldura {
        background-color: white;
        border-radius: 14px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.08);
        border: 1px solid #e2e8f0;
        margin-bottom: 25px;
        overflow: hidden;
        width: 100%;
    }
    /* Barra superior cinza para o título */
    .modulo-barra-titulo {
        background-color: #f8fafc;
        padding: 18px 24px;
        border-bottom: 1px solid #edf2f7;
        font-size: 1.25rem;
        font-weight: 700;
        color: #1e293b;
        letter-spacing: 0.5px;
    }
    /* Área interna branca onde a imagem vai ficar emoldurada */
    .modulo-conteudo-imagem {
        padding: 24px;
        background-color: #ffffff;
        display: flex;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# ---- MENU LATERAL DE ACESSO ----
st.sidebar.title("MathXplore")
st.sidebar.markdown("**Fundamentos de Matemática**\n*Licenciatura em MATD*")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Menu :",
    [
        "🏠 Página Inicial",
        "🔵 Módulo 1: Grupos de Simetria",
        "🟤 Módulo 2: 17 Grupos Cristalográficos",
        "🟢 Módulo 3: Lógica do Number Match",
        "🟣 Módulo 4: Padrões dos Primos",
        "🟡 Módulo 5: Padrões Numéricos"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Trabalhos desenvolvidos por:")
st.sidebar.caption("Catarina Pereira & Beatriz Correia")
st.sidebar.caption("Docente: Prof. Rosário Laureano")
st.sidebar.caption("ISCTE Sintra")

# ==============================================================================
# 🏠 PÁGINA INICIAL
# ==============================================================================
if page == "🏠 Página Inicial":
    st.title("🚀 Bem-vindo ao MathXplore")
    st.subheader("Plataforma de Demonstração e Investigação de Fundamentos de Matemática")
    
    st.markdown("""
    Este ecossistema digital foi desenvolvido para integrar a totalidade dos conteúdos teóricos, formulações e dados 
    científicos presentes nos cinco projetos académicos desenvolvidos no ISCTE Sintra.
    
    A nossa abordagem converte a teoria exaustiva dos relatórios em componentes de aprendizagem dinâmicos, estruturados rigorosamente sob a metodologia de **Explicação Teórica Exaustiva**, **Aplicação Prática no Quotidiano** e **Questionários Gerais com Pontuação** automática.
    
    ### 📂 Mapeamento dos Projetos Reordenados:
    * **Módulo 1 :** Axiomas de Grupos, Isometrias lineares, Caleidoscópios, a arte de Escher e as cápsides de vírus icosaédricos.
    * **Módulo 2 :** Estudo e classificação de todas as pavimentações periódicas através dos 17 Grupos Cristalográficos do Plano.
    * **Módulo 3 :** Modelação proposicional, Teoria de Grafos e Combinatória de paridade aplicadas ao jogo *Number Match*.
    * **Módulo 4 :** Investigação da distribuição de primos na reta, Espiral de Ulam e Função Totiente de Euler.
    * **Módulo 5 :** Números Triangulares, Números Perfeitos, as propriedades cíclicas do Número 9 e o Último Teorema de Fermat.
    """)

# ==============================================================================
# MÓDULO 1: GRUPOS DE SIMETRIA
# ==============================================================================
elif page == "🔵 Módulo 1: Grupos de Simetria":
    # Abre o retângulo e injeta a barra cinza de título
    st.markdown('<div class="modulo-caixa-moldura"><div class="modulo-barra-titulo">🔵 MÓDULO 1: GRUPOS DE SIMETRIA</div><div class="modulo-conteudo-imagem">', unsafe_allow_html=True)
    # Roda a imagem local dentro do corpo do retângulo
    try:
        st.image(IMG_MODULO_1, use_container_width=True)
    except:
        st.error(f"Erro: Ficheiro '{IMG_MODULO_1}' não encontrado no repositório.")
    # Fecha as tags HTML do retângulo com segurança antes de iniciar a matéria
    st.markdown('</div></div>', unsafe_allow_html=True)
        
    tab1, tab2 = st.tabs(["📖 Matéria Completa & Isometrias", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("1.1 Isometrias e Estrutura Abstrata da Teoria de Grupos", expanded=True):
            st.markdown("""
            **Explicação Teórica:**
            A simetria é um conceito central em múltiplas áreas da Matemática, desde a Geometria à Álgebra e até à Física. De forma intuitiva, dizemos que um objeto apresenta simetria quando permanece inalterado após uma transformação como uma rotação, reflexão ou translação. Estas transformações, designadas no seu conjunto por isometrias, podem ser estudadas de forma estruturada através da Teoria de Grupos, uma área formalizada no século XIX e hoje utilizada para descrever padrões geométricos, moléculas, cristais e estruturas biológicas (Durbin, Modern Algebra).
            
            As quatro isometrias fundamentais do plano incluem:
            * **Translações:** Deslocamento da figura numa direção constante.
            * **Rotações:** Giro da figura em torno de um ponto fixo por um determinado ângulo.
            * **Reflexões:** "Espelhamento" da figura em relação a uma reta.
            * **Reflexões Deslizantes (*glide reflections*):** Combinação de uma reflexão com uma translação paralela ao eixo de reflexão.
            
            Formalmente, um grupo $(G, *)$ satisfaz quatro propriedades essenciais: **Fecho** ($a*b \\in G$), **Associatividade** ($(a*b)*c = a*(b*c)$), **Elemento Neutro** ($e*a=a*e=a$) e **Elemento Inverso** ($a*a^{-1}=a^{-1} * a=e$). Um exemplo clássico é o grupo das rotações do triângulo equilátero, que forma o grupo cíclico $C_3$.
            """)
            
        with st.expander("1.2 Eficiência Viral e Simetrias na Natureza e na Arte", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            Muitos vírus ditos "esféricos" apresentam, na verdade, uma estrutura baseada no **icosaedro**, um dos sólidos platónicos mais simétricos. A geometria icosaédrica oferece eixos de rotação múltiplos de ordem 2, 3 e 5. Isto permite que subunidades proteicas idênticas (capsómeros) se encaixem perfeitamente para formar uma cápsula (capsídeo) fechada e estável. Esta organização repetitiva confere uma enorme **eficiência genética**, permitindo que o vírus utilize um único gene para codificar uma pequena proteína que se organiza através de rotações para formar uma estrutura grande e complexa. O adenovírus, o poliovírus ou o vírus Zika seguem o modelo estrutural de Caspar-Klug.
            
            Na estrutura tridimensional de proteínas e do ADN observamos também a simetria helicoidal, que utiliza uma combinação de rotação e translação, assemelhando-se às reflexões deslizantes aplicadas a um eixo central. Na arte, M. C. Escher explorou intensamente estas isometrias para pavimentar o plano de forma regular sem deixar espaços vazios. No caleidoscópio, o efeito visual resulta de múltiplas reflexões entre espelhos dispostos em triângulo, gerando simetrias rotacionais de ângulo $360/n$ e repetições cíclicas infinitas.
            """)

    with tab2:
        st.subheader("🧠 Questionário Geral de Avaliação — Módulo 1")
        score1 = 0
        r1_1 = st.radio("1. Quantas propriedades estruturais rígidas definem formalmente um grupo matemático?", ["Duas", "Quatro", "Dez"], key="r1_1")
        r1_2 = st.radio("2. O que caracteriza o movimento de uma reflexão deslizante (glide reflection)?", ["Apenas um giro de 90 graus.", "A combinação paralela e síncrona de uma reflexão axial e uma translação.", "Um deslocamento ortogonal isolado."], key="r1_2")
        r1_3 = st.radio("3. Qual a principal vantagem biológica da simetria rotacional icosaédrica nas cápsides dos vírus?", ["Aumentar a velocidade do vírus.", "Permitir a construção de um invólucro volumoso e estável poupando informação genética por repetição proteica.", "Inibir a replicação celular."], key="r1_3")
        
        if r1_1 == "Quatro": score1 += 3.33
        if r1_2 == "A combinação paralela e síncrona de uma reflexão axial e uma translação.": score1 += 3.33
        if r1_3 == "Permitir a construção de um invólucro volumoso e estável poupando informação genética por repetição proteica.": score1 += 3.34
        
        if st.button("Submeter Exame do Módulo 1", key="b1"):
            st.metric("A tua Nota Final:", f"{round(score1, 1)}/10")

# ==============================================================================
# MÓDULO 2: 17 GRUPOS CRISTALOGRÁFICOS
# ==============================================================================
elif page == "🟤 Módulo 2: 17 Grupos Cristalográficos":
    st.markdown('<div class="modulo-caixa-moldura"><div class="modulo-barra-titulo">🟤 MÓDULO 2: 17 GRUPOS CRISTALOGRÁFICOS</div><div class="modulo-conteudo-imagem">', unsafe_allow_html=True)
    try:
        st.image(IMG_MODULO_2, use_container_width=True)
    except:
        st.error(f"Erro: Ficheiro '{IMG_MODULO_2}' não encontrado no repositório.")
    st.markdown('</div></div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa & Classificação", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("2.1 Grupos de Simetria e as Restrições das Tesselações Periódicas", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            As tesselações periódicas são padrões que cobrem o plano de forma contínua, repetindo-se indefinidamente através de translações. Cada tesselação possui um grupo de simetria, isto é, o conjunto de todas as isometrias que deixam o padrão inalterado. A base teórica assenta na apresentação moderna desenvolvida por Conway, Burgiel e Goodman-Strauss em *The Symmetries of Things* (2008).
            
            Apesar da grande variedade de padrões que observamos em azulejos, cristais ou nas obras de M. C. Escher, a Matemática demonstra que **apenas 17 tipos distintos de simetria podem pavimentar o plano de forma regular**. Esta limitação resulta das combinações possíveis entre as isometrias estudadas anteriormente e das restrições geométricas que garantem repetição periódica estável no plano.
            """)
            
            st.markdown("#### 📋 Matriz Oficial de Classificação dos 17 Wallpaper Groups")
            st.dataframe({
                "Grupo": ["pl", "p2", "pm", "pg", "cm", "pmm", "pmg", "Pgg", "cmm", "p4", "p4m", "p4g", "p3", "p3ml", "p31m", "p6", "p6m"],
                "Simetrias Principais": [
                    "Apenas translações", "Rotações de ordem 2", "Reflexões", "Reflexões deslizantes", 
                    "Reflexões e translações oblíquas", "Reflexões e rotações de ordem 2", 
                    "Reflexões e reflexões deslizantes", "Reflexões deslizantes e rotações de ordem 2", 
                    "Reflexões múltiplas e rotações de ordem 2", "Rotações de ordem 4", 
                    "Rotações de ordem 4 e reflexões", "Rotações de ordem 4 e reflexões deslizantes", 
                    "Rotações de ordem 3", "Rotações de ordem 3 e reflexões", 
                    "Rotações de ordem 3 e reflexões em disposição diferente", "Rotações de ordem 6", 
                    "Rotações de ordem 6 e reflexões"
                ]
            }, use_container_width=True)
            
        with st.expander("2.2 Análise Comparativa Profunda dos Subgrupos p4, p6 e pm", expanded=True):
            st.markdown("""
            **Explicação Teórica dos Subgrupos:**
            * **Grupo p4 (Simetria Quadrada):** Caracteriza-se pela presença de rotações de ordem 4 (simetrias de 90°, 180° e 270°), mas **não possui eixos de reflexão nem reflexões deslizantes**. As suas translações ocorrem em duas direções perpendiculares, formando uma rede quadrada. A ausência de eixos de reflexão é o elemento distintivo face aos grupos *p4m* e *p4g*.
            * **Grupo p6 (Simetria Hexagonal):** É um dos mais simétricos e apresenta rotações de ordem 6 (ângulos de 60°, 120°, 180°, 240° e 300°), ordem 3 e ordem 2. As suas translações organizam-se numa rede hexagonal, muito comum em estruturas naturais como favos de mel pela sua eficiência geométrica. **Não possui reflexões**, o que o distingue de *p6m*.
            * **Grupo pm (Simetria Axial):** É um dos exemplos mais simples entre os grupos com reflexão. Caracteriza-se pela presença de **eixos de reflexão paralelos**, combinados com translações perpendiculares a esses eixos, gerando bandas simétricas especulares em rede retangular. Não possui rotações.
            """)
            
            s_grupo = st.selectbox("Selecione uma lei estrutural para inspecionar:", ["p4 (Quadrada)", "p6 (Hexagonal)", "pm (Retangular)"], key="s_grupo")
            if "p4" in s_grupo:
                st.info("🔄 Propriedades: Rotações de ordem 4 e 2. Rede ortogonal rígida. Total ausência de eixos axiais de espelhamento.")
            elif "p6" in s_grupo:
                st.success("🐝 Propriedades: Rotações de ordens 6, 3 e 2. Estrutura geométrica idêntica à estabilidade mecânica dos favos naturais.")
            elif "pm" in s_grupo:
                st.warning("🪞 Propriedades: Eixos axiais paralelos puros. Domínio exclusivo de reflexões especulares lineares.")

    with tab2:
        st.subheader("🧠 Questionário Geral de Avaliação — Módulo 2")
        score2 = 0
        r2_1 = st.radio("1. Qual o número máximo de grupos cristalográficos abstratos que a restrição geométrica permite existir para pavimentar o plano bidimensional?", ["Infinitos", "Apenas 12", "Exatamente 17"], key="r2_1")
        r2_2 = st.radio("2. O que diferencia fundamentalmente o grupo cristalográfico 'p6' do grupo 'p6m'?", ["O grupo p6 possui eixos axiais de reflexão.", "Ambos possuem rotações de ordem 6, mas o grupo p6 carece inteiramente de eixos de reflexão.", "O grupo p6 não possui translações hexagonais."], key="r2_2")
        r2_3 = st.radio("3. Que tipo de simetria e rede de translação definem o comportamento do subgrupo 'pm'?", ["Simetria puramente rotacional em malha quadrada.", "Simetria axial dominante baseada em eixos de reflexão paralelos numa rede retangular.", "Reflexões deslizantes exclusivas em rede oblíqua."], key="r2_3")
        
        if r2_1 == "Exatamente 17": score2 += 3.33
        if r2_2 == "Ambos possuem rotações de ordem 6, mas o grupo p6 carece inteiramente de eixos de reflexão.": score2 += 3.33
        if r2_3 == "Simetria axial dominante baseada em eixos de reflexão paralelos numa rede retangular.": score2 += 3.34
        
        if st.button("Submeter Exame do Módulo 2", key="b2"):
            st.metric("A tua Nota Final:", f"{round(score2, 1)}/10")

# ==============================================================================
# MÓDULO 3: LÓGICA DO NUMBER MATCH
# ==============================================================================
elif page == "🟢 Módulo 3: Lógica do Number Match":
    st.markdown('<div class="modulo-caixa-moldura"><div class="modulo-barra-titulo">🟢 MÓDULO 3: LÓGICA DO NUMBER MATCH</div><div class="modulo-conteudo-imagem">', unsafe_allow_html=True)
    try:
        st.image(IMG_MODULO_3, use_container_width=True)
    except:
        st.error(f"Erro: Ficheiro '{IMG_MODULO_3}' não encontrado no repositório.")
    st.markdown('</div></div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["💡 Lição do Sistema & Simulador", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("3.1 Formalização Lógica e Regras Proposicionais do Tabuleiro", expanded=True):
            st.markdown("""
            **Explicação Teórica :**
            O *Number Match* é um jogo de lógica e aritmética popular em plataformas digitais devido às suas regras simples e à dinâmica progressiva do tabuleiro. As decisões do jogador dependem simultaneamente de condições lógicas e de propriedades aritméticas elementares, como igualdade, soma e paridade, que influenciam diretamente a evolução do jogo (Rosen, 2012). 
            
            A formalização das condições de jogada pode ser feita recorrendo à lógica proposicional, permitindo descrever de forma precisa quando uma jogada é válida. Uma jogada válida ocorre quando dois números $a$ e $b$ satisfazem simultaneamente uma condição numérica e uma condição estrutural de acessibilidade. A condição numérica é satisfeita quando se verifica pelo menos uma das seguintes situações:
            1. $a=b$, isto é, os dois números são iguais;
            2. $a+b=10$, correspondendo a uma relação aritmética complementar.
            
            Deste modo, a proposição \"Jogada Válida ($a, b$)\" pode ser formalizada da seguinte forma:
            """)
            st.latex(r"\text{JogadaVálida}(a, b) \leftrightarrow (a = b \lor a + b = 10) \land \text{Conectados}(a, b)")
            st.markdown("""
            Esta expressão representa uma fórmula booleana composta, na qual as condições aritméticas e estruturais são combinadas através dos conectivos lógicos usuais. Assim, uma jogada é válida apenas quando simultaneamente se verifica uma relação lógica entre os valores dos números e uma relação estrutural no tabuleiro.
            """)
            
            st.markdown("#### 🕹️ Simulador de Validação Lógica Discreta")
            col1, col2, col3 = st.columns(3)
            with col1: s_a = st.number_input("Introduza o valor da Carta A:", 1, 9, 5, key="s_a")
            with col2: s_b = st.number_input("Introduza o valor da Carta B:", 1, 9, 5, key="s_b")
            with col3: s_con = st.checkbox("Estão acessíveis/conectados de forma contígua?", value=True, key="s_con")
            
            c_num = (s_a == s_b) or (s_a + s_b == 10)
            c_valida = c_num and s_con
            if c_valida:
                st.success(f"🟩 Proposição VERDADEIRA! A jogada ({s_a},{s_b}) cumpre a conjunção e os vértices podem ser colapsados.")
            else:
                st.error("🟥 Proposição FALSA! Operação impedida pelas restrições booleanas do sistema.")
                
        with st.expander("3.2 Modelação em Teoria de Grafos e Estratégia Combinatória de Paridade", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            O tabuleiro do jogo pode ser representado como um grafo dinâmico, no qual os números correspondem a vértices e as relações de jogada válida a arestas. Nesta perspetiva, o jogo pode ser entendido como um processo iterativo de remoção de vértices e arestas, cuja estrutura se altera ao longo do tempo. À medida que o jogador elimina pares, o grafo sofre transformações sucessivas. Neste contexto, o grau de um vértice — isto é, o número de arestas incidentes — assume um papel importante. Vértices de grau elevado correspondem a números com várias jogadas possíveis, enquanto vértices de grau zero representam números isolados que não podem ser eliminados. Estes vértices isolados contribuem diretamente para estados de bloqueio do tabuleiro.
            
            **Análise Combinatória e o Impacto do Número 5:**
            Técnicas combinatórias baseiam-se em princípios de contagem, análise de frequências e argumentos de paridade. Cada número entre 1 e 9 possui exatamente um único parceiro que permite obter a soma 10 ($1\\leftrightarrow9, 2\\leftrightarrow8, 3\\leftrightarrow7, 4\\leftrightarrow6$). O número 5 constitui um caso particular, pois **apenas pode formar par consigo mesmo** ($5\\leftrightarrow5$). Isto implica que a sua frequência no tabuleiro deve ser impreterivelmente **par** para permitir a eliminação completa e evitar a criação de números isolados. Se aparecer um número ímpar de vezes, pelo menos um 5 ficará inevitavelmente isolado, por um argumento direto de paridade.
            """)

    with tab2:
        st.subheader("🧠 Questionário Geral de Avaliação — Módulo 3")
        score3 = 0
        r3_1 = st.radio("1. Qual o estado de um número que se transforma num vértice de grau zero no grafo?", ["Fica isolado e bloqueia o progresso do jogo.", "Garante uma jogada imediata por igualdade.", "Duplica o número de arestas incidentes."], key="r3_1")
        r3_2 = st.radio("2. Qual a correspondência biunívoca correta para somas complementares de valor 10?", [r"$2 \leftrightarrow 8$", r"$3 \leftrightarrow 7$", r"$4 \leftrightarrow 4$"], key="r3_2")
        r3_3 = st.radio("3. Por que razão a contagem combinatória do número 5 exige uma frequência obrigatoriamente par?", ["Porque é um número ímpar.", "Porque apenas pode emparelhar consigo próprio para atingir a soma 10.", "Porque é o vértice central de Euler."], key="r3_3")
        
        if r3_1 == "Fica isolado e bloqueia o progresso do jogo.": score3 += 3.33
        if r3_2 == r"$3 \leftrightarrow 7$": score3 += 3.33
        if r3_3 == "Porque apenas pode emparelhar consigo próprio para atingir a soma 10.": score3 += 3.34
        
        if st.button("Submeter Exame do Módulo 3", key="b3"):
            st.metric("A tua Nota Final:", f"{round(score3, 1)}/10")

# ==============================================================================
# MÓDULO 4: PADRÕES DOS PRIMOS
# ==============================================================================
elif page == "🟣 Módulo 4: Padrões dos Primos":
    st.markdown('<div class="modulo-caixa-moldura"><div class="modulo-barra-titulo">🟣 MÓDULO 4: PADRÕES DOS PRIMOS</div><div class="modulo-conteudo-imagem">', unsafe_allow_html=True)
    try:
        st.image(IMG_MODULO_4, use_container_width=True)
    except:
        st.error(f"Erro: Ficheiro '{IMG_MODULO_4}' não encontrado no repositório.")
    st.markdown('</div></div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa & Aplicações", "✍️ Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("4.1 A Natureza e Distribuição Irregular dos Números Primos", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            A Teoria dos Números é um dos ramos mais antigos e fascinantes da matemática. Apesar de lidar com objetos aparentemente simples, os números inteiros, revela estruturas profundas e padrões inesperados. Esta ideia é destacada por G. H. Hardy na sua obra *A Mathematician's Apology* (1940), onde defende que a matemática pura possui uma beleza intrínseca, comparável à arte, precisamente porque revela ordem onde antes se supunha irregularidade. Hardy via nesta área um exemplo perfeito de como estruturas elegantes podem emergir de objetos aparentemente elementares. A distribuição dos números primos, irregular à primeira vista mas repleta de padrões subtis, é um dos casos mais emblemáticos dessa visão.
            
            Os números primos são fundamentais na aritmética. O Teorema Fundamental da Aritmética estabelece que qualquer número inteiro positivo pode ser decomposto de forma única num produto de primos. Esta unicidade confere aos primos um papel central na estrutura dos números inteiros. Apesar da sua importância, a distribuição dos primos é notoriamente irregular. Du Sautoy (2003) descreve-os como "notas musicais" que parecem seguir um ritmo aparentemente aleatório, mas que escondem uma harmonia profunda. 
            
            A irregularidade aparente levou matemáticos como Gauss e Riemann a procurar padrões estatísticos que explicassem esta oscilação entre ordem e caos. Foi neste contexto que Riemann, em 1859, introduziu a função zeta complexa e formulou a célebre Hipótese de Riemann, segundo a qual todas as raízes não triviais dessa função têm parte real igual a 1/2. Esta afirmação estabelece uma ligação direta entre o comportamento analítico da função zeta e a distribuição dos números primos. A hipótese permanece em aberto e é considerada um dos problemas centrais da matemática contemporânea.
            """)
            
        with st.expander("4.2 Representações Visuais e Padrões Inesperados na Espiral de Ulam", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            A visualização é uma ferramenta poderosa para revelar padrões. Stewart (2006) argumenta que muitas descobertas matemáticas surgem quando se representa um problema de forma inesperada. Foi precisamente isso que aconteceu com Stanislaw Ulam em 1963. Durante uma conferência, Ulam começou a desenhar os números naturais numa espiral quadrada, marcando os números primos. O que parecia um exercício casual revealed algo extraordinário: os números primos alinhavam-se em diagonais longas e bem definidas.
            
            **Processo de Construção:**
            * Coloca-se o número 1 no centro.
            * Os números seguintes são escritos em espiral, no sentido horário (sentido negativo).
            * Os números primos são destacados.
            
            As diagonais da espiral correspondem a expressões quadráticas do tipo $an^2+bn+c$. Euler estudou estas expressões e descobriu que algumas geram muitos primos consecutivos. O exemplo mais famoso é o polinómio de Euler, $n^2+n+41$, que produz primos para $n=0,1,2,\dots,39$. Quando estes polinómios geram muitos primos, a diagonal correspondente torna-se visualmente densa. Assim, a espiral não cria primos, apenas torna visível a aritmética escondida nos polinómios.
            """)
            
            st.markdown("#### 🎛️ Laboratório Dinâmico: Gerador de Primos de Euler")
            n_slider = st.slider("Altere o valor de n para validar o polinómio de Euler:", 0, 39, 0, key="euler_slider")
            res_euler = (n_slider**2) + n_slider + 41
            st.metric(label=f"Resultado para n={n_slider}", value=int(res_euler), delta="É um número primo!")
            
        with st.expander("4.3 A Função Totiente de Euler e Estrutura Multiplicativa Modular", expanded=True):
            st.markdown("""
            **Explicação Teórica:**
            A função totiente $\\varphi(n)$, introduzida por Euler, conta quantos naturais até $n$ são coprimos com $n$. Segundo Rosen (2010), esta função é central na aritmética modular, pois conta a quantidade de inteiros que mantêm uma relação \"simples\" com $n$ quando considerados módulo $n$. Assim, $\\varphi(n)$ evidencia a estrutura multiplicativa dos inteiros e revela padrões que dependem diretamente dos fatores primos de cada número.
            
            **Fórmula Multiplicativa Geral:**
            Se $n=p_1^{a_1}p_2^{a_2}\dots p_k^{a_k}$ em que $p_1,p_2,\dots,p_k$ são os fatores primos distintos de $n$, então:
            """)
            st.latex(r"\varphi(n)=n\prod_{i=1}^{k}\left(1-\frac{1}{p_i}\right)")
            st.markdown("""
            Além disso, a função totiente cumpre a propriedade multiplicativa quando os fatores são coprimos entre si: $\\varphi(ab)=\\varphi(ab)$ se $gcd(a,b)=1$.
            
            **Propriedades Fundamentais:**
            1. **Totiente de um Número Primo:** Se $p$ é primo, então $\\varphi(p)=p-1$, porque todos os inteiros menores que um primo são coprimos com ele.
            2. **Totiente de uma Potência de Primo:** Para qualquer primo $p$ e inteiro $k \ge 1$: $\\varphi(p^k)=p^k-p^{k-1}=p^k(1-\\frac{1}{p})$, pois num número da forma $p^k$, apenas os múltiplos de $p$ não são coprimos.
            3. **Influência dos Fatores:** Se $n$ tem muitos fatores primos distintos, então $\\varphi(n)$ é significativamente menor do que $n$. A função totiente tem ainda um papel central na criptografia moderna, em particular no algoritmo RSA, onde a segurança do sistema depende da dificuldade de determinar $\\varphi(n)$ sem conhecer a fatorização de $n$.
            """)
            
            num_input = st.number_input("Introduza um valor (n) para calcular o totiente:", min_value=2, max_value=500, value=12, key="tot_input")
            def phi_alg(n):
                result = n
                p = 2
                while p * p <= n:
                    if n % p == 0:
                        while n % p == 0: n //= p
                        result -= result // p
                    p += 1
                if n > 1: result -= result // n
                return result
            st.write(f"**Resultado:** $\\varphi({num_input}) =$ `{phi_alg(num_input)}`")

    with tab2:
        st.subheader("🧠 Questionário Geral de Avaliação — Módulo 4")
        score4 = 0
        r4_1 = st.radio("1. O que postula a célebre Hipótese de Riemann formulada em 1859?", ["Que todas as diagonais quadráticas geram primos.", "Que todas as raízes não triviais da função zeta complexa têm parte real igual a 1/2.", "Que a função totiente é constante."], key="r4_1")
        r4_2 = st.radio("2. Quanto vale a função totiente de Euler para n=12?", ["12", "6", "4", "2"], key="r4_2")
        r4_3 = st.radio("3. Qual a propriedade fundamental de um número primo p em relação ao seu totiente?", [r"$\varphi(p) = p$", r"$\varphi(p) = p - 1$", r"$\varphi(p) = 1$"], key="r4_3")
        
        if r4_1 == "Que todas as raízes não triviais da função zeta complexa têm parte real igual a 1/2.": score4 += 3.33
        if r4_2 == "4": score4 += 3.33
        if r4_3 == r"$\varphi(p) = p - 1$": score4 += 3.34
        
        if st.button("Submeter Exame do Módulo 4", key="b4"):
            st.metric("A tua Nota Final:", f"{round(score4, 1)}/10")

# ==============================================================================
# MÓDULO 5: PADRÕES NUMÉRICOS
# ==============================================================================
elif page == "🟡 Módulo 5: Padrões Numéricos":
    st.markdown('<div class="modulo-caixa-moldura"><div class="modulo-barra-titulo">🟡 MÓDULO 5: PADRÕES NUMÉRICOS</div><div class="modulo-conteudo-imagem">', unsafe_allow_html=True)
    try:
        st.image(IMG_MODULO_5, use_container_width=True)
    except:
        st.error(f"Erro: Ficheiro '{IMG_MODULO_5}' não encontrado no repositório.")
    st.markdown('</div></div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa & Gráficos", "✍️ Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("5.1 Números Triangulares e a Abordagem Geométrica de Contagem", expanded=True):
            st.markdown("""
            **Explicação Teórica:**
            Os números triangulares pertencem ao grupo dos chamados números figurados, que se caracterizam por serem números que podem ser representados através de arranjos geométricos de pontos regulares. Esta abordagem visual transforma problemas de contagem abstrata numa perceção geométrica de tal forma intuitiva que minimiza o peso algébrico inicial. Eles representam a quantidade de pontos necessária para construir um triângulo equilátero com um determinado número de linhas. Como cada nova linha adiciona sempre mais um ponto do que a linha anterior, um número triangular corresponds diretamente à soma dos primeiros números naturais.
            """)
            st.latex(r"T_{n}=1+2+3+\cdot\cdot\cdot+n=\frac{n(n+1)}{2}")
            st.markdown("""
            Esta fórmula matemática pode ser explicada através de um raciocínio geométrico muito simples que é atribuído historicamente a Gauss. Se escrevermos a sequência da soma na sua ordem direta e na sua ordem inversa, conseguimos agrupar os termos verticalmente aos pares. Ao somarmos as duas equações, cada par de termos resulta invariavelmente no valor de $n+1$. Dado que existem exatamente $n$ termos nesta sequência, a soma total das duas linhas passa a ser escrita como $2T_{n}=n(n+1)$. Logo, basta dividir o resultado por dois para isolar o termo inicial.
            
            **Aplicação Concreta no Quotidiano:**
            Os números triangulares possuem diversas aplicações práticas em problemas reais de contagem. Um exemplo clássico é a modelação de contagem de ligações em redes ou interações sociais. Se tivermos uma sala com 6 pessoas e quisermos saber quantos apertos de mão únicos ocorrem se todas se cumprimentarem uma única vez, o cálculo resolve-se através do número triangular $T_{5}$:
            """)
            st.latex(r"T_5 = \frac{5 \times (5+1)}{2} = 15 \text{ apertos de mão}")
            st.markdown("Este mesmo raciocínio aplica-se ao determinar o número de canais diretos necessários para interligar computadores numa rede sem que haja repetições de caminhos.")
            
        with st.expander("5.2 Números Perfeitos e Harmonia de Divisores", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            Um número perfeito define-se como um número inteiro positivo que é exatamente igual à soma de todos os seus divisores próprios, considerando-se divisores próprios todos os fatores que são estritamente menores do que o próprio número. Esta definição clássica remonta aos *Elementos de Euclides*, refletindo o interesse por propriedades estéticas de equilíbrio e harmonia aritmética.
            
            **Exemplos Clássicos:**
            * **Número 6:** Os seus divisores próprios são {1, 2, 3}. Ao somarmos estes fatores, obtemos: $1+2+3=6$.
            * **Número 28:** Os seus divisores próprios são {1, 2, 4, 7, 14}. A sua soma resulta em: $1+2+4+7+14=28$.
            
            A análise profunda dos números perfeitos pares revela uma ligação direta com os Primos de Mersenne, que assumem a forma de $2^{p}-1$, onde o expoente $p$ é primo. Euclides demonstrou formalmente que, sempre que $2^{p}-1$ for um número primo, gera-se um número perfeito par através da fórmula:
            """)
            st.latex(r"n=2^{p-1}(2^{p}-1)")
            st.markdown("""
            Seguindo outra linguagem formal recorrendo à função soma dos divisores $\\sigma(n)$, um número é perfeito sempre que satisfizer a identidade $\\sigma(n)=2n$. No caso do número 6, $\\sigma(6)=12$, que equivale precisamente ao dobro do número original. Permanentem em aberto mistérios para termos perfeitos ímpares.
            """)
            
        with st.expander("5.3 Exploração do Número 9 na Base Decimal", expanded=True):
            st.markdown("""
            **Explicação Teórica:**
            O número 9 ocupa um lugar de destaque devido à organização do nosso sistema de numeração posicional em base 10. Pelo facto de o número 9 ser uma unidade inferior à base do sistema ($10-1$), cria-se um conjunto único de simetrias repetitivas, regras de divisibilidade facilitadas e padrões visuais claros nos seus algarismos.
            
            Qualquer número inteiro positivo é sempre congruente com a soma dos seus próprios algarismos em módulo 9: $n \equiv \\text{soma dos dígitos de } n \\pmod 9$. Esta propriedade justifica o critério de divisibilidade por 9. Adicionalmente, as dezenas e as unidades da tabuada do 9 funcionam como um verdadeiro espelho numérico: $9\\times2=18$ e $9\\times9=81$ invertem-se simetricamente em pares.
            
            Analisando a redução digital das potências do número 9, a soma das suas componentes numéricas gera ciclos regulares invariáveis ($9^1=9$, $9^2=81 \\rightarrow 9$, $9^3=729 \\rightarrow 18 \\rightarrow 9$).
            """)
            
        with st.expander("5.4 O Último Teorema de Fermat e a Limitação de Padrões", expanded=True):
            st.markdown("""
            **Explicação Teórica:**
            O Último Teorema de Fermat ilustra como pequenas alterações numa expressão matemática podem fazer com que um padrão de soluções infinitas desapareça por completo. No caso do expoente $n=2$, a equação transforma-se na clássica expressão de Pitágoras: $a^2+b^2=c^2$. Esta estrutura admite uma infinidade de triplas pitagóricas inteiras positivas, como o caso 3-4-5 ($3^2+4^2=5^2$).
            
            Contudo, Fermat afirmou na margem do seu livro que a equação geral:
            """)
            st.latex(r"a^{n}+b^{n}=c^{n}")
            st.markdown("""
            **não admite qualquer tipo de solução inteira não trivial** sempre que o expoente $n$ for um número estritamente maior do que 2 ($n>2$). Ao alterarmos apenas o valor do expoente, passamos de soluções infinitas para um vazio total. A prova definitiva foi alcançada em 1994 por Andrew Wiles, utilizando curvas elípticas.
            """)
            
            if GRAFICOS_ATIVOS:
                st.markdown("#### 📊 Laboratório Gráfico de Fermat (Simulação em Tempo Real)")
                n_fermat = st.slider("Ajuste o expoente n:", 2.0, 15.0, 2.0, step=0.5, key="fermat_slider")
                x_val = np.linspace(0, 5, 200)
                fig, ax = plt.subplots(figsize=(5, 3.5))
                with np.errstate(invalid='ignore'):
                    y_val = (5**n_fermat - x_val**n_fermat)**(1/n_fermat)
                ax.plot(x_val, y_val, label=f"n = {n_fermat}", color="#4f46e5", linewidth=3)
                if n_fermat == 2.0:
                    ax.plot(3, 4, 'go', markersize=10, label="Solução Inteira (3,4)")
                ax.set_xlim(0, 5.2)
                ax.set_ylim(0, 5.2)
                ax.grid(True, linestyle=":", alpha=0.5)
                ax.legend()
                st.pyplot(fig)

    with tab2:
        st.subheader("🧠 Questionário Geral de Avaliação — Módulo 5")
        score5 = 0
        r5_1 = st.radio("1. Qual a expressão utilizada para calcular o n-ésimo número triangular?", [r"$T_n = \frac{n(n+1)}{2}$", r"$T_n = 2^n - 1$", r"$T_n = n^2 + n + 41$"], key="r5_1")
        r5_2 = st.radio("2. Qual a relação matemática que define se um número é perfeito?", [r"$\sigma(n) = n$", r"$\sigma(n) = 2n$", r"$\sigma(n) = n - 1$"], key="r5_2")
        r5_3 = st.radio("3. A partir de que expoente n deixa de existir qualquer solução inteira não trivial segundo Fermat?", [r"$n > 1$", r"$n > 2$", r"$n > 5$"], key="r5_3")
        
        if r5_1 == r"$T_n = \frac{n(n+1)}{2}$": score5 += 3.33
        if r5_2 == r"$\sigma(n) = 2n$": score5 += 3.33
        if r5_3 == r"$n > 2$": score5 += 3.34
        
        if st.button("Submeter Exame do Módulo 5", key="b5"):
            st.metric("A tua Nota Final:", f"{round(score5, 1)}/10")