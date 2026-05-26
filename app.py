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

# Injeção de CSS Avançado para Animações e Transições Fluídas
st.markdown("""
    <style>
    /* Importar fonte moderna */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Cor de fundo sólida e moderna */
    .stApp {
        background-color: #f8fafc;
    }
    
    /* --- ANIMAÇÃO DE ENTRADA SUAVE (FADE-IN) --- */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Aplica a animação ao bloco principal de conteúdo */
    .block-container {
        animation: fadeInUp 0.5s ease-out;
    }
    
    /* --- BOTÕES INTERATIVOS ULTRA-FLUIDOS --- */
    .stButton>button {
        border-radius: 12px;
        background: linear-gradient(135deg, #4f46e5 0%, #3730a3 100%);
        color: white;
        border: none;
        padding: 12px 28px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
        box-shadow: 0 4px 14px rgba(79, 70, 229, 0.2);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(79, 70, 229, 0.4);
        background: linear-gradient(135deg, #4338ca 0%, #2e288a 100%);
    }
    
    /* --- RETÂNGULO DO MÓDULO COM DESIGN PREMIUM --- */
    .modulo-caixa-moldura {
        background-color: white;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.04);
        border: 1px solid #e2e8f0;
        margin-bottom: 25px;
        overflow: hidden;
    }
    .modulo-barra-titulo {
        background: linear-gradient(90deg, #f1f5f9 0%, #ffffff 100%);
        padding: 18px 24px;
        border-bottom: 1px solid #e2e8f0;
        font-size: 1.25rem;
        font-weight: 700;
        color: #1e293b;
        letter-spacing: 0.5px;
    }
    
    /* --- ESTILIZAÇÃO DINÂMICA DOS EXPANDERS --- */
    div[data-testid="stExpander"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        margin-bottom: 15px !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stExpander"]:hover {
        border-color: #a5b4fc !important;
        box-shadow: 0 6px 12px rgba(79, 70, 229, 0.05) !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---- MENU LATERAL DE ACESSO ----
st.sidebar.title("🔢 MathXplore")
st.sidebar.markdown("**Fundamentos de Matemática**\n*Licenciatura em MATD*")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Menu de Navegação :",
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
st.sidebar.caption("💡 Catarina Pereira & Beatriz Correia")
st.sidebar.caption("👨‍🏫 Docente: Prof. Rosário Laureano")
st.sidebar.caption("🏫 ISCTE Sintra")

# ==============================================================================
# 🏠 PÁGINA INICIAL
# ==============================================================================
if page == "🏠 Página Inicial":
    st.title("🚀 Bem-vindo ao MathXplore")
    st.subheader("Plataforma de Demonstração e Investigação de Fundamentos de Matemática")
    
    st.markdown("""
    Este ecossistema digital foi desenvolvido para integrar a totalidade dos conteúdos teóricos, formulações e dados 
    científicos presentes nos cinco projetos académicos desenvolvidos nos relatórios originais.
    
    A nossa abordagem converte a teoria exaustiva dos relatórios em componentes de aprendizagem dinâmicos, estruturados rigorosamente sob a metodologia de **Explicação Teórica Exaustiva**, **Aplicação Prática no Quotidiano** e **Questionários Gerais com Pontuação** automática.
    """)

# ==============================================================================
# MÓDULO 1: GRUPOS DE SIMETRIA
# ==============================================================================
elif page == "🔵 Módulo 1: Grupos de Simetria":
    st.markdown('<div class="modulo-caixa-moldura"><div class="modulo-barra-titulo">🔵 MÓDULO 1: GRUPOS DE SIMETRIA</div></div>', unsafe_allow_html=True)
        
    tab1, tab2 = st.tabs(["📖 Matéria Completa & Isometrias", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("1.1 Isometrias e Estrutura Abstrata da Teoria de Grupos", expanded=False):
            st.markdown("""
            **Explicação Teórica:**
            A simetria é um conceito central em múltiplas áreas da Matemática, desde a Geometria à Álgebra e até à Física. De forma intuitiva, dizemos que um objeto apresenta simetria quando permanece inalterado após uma transformação como uma rotação, reflexão ou translação. Estas transformações, designadas no seu conjunto por isometrias, podem ser estudadas de forma estruturada através da Teoria de Grupos, uma área utilizada para descrever padrões geométricos, moléculas, cristais e estruturas biológicas.
            
            As quatro isometrias fundamentais do plano incluem:
            * **Translações:** Deslocamento da figura numa direção constante.
            * **Rotações:** Giro da figura em torno de um ponto fixo por um determinado ângulo.
            * **Reflexões:** "Espelhamento" da figura em relação a uma reta.
            * **Reflexões Deslizantes (*glide reflections*):** Combinação de uma reflexão com uma translação paralela ao eixo de reflexão.
            """)
            
        with st.expander("1.2 Eficiência Viral e Simetrias na Natureza e na Arte", expanded=False):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            Muitos vírus ditos "esféricos" apresentam, na verdade, uma estrutura baseada no **icosaedro**, um dos sólidos platónicos mais simétricos. A geometria icosaédrica oferece eixos de rotação múltiplos de ordem 2, 3 e 5. Isto permite que subunidades proteicas idênticas (capsómeros) se encaixem perfeitamente para formar uma cápsula (capsídeo) fechada e estável. Esta organização repetitiva confere uma enorme **eficiência genética**, permitindo que o vírus utilize um único gene para codificar uma pequena proteína que se organiza através de rotações para formar uma estrutura grande e complexa.
            
            Na arte, M. C. Escher explorou intensamente estas isometrias para pavimentar o plano de forma regular sem deixar espaços vazios. No caleidoscópio, o efeito visual resulta de múltiplas reflexões entre espelhos dispostos em triângulo, gerando simetrias rotacionais de ângulo $360/n$ e repetições cíclicas infinitas.
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
    st.markdown('<div class="modulo-caixa-moldura"><div class="modulo-barra-titulo">🟤 MÓDULO 2: 17 GRUPOS CRISTALOGRÁFICOS</div></div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa & Classificação", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("2.1 Grupos de Simetria e as Restrições das Tesselações Periódicas", expanded=False):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            As tesselações periódicas são padrões que cobrem o plano de forma contínua, repetindo-se indefinidamente através de translações. Cada tesselação possui um grupo de simetria, isto é, o conjunto de todas as isometrias que deixam o padrão inalterado.
            
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
            
        with st.expander("2.2 Análise Comparativa Profunda dos Subgrupos p4, p6 e pm", expanded=False):
            st.markdown("""
            **Explicação Teórica dos Subgrupos:**
            * **Grupo p4 (Simetria Quadrada):** Caracteriza-se pela presença de rotações de ordem 4 (simetrias de 90°, 180° e 270°), mas **não possui eixos de reflexão nem reflexões deslizantes**.
            * **Grupo p6 (Simetria Hexagonal):** É um dos mais simétricos e apresenta rotações de ordem 6 (ângulos de 60°, 120°, 180°, 240° e 300°), ordem 3 e ordem 2. **Não possui reflexões**.
            * **Grupo pm (Simetria Axial):** Caracteriza-se pela presença de **eixos de reflexão paralelos**, combinados com translações perpendiculares a esses eixos. Não possui rotações.
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
    st.markdown('<div class="modulo-caixa-moldura"><div class="modulo-barra-titulo">🟢 MÓDULO 3: LÓGICA DO NUMBER MATCH</div></div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["💡 Lição do Sistema & Simulador", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("3.1 Formalização Lógica e Regras Proposicionais do Tabuleiro", expanded=False):
            st.markdown("""
            **Explicação Teórica :**
            O *Number Match* é um jogo de lógica e aritmética cujas decisões do jogador dependem simultaneamente de condições lógicas e de propriedades aritméticas elementares, como igualdade, soma e paridade.
            
            A formalização das condições de jogada pode ser feita recorrendo à lógica proposicional. Uma jogada válida ocorre quando dois números $a$ e $b$ satisfazem simultaneamente uma condition numérica e uma condição estrutural de acessibilidade:
            """)
            st.latex(r"\text{JogadaVálida}(a, b) \leftrightarrow (a = b \lor a + b = 10) \land \text{Conectados}(a, b)")
            
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
                
        with st.expander("3.2 Modelação em Teoria de Grafos e Estratégia Combinatória de Paridade", expanded=False):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            O tabuleiro do jogo pode ser representado como um grafo dinâmico, no qual os números correspondem a vértices e as relações de jogada válida a arestas. À medida que o jogador elimina pares, o grafo sofre transformações sucessivas. Vértices de grau zero representam números isolados que não podem ser eliminados e bloqueiam o tabuleiro.
            
            **Análise Combinatória e o Impacto do Número 5:**
            Cada número entre 1 e 9 possui exatamente um único parceiro que permite obter a soma 10 ($1\leftrightarrow9, 2\leftrightarrow8, 3\leftrightarrow7, 4\leftrightarrow6$). O número 5 constitui um caso particular, pois **apenas pode formar par consigo mesmo** ($5\leftrightarrow5$). Isto implica que a sua frequência no tabuleiro deve ser impreterivelmente **par** para permitir a eliminação completa e evitar a criação de números isolados.
            """)

    with tab2:
        st.subheader("🧠 Questionário Geral de Avaliação — Módulo 3")
        score3 = 0
        r3_1 = st.radio("1. Qual o estado de um número que se transforma num vértice de grau zero no grafo?", ["Fica isolado e bloqueia o progresso do jogo.", "Garante uma jogada imediata por igualdade.", "Duplica o número de arestas incidentes."], key="r3_1")
        r3_2 = st.radio("2. Qual a correspondência biunívoca correta para somas complementares de valor 10?", [r"$2 \leftrightarrow 8$", r"$3 \leftrightarrow 7$", r"$4 \leftrightarrow 4$"], key="r3_2")
        r3_3 = st.radio("3. Por que razão a contagem combinatória do número 5 exige uma frequência obrigatoriamente par?", ["Because é um número ímpar.", "Porque apenas pode emparelhar consigo próprio para atingir a soma 10.", "Porque é o vértice central de Euler."], key="r3_3")
        
        if r3_1 == "Fica isolado e bloqueia o progresso do jogo.": score3 += 3.33
        if r3_2 == r"$3 \leftrightarrow 7$": score3 += 3.33
        if r3_3 == "Porque apenas pode emparelhar consigo próprio para atingir a soma 10.": score3 += 3.34
        
        if st.button("Submeter Exame do Módulo 3", key="b3"):
            st.metric("A tua Nota Final:", f"{round(score3, 1)}/10")

# ==============================================================================
# MÓDULO 4: PADRÕES DOS PRIMOS
# ==============================================================================
elif page == "🟣 Módulo 4: Padrões dos Primos":
    st.markdown('<div class="modulo-caixa-moldura"><div class="modulo-barra-titulo">🟣 MÓDULO 4: PADRÕES DOS PRIMOS</div></div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa & Aplicações", "✍️ Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("4.1 A Natureza e Distribuição Irregular dos Números Primos", expanded=False):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            A Teoria dos Números revela estruturas profundas e padrões inesperados. A matemática pura possui uma beleza intrínseca precisamente porque revela ordem onde antes se supunha irregularidade. Os números primos são fundamentais na aritmética: o Teorema Fundamental da Aritmética estabelece que qualquer número inteiro positivo pode ser decomposto de forma única num produto de primos.
            
            A distribuição dos primos é notoriamente irregular. Essa oscilação entre ordem e caos levou à introdução da função zeta complexa e à formulação da célebre Hipótese de Riemann, segundo a qual todas as raízes não triviais dessa função têm parte real igual a 1/2.
            """)
            
        with st.expander("4.2 Representações Visuais e Padrões Inesperados na Espiral de Ulam", expanded=False):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            A visualização na Espiral de Ulam revelou que os números primos se alinham em diagonais longas e bem definidas. As diagonais da espiral correspondem a expressões quadráticas do tipo $an^2+bn+c$. O exemplo mais famoso é o polinómio de Euler, $n^2+n+41$, que produz números primos para todos os inteiros de $n=0$ a $39$.
            """)
            
            st.markdown("#### 🎛️ Laboratório Dinâmico: Gerador de Primos de Euler")
            n_slider = st.slider("Altere o valor de n para validar o polinómio de Euler:", 0, 39, 0, key="euler_slider")
            res_euler = (n_slider**2) + n_slider + 41
            st.metric(label=f"Resultado para n={n_slider}", value=int(res_euler), delta="É um número primo!")
            
        with st.expander("4.3 A Função Totiente de Euler e Estrutura Multiplicativa Modular", expanded=False):
            st.markdown("""
            **Explicação Teórica:**
            A função totiente $\\varphi(n)$, introduzida por Euler, conta quantos naturais até $n$ são coprimos com $n$.
            
            **Fórmula Multiplicativa Geral:**
            Se $n=p_1^{a_1}p_2^{a_2}\dots p_k^{a_k}$ em que $p_1,p_2,\dots,p_k$ são os fatores primos distintos de $n$, então:
            """)
            st.latex(r"\varphi(n)=n\prod_{i=1}^{k}\left(1-\frac{1}{p_i}\right)")
            
            st.markdown("""
            **Propriedades Fundamentais:**
            1. **Totiente de um Número Primo:** Se $p$ é primo, então $\\varphi(p)=p-1$.
            2. **Totiente de uma Potência de Primo:** $\\varphi(p^k)=p^k-p^{k-1}=p^k(1-\\frac{1}{p})$.
            Esta função é central na criptografia moderna, nomeadamente no algoritmo RSA.
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
        r4_1 = st.radio("1. O que postula a célebre Hipótese de Riemann?", ["Que todas as diagonais quadráticas geram primos.", "Que todas as raízes não triviais da função zeta complexa têm parte real igual a 1/2.", "Que a função totiente é constante."], key="r4_1")
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
    st.markdown('<div class="modulo-caixa-moldura"><div class="modulo-barra-titulo">🟡 MÓDULO 5: PADRÕES NUMÉRICOS</div></div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa & Gráficos", "✍️ Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("5.1 Números Triangulares e a Abordagem Geométrica de Contagem", expanded=False):
            st.markdown("""
            **Explicação Teórica:**
            Os números triangulares pertencem ao grupo dos chamados números figurados, que se caracterizam por serem números que podem ser representados através de arranjos geométricos de pontos regulares. Esta abordagem visual é de extrema importância na aprendizagem matemática, pois transforma problemas de contagem abstrata numa perceção geométrica muito intuitiva. Eles representam a quantidade de pontos necessária para construir um triângulo equilátero com um determinado número de linhas. Como cada nova linha adiciona sempre mais um ponto do que a linha anterior, um número triangular corresponde diretamente à soma dos primeiros números naturais.
            """)
            st.latex(r"T_{n}=1+2+3+\dots+n=\frac{n(n+1)}{2}")
            st.markdown("""
            Esta fórmula matemática pode ser explicada através de um raciocínio geométrico muito simples que é atribuído historicamente a Gauss. Se escrevermos a sequência da soma na sua ordem direta e na sua ordem inversa, conseguimos agrupar os termos verticalmente aos pares. Ao somarmos as duas equações, cada par de termos resulta invariavelmente no valor de $n+1$. Dado que existem exatamente $n$ termos nesta sequência, a soma total das duas linhas passa a ser escrita como $2T_{n}=n(n+1)$. Logo, basta dividir o resultado por dois para isolar o termo inicial.
            
            **Aplicação Concreta no Quotidiano:**
            Os números triangulares possuem diversas aplicações práticas em problemas reais de contagem e organização. Um exemplo clássico é a modelação e contagem de ligações em redes de comunicação. Se tivermos uma sala com 6 pessoas e quisermos saber quantos apertos de mão únicos ocorrem se todas se cumprimentarem uma única vez, o cálculo resolve-se através do número triangular $T_{5}$:
            """)
            st.latex(r"T_5 = \frac{5 \times (5+1)}{2} = 15 \text{ apertos de mão}")
            st.markdown("Este mesmo raciocínio aplica-se ao determinar o número de canais diretos necessários para interligar computadores ou servidores numa rede sem que haja repetições de caminhos.")
            
            if GRAFICOS_ATIVOS:
                st.markdown("<div style='text-align: center; font-weight: bold;'>📐 Representação Geométrica do Triângulo Pitagórico (3, 4, 5)</div>", unsafe_allow_html=True)
                fig_tri, ax_tri = plt.subplots(figsize=(1.8, 1.8))
                x_tri = [0, 4, 0, 0]
                y_tri = [0, 0, 3, 0]
                ax_tri.plot(x_tri, y_tri, 'k-', linewidth=1.5)
                ax_tri.fill([0, 4, 0], [0, 0, 3], color='lightblue', alpha=0.4)
                
                ax_tri.text(2, -0.5, "4", fontsize=10, ha='center')
                ax_tri.text(-0.5, 1.5, "3", fontsize=10, va='center', rotation=90)
                ax_tri.text(2, 1.7, "5", fontsize=10, ha='center')
                
                ax_tri.plot([0, 0.3, 0.3, 0], [0, 0, 0.3, 0], 'k-', linewidth=1.2)
                ax_tri.axis('equal')
                ax_tri.axis('off')
                st.pyplot(fig_tri)
            
        with st.expander("5.2 Números Perfeitos e Harmonia de Divisores", expanded=False):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            Um número perfeito define-se como um número inteiro positivo que é exatamente igual à soma de todos os seus divisores próprios, considerando-se divisores próprios todos os fatores que são estritamente menores do que o próprio número. Esta definição clássica remonta aos *Elementos de Euclides*, refletindo o interesse por propriedades estéticas de equilíbrio e harmonia aritmética.
            
            **Exemplos Clássicos:**
            * **Número 6:** Os seus divisores próprios são {1, 2, 3}. Ao somarmos estes fatores, obtemos: $1+2+3=6$.
            * **Número 28:** Os seus divisores próprios são {1, 2, 4, 7, 14}. A sua soma resulta em: $1+2+4+7+14=28$.
            
            A análise profunda dos números perfeitos pares revela uma ligação direta com os Primos de Mersenne, que assumem a forma de $2^{p}-1$, onde o expoente $p$ é primo. Euclides demonstrou formalmente que, sempre que $2^{p}-1$ for um número primo, gera-se um número perfeito par através da fórmula:
            """)
            st.latex(r"n=2^{p-1}(2^{p}-1)")
            
        with st.expander("5.3 Exploração do Número 9 na Base Decimal", expanded=False):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            O número 9 ocupa um lugar de destaque no âmbito da aritmética elementar devido à organização do nosso sistema de numeração posicional em base 10. Pelo facto de o número 9 ser exatamente uma unidade inferior à base do sistema $(10-1)$, cria-se um conjunto único de simetrias repetitivas, regras de divisibilidade facilitadas e padrões visuais muito claros nos seus algarismos.
            
            Iniciando com as propriedades modulares, verifica-se que qualquer número inteiro positivo é sempre congruente com a soma dos seus próprios algarismos em módulo 9:
            """)
            st.latex(r"n \equiv \text{soma dos dígitos de } n \pmod 9")
            st.markdown("""
            Esta propriedade fundamental serve para justificar o critério de divisibilidade por 9. Adicionalmente, os resultados da tabuada elementar do 9 funcionam como um verdadeiro **espelho numérico** que ilustra com precisão a complementaridade entre as dezenas e as unidades. 
            
            Se analisarmos a progressão dos produtos desde o início, observamos uma simetria visual inversa evidente onde os resultados se invertem simetricamente em pares: por exemplo, os resultados de $9 \times 2 = 18$ e $9 \times 9 = 81$ são o espelho exato um do outro. O mesmo fenómeno ocorre com o par $9 \times 3 = 27$ e $9 \times 8 = 72$, ou com $9 \times 4 = 36$ e $9 \times 7 = 63$. Em todos estes produtos da tabuada, a soma dos dígitos mantém-se fixa no valor de 9.
            
            Esta estabilidade nos padrões numéricos estende-se também ao comportamento das potências do número 9, cuja explicação algébrica assenta na relação matemática onde $9^{n}=(10-1)^{n}$. Analisando a redução digital destas potências, as somas dos algarismos geram ciclos regulares invariáveis ($9^1=9$; $9^2=81 \rightarrow 9$; $9^3=729 \rightarrow 18 \rightarrow 9$).
            """)
            
            st.markdown("#### 🔄 Laboratório de Redução Digital Dinâmica (Módulo 9)")
            st.markdown("Insira qualquer número inteiro positivo para ver a propriedade teórica do colapso digital e o seu resto na congruência modular:")
            
            num_9_input = st.text_input("Introduza um número inteiro grande:", value="432", key="num_9_input")
            
            if num_9_input.isdigit() and int(num_9_input) > 0:
                n_atual = int(num_9_input)
                passos = [str(n_atual)]
                
                while n_atual > 9:
                    soma_digitos = sum(int(d) for d in str(n_atual))
                    passos.append(str(soma_digitos))
                    n_atual = soma_digitos
                
                caminho_setas = " ➔ ".join(passos)
                st.info(f"**Cadeia de Colapso Digital:** {caminho_setas}")
                
                col_9_1, col_9_2 = st.columns(2)
                with col_9_1:
                    st.metric("Raiz Digital Final (Dígito Único):", f"{n_atual}")
                with col_9_2:
                    resto_mod = int(num_9_input) % 9
                    st.metric("Resto da Divisão por 9 (Módulo 9):", f"{resto_mod}")
                
                if n_atual == 9:
                    st.success(f"🟩 Como a raiz digital colapsou em 9, o número {num_9_input} é um múltiplo exato de 9!")
                else:
                    st.warning(f"🟨 O número colapsou em {n_atual}, logo não é múltiplo exato de 9. O seu resto modular é exatamente {resto_mod}.")
            else:
                st.error("Por favor, introduza apenas números inteiros estritamente positivos.")
            
        with st.expander("5.4 O Último Teorema de Fermat e a Limitação de Padrões", expanded=False):
            st.markdown("""
            **Explicação Teórica:**
            O Último Teorema de Fermat ilustra como pequenas alterações numa expressão matemática podem fazer com que um padrão de soluções infinitas desapareça por completo. No caso do expoente $n=2$, a equação transforma-se na clássica expressão de Pitágoras: $a^2+b^2=c^2$. Esta estrutura admite uma infinidade de triplas pitagóricas inteiras positivas, como o caso 3-4-5 ($3^2+4^2=5^2$).
            
            Contudo, Fermat afirmou na margem do seu livro que a equação geral:
            """)
            st.latex(r"a^{n}+b^{n}=c^{n}")
            st.markdown("""
            **não admite qualquer tipo de solução inteira não trivial** sempre que o expoente $n$ for um número estritamente maior do que 2 ($n>2$). Ao alterarmos apenas o valor do expoente, passamos de soluções infinitas para um vazio total. A prova definitiva foi alcançada utilizando conceitos contemporâneos sofisticados como curvas elípticas.
            """)
            
            if GRAFICOS_ATIVOS:
                st.markdown("<div style='text-align: center; font-weight: bold;'>📊 Simulação Dinâmica e Comparação Conceitual das Curvas de Fermat</div>", unsafe_allow_html=True)
                
                n_input_txt = st.text_input("Introduza o expoente n (> 2) para testar graficamente ($a^n + b^n = 5^n$):", value="3.0")
                
                try:
                    n_fermat = float(n_input_txt)
                    if n_fermat <= 2:
                        st.warning("Introduza um valor estritamente superior a 2 para analisar o comportamento geométrico das curvas limites.")
                        n_fermat = 2.1
                except ValueError:
                    st.error("Introduza um valor numérico válido (ex: 3, 4.2).")
                    n_fermat = 3.0

                a_grid = np.linspace(0, 5, 400)
                b_grid = np.linspace(0, 5, 400)
                A, B = np.meshgrid(a_grid, b_grid)
                
                fig_fer, ax_fer = plt.subplots(figsize=(2.0, 2.0))
                
                C2 = A**2 + B**2
                ax_fer.contour(A, B, C2, levels=[25], colors='blue', linewidths=1.5)
                
                Cn = A**n_fermat + B**n_fermat
                ax_fer.contour(A, B, Cn, levels=[25], colors='red', linestyles='--', linewidths=1.5)
                
                ax_fer.scatter([3], [4], color='blue', s=30, zorder=5)
                
                ax_fer.set_title("Curva Limite: $a^n + b^n = c^n$", fontsize=9)
                ax_fer.set_xlabel("a", fontsize=8)
                ax_fer.set_ylabel("b", fontsize=8)
                ax_fer.grid(alpha=0.2)
                
                from matplotlib.lines import Line2D
                handles = [
                    Line2D([0], [0], color='blue', lw=1.5, linestyle='-'),
                    Line2D([0], [0], color='red', lw=1.5, linestyle='--')
                ]
                labels = ["n = 2", f"n = {n_fermat:.1f}"]
                ax_fer.legend(handles, labels, loc="upper right", fontsize=7)
                
                st.pyplot(fig_fer)

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