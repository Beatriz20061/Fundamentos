import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página web para alto impacto visual
st.set_page_config(page_title="MathXplore Completo", layout="wide", page_icon="🔢")

# Injeção de CSS personalizado para estética de plataforma premium e animações
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stButton>button {
        border-radius: 12px;
        background: linear-gradient(135deg, #4f46e5 0%, #3730a3 100%);
        color: white;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.4);
    }
    .section-block {
        background-color: white;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- NAVEGAÇÃO LATERAL ----
st.sidebar.title("🔢 MathXplore Pro")
st.sidebar.markdown("*Fundamentos de Matemática — ISCTE Sintra*")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navegação Principal:",
    [
        "🏠 Página Inicial",
        "🟣 Módulo 1: Padrões dos Primos (Da Espiral ao Totiente)",
        "🟡 Módulo 2: Padrões Numéricos (Dos Triangulares a Fermat)",
        "🟢 Módulo 3: A Lógica por Trás do Number Match",
        "🔵 Módulo 4: Introdução aos Grupos de Simetria",
        "🟤 Módulo 5: 17 Grupos Cristalográficos do Plano"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Desenvolvido por: Catarina Pereira & Beatriz Correia")
st.sidebar.caption("Docente: Prof. Rosário Laureano (2026)")

# ==============================================================================
# 🏠 PÁGINA INICIAL
# ==============================================================================
if page == "🏠 Página Inicial":
    st.title("💡 Bem-vindo ao MathXplore")
    st.subheader("Enciclopédia Digital Interativa de Fundamentos de Matemática")
    
    st.markdown("""
    Esta plataforma foi desenhada para albergar a totalidade dos conteúdos teóricos, dados e representações 
    gráficas desenvolvidos ao longo do ano letivo. O nosso grande objetivo é demonstrar que a estrutura 
    dos números inteiros combina uma enorme regularidade com limites rígidos que desafiaram os matemáticos durante séculos.
    
    Aqui, a teoria exaustiva une-se a simulações computacionais em Python, permitindo-te testar e validar 
    propriedades aritméticas em tempo real.
    
    ### 📂 Navegação por Trabalhos Originais:
    * **Módulo 1:** Teoria dos Números, Espiral de Ulam e Função Totiente de Euler.
    * **Módulo 2:** Números Figurados (Triangulares), Números Perfeitos e o Último Teorema de Fermat.
    * **Módulo 3:** Lógica Proposicional, Teoria de Grafos Dinâmicos e Combinatória de Paridade no *Number Match*.
    * **Módulo 4:** Isometrias, Teoria Abstrata de Grupos e Eficiência de Estruturas Virais Icosaédricas.
    * **Módulo 5:** Classificação Periódica Bidimensional e aprofundamento dos 17 Grupos de Wallpaper.
    """)
    st.image("https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&w=800&q=80")

# ==============================================================================
# 🟣 MÓDULO 1: PADRÕES DOS PRIMOS
# ==============================================================================
elif page == "🟣 Módulo 1: Padrões dos Primos (Da Espiral ao Totiente)":
    st.title("🟣 Módulo 1: Padrões dos Primos – Da Espiral ao Totiente")
    
    st.markdown("""
    A Teoria dos Números é um dos ramos mais antigos e fascinantes da matemática. Apesar de lidar com objetos aparentemente simples, 
    os números inteiros, revela estruturas profundas e padrões inesperados. Esta ideia é destacada por G. H. Hardy na sua obra 
    *A Mathematician's Apology* (1940), onde defende que a matemática pura possui uma beleza intrínseca, comparável à arte, 
    precisamente porque revela ordem onde antes se supunha irregularidade.
    """)
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa & Aplicações", "✍️ Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("1.1 A Natureza dos Números Primos", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            Os números primos são fundamentais na aritmética. O Teorema Fundamental da Aritmética estabelece que qualquer número inteiro positivo 
            pode ser decomposto de forma única num produto de primos. Esta unicidade confere aos primos um papel central na estrutura dos números inteiros. 
            Apesar da sua importância, a distribuição dos primos é notoriamente irregular. Du Sautoy (2003) descreve-os como 'notas musicais' 
            que parecem seguir um ritmo aparentemente aleatório, mas que escondem uma harmonia profunda.
            
            A irregularidade aparente levou matemáticos como Gauss e Riemann a procurar padrões estatísticos que explicassem esta oscilação entre ordem e caos. 
            Foi neste contexto que Riemann, em 1859, introduziu a função zeta complexa e formulou a célebre Hipótese de Riemann, segundo a qual todas as 
            raízes não triviais dessa função têm parte real igual a 1/2. Esta afirmação estabelece uma ligação direta entre o comportamento analítico da 
            função zeta e a distribuição dos números primos. A hipótese permanece em aberto e é considerada um dos problemas centrais da matemática contemporânea.
            """)
            
        with st.expander("1.2 Representações Visuais e a Construção da Espiral de Ulam", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            A visualização é uma ferramenta poderosa para revelar padrões. Muitas descobertas matemáticas surgem quando se representa um problema de forma inesperada (Stewart, 2006). 
            Foi precisamente isso que aconteceu com Stanislaw Ulam em 1963. Durante uma conferência, Ulam começou a desenhar os números naturais numa espiral quadrada, 
            marcando os números primos. O que parecia um exercício casual revelou algo extraordinário: os números primos alinhavam-se em diagonais longas e bem definidas.
            
            **Processo de Construção da Espiral:**
            * Coloca-se o número 1 no centro.
            * Os números seguintes são escritos em espiral, no sentido horário (sentido negativo).
            * Os números primos são destacados, revelando as matrizes diagonais densas.
            
            **Interpretação Matemática dos Alinhamentos:**
            As diagonais da espiral correspondem a expressões quadráticas do tipo $an^2+bn+c$. Quando estes polinómios geram muitos primos, 
            a diagonal correspondente torna-se visualmente densa. Assim, a espiral não cria primos, apenas torna visível a aritmética escondida nos polinómios.
            """)
            
            st.markdown("#### 🎛️ Laboratório Dinâmico: Polinómio de Euler ($n^2 + n + 41$)")
            st.markdown("**Aplicação:** Euler descobriu que algumas expressões quadráticas geram muitos primos consecutivos. O exemplo mais famoso produz primos para $n=0,1,2,\\dots,39$. Teste abaixo:")
            n_slider = st.slider("Altere o valor de n para verificar a geração determinística de primos:", 0, 39, 0)
            res_euler = (n_slider**2) + n_slider + 41
            st.metric(label=f"Resultado da Expressão para n={n_slider}", value=int(res_euler), delta="É um número Primo Confirmado!")
            
        with st.expander("1.3 A Função Totiente de Euler e Fórmula Multiplicativa", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            A função totiente $\\varphi(n)$, introduzida por Euler, conta quantos naturais até $n$ são coprimos com $n$. Segundo Rosen (2010), esta função é central na aritmética modular, 
            pois conta a quantidade de inteiros que mantêm uma relação 'simples' com $n$ quando considerados módulo $n$. Assim, $\\varphi(n)$ evidencia a estrutura multiplicativa dos inteiros e revela padrões que dependem diretamente dos fatores primos de cada número.
            
            **Fórmula Multiplicativa Geral:**
            Todo o número natural admite uma decomposição em fatores primos. Se $n=p_1^{a_1}p_2^{a_2}\\dots p_k^{a_k}$, em que os fatores são primos distintos, então:
            """)
            st.latex(r"\varphi(n)=n\prod_{i=1}^{k}\left(1-\frac{1}{p_i}\right)")
            st.markdown("""
            A função totiente é estritamente multiplicativa quando os fatores são coprimos entre si, ou seja, $\\varphi(ab)=\\varphi(a)\\varphi(b)$ se $mdc(a,b)=1$.
            
            **Propriedades Fundamentais:**
            1. **Totiente de um Número Primo:** Se $p$ é primo, então $\\varphi(p)=p-1$, porque todos os inteiros menores que ele são coprimos.
            2. **Totiente de uma Potência de Primo:** Para qualquer primo $p$ e inteiro $k \\ge 1$: $\\varphi(p^k)=p^k-p^{k-1}=p^k(1-\\frac{1}{p})$, pois apenas os múltiplos de $p$ não são coprimos.
            3. **Proporção:** A razão $\\frac{\\varphi(n)}{n}$ mede a fração de inteiros até $n$ coprimos com $n$. Se $n$ tem muitos fatores primos distintos, $\\varphi(n)$ é significativamente menor do que $n$.
            """)
            
            st.markdown("#### 🧮 Aplicação Prática: Calculadora Multiplicativa do Totiente")
            num_input = st.number_input("Introduza qualquer valor de n para executar o algoritmo computacional de Euler:", min_value=2, max_value=500, value=12)
            
            def phi(n):
                result = n
                p = 2
                while p * p <= n:
                    if n % p == 0:
                        while n % p == 0: n //= p
                        result -= result // p
                    p += 1
                if n > 1: result -= result // n
                return result
            st.write(f"**Resultado:** A quantidade de inteiros coprimos com {num_input} é: $\\varphi({num_input}) =$ `{phi(num_input)}`")

    with tab2:
        st.subheader("✍️ Questionário de Avaliação Geral — Módulo 1")
        score1 = 0
        q1 = st.radio("1. Qual foi a célebre hipótese formulada por Riemann em 1859 sobre a função zeta complexa?", 
                      ["Que todas as diagonais quadráticas geram infinitos números primos.", 
                       "Que todas as raízes não triviais da função têm parte real igual a 1/2.", 
                       "Que a função totiente é estritamente estável e periódica."])
        q2 = st.radio("2. Para n=12, os números coprimos com 12 são {1, 5, 7, 11}. Quanto vale o totiente de 12?", 
                      ["12", "6", "4", "2"])
        q3 = st.radio("3. Qual a fórmula correta do totiente de uma potência de um número primo (p^k)?",
                      [r"\phi(p^k) = p^k - p^(k-1)", r"\phi(p^k) = p^k - 1", r"\phi(p^k) = p - 1"])
        
        if q1 == "Que todas as raízes não triviais da função têm parte real igual a 1/2.": score1 += 3.33
        if q2 == "4": score1 += 3.33
        if q3 == r"\phi(p^k) = p^k - p^(k-1)": score1 += 3.34
        
        if st.button("Submeter Respostas do Módulo 1"):
            st.metric("Pontuação Obtida:", f"{round(score1, 1)}/10")

# ==============================================================================
# 🟡 MÓDULO 2: PADRÕES NUMÉRICOS
# ==============================================================================
elif page == "🟡 Módulo 2: Padrões Numéricos (Dos Triangulares a Fermat)":
    st.title("🟡 Módulo 2: Padrões Numéricos e Estruturas Aritméticas")
    
    tab1, tab2 = st.tabs(["Trabalho Teórico & Gráficos", "✍️ Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("2.1 Números Triangulares e a Abordagem Geométrica", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            Os números triangulares pertencem ao grupo dos chamados números figurados, que se caracterizam por ser números que podem ser representados através de arranjos geométricos de pontos regulares. 
            Esta abordagem visual é de extrema importância na aprendizagem matemática, pois transforma problemas de contagem abstrata numa perceção geométrica muito intuitiva. 
            No caso específico dos números triangulares, eles representam a quantidade de pontos necessária para construir um triângulo equilátero com um determinado número de linhas.
            
            Como cada nova linha adiciona sempre mais um ponto do que a linha anterior, um número triangular corresponde diretamente à soma dos primeiros números naturais. 
            A sua fórmula geral estabelece que a soma consecutiva até $n$ se calcula através da expressão:
            """)
            st.latex(r"T_n = 1+2+3+\dots+n = \frac{n(n+1)}{2}")
            st.markdown("""
            Esta fórmula matemática pode ser obtida através de um raciocínio geométrico simples atribuído historicamente a Gauss: se escrevermos a sequência da soma na sua ordem direta e, 
            logo abaixo, na sua ordem inversa, conseguimos agrupar os termos verticalmente aos pares, onde cada par resulta invariavelmente no valor de $n+1$. Como existem exatamente $n$ termos, 
            a soma total das duas linhas passa a ser escrita como $2T_n = n(n+1)$, bastando dividir por dois.
            
            **Aplicação Concreta:**
            Um exemplo clássico é a modelação e contagem de ligações em redes de comunicação. Se tivermos uma sala com 6 pessoas e quisermos saber quantos apertos de mão únicos ocorrem se todas se cumprimentarem uma única vez, o cálculo resolve-se através do número triangular $T_5 = \\frac{5 \\times (5+1)}{2} = 15$ apertos de mão. Este mesmo raciocínio aplica-se ao determinar o número de canais diretos necessários para interligar computadores ou servidores numa rede sem que haja repetições de caminhos.
            """)
            
        with st.expander("2.2 Números Perfeitos e Harmonia de Divisores", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            Um número perfeito define-se como um número inteiro positivo que é exatamente igual à soma de todos os seus divisores próprios, considerando-se divisores próprios todos os fatores que são estritamente menores do que o próprio número. Esta definição clássica remonta aos *Elementos de Euclides*, refletindo o interesse dos antigos matemáticos gregos por números que apresentassem propriedades estéticas de equilíbrio e harmonia aritmética.
            
            **Exemplos Práticos do Relatório:**
            * Para o número 6: os divisores próprios são {1, 2, 3}. Ao somarmos estes fatores, obtemos: $1+2+3=6$.
            * Para o número 28: os divisores próprios são {1, 2, 4, 7, 14}. A sua soma combinada resulta em: $1+2+4+7+14=28$.
            
            A análise profunda dos números perfeitos pares revela uma ligação direta com uma classe especial de números primos conhecidos como Primos de Mersenne, que assumem a forma matemática de $2^p-1$, onde o expoente $p$ é também um número primo. Euclides demonstrou formalmente que, sempre que o termo $2^p-1$ for de facto um número primo, é possível gerar um número perfeito par através da fórmula:
            """)
            st.latex(r"n = 2^{p-1}(2^p-1)")
            st.markdown("""
            Seguindo outra linguagem formal recorrendo à função soma de todos os divisores $\\sigma(n)$, diz-se que um número é perfeito sempre que satisfizer a identidade $\\sigma(n)=2n$. No caso do número 6, $\\sigma(6)=12$, que equivale precisamente ao dobro do número original. O estudo destes números revela ainda que todos os números perfeitos pares conhecidos são também números triangulares. Por outro lado, permanece em aberto a grande questão sobre a existência de números perfeitos ímpares. Autores de referência indicam que, se existir algum, ele terá de ser extraordinariamente grande e possuir uma estrutura de divisores extremamente restrita.
            """)
            
        with st.expander("2.3 Exploração do Número 9 na Base Decimal", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            O número 9 ocupa um lugar de destaque no âmbito da aritmética elementar devido à organização do nosso sistema de numeração posicional em base 10. Pelo facto de o número 9 ser precisamente uma unidade inferior à base do sistema ($10-1$), cria-se um conjunto único de simetrias repetitivas, regras de divisibilidade facilitadas e padrões visuais muito claros nos seus algarismos.
            
            Iniciando com as propriedades modulares, verifica-se que qualquer número inteiro positivo é sempre congruente com a soma dos seus próprios algarismos em módulo 9: $n \\equiv \\text{soma dos dígitos de } n \\pmod 9$. Esta propriedade justifica o critério de divisibilidade por 9. Tomemos como exemplo prático o número 432. Somando os algarismos: $4+3+2=9$, logo 432 é divisível por 9. Para um número maior como 981, a soma resulta em $9+8+1=18$, e somando novamente $1+8=9$, ilustrando como qualquer múltiplo de 9 acaba sempre por colapsar no próprio algarismo 9.
            
            Adicionalmente, os resultados da tabuada do 9 funcionam como um espelho numérico: os resultados de $9 \\times 2 = 18$ e $9 \\times 9 = 81$ são o inverso um do outro, o mesmo acontecendo com $9 \\times 3 = 27$ e $9 \\times 8 = 72$. Esta estabilidade estende-se ao comportamento das potências do número 9, cuja explicação algébrica assenta na relação matemática onde $9^n=(10-1)^n$. Ao expandirmos esta expressão através do Binómio de Newton, todos os termos desenvolvidos na equação passam a ser múltiplos diretos de 10, com a única exceção do último termo, ditando um comportamento cíclico invariável na redução digital.
            """)
            
        with st.expander("2.4 O Último Teorema de Fermat e Simulação de Curva", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            O Último Teorema de Fermat constitui o encerramento ideal para o estudo de estruturas aritméticas, pois ilustra como pequenas alterações numa expressão matemática podem fazer com que um padrão de infinitas soluções desapareça por completo. No caso do expoente $n=2$, a equação transforma-se na clássica expressão do Teorema de Pitágoras: $a^2+b^2=c^2$. Desde a Antiguidade que se sabe que esta estrutura admite uma infinidade de soluções inteiras e positivas, conhecidas como triplas pitagóricas. O exemplo mais famoso é a tripla 3-4-5, onde $3^2+4^2=9+16=25=5^2$.
            
            Contudo, no século XVII, Pierre de Fermat introduziu uma rutura neste cenário de continuidade. Fermat afirmou na margem do seu livro que a equação geral $a^n+b^n=c^n$ não admite qualquer tipo de solução inteira não trivial sempre que o expoente $n$ for um número estritamente maior do que 2 ($n>2$). Como faleceu sem deixar registo da prova, o enigma resistiu por mais de três séculos e meio. A prova universal e definitiva só foi alcançada em 1994 por Andrew Wiles, utilizando conceitos contemporâneos sofisticados como curvas elípticas. O contraste drástico mostra como pequenas variações numa expressão algébrica alteram radicalmente o comportamento aritmético subjacente.
            """)
            
            st.markdown("#### 📈 Manipulador Geométrico Interativo da Curva de Fermat")
            n_slider = st.slider("Altere o valor do expoente (n) para testar a deformação e colapso das soluções geométricas de Fermat:", 2.0, 15.0, 2.0, step=0.5)
            
            x = np.linspace(0, 5, 200)
            fig, ax = plt.subplots(figsize=(5, 4))
            with np.errstate(invalid='ignore'):
                y = (5**n_slider - x**n_slider)**(1/n_slider)
            
            ax.plot(x, y, label=f"n = {n_slider}", color="#4f46e5", linewidth=3)
            if n_slider == 2.0:
                ax.plot(3, 4, 'go', markersize=10, label="Solução Inteira (3,4)")
            ax.set_xlim(0, 5.2)
            ax.set_ylim(0, 5.2)
            ax.set_xlabel("Eixo a")
            ax.set_ylabel("Eixo b")
            ax.set_title(r"Deformação da Curva $a^n + b^n = 5^n$")
            ax.grid(True, linestyle=":", alpha=0.5)
            ax.legend()
            st.pyplot(fig)

    with tab2:
        st.subheader("✍️ Questionário de Avaliação Geral — Módulo 2")
        score2 = 0
        q2_1 = st.radio("1. Qual a expressão utilizada para calcular o n-ésimo número triangular (soma de 1 até n)?",
                        [r"T_n = n(n+1)/2", r"T_n = 2^n - 1", r"T_n = n^2 + n + 41"])
        q2_2 = st.radio("2. Qual a relação matemática que define se um número é perfeito usando a função da soma total de todos os divisores?",
                        [r"\sigma(n) = n", r"\sigma(n) = 2n", r"\sigma(n) = n - 1"])
        q2_3 = st.radio("3. Qual o expoente máximo estável que admite infinitas soluções inteiras positivas na equação de Fermat antes do colapso das soluções?",
                        ["n = 1", "n = 2", "n = 3", "Não existem limites"])
        
        if q2_1 == r"T_n = n(n+1)/2": score2 += 3.33
        if q2_2 == r"\sigma(n) = 2n": score2 += 3.33
        if q2_3 == "n = 2": score2 += 3.34
        
        if st.button("Submeter Respostas do Módulo 2"):
            st.metric("Pontuação Obtida:", f"{round(score2, 1)}/10")

# ==============================================================================
# 🟢 MÓDULO 3: LOGICA DO NUMBER MATCH
# ==============================================================================
elif page == "🟢 Módulo 3: A Lógica por Trás do Number Match":
    st.title("🟢 Módulo 3: A Lógica Matemática por Trás do Jogo Number Match")
    
    tab1, tab2 = st.tabs(["🎮 Modelação de Sistemas & Simulador", "✍️ Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("3.1 Introdução e Formalização Proposicional do Sistema", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            O *Number Match* é um jogo de lógica e aritmética popular em plataformas digitais. Apesar de aparentar baixa complexidade, o jogo pode ser analisado de forma rigorosa através de conceitos fundamentais da matemática discreta. As decisões do jogador dependem simultaneamente de condições lógicas e de propriedades aritméticas elementares, como igualdade, soma e paridade, que influenciam diretamente a evolução do jogo (Rosen, 2012).
            
            A formalização das condições de jogada pode ser feita recorrendo à lógica proposicional, permitindo descrever de forma precisa quando uma jogada é válida. Uma jogada válida ocorre quando dois números $a$ e $b$ satisfazem simultaneamente uma condição numérica e uma condição estrutural de acessibilidade. A condição numérica é satisfeita quando se verifica pelo menos uma das seguintes situações:
            1. $a = b$ (os dois números são iguais).
            2. $a + b = 10$ (relação aritmética complementar).
            
            Deste modo, a proposição composta 'Jogada Válida ($a, b$)' pode ser formalizada logicamente da seguinte forma:
            """)
            st.latex(r"\text{Jogada Válida}(a, b) \leftrightarrow (a = b \lor a + b = 10) \land \text{Conectados}(a, b)")
            st.markdown("""
            Esta expressão representa uma fórmula booleana composta, na qual as condições aritméticas e estruturais são combinadas através dos conectivos lógicos usuais. Assim, uma jogada é válida apenas quando simultaneamente se verifica uma relação lógica entre os valores dos números e uma relação estrutural no tabuleiro.
            """)
            
            st.markdown("#### 🕹️ Simulador de Validação Lógica do Tabuleiro")
            col1, col2, col3 = st.columns(3)
            with col1: val_a = st.number_input("Introduza o valor do número A:", 1, 9, 3)
            with col2: val_b = st.number_input("Introduza o valor do número B:", 1, 9, 7)
            with col3: conectado = st.checkbox("Os números estão conectados no tabuleiro?", value=True)
            
            # Execução real da lógica booleana do relatório
            check_numerico = (val_a == val_b) or (val_a + val_b == 10)
            check_valido = check_numerico and conectado
            
            if check_valido:
                st.success(f"🟩 JOGADA VÁLIDA! A proposição assume valor lógico VERDADEIRO. O par ({val_a},{val_b}) pode ser eliminado.")
            else:
                st.error("🟥 JOGADA INVÁLIDA! O sistema booleano retornou FALSO. Verifique as regras de adjacência ou valores.")
                
        with st.expander("3.2 Modelação em Teoria de Grafos e Estratégia Combinatória", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            A representação matemática do jogo através da teoria de grafos permite compreender de forma mais profunda as propriedades estruturais do tabuleiro e a evolução do jogo ao longo do tempo (West, 2001). Nesta perspetiva, o tabuleiro pode ser modelado como um grafo não dirigido, no qual cada número ativo do tabuleiro corresponde a um **vértice**, e cada par eliminável válido corresponde a uma **aresta** que liga dois vértices.
            
            À medida que o jogador elimina pares, o grafo sofre transformações sucessivas: os vértices associados aos números eliminados são removidos, bem como todas as arestas incidentes nesses vértices. Neste contexto, o grau de um vértice (o número de arestas incidentes) assume um papel importante. Vértices de grau elevado correspondem a números com várias jogadas possíveis, enquanto vértices de grau zero representam números isolados que não podem ser eliminados, contribuindo diretamente para estados de bloqueio do tabuleiro.
            
            **A Combinatória e a Paridade do Número 5:**
            A combinatória desempenha um papel central na análise do tabuleiro para prever bloqueios (Grimaldi, 2004). Considere-se as jogadas por igualdade e soma: cada número entre 1 e 9 possui exatamente um parceiro distinto que permite obter a soma 10 ($1 \\leftrightarrow 9$, $2 \\leftrightarrow 8$). No entanto, o número 5 constitui um caso particular, pois **apenas pode formar par consigo mesmo**. Isto implica que a sua frequência total no tabuleiro deve ser estritamente **par** para permitir a eliminação completa. Se aparecer um número ímpar de vezes, pelo menos um 5 ficará inevitavelmente isolado com grau zero, impossibilitando a vitória por um argumento direto de paridade (Stanley, 2011).
            """)

    with tab2:
        st.subheader("✍️ Questionário de Avaliação Geral — Módulo 3")
        score3 = 0
        q3_1 = st.radio("1. Qual o conectivo lógico principal que une a condição numérica e a estrutural para validar uma jogada?",
                        ["Disjunção (OU / \lor)", "Conjunção (E / \land)", "Condicional (Se... então)"])
        q3_2 = st.radio("2. No modelo de grafos do jogo, o que representa um número isolado que não pode ser eliminado?",
                        ["Um vértice de grau zero", "Uma aresta conexa", "Um subgrafo regular"])
        q3_3 = st.radio("3. Por que motivo o aparecimento de uma quantidade ímpar de números 5 bloqueia o jogo?",
                        ["Porque o 5 é um número primo.", "Porque o 5 apenas faz par de soma 10 consigo próprio, quebrando a paridade de emparelhamento.", "Porque diminui o grau de todos os outros vértices."])
        
        if q3_1 == "Conjunção (E / \land)": score3 += 3.33
        if q3_2 == "Um vértice de grau zero": score3 += 3.33
        if q3_3 == "Porque o 5 apenas faz par de soma 10 consigo próprio, quebrando a paridade de emparelhamento.": score3 += 3.34
        
        if st.button("Submeter Respostas do Módulo 3"):
            st.metric("Pontuação Obtida:", f"{round(score3, 1)}/10")

# ==============================================================================
# MÓDULO 4: GRUPOS DE SIMETRIA
# ==============================================================================
elif page == "🔵 Módulo 4: Introdução aos Grupos de Simetria":
    st.title("🔵 Módulo 4: Introdução aos Grupos de Simetria: Perspetiva Matemática")
    st.caption("Baseado em: *FM_1ºprojeto .pdf* | Temas: Isometrias, Teoria de Grupos e Estruturas Icosaédricas Virais")
    
    tab1, tab2 = st.tabs(["📖 Conteúdo Científico", "✍️ Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("4.1 Geometria das Isometrias Fundamentais do Plano", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            A simetria é um conceito central em múltiplas áreas da Matemática, desde a Geometria à Álgebra e até à Física. De forma intuitiva, dizemos que um objeto apresenta simetria quando permanece inalterado após uma transformação como uma rotação, reflexão ou translação. Estas transformações, designadas no seu conjunto por **isometrias**, caracterizam-se por preservar integralmente as distâncias e os ângulos das figuras.
            
            As quatro isometrias fundamentais do plano incluem:
            * **Translações:** Deslocamento linear da figura numa direção e magnitude constantes.
            * **Rotações:** Giro da figura em torno de um ponto fixo por um determinado ângulo.
            * **Reflexões:** Espelhamento axial da figura em relação a uma reta diretriz.
            * **Reflexões Deslizantes (*Glide Reflections*):** Composição de uma reflexão com uma translação paralela ao próprio eixo de reflexão.
            
            Estas transformações podem combinar-se entre si e continuam a ser isometrias (Durbin, *Modern Algebra*). Por exemplo, a composição de duas reflexões em retas que se cruzam gera invariavelmente uma rotação em torno do ponto de interseção.
            """)
            
        with st.expander("4.2 Teoria de Grupos e Estrutura Abstrata", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            A Teoria de Grupos surge quando deixamos de estudar a figura geométrica isolada e passamos a focar o estudo no **conjunto de todas as simetrias** associadas a essa figura. Formalmente, um conjunto $G$ munido de uma operação binária $*$ satisfaz a definição de grupo se cumprir quatro propriedades essenciais:
            1. **Fecho:** Para quaisquer $a, b \\in G$, o elemento resultante $a * b$ pertence também a $G$.
            2. **Associatividade:** Para quaisquer $a, b, c \\in G$, vale a identidade $(a * b) * c = a * (b * c)$.
            3. **Elemento Neutro:** Existe um elemento $e \\in G$ tal que $e * a = a * e = a$ para todo o elemento $a \\in G$.
            4. **Elemento Inverso:** Para cada elemento $a \\in G$, existe um correspondente $a^{-1} \\in G$ tal que $a * a^{-1} = a^{-1} * a = e$.
            
            Um exemplo clássico e fundamental discutido no projeto é o grupo das rotações do triângulo equilátero, que forma o grupo cíclico $C_3$. Esta linguagem unifica análises em ramos tão distintos como tesselações artísticas de M. C. Escher, padrões cristalinos e interações moleculares.
            """)
            
        with st.expander("4.3 Estruturas Virais Icosaédricas e Eficiência Genética", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            A simetria desempenha um papel crítico na Biologia Molecular e na Virologia. Muitos vírus ditos 'esféricos' (como o Adenovírus, Poliovírus ou o vírus Zika) apresentam, na verdade, uma estrutura baseada na geometria de um **icosaedro regular**, um dos cinco sólidos platónicos.
            
            A geometria icosaédrica oferece vantagens evolutivas gigantescas:
            * **Simetria Rotacional de Eixos:** Estas estruturas apresentam múltiplos eixos de simetria rotacional de ordens 2, 3 e 5. Isto permite que subunidades proteicas rigorosamente idênticas (capsómeros) se encaixem perfeitamente para formar uma cápsula fechada estável.
            * **Eficiência Genética:** Conforme detalhado no estudo das proteínas virais, esta organização repetitiva permite que o vírus utilize um único gene para codificar uma pequena proteína que se organiza através de rotações espaciais para formar uma cápsula grande (capsídeo). O vírus economiza espaço de armazenamento genético gerando volume estável por replicação geométrica (Modelo de Caspar-Klug).
            """)

    with tab2:
        st.subheader("✍️ Questionário de Avaliação Geral — Módulo 4")
        score4 = 0
        q4_1 = st.radio("1. Qual o nome da isometria plana que combina uma operação de espelhamento com uma translação paralela?",
                        ["Reflexão deslizante", "Translação oblíqua", "Rotação síncrona"])
        q4_2 = st.radio("2. Quantas propriedades/axiomas definem formalmente um Grupo (G, *) na álgebra abstrata?",
                        ["3 propriedades", "4 propriedades", "5 propriedades"])
        q4_3 = st.radio("3. Quais as ordens de simetria rotacional exibidas pelos vírus de estrutura baseada no icosaedro?",
                        ["Ordens 2, 4 e 6", "Ordens 2, 3 e 5", "Ordens 3, 6 e 9"])
        
        if q4_1 == "Reflexão deslizante": score4 += 3.33
        if q4_2 == "4 properties": score4 += 3.33
        if q4_3 == "Ordens 2, 3 e 5": score4 += 3.34
        
        if st.button("Submeter Respostas do Módulo 4"):
            st.metric("Pontuação Obtida:", f"{round(score4, 1)}/10")

# ==============================================================================
# MÓDULO 5: 17 GRUPOS CRISTALOGRÁFICOS
# ==============================================================================
elif page == "🟤 Módulo 5: 17 Grupos Cristalográficos do Plano":
    st.title("🟤 Módulo 5: Os 17 Grupos Cristalográficos do Plano (Wallpaper Groups)")
    st.caption("Baseado em: *FM_2ºProjeto.pdf* | Temas: Tesselações Periódicas, Restrições e Inspeção de Subgrupos p4, p6 e pm")
    
    tab1, tab2 = st.tabs(["📖 Classificação Completa", "✍️ Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("5.1 Grupos de Simetria e Mosaicos Periódicos", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva:**
            As tesselações periódicas são padrões que cobrem o plano de forma contínua, repetindo-se indefinidamente através de translações. A definição formal e a análise estrutural destas tesselações (Grünbaum e Shephard, 1987) demonstram como as isometrias do plano determinam a organização dos padrões. Cada tesselação possui um grupo de simetria, isto é, o conjunto de todas as isometrias que deixam o padrão inalterado. 
            
            A existência de eixos de reflexão, centros de rotação de diferentes ordens ou reflexões deslizantes permite distinguir padrões que, visualmente, podem parecer semelhantes. Um dos resultados mais importantes deste estudo é a restrição cristalográfica: **existem exatamente e apenas 17 grupos cristalográficos do plano**, resultado que limita a diversidade estrutural de qualquer parede ou malha periódica bidimensional (Conway, 2008).
            """)
            
            # Tabela Completa dos 17 Grupos extraída diretamente do Projeto 2!
            st.markdown("#### 📋 Classificação Oficial dos 17 Grupos Cristalográficos do Plano")
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
            
        with st.expander("5.2 Análise Detalhada dos Subgrupos de Referência: p4, p6 e pm", expanded=True):
            st.markdown("""
            **Explicação Teórica Exaustiva dos Subgrupos:**
            * **Grupo p4:** Caracteriza-se pela presença de rotações de ordem 4, isto é, simetrias rotacionais de 90°, 180° e 270°, mas **não possui quaisquer eixos de reflexão ou reflexões deslizantes**. As suas translações ocorrem em duas direções perpendiculares, formando uma rede quadrada. A ausência de eixos de espelhamento distingue-o dos grupos homólogos *p4m* e *p4g*.
            * **Grupo p6:** Representa a simetria hexagonal pura. É um dos mais simétricos e apresenta rotações de ordem 6 (ângulos de 60°), ordem 3 e ordem 2. As suas translações organizam-se numa rede hexagonal regular altamente eficiente (como os favos de mel estruturais). Crucialmente, **não possui reflexões**, o que o distingue estruturalmente do grupo *p6m*.
            * **Grupo pm:** É um dos exemplos mais simples entre os grupos com simetria axial. Caracteriza-se estritamente pela presença de **eixos de reflexão paralelos**, combinados com translações perpendiculares a esses eixos em malha retangular, gerando bandas simétricas lineares especulares. Não contém rotações.
            """)
            
            st.markdown("#### 🔍 Inspetor Geométrico de Subgrupos")
            grupo_sel = st.selectbox("Selecione um subgrupo para inspecionar as propriedades mecânicas de translação:", ["p4 (Rede Quadrada)", "p6 (Rede Hexagonal)", "pm (Rede Retangular)"])
            if "p4" in grupo_sel:
                st.info("🔄 **Foco Rotacional:** Rotações de 90° e 180°. Zero Reflexões. Padrões comuns em mosaicos rotativos decorativos.")
            elif "p6" in grupo_sel:
                st.success("🐝 **Máxima Eficiência Natural:** Rotações de 60°, 120°, 180°, 240° e 300°. Estrutura geométrica idêntica à dos cristais hexagonais e favos.")
            elif "pm" in grupo_sel:
                st.warning("🪞 **Simetria Especular:** Repetição linear e simetria estritamente axial em faixas. Comum em motivos arquitetónicos repetidos.")

    with tab2:
        st.subheader("✍️ Questionário de Avaliação Geral — Módulo 5")
        score5 = 0
        q5_1 = st.radio("1. O que distingue fundamentalmente o grupo cristalográfico puro 'p4' do grupo 'p4m'?",
                        ["O grupo p4 não possui rotações.", "O grupo p4 carece inteiramente de eixos de reflexão.", "A rede do p4 é hexagonal."])
        q5_2 = st.radio("2. Qual destes grupos está associado à eficiência geométrica dos favos de mel e não possui reflexões?",
                        ["Grupo pm", "Grupo p6", "Grupo p2"])
        q5_3 = st.radio("3. Qual a característica geométrica dominante das figuras que pertencem ao grupo 'pm'?",
                        ["Simetria rotacional forte", "Repetição linear e simetria especular por reflexões paralelas", "Reflexões deslizantes cruzadas"])
        
        if q5_1 == "O grupo p4 carece inteiramente de eixos de reflexão.": score5 += 3.33
        if q5_2 == "Grupo p6": score5 += 3.33
        if q5_3 == "Repetição linear e simetria especular por reflexões paralelas": score5 += 3.34
        
        if st.button("Submeter Respostas do Módulo 5"):
            st.metric("Pontuação Obtida:", f"{round(score5, 1)}/10")