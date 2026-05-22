import streamlit as st

# Configuração da página web
st.set_page_config(page_title="MathXplore - ISCTE Sintra", layout="wide")

# ---- MENU LATERAL (Navegação por Módulos/Trabalhos) ----
st.sidebar.title("🌐 MathXplore")
st.sidebar.markdown("**Fundamentos de Matemática**\n*Licenciatura em MATD*")
st.sidebar.markdown("---")

# Opções de navegação baseadas exatamente nos 5 documentos enviados
page = st.sidebar.radio(
    "Selecione o Módulo de Estudo:",
    [
        "Página Inicial",
        "Módulo 1: Padrões dos Primos",
        "Módulo 2: Padrões Numéricos",
        "Módulo 3: Lógica do Number Match",
        "Módulo 4: Grupos de Simetria",
        "Módulo 5: 17 Grupos do Plano"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 ISCTE Sintra")
st.sidebar.caption("Catarina Pereira & Beatriz Correia")

# ==============================================================================
# PÁGINA INICIAL
# ==============================================================================
if page == "Página Inicial":
    st.title("🚀 Bem-vindo ao MathXplore")
    st.subheader("Plataforma Interativa de Fundamentos de Matemática")
    
    st.markdown("""
    Este ecossistema digital reúne e estende os conteúdos científicos desenvolvidos nos cinco projetos teóricos da unidade curricular.
    Cada página corresponde a um documento original, ramificado em conceitos estruturados sob a metodologia de **Explicação, Aplicação e Exercício**.
    
    ### 📂 Estrutura de Aprendizagem:
    * **Módulo 1:** Teoria dos Números, Espiral de Ulam e Função Totiente de Euler.
    * **Módulo 2:** Números Figurados (Triangulares), Números Perfeitos e o Último Teorema de Fermat.
    * **Módulo 3:** Modelação de Sistemas Discretos (Jogo *Number Match*) através de Lógica Proposicional e Teoria de Grafos.
    * **Módulo 4:** Introdução Abstrata à Teoria de Grupos, Isometrias e Eficiência de Estruturas Virais.
    * **Módulo 5:** Classificação Periódica Bidimensional e Análise dos 17 Grupos Cristalográficos do Plano.
    
    *Navegue utilizando o menu lateral à esquerda para iniciar os estudos e os laboratórios práticos.*
    """)

# ==============================================================================
# MÓDULO 1: PADRÕES DOS PRIMOS (FM_4ºprojeto.pdf)
# ==============================================================================
elif page == "Módulo 1: Padrões dos Primos":
    st.title("🟣 Módulo 1: Padrões dos Primos – Da Espiral ao Totiente")
    st.caption("Baseado em: *FM_4ºprojeto.pdf* | Autoras: Catarina Pereira, Beatriz Correia | Prof. Rosário Laureano (Março 2026)")
    
    # --- CONCEITO 1 ---
    st.markdown("---")
    st.header("1. A Espiral de Ulam e Alinhamentos Quadráticos")
    
    st.info("💡 **Explicação:**")
    st.markdown("Em 1963, Stanislaw Ulam organizou os números naturais numa espiral quadrada bidimensional[cite: 66, 67]. Ao destacar os números primos, descobriu que estes não se distribuíam aleatoriamente, mas sim em **diagonais longas e bem definidas**[cite: 68]. Estas diagonais correspondem a polinómios quadráticos da forma $an^2 + bn + c$[cite: 184].")
    
    st.success("🎯 **Aplicação:**")
    st.markdown("O exemplo histórico mais célebre é o polinómio de Euler, $n^2 + n + 41$, que é capaz de gerar números primos consecutivos para todos os valores inteiros de $n$ no intervalo de $0$ a $39$[cite: 186, 187, 188].")
    
    # Exercício 1
    q1_1 = st.radio(
        "**Exercício 1.1:** O que justifica a densidade visual de certas diagonais na Espiral de Ulam?",
        ["Apenas uma coincidência estatística sem fundo matemático.", 
         "O facto de essas diagonais corresponderem a polinómios quadráticos que geram uma elevada quantidade de primos.", 
         "A organização exclusiva de números pares naquelas linhas."],
        key="q1_1", index=0
    )
    if q1_1 == "O facto de essas diagonais corresponderem a polinómios quadráticos que geram uma elevada quantidade de primos.":
        st.success("⭐ **Correto!** Quando estes polinómios geram muitos primos, a diagonal correspondente torna-se visualmente densa[cite: 191].")
        
    # --- CONCEITO 2 ---
    st.markdown("###")
    st.info("💡 **Explicação:**")
    st.markdown("A **Função Totiente de Euler**, $\\varphi(n)$, introduzida por Euler, conta quantos números naturais até $n$ são coprimos com $n$ [cite: 204] (ou seja, cujo $mdc(a,b)=1$ [cite: 219, 220]). Se $p$ for um número primo, todos os inteiros menores que ele são coprimos, logo $\\varphi(p) = p - 1$[cite: 225, 226, 227, 228].")
    
    st.success("🎯 **Aplicação:**")
    st.markdown("Para $n = 12$, os números menores ou iguais coprimos são {1, 5, 7, 11}, logo $\\varphi(12) = 4$[cite: 208, 209]. Em criptografia moderna (como o algoritmo RSA), a segurança baseia-se na extrema dificuldade de calcular $\\varphi(n)$ para números grandes sem conhecer a sua fatorização primordial[cite: 271].")
    
    # Exercício 2
    q1_2 = st.radio(
        "**Exercício 1.2:** Sendo 17 um número primo, qual é o valor exato da função totiente $\\varphi(17)$?",
        ["17", "16", "1", "8"],
        key="q1_2", index=0
    )
    if q1_2 == "16":
        st.success("⭐ **Correto!** Como 17 é primo, todos os 16 números inferiores são coprimos com ele, logo $\\varphi(17) = 17 - 1 = 16$[cite: 227, 228].")

# ==============================================================================
# MÓDULO 2: PADRÕES NUMÉRICOS (trabalho_5_novo.pdf)
# ==============================================================================
elif page == "Módulo 2: Padrões Numéricos":
    st.title("🟡 Módulo 2: Padrões Numéricos – Dos Triangulares a Fermat")
    st.caption("Baseado em: *trabalho_5_novo.pdf* | Autoras: Catarina Pereira, Beatriz Correia | Prof. Rosário Laureano (Maio 2026)")
    
    # --- CONCEITO 1 ---
    st.markdown("---")
    st.header("1. Números Triangulares e Contagem")
    
    st.info("💡 **Explicação:**")
    st.markdown("Os números triangulares pertencem aos números figurados e representam a quantidade de pontos necessários para construir um triângulo equilátero com $n$ linhas[cite: 324, 326]. Correspondem diretamente à soma dos primeiros $n$ números naturais, cuja fórmula geral é[cite: 327, 328]:")
    st.latex(r"T_n = \frac{n(n+1)}{2}")
    
    st.success("🎯 **Aplicação:**")
    st.markdown("Este raciocínio aplica-se na modelação de canais de redes de comunicação ou problemas de partilha[cite: 350, 355]. Por exemplo, numa sala com 6 pessoas, se todas se cumprimentarem uma única vez, o número de apertos de mão é dado por $T_5 = \\frac{5 \\times 6}{2} = 15$[cite: 351, 352, 353, 354].")
    
    # Exercício 1
    q2_1 = st.radio(
        "**Exercício 2.1:** Pretende-se interligar 8 computadores numa rede local de modo a que cada um tenha um canal direto e único com todos os outros. Quantas ligações são necessárias?",
        ["64 ligações", "56 ligações", "28 ligações"],
        key="q2_1", index=0
    )
    if q2_1 == "28 ligações":
        st.success("⭐ **Correto!** O problema é modelado pelo número triangular $T_7$ (visto que o último computador liga aos 7 anteriores). $T_7 = \\frac{7 \\times 8}{2} = 28$ ligações.")

    # --- CONCEITO 2 ---
    st.markdown("###")
    st.header("2. O Último Teorema de Fermat")
    
    st.info("💡 **Explicação:**")
    st.markdown("O Último Teorema de Fermat estabelece limites rígidos aos padrões aritméticos[cite: 401, 402]. Enquanto a equação de expoente quadrático $a^2 + b^2 = c^2$ possui infinitas soluções inteiras positivas (triplas pitagóricas)[cite: 403, 405], Fermat afirmou que a equação geral:")
    st.latex(r"a^n + b^n = c^n")
    st.markdown("**não admite qualquer solução inteira não trivial** para expoentes estritamente maiores que 2 ($n > 2$)[cite: 414, 416].")
    
    st.success("🎯 **Aplicação:**")
    st.markdown("No caso $n=2$, temos a famosa tripla estável 3-4-5, onde $3^2 + 4^2 = 9 + 16 = 25 = 5^2$[cite: 406, 407, 408]. Se alterarmos o expoente para $n=3$, torna-se matematicamente impossível encontrar três inteiros limpos que satisfaçam a igualdade Cubo[cite: 425, 426]. A prova universal só foi obtida em 1994 por Andrew Wiles[cite: 431].")
    
    # Exercício 2
    q2_2 = st.radio(
        "**Exercício 2.2:** Qual é a principal lição conceptual dada pelo Último Teorema de Fermat na Teoria dos Números?",
        ["Que todas as equações algébricas têm soluções inteiras se os números forem muito grandes.",
         "Que pequenas variações no expoente de uma equação alteram radicalmente o comportamento e a existência de soluções, provando que os padrões têm fronteiras.",
         "Que o Teorema de Pitágoras deixa de funcionar em triângulos retângulos se mudarmos de escala."],
        key="q2_2", index=0
    )
    if q2_2 == "Que pequenas variações no expoente de uma equação alteram radicalmente o comportamento e a existência de soluções, provando que os padrões têm fronteiras.":
        st.success("⭐ **Correto!** Mostra como passamos de um sistema rico em soluções infinitas para um vazio total através de uma ligeira alteração estrutural[cite: 426, 433].")

# ==============================================================================
# MÓDULO 3: LOGICA DO NUMBER MATCH (FM_3ºProjeto__Copy_.pdf)
# ==============================================================================
elif page == "Módulo 3: Lógica do Number Match":
    st.title("🟢 Módulo 3: A Lógica Matemática por Trás do Jogo Number Match")
    st.caption("Baseado em: *FM_3ºProjeto__Copy_.pdf* | Autoras: Catarina Pereira, Beatriz Correia | Prof. Rosário Laureano (Abril 2026)")
    
    # --- CONCEITO 1 ---
    st.markdown("---")
    st.header("1. Formalização Lógica de Regras")
    
    st.info("💡 **Explicação:**")
    st.markdown("Sistemas finitos baseados em regras discretas, como jogos, podem ser formalizados via lógica proposicional. No *Number Match*, uma eliminação de um par de números $a$ e $b$ só é válida se a condição numérica (serem iguais ou somarem 10) **E** a condição estrutural (estarem conectados) forem simultaneamente verdadeiras:")
    st.latex(r"\text{Jogada Válida}(a, b) \leftrightarrow (a = b \lor a + b = 10) \land \text{Conectados}(a, b)")
    
    st.success("🎯 **Aplicação:**")
    st.markdown("Se tivermos um 3 e um 7 adjacentes no tabuleiro, a conjunção é verdadeira e o par é eliminado. Contudo, se tivermos dois números 5 em posições isoladas e distantes, a condição de conectividade falha, tornando a proposição logicamente falsa e impedindo a jogada.")
    
    # Exercício 1
    q3_1 = st.radio(
        "**Exercício 3.1:** Se o tabuleiro contiver dois algarismos iguais (ex: 4 e 4) mas que estão bloqueados por outras linhas, a proposição 'Jogada Válida(4, 4)' assume que valor lógico?",
        ["Verdadeiro, porque a condição numérica de igualdade (a=b) foi satisfeita.",
         "Falso, porque a conjunção lógica exige que a condição estrutural 'Conectados' também seja verdadeira.",
         "Inconclusivo sem analisar os graus de todos os vértices."],
        key="q3_1", index=0
    )
    if q3_1 == "Falso, because a conjunção lógica exige que a condição estrutural 'Conectados' também seja verdadeira.":
        st.success("⭐ **Correto!** O conectivo lógico $\\land$ (E) obriga a que ambas as premissas sejam simultaneamente verdadeiras para validar a operação.")

    # --- CONCEITO 2 ---
    st.markdown("###")
    st.header("2. O Fator de Paridade do Número 5")
    
    st.info("💡 **Explicação:**")
    st.markdown("Analisando o jogo sob a ótica combinatória e de paridade, cada número de 1 a 9 possui um parceiro único para somar 10 (ex: $3 \\leftrightarrow 7$)[cite: 529, 530]. Contudo, o **número 5 constitui um caso particular**, pois apenas pode formar par de soma 10 **consigo próprio** ($5 \\leftrightarrow 5$).")
    
    st.success("🎯 **Aplicação:**")
    st.markdown("Isto implica que, para garantir a eliminação completa do tabuleiro sem estados permanentes de bloqueio, a frequência total de aparecimento do número 5 no jogo deve ser obrigatoriamente **par**. Se surgir um número ímpar de vezes, pelo menos um 5 ficará fatalmente isolado (vértice de grau zero).")
    
    # Exercício 2
    q3_2 = st.radio(
        "**Exercício 3.2:** Se a distribuição de números num tabuleiro deixar sobrar exatamente três cartas com o número 5, qual será o impacto estratégico?",
        ["Nenhum, pois podem ser eliminados com cartas de valor 1 e 9.",
         "O jogo entrará inevitavelmente num estado de bloqueio permanente, pois um 5 ficará isolado por argumentos de paridade.",
         "O grafo transforma-se num circuito fechado de Euler."],
        key="q3_2", index=0
    )
    if q3_2 == "O jogo entrará inevitavelmente num estado de bloqueio permanente, pois um 5 ficará isolado por argumentos de paridade.":
        st.success("⭐ **Correto!** Como o 5 só emparelha consigo mesmo para somar 10, quantidades ímpares quebram a simetria de emparelhamento em conjuntos finitos.")

# ==============================================================================
# MÓDULO 4: GRUPOS DE SIMETRIA (FM_1ºprojeto .pdf)
# ==============================================================================
elif page == "Módulo 4: Grupos de Simetria":
    st.title("🔵 Módulo 4: Introdução aos Grupos de Simetria")
    st.caption("Baseado em: *FM_1ºprojeto .pdf* | Autoras: Catarina Pereira, Beatriz Correia | Prof. Rosário Laureano (Março 2026)")
    
    # --- CONCEITO 1 ---
    st.markdown("---")
    st.header("1. Isometrias no Plano Bidimensional")
    
    st.info("💡 **Explicação:**")
    st.markdown("Uma isometria é uma transformação geométrica que preserva as distâncias e os ângulos entre pontos. No plano, existem quatro transformações rígidas fundamentais:")
    st.markdown("""
    * **Translações:** Deslocação de uma figura numa direção e magnitude constantes.
    * **Rotações:** Giro de uma figura em torno de um ponto fixo por um determinado ângulo.
    * **Reflexões:** Espelhamento simétrico de uma figura em relação a uma reta direta.
    * **Reflexões Deslizantes (*Glide Reflections*):** Composição de uma reflexão axial com uma translação paralela a esse mesmo eixo.
    """)
    
    st.success("🎯 **Aplicação:**")
    st.markdown("Observamos estas transformações na arte (como as pavimentações ornamentais de peixes de M. C. Escher) e em instrumentos óticos como o caleidoscópio, que multiplica reflexões para gerar rotações cíclicas.")
    
    # Exercício 1
    q4_1 = st.radio(
        "**Exercício 4.1:** Que nome se dá à transformação rígida que combina, de forma síncrona, uma reflexão e uma translação com eixo paralelo?",
        ["Rotação oblíqua", "Reflexão deslizante (Glide reflection)", "Composição de Fecho neutro"],
        key="q4_1", index=0
    )
    if q4_1 == "Reflexão deslizante (Glide reflection)":
        st.success("⭐ **Correto!** Esta combinação mantém a preservação de distâncias planeares sendo uma isometria fundamental].")

    # --- CONCEITO 2 ---
    st.markdown("###")
    st.header("2. Eficiência Biológica do Icosaedro Regular")
    
    st.info("💡 **Explicação:**")
    st.markdown("A Teoria de Grupos permite estudar o conjunto de simetrias de um objeto tridimensional através de propriedades abstratas. Na natureza, destaca-se o **Icosaedro** (um dos cinco Sólidos Platónicos), composto por 20 faces triangulares regulares.")
    
    st.success("🎯 **Aplicação:**")
    st.markdown("Muitos vírus esféricos (como o vírus Zika, Adenovírus ou Poliovírus) adotam cápsides icosaédricas. Geometricamente, esta estrutura exibe múltiplos eixos de simetria rotacional de ordens 2, 3 e 5. Isto permite ao vírus usar um único gene para codificar uma pequena proteína repetitiva que se monta perfeitamente por rotações, minimizando o gasto de informação genética para encapsular o genoma.")
    
    # Exercício 2
    q4_2 = st.radio(
        "**Exercício 4.2:** Sob o ponto de vista da eficiência genética dos capsídeos virais, qual a vantagem da simetria rotacional icosaédrica?",
        ["Permite codificar proteínas maiores e mais pesadas.",
         "Permite que subunidades proteicas idênticas e pequenas se encaixem repetidamente por rotações para formar uma cápsula estável, poupando espaço genético.",
         "Impede a translação linear do vírus no sangue."],
        key="q4_2", index=0
    )
    if q4_2 == "Permite que subunidades proteicas idênticas e pequenas se encaixem repetidamente por rotações para formar uma cápsula estável, poupando espaço genético.":
        st.success("⭐ **Correto!** Esta organização repetitiva permite otimizar o espaço de armazenamento do código genético do vírus através da repetição geométrica simétrica.")

# ==============================================================================
# MÓDULO 5: 17 GRUPOS CRISTALOGRÁFICOS (FM_2ºProjeto.pdf)
# ==============================================================================
elif page == "Módulo 5: 17 Grupos do Plano":
    st.title("🟤 Módulo 5: Os 17 Grupos Cristalográficos do Plano")
    st.caption("Baseado em: *FM_2ºProjeto.pdf* | Autoras: Catarina Pereira, Beatriz Correia | Prof. Rosário Laureano (Março 2026)")
    
    # --- CONCEITO 1 ---
    st.markdown("---")
    st.header("1. A Restrição Cristalográfica Plana")
    
    st.info("💡 **Explicação:**")
    st.markdown("Uma tesselação periódica é um padrão geométrico capaz de cobrir o plano bidimensional de forma contínua, repetindo-se indefinidamente através de translações]. Embora a criatividade humana permita desenhar infinitos mosaicos, a restrição geométrica demonstra de forma absoluta que **existem apenas exatamente 17 tipos estruturais de simetria** capazes de pavimentar o plano.")
    
    st.success("🎯 **Aplicação:**")
    st.markdown("Esta classificação unifica os padrões observados nos azulejos históricos da Andaluzia, as estruturas cristalinas em laboratório e as gravuras periódicas de M. C. Escher.")
    
    # Exercício 1
    q5_1 = st.radio(
        "**Exercício 5.1:** Quantas variedades estruturais de simetria bidimensional existem para classificar qualquer padrão que pavimente o plano de forma periódica?",
        ["Infinitas variações dependendo do design.", "Exatamente 17 grupos.", "Apenas 4 grupos devido às 4 isometrias."],
        key="q5_1", index=0
    )
    if q5_1 == "Exatamente 17 grupos.":
        st.success("⭐ **Correto!** Qualquer mosaico periódico no mundo pertence estritamente a um dos 17 'wallpaper groups' cristalográficos.")

    # --- CONCEITO 2 ---
    st.markdown("###")
    st.header("2. Comparação de Subgrupos: p4, p6 e pm")
    
    st.info("💡 **Explicação:**")
    st.markdown("Os 17 grupos diferenciam-se pelas ordens de rotação permitidas e pela existência de eixos axiais de reflexão ou reflexões deslizantes:")
    st.markdown("""
    * **Grupo p4:** Caracteriza-se por rotações de ordem 4 e 2 (90° e 180°), numa rede de translação quadrada, mas **não possui reflexões axiais**.
    * **Grupo p6:** O mais simétrico em termos rotacionais. Possui rotações de ordem 6, 3 e 2 (ângulos de 60°), rede hexagonal (como favos de mel), mas **carece de reflexões**.
    * **Grupo pm:** Estrutura simples sem qualquer rotação. Baseia-se em **reflexões axiais paralelas** com rede retangular.
    """)
    
    st.success("🎯 **Aplicação:**")
    st.markdown("Se analisares os favos de mel das abelhas, encontras a eficiência e simetria hexagonal pura ligada ao grupo *p6*. O que distingue o grupo puro *p4* do grupo *p4m*, por exemplo, é a ausência ou presença de eixos de espelhamento verdadeiros na malha quadrada[cite: 728].")
    
    # Exercício 2
    q5_2 = st.radio(
        "**Exercício 5.2:** Qual é a diferença fundamental que distingue o grupo cristalográfico 'p6' do grupo 'p6m'?",
        ["O grupo p6 possui rotações de 90° e o p6m não.",
         "Ambos têm rotações hexagonais, mas o grupo p6 não possui eixos axiais de reflexão, ao contrário do p6m.",
         "A rede de translação do p6 é retangular e a do p6m é quadrada."],
        key="q5_2", index=0
    )
    if q5_2 == "Ambos têm rotações hexagonais, mas o grupo p6 não possui eixos axiais de reflexão, ao contrário do p6m.":
        st.success("⭐ **Correto!** A ausência de reflexões puras é o critério geométrico que define o grupo p6 face ao seu homólogo p6m.")