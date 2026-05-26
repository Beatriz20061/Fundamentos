import streamlit as st
import math

# Tentar importar módulos gráficos com proteção para falhas de cloud
try:
    import numpy as np
    import matplotlib.pyplot as plt
    GRAFICOS_ATIVOS = True
except ImportError:
    GRAFICOS_ATIVOS = False

# Configuração da plataforma web para alto impacto visual e responsividade
st.set_page_config(page_title="MathXplore - ISCTE Sintra", layout="wide", page_icon="🔢")

# ============================================================================
# CSS AVANÇADO - DESIGN SYSTEM NEXT-LEVEL
# ============================================================================
st.markdown("""
<style>
/* ===== IMPORTS E VARIÁVEIS ===== */
@import url('[fonts.googleapis.com](https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap)');

:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    --dark-gradient: linear-gradient(135deg, #0c0c1e 0%, #1a1a3e 100%);
    --glass-bg: rgba(255, 255, 255, 0.08);
    --glass-border: rgba(255, 255, 255, 0.18);
    --shadow-color: rgba(102, 126, 234, 0.25);
    --text-primary: #ffffff;
    --text-secondary: rgba(255, 255, 255, 0.7);
    --card-bg: rgba(255, 255, 255, 0.05);
}

/* ===== RESET E BASE ===== */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

/* ===== FUNDO ANIMADO COM GRADIENTE ===== */
.stApp {
    background: linear-gradient(-45deg, #0f0f23, #1a1a3e, #2d1b4e, #1e3a5f, #0f2027);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    min-height: 100vh;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ===== PARTÍCULAS FLUTUANTES (PSEUDO-ELEMENTOS) ===== */
.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        radial-gradient(2px 2px at 20px 30px, rgba(255,255,255,0.3), transparent),
        radial-gradient(2px 2px at 40px 70px, rgba(255,255,255,0.2), transparent),
        radial-gradient(3px 3px at 50px 160px, rgba(255,255,255,0.3), transparent),
        radial-gradient(2px 2px at 90px 40px, rgba(255,255,255,0.2), transparent),
        radial-gradient(3px 3px at 130px 80px, rgba(255,255,255,0.25), transparent),
        radial-gradient(2px 2px at 160px 120px, rgba(255,255,255,0.15), transparent);
    background-repeat: repeat;
    background-size: 200px 200px;
    animation: floatParticles 20s linear infinite;
    pointer-events: none;
    z-index: 0;
}

@keyframes floatParticles {
    0% { transform: translateY(0) translateX(0); }
    100% { transform: translateY(-200px) translateX(50px); }
}

/* ===== ANIMAÇÕES DE ENTRADA ===== */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-50px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes scaleIn {
    from {
        opacity: 0;
        transform: scale(0.9);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

@keyframes glowPulse {
    0%, 100% { box-shadow: 0 0 20px rgba(102, 126, 234, 0.3); }
    50% { box-shadow: 0 0 40px rgba(102, 126, 234, 0.6), 0 0 60px rgba(118, 75, 162, 0.3); }
}

@keyframes shimmer {
    0% { background-position: -200% center; }
    100% { background-position: 200% center; }
}

@keyframes borderGlow {
    0%, 100% { border-color: rgba(102, 126, 234, 0.5); }
    50% { border-color: rgba(240, 147, 251, 0.8); }
}

/* ===== BLOCO PRINCIPAL ===== */
.block-container {
    animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    padding-top: 2rem !important;
    position: relative;
    z-index: 1;
}

/* ===== SIDEBAR PREMIUM ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(15, 15, 35, 0.95) 0%, rgba(30, 30, 60, 0.95) 100%) !important;
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

section[data-testid="stSidebar"] .stMarkdown {
    color: var(--text-primary) !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* ===== RADIO BUTTONS ESTILIZADOS ===== */
section[data-testid="stSidebar"] .stRadio > div {
    gap: 8px !important;
}

section[data-testid="stSidebar"] .stRadio > div > label {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    margin: 4px 0 !important;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    cursor: pointer !important;
}

section[data-testid="stSidebar"] .stRadio > div > label:hover {
    background: rgba(102, 126, 234, 0.2) !important;
    border-color: rgba(102, 126, 234, 0.5) !important;
    transform: translateX(5px) !important;
}

section[data-testid="stSidebar"] .stRadio > div > label[data-checked="true"] {
    background: var(--primary-gradient) !important;
    border-color: transparent !important;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
}

/* ===== TÍTULOS COM GRADIENTE ===== */
h1, h2, h3 {
    background: linear-gradient(135deg, #667eea 0%, #f093fb 50%, #4facfe 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 700 !important;
    letter-spacing: -0.02em;
}

h1 {
    font-size: 3rem !important;
    animation: fadeInUp 0.6s ease-out;
}

/* ===== TEXTO GERAL ===== */
p, span, li, .stMarkdown {
    color: var(--text-secondary) !important;
}

strong, b {
    color: var(--text-primary) !important;
    font-weight: 600 !important;
}

/* ===== CARDS GLASSMORPHISM ===== */
.glass-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 24px;
    padding: 2rem;
    margin: 1.5rem 0;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    overflow: hidden;
}

.glass-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    transition: left 0.5s ease;
}

.glass-card:hover::before {
    left: 100%;
}

.glass-card:hover {
    transform: translateY(-5px);
    border-color: rgba(102, 126, 234, 0.5);
    box-shadow: 
        0 20px 40px rgba(0, 0, 0, 0.3),
        0 0 30px rgba(102, 126, 234, 0.2);
}

/* ===== MÓDULO HEADER PREMIUM ===== */
.modulo-header {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 20px;
    padding: 1.5rem 2rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    animation: scaleIn 0.5s ease-out;
}

.modulo-header::after {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 150px;
    height: 150px;
    background: radial-gradient(circle, rgba(102, 126, 234, 0.3) 0%, transparent 70%);
    transform: translate(30%, -30%);
}

.modulo-header h2 {
    margin: 0 !important;
    font-size: 1.8rem !important;
    position: relative;
    z-index: 1;
}

/* ===== BOTÕES ULTRA-MODERNOS ===== */
.stButton > button {
    background: var(--primary-gradient) !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 14px 32px !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    letter-spacing: 0.5px !important;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
    position: relative !important;
    overflow: hidden !important;
}

.stButton > button::before {
    content: '' !important;
    position: absolute !important;
    top: 0 !important;
    left: -100% !important;
    width: 100% !important;
    height: 100% !important;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent) !important;
    transition: left 0.5s ease !important;
}

.stButton > button:hover::before {
    left: 100% !important;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 
        0 8px 25px rgba(102, 126, 234, 0.5),
        0 0 40px rgba(102, 126, 234, 0.3) !important;
}

.stButton > button:active {
    transform: translateY(-1px) scale(0.98) !important;
}

/* ===== EXPANDERS PREMIUM ===== */
div[data-testid="stExpander"] {
    background: rgba(255, 255, 255, 0.03) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 16px !important;
    margin-bottom: 12px !important;
    overflow: hidden !important;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

div[data-testid="stExpander"]:hover {
    border-color: rgba(102, 126, 234, 0.4) !important;
    background: rgba(102, 126, 234, 0.08) !important;
    box-shadow: 0 8px 30px rgba(102, 126, 234, 0.15) !important;
    transform: translateX(5px) !important;
}

div[data-testid="stExpander"] summary {
    color: var(--text-primary) !important;
    font-weight: 500 !important;
    padding: 1rem 1.25rem !important;
}

/* ===== TABS ESTILIZADAS ===== */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255, 255, 255, 0.05) !important;
    border-radius: 16px !important;
    padding: 8px !important;
    gap: 8px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
}

.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: var(--text-secondary) !important;
    border-radius: 12px !important;
    padding: 12px 24px !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
}

.stTabs [data-baseweb="tab"]:hover {
    background: rgba(102, 126, 234, 0.2) !important;
    color: var(--text-primary) !important;
}

.stTabs [aria-selected="true"] {
    background: var(--primary-gradient) !important;
    color: white !important;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
}

.stTabs [data-baseweb="tab-highlight"] {
    display: none !important;
}

.stTabs [data-baseweb="tab-border"] {
    display: none !important;
}

/* ===== INPUTS MODERNOS ===== */
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stSelectbox > div > div > div {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
    padding: 12px 16px !important;
    transition: all 0.3s ease !important;
}

.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {
    border-color: rgba(102, 126, 234, 0.6) !important;
    box-shadow: 0 0 20px rgba(102, 126, 234, 0.2) !important;
    background: rgba(102, 126, 234, 0.1) !important;
}

/* ===== SLIDER MODERNO ===== */
.stSlider > div > div > div > div {
    background: var(--primary-gradient) !important;
}

.stSlider > div > div > div > div > div {
    background: white !important;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3) !important;
}

/* ===== MÉTRICAS COM GLOW ===== */
div[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.05) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 16px !important;
    padding: 1.5rem !important;
    animation: glowPulse 3s ease-in-out infinite !important;
}

div[data-testid="stMetric"] label {
    color: var(--text-secondary) !important;
}

div[data-testid="stMetric"] > div {
    color: var(--text-primary) !important;
    font-weight: 700 !important;
}

/* ===== ALERTS ESTILIZADOS ===== */
.stAlert {
    border-radius: 16px !important;
    border: none !important;
    backdrop-filter: blur(10px) !important;
}

div[data-testid="stAlert"][data-baseweb="notification"][kind="info"] {
    background: rgba(79, 172, 254, 0.15) !important;
    border-left: 4px solid #4facfe !important;
}

div[data-testid="stAlert"][data-baseweb="notification"][kind="success"] {
    background: rgba(0, 242, 254, 0.15) !important;
    border-left: 4px solid #00f2fe !important;
}

div[data-testid="stAlert"][data-baseweb="notification"][kind="warning"] {
    background: rgba(240, 147, 251, 0.15) !important;
    border-left: 4px solid #f093fb !important;
}

div[data-testid="stAlert"][data-baseweb="notification"][kind="error"] {
    background: rgba(245, 87, 108, 0.15) !important;
    border-left: 4px solid #f5576c !important;
}

/* ===== DATAFRAMES ===== */
.stDataFrame {
    border-radius: 16px !important;
    overflow: hidden !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
}

.stDataFrame > div {
    background: rgba(255, 255, 255, 0.03) !important;
}

/* ===== CHECKBOXES E RADIOS ===== */
.stCheckbox > label,
.stRadio > div > label {
    color: var(--text-secondary) !important;
    transition: color 0.3s ease !important;
}

.stCheckbox > label:hover,
.stRadio > div > label:hover {
    color: var(--text-primary) !important;
}

/* ===== FEATURE CARDS ===== */
.feature-card {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    overflow: hidden;
}

.feature-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: rgba(102, 126, 234, 0.5);
    box-shadow: 
        0 25px 50px rgba(0, 0, 0, 0.3),
        0 0 40px rgba(102, 126, 234, 0.2);
}

.feature-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    display: block;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

.feature-title {
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.feature-desc {
    color: var(--text-secondary);
    font-size: 0.95rem;
    line-height: 1.6;
}

/* ===== HERO SECTION ===== */
.hero-section {
    text-align: center;
    padding: 3rem 0;
    position: relative;
}

.hero-title {
    font-size: 4rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #667eea 0%, #f093fb 30%, #4facfe 60%, #00f2fe 100%);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 3s linear infinite;
    margin-bottom: 1rem;
}

.hero-subtitle {
    font-size: 1.4rem;
    color: var(--text-secondary);
    max-width: 700px;
    margin: 0 auto;
    line-height: 1.7;
}

/* ===== STAT BOXES ===== */
.stat-box {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    transition: all 0.3s ease;
}

.stat-box:hover {
    transform: scale(1.05);
    border-color: rgba(102, 126, 234, 0.5);
}

.stat-number {
    font-size: 2.5rem;
    font-weight: 800;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.stat-label {
    color: var(--text-secondary);
    font-size: 0.9rem;
    margin-top: 0.5rem;
}

/* ===== QUIZ OPTION CARDS ===== */
.quiz-option {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 1rem 1.5rem;
    margin: 0.5rem 0;
    transition: all 0.3s ease;
    cursor: pointer;
}

.quiz-option:hover {
    background: rgba(102, 126, 234, 0.15);
    border-color: rgba(102, 126, 234, 0.5);
    transform: translateX(10px);
}

/* ===== SCROLLBAR CUSTOM ===== */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: var(--primary-gradient);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
}

/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
    .hero-title {
        font-size: 2.5rem !important;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
    }
    
    .feature-card {
        padding: 1.5rem;
    }
}

/* ===== ANIMAÇÃO DE NÚMERO ===== */
.number-animate {
    display: inline-block;
    animation: countUp 1s ease-out forwards;
}

@keyframes countUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ===== BADGE PREMIUM ===== */
.badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.badge-primary {
    background: var(--primary-gradient);
    color: white;
}

.badge-secondary {
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-secondary);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

/* ===== DIVIDER CUSTOM ===== */
.custom-divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.5), transparent);
    margin: 2rem 0;
    border: none;
}

/* ===== CÓDIGO EM LATEX ===== */
.katex {
    color: var(--text-primary) !important;
}
</style>
""", unsafe_allow_html=True)

# ============================================================================
# COMPONENTES CUSTOMIZADOS
# ============================================================================

def render_module_header(icon, title, color_class="primary"):
    """Renderiza um header de módulo premium"""
    st.markdown(f"""
    <div class="modulo-header">
        <h2>{icon} {title}</h2>
    </div>
    """, unsafe_allow_html=True)

def render_feature_card(icon, title, description):
    """Renderiza um card de feature"""
    return f"""
    <div class="feature-card">
        <span class="feature-icon">{icon}</span>
        <div class="feature-title">{title}</div>
        <div class="feature-desc">{description}</div>
    </div>
    """

def render_stat_box(number, label):
    """Renderiza uma caixa de estatística"""
    return f"""
    <div class="stat-box">
        <div class="stat-number">{number}</div>
        <div class="stat-label">{label}</div>
    </div>
    """

def render_glass_card(content):
    """Renderiza um card com efeito glass"""
    st.markdown(f"""
    <div class="glass-card">
        {content}
    </div>
    """, unsafe_allow_html=True)

def render_divider():
    """Renderiza um divisor customizado"""
    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# ============================================================================
# SIDEBAR PREMIUM
# ============================================================================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">🔢</div>
        <h1 style="font-size: 1.8rem; margin: 0;">MathXplore</h1>
        <p style="font-size: 0.9rem; opacity: 0.7; margin-top: 0.5rem;">Fundamentos de Matemática</p>
        <p style="font-size: 0.8rem; opacity: 0.5;">Licenciatura em MATD</p>
    </div>
    """, unsafe_allow_html=True)
    
    render_divider()
    
    page = st.radio(
        "📍 Navegação",
        [
            "🏠 Página Inicial",
            "🔵 Grupos de Simetria",
            "🟤 17 Grupos Cristalográficos",
            "🟢 Lógica do Number Match",
            "🟣 Padrões dos Primos",
            "🟡 Padrões Numéricos"
        ],
        label_visibility="collapsed"
    )
    
    render_divider()
    
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0; opacity: 0.7;">
        <p style="font-size: 0.85rem; margin-bottom: 0.5rem;">👩‍🎓 Desenvolvido por</p>
        <p style="font-size: 0.9rem; font-weight: 600;">Catarina Pereira</p>
        <p style="font-size: 0.9rem; font-weight: 600;">Beatriz Correia</p>
        <br>
        <p style="font-size: 0.8rem;">👨‍🏫 Prof. Rosário Laureano</p>
        <p style="font-size: 0.8rem;">🏫 ISCTE Sintra</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🏠 PÁGINA INICIAL
# ==============================================================================
if page == "🏠 Página Inicial":
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">🚀 MathXplore</h1>
        <p class="hero-subtitle">
            Plataforma interativa com conhecimentos nas mais vastas areas da matemática.
            Explore conceitos através de visualizações dinâmicas, simuladores e quizzes.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    render_divider()
    
    # Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(render_stat_box("5", "Módulos"), unsafe_allow_html=True)
    with col2:
        st.markdown(render_stat_box("15+", "Simuladores"), unsafe_allow_html=True)
    with col3:
        st.markdown(render_stat_box("∞", "Possibilidades"), unsafe_allow_html=True)
    with col4:
        st.markdown(render_stat_box("100%", "Interativo"), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(render_feature_card(
            "📐",
            "Teoria",
            "Conteúdos teóricos completos baseados nos relatórios académicos originais."
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown(render_feature_card(
            "🎮",
            "Simuladores Dinâmicos",
            "Laboratórios interativos para experimentar conceitos matemáticos em tempo real."
        ), unsafe_allow_html=True)
    
    with col3:
        st.markdown(render_feature_card(
            "🧠",
            "Quizzes Avaliativos",
            "Questionários com pontuação automática para testar os conhecimentos."
        ), unsafe_allow_html=True)
    
    render_divider()
    
    # About Section
    render_glass_card("""
        <h3 style="margin-top: 0;">💡 Sobre a Plataforma</h3>
        <p>Esta plataforma digital foi desenvolvida para integrar a totalidade dos conteúdos teóricos
        presentes nos cinco projetos académicos desenvolvidos nos relatórios originais.</p>
        <p>A nossa abordagem converte a teoria exaustiva dos relatórios em componentes de aprendizagem dinâmicos, 
        estruturados rigorosamente sob a metodologia de <strong>Explicação Teórica</strong>, 
        <strong>Aplicação Prática</strong> e <strong>Questionários Gerais com Pontuação</strong> automática.</p>
    """)
    
    # Quick Access
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🎯 Acesso Rápido aos Módulos")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="glass-card" style="padding: 1.5rem;">
            <p><strong>🔵 Módulo 1:</strong> Grupos de Simetria</p>
            <p><strong>🟤 Módulo 2:</strong> 17 Grupos Cristalográficos</p>
            <p><strong>🟢 Módulo 3:</strong> Lógica do Number Match</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="glass-card" style="padding: 1.5rem;">
            <p><strong>🟣 Módulo 4:</strong> Padrões dos Primos</p>
            <p><strong>🟡 Módulo 5:</strong> Padrões Numéricos</p>
            <p style="opacity: 0.5;">Seleciona um módulo no menu lateral →</p>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# MÓDULO 1: GRUPOS DE SIMETRIA
# ==============================================================================
elif page == "🔵 Grupos de Simetria":
    render_module_header("🔵", "MÓDULO 1: GRUPOS DE SIMETRIA")
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("📘 1. Introdução à Simetria e Teoria de Grupos", expanded=True):
            st.markdown("""

    A **simetria** é um conceito central em múltiplas áreas da Matemática, desde a Geometria à Álgebra e até à Física. 

    De forma intuitiva, dizemos que um objeto apresenta simetria quando permanece **inalterado** após uma transformação — como uma rotação, reflexão ou translação. 

    Estas transformações, designadas no seu conjunto por **isometrias**, podem ser estudadas de forma estruturada através da **Teoria de Grupos**, uma área formalizada no século XIX e hoje amplamente utilizada para descrever padrões geométricos, 
    moléculas, cristais e estruturas biológicas (Durbin, *Modern Algebra*).

    ---

    O estudo das simetrias permite **unificar fenómenos naturais e construções humanas**: desde os padrões em azulejos portugueses, aos capsídeos virais, passando pelas fascinantes tesselações artísticas. 

    Neste trabalho, exploramos as simetrias presentes em:
    - Polígonos regulares
    - Sólidos platónicos  
    - Estruturas virais
    - Obras de arte, com especial destaque para o génio **M. C. Escher**
    """)
        with st.expander("📐 2. Geometria dos Polígonos e Sólidos Platónicos", expanded=False):
            st.markdown("""
    ### Geometria dos Polígonos e Sólidos Platónicos

    O estudo das simetrias inicia-se pelas **isometrias** — transformações que preservam distâncias e ângulos.

    #### Polígonos Regulares (Geometria Bidimensional)
    Os polígonos regulares são figuras bidimensionais que apresentam **simetrias rotacionais** e **eixos de reflexão** bem definidos. 

    Por exemplo, um **quadrado** possui:
    - Simetria rotacional de **ordem 4** (rotações de 90°, 180°, 270° e 360°)
    - Quatro eixos de reflexão

    #### Sólidos Platónicos (Geometria Tridimensional)
    No espaço tridimensional, destacam-se os **Sólidos Platónicos**. As suas simetrias são fundamentais não apenas em geometria, mas também em fenómenos biológicos.

    O **icosaedro**, em particular, surge frequentemente na modelação de vírus graças à sua **elevada eficiência rotacional**, permitindo uma estrutura estável com o mínimo de informação genética (Flint et al., *Principles of Virology*).

    ---

    ### As Quatro Isometrias Fundamentais do Plano

    - **Translações**: Deslocamento da figura numa direção constante.
    - **Rotações**: Giro da figura em torno de um ponto fixo por um determinado ângulo.
    - **Reflexões**: “Espelhamento” da figura em relação a uma reta.
    - **Reflexões Deslizantes (glide reflections)**: Combinação de uma reflexão com uma translação paralela ao eixo de reflexão.

    Estas transformações podem combinar-se entre si e continuam a ser isometrias (Durbin, *Modern Algebra*). 

    **Exemplo**: A composição de duas reflexões em retas que se cruzam gera uma rotação.
    """)
            
        with st.expander("🔢 3. Teoria de Grupos: Estrutura Abstrata", expanded=False):
            st.markdown("""
    ### Teoria de Grupos: Estrutura Abstrata

    A **Teoria de Grupos** surge quando deixamos de estudar apenas a figura geométrica e passamos a analisar o **conjunto de todas as simetrias** associado a essa figura.

    Formalmente, um **grupo** $(G, ∗)$ é um conjunto munido de uma operação que satisfaz **quatro propriedades essenciais**:

    - **Fecho**: Para quaisquer $a, b \in G$, o elemento $a ∗ b$ também pertence a $G$.
    - **Associatividade**: Para quaisquer $a, b, c \in G$, $(a ∗ b) ∗ c = a ∗ (b ∗ c)$.
    - **Elemento Neutro**: Existe um elemento $e \in G$ tal que $e ∗ a = a ∗ e = a$, para todo $a \in G$.
    - **Elemento Inverso**: Para cada $a \in G$, existe $a^{-1} \in G$ tal que $a ∗ a^{-1} = a^{-1} ∗ a = e$.

    Um exemplo clássico é o **grupo das rotações do triângulo equilátero**, que forma o **grupo cíclico $C_3$**.

    Esta perspetiva abstrata permite aplicar a mesma linguagem formal na análise de fenómenos tão distintos como tesselações islâmicas, padrões em cristais ou interações moleculares (Lehninger, *Principles of Biochemistry*).
    """)
        with st.expander("🦠 4. Estruturas Virais Icosaédricas", expanded=False):
            st.markdown("""
    ### Estruturas Virais Icosaédricas

    Muitos vírus ditos “esféricos” apresentam, na verdade, uma estrutura altamente organizada baseada no **icosaedro**, um dos sólidos platónicos mais simétricos.

    A geometria icosaédrica oferece vantagens excecionais:

    - **Simetria Rotacional Avançada**: A maioria dos vírus esféricos possui uma estrutura baseada no icosaedro, com múltiplos eixos de simetria rotacional de ordem **2, 3 e 5**.
    - **Eficiência Estrutural**: Permite que subunidades proteicas idênticas (chamadas **capsómeros**) se encaixem perfeitamente, formando uma cápsula (capsídeo) fechada, estável e de grande resistência.
    - **Eficiência Genética**: Esta organização repetitiva permite que o vírus utilize um **único gene** para codificar uma pequena proteína, que através de rotações se multiplica para formar uma estrutura grande e complexa.

    Exemplos clássicos incluem o **adenovírus**, o **poliovírus** e o **vírus Zika**. Esta arquitetura viral é elegantemente descrita pelo modelo de **Caspar–Klug** (Flint et al., *Principles of Virology*).
    """)
        with st.expander("🧬 5. Estruturas Helicoidais e Simetria Quaternária", expanded=False):
            st.markdown("""
    ### Estruturas Helicoidais e Simetria Quaternária

    A simetria não se limita às estruturas virais. Ela desempenha um papel **fundamental na Biologia Molecular**, especialmente nas estruturas tridimensionais de proteínas e do ADN.

    #### Principais Manifestações de Simetria:

    - **Simetria Helicoidal**: Proteínas em hélice-alfa e a molécula de ADN utilizam uma elegante combinação de **rotação e translação** ao longo de um eixo. Matematicamente, este movimento é equivalente às **reflexões deslizantes** ou simetrias de translação aplicadas a um eixo central.
      
    - **Repetição e Estabilidade**: As subunidades rodam em torno de um eixo enquanto avançam verticalmente, gerando um padrão repetitivo, infinito e extremamente estável.

    - **Simetria Quaternária Cíclica**: Várias cadeias polipeptídicas organizam-se em torno de um eixo comum, formando estruturas altamente estáveis e funcionais.

    ---

    Assim como nas obras de **M. C. Escher**, onde padrões complexos e hipnóticos emergem de transformações simples, a natureza utiliza rotações e translações para construir sistemas moleculares altamente eficientes e estáveis.
    """)
    with st.expander("🎨 1.5 Simetria na Arte de M. C. Escher", expanded=True):
        st.markdown("""
        ### Simetria na Arte de M. C. Escher

        M. C. Escher é um dos artistas que melhor explorou as simetrias do plano, apesar de não possuir formação matemática formal. A sua obra é um fascinante exemplo da ligação profunda entre **arte e matemática**.

        Escher construiu tesselações complexas utilizando as quatro isometrias fundamentais:

        - **Rotações**
        - **Reflexões**
        - **Translações**
        - **Reflexões Deslizantes (glide reflections)**
        """)

        st.markdown("""
        #### Exemplo: Regular Division of the Plane nº 31

        Nesta obra icónica, observam-se claramente rotações de 180°, eixos de reflexão e translações regulares que repetem a figura base do peixe.
        """)

        # Imagem depois do texto
        try:
            st.image("/home/workdir/attachments/Regular-division-31.jpg", 
                    caption="M. C. Escher - Regular Division of the Plane nº 31 (1950)",
                    use_container_width=True)
        except:
            st.error("Não foi possível carregar a imagem. Verifique o caminho do ficheiro.")
            
    with st.expander("🔭 7. O Caleidoscópio e a Força Unificadora da Simetria", expanded=False):
        st.markdown("""
    ### O Caleidoscópio: Simetria em Ação

    O **caleidoscópio** é uma das demonstrações mais belas e intuitivas de como simetrias simples podem gerar padrões complexos e hipnóticos.

    O efeito visual resulta de **múltiplas reflexões** entre espelhos dispostos em triângulo, produzindo:

    - **Simetrias Rotacionais** de ângulo $\frac{360^\circ}{n}$
    - **Simetrias de Reflexão** múltiplas
    - **Padrões Regulares** infinitamente repetidos

    Cada reflexão corresponde a uma transformação geométrica precisa, criando repetições cíclicas infinitas que encantam o observador.

    ---

    ### A Força Unificadora da Simetria

    O estudo das simetrias revela a extraordinária capacidade da Matemática em **unificar fenómenos** aparentemente distintos:

    - Padrões presentes na **natureza** (estruturas virais e proteínas)
    - Manifestações **artísticas** (tesselações de Escher)
    - Construções **humanas** (azulejos, arquitetura e design)

    Através das **isometrias** e da **Teoria de Grupos**, conseguimos compreender e apreciar a profunda ordem matemática subjacente ao mundo que nos rodeia — desde o microscópico até ao artístico.
    """)

    with tab2:
        st.markdown("### 🧠 Questionário de Avaliação — Módulo 1")
        
        render_glass_card("""
            <p style="opacity: 0.7;">Responde às seguintes questões para testar os teus conhecimentos sobre Grupos de Simetria.</p>
        """)
        
        score1 = 0
        
        st.markdown("**Questão 1:** Quantas propriedades estruturais rígidas definem formalmente um grupo matemático?")
        r1_1 = st.radio("", ["Duas", "Quatro", "Dez"], key="r1_1", label_visibility="collapsed")
        
        st.markdown("**Questão 2:** O que caracteriza o movimento de uma reflexão deslizante (glide reflection)?")
        r1_2 = st.radio("", [
            "Apenas um giro de 90 graus.",
            "A combinação paralela e síncrona de uma reflexão axial e uma translação.",
            "Um deslocamento ortogonal isolado."
        ], key="r1_2", label_visibility="collapsed")
        
        st.markdown("**Questão 3:** Qual a principal vantagem biológica da simetria rotacional icosaédrica nas cápsides dos vírus?")
        r1_3 = st.radio("", [
            "Aumentar a velocidade do vírus.",
            "Permitir a construção de um invólucro volumoso e estável poupando informação genética por repetição proteica.",
            "Inibir a replicação celular."
        ], key="r1_3", label_visibility="collapsed")
        
        if r1_1 == "Quatro": score1 += 3.33
        if r1_2 == "A combinação paralela e síncrona de uma reflexão axial e uma translação.": score1 += 3.33
        if r1_3 == "Permitir a construção de um invólucro volumoso e estável poupando informação genética por repetição proteica.": score1 += 3.34
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("✅ Submeter Exame do Módulo 1", key="b1"):
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.metric("🎯 A tua Nota Final", f"{round(score1, 1)}/10")
                if score1 >= 8:
                    st.success("🏆 Excelente! Dominas os conceitos de simetria!")
                elif score1 >= 5:
                    st.warning("📚 Bom trabalho! Revê alguns conceitos para melhorar.")
                else:
                    st.error("💪 Continua a estudar! Revê a matéria e tenta novamente.")

# ==============================================================================
# MÓDULO 2: 17 GRUPOS CRISTALOGRÁFICOS
# ==============================================================================
elif page == "🟤 17 Grupos Cristalográficos":
    render_module_header("🟤", "MÓDULO 2: 17 GRUPOS CRISTALOGRÁFICOS")
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa & Classificação", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("📘 2.1 Grupos de Simetria e as Restrições das Tesselações Periódicas", expanded=False):
            st.markdown("""
            ### Explicação Teórica Exaustiva
            
            As tesselações periódicas são padrões que cobrem o plano de forma contínua, repetindo-se 
            indefinidamente através de translações. Cada tesselação possui um **grupo de simetria**, 
            isto é, o conjunto de todas as isometrias que deixam o padrão inalterado.
            
            Apesar da grande variedade de padrões que observamos em azulejos, cristais ou nas obras de 
            M. C. Escher, a Matemática demonstra que **apenas 17 tipos distintos de simetria podem 
            pavimentar o plano de forma regular**.
            
            Esta limitação resulta das combinações possíveis entre as isometrias estudadas anteriormente 
            e das restrições geométricas que garantem repetição periódica estável no plano.
            """)
            
            st.markdown("#### 📋 Matriz Oficial de Classificação dos 17 Wallpaper Groups")
            
            df_data = {
                "Grupo": ["p1", "p2", "pm", "pg", "cm", "pmm", "pmg", "pgg", "cmm", "p4", "p4m", "p4g", "p3", "p3m1", "p31m", "p6", "p6m"],
                "Simetrias Principais": [
                    "Apenas translações",
                    "Rotações de ordem 2",
                    "Reflexões",
                    "Reflexões deslizantes",
                    "Reflexões e translações oblíquas",
                    "Reflexões e rotações de ordem 2",
                    "Reflexões e reflexões deslizantes",
                    "Reflexões deslizantes e rotações de ordem 2",
                    "Reflexões múltiplas e rotações de ordem 2",
                    "Rotações de ordem 4",
                    "Rotações de ordem 4 e reflexões",
                    "Rotações de ordem 4 e reflexões deslizantes",
                    "Rotações de ordem 3",
                    "Rotações de ordem 3 e reflexões",
                    "Rotações de ordem 3 e reflexões (disposição diferente)",
                    "Rotações de ordem 6",
                    "Rotações de ordem 6 e reflexões"
                ]
            }
            st.dataframe(df_data, use_container_width=True, hide_index=True)
            
        with st.expander("🔍 2.2 Análise Comparativa dos Subgrupos p4, p6 e pm", expanded=False):
            st.markdown("""
            ### Explicação Teórica dos Subgrupos
            
            | Grupo | Características |
            |-------|-----------------|
            | **p4** (Simetria Quadrada) | Rotações de ordem 4 (90°, 180°, 270°). **Não possui** eixos de reflexão nem reflexões deslizantes. |
            | **p6** (Simetria Hexagonal) | Rotações de ordem 6 (60°, 120°, 180°, 240°, 300°), ordem 3 e ordem 2. **Não possui** reflexões. |
            | **pm** (Simetria Axial) | Eixos de reflexão paralelos combinados com translações perpendiculares. **Não possui** rotações. |
            """)
            
            st.markdown("#### 🎛️ Explorador Interativo de Grupos")
            
            s_grupo = st.selectbox(
                "Seleciona um grupo para inspecionar:",
                ["p4 (Quadrada)", "p6 (Hexagonal)", "pm (Retangular)"],
                key="s_grupo"
            )
            
            if "p4" in s_grupo:
                st.info("🔄 **Propriedades p4:** Rotações de ordem 4 e 2. Rede ortogonal rígida. Total ausência de eixos axiais de espelhamento.")
            elif "p6" in s_grupo:
                st.success("🐝 **Propriedades p6:** Rotações de ordens 6, 3 e 2. Estrutura geométrica idêntica à estabilidade mecânica dos favos naturais.")
            elif "pm" in s_grupo:
                st.warning("🪞 **Propriedades pm:** Eixos axiais paralelos puros. Domínio exclusivo de reflexões especulares lineares.")

    with tab2:
        st.markdown("### 🧠 Questionário de Avaliação — Módulo 2")
        
        score2 = 0
        
        st.markdown("**Questão 1:** Qual o número máximo de grupos cristalográficos abstratos que a restrição geométrica permite existir para pavimentar o plano bidimensional?")
        r2_1 = st.radio("", ["Infinitos", "Apenas 12", "Exatamente 17"], key="r2_1", label_visibility="collapsed")
        
        st.markdown("**Questão 2:** O que diferencia fundamentalmente o grupo cristalográfico 'p6' do grupo 'p6m'?")
        r2_2 = st.radio("", [
            "O grupo p6 possui eixos axiais de reflexão.",
            "Ambos possuem rotações de ordem 6, mas o grupo p6 carece inteiramente de eixos de reflexão.",
            "O grupo p6 não possui translações hexagonais."
        ], key="r2_2", label_visibility="collapsed")
        
        st.markdown("**Questão 3:** Que tipo de simetria e rede de translação definem o comportamento do subgrupo 'pm'?")
        r2_3 = st.radio("", [
            "Simetria puramente rotacional em malha quadrada.",
            "Simetria axial dominante baseada em eixos de reflexão paralelos numa rede retangular.",
            "Reflexões deslizantes exclusivas em rede oblíqua."
        ], key="r2_3", label_visibility="collapsed")
        
        if r2_1 == "Exatamente 17": score2 += 3.33
        if r2_2 == "Ambos possuem rotações de ordem 6, mas o grupo p6 carece inteiramente de eixos de reflexão.": score2 += 3.33
        if r2_3 == "Simetria axial dominante baseada em eixos de reflexão paralelos numa rede retangular.": score2 += 3.34
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("✅ Submeter Exame do Módulo 2", key="b2"):
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.metric("🎯 A tua Nota Final", f"{round(score2, 1)}/10")
                if score2 >= 8:
                    st.success("🏆 Excelente! Dominas os grupos cristalográficos!")
                elif score2 >= 5:
                    st.warning("📚 Bom trabalho! Revê alguns conceitos para melhorar.")
                else:
                    st.error("💪 Continua a estudar! Revê a matéria e tenta novamente.")

# ==============================================================================
# MÓDULO 3: LÓGICA DO NUMBER MATCH
# ==============================================================================
elif page == "🟢 Lógica do Number Match":
    render_module_header("🟢", "MÓDULO 3: LÓGICA DO NUMBER MATCH")
    
    tab1, tab2 = st.tabs(["💡 Lição do Sistema & Simulador", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("📘 3.1 Formalização Lógica e Regras Proposicionais do Tabuleiro", expanded=False):
            st.markdown("""
            ### Explicação Teórica
            
            O *Number Match* é um jogo de lógica e aritmética cujas decisões do jogador dependem 
            simultaneamente de **condições lógicas** e de **propriedades aritméticas elementares**, 
            como igualdade, soma e paridade.
            
            A formalização das condições de jogada pode ser feita recorrendo à **lógica proposicional**. 
            Uma jogada válida ocorre quando dois números $$a$$ e $$b$$ satisfazem simultaneamente uma 
            condição numérica e uma condição estrutural de acessibilidade:
            """)
            
            st.latex(r"\text{JogadaVálida}(a, b) \leftrightarrow (a = b \lor a + b = 10) \land \text{Conectados}(a, b)")
            
            st.markdown("---")
            
            st.markdown("#### 🕹️ Simulador de Validação Lógica")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                s_a = st.number_input("Valor da Carta A", 1, 9, 5, key="s_a")
            with col2:
                s_b = st.number_input("Valor da Carta B", 1, 9, 5, key="s_b")
            with col3:
                s_con = st.checkbox("Conectados/Contíguos?", value=True, key="s_con")
            
            c_num = (s_a == s_b) or (s_a + s_b == 10)
            c_valida = c_num and s_con
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if c_valida:
                st.success(f"🟩 **JOGADA VÁLIDA!** O par ({s_a}, {s_b}) cumpre todas as condições e pode ser eliminado.")
            else:
                reasons = []
                if not c_num:
                    reasons.append(f"Os valores não são iguais nem somam 10 ({s_a} + {s_b} = {s_a + s_b})")
                if not s_con:
                    reasons.append("As cartas não estão conectadas")
                st.error(f"🟥 **JOGADA INVÁLIDA!** Razões: {'; '.join(reasons)}")
                
        with st.expander("📈 3.2 Modelação em Teoria de Grafos e Estratégia de Paridade", expanded=False):
            st.markdown("""
            ### Explicação Teórica Exaustiva
            
            O tabuleiro do jogo pode ser representado como um **grafo dinâmico**, no qual os números 
            correspondem a vértices e as relações de jogada válida a arestas. À medida que o jogador 
            elimina pares, o grafo sofre transformações sucessivas.
            
            **Vértices de grau zero** representam números isolados que não podem ser eliminados e 
            bloqueiam o tabuleiro.
            
            ---
            
            ### Análise Combinatória e o Impacto do Número 5
            
            Cada número entre 1 e 9 possui exatamente um único parceiro que permite obter a soma 10:
            
            | Par | Soma |
            |-----|------|
            | 1 ↔ 9 | 10 |
            | 2 ↔ 8 | 10 |
            | 3 ↔ 7 | 10 |
            | 4 ↔ 6 | 10 |
            | **5 ↔ 5** | 10 |
            
            O número **5** constitui um caso particular, pois **apenas pode formar par consigo mesmo**. 
            Isto implica que a sua frequência no tabuleiro deve ser impreterivelmente **par** para 
            permitir a eliminação completa e evitar a criação de números isolados.
            """)

    with tab2:
        st.markdown("### 🧠 Questionário de Avaliação — Módulo 3")
        
        score3 = 0
        
        st.markdown("**Questão 1:** Qual o estado de um número que se transforma num vértice de grau zero no grafo?")
        r3_1 = st.radio("", [
            "Fica isolado e bloqueia o progresso do jogo.",
            "Garante uma jogada imediata por igualdade.",
            "Duplica o número de arestas incidentes."
        ], key="r3_1", label_visibility="collapsed")
        
        st.markdown("**Questão 2:** Qual a correspondência biunívoca correta para somas complementares de valor 10?")
        r3_2 = st.radio("", [
            r"2 ↔ 8",
            r"3 ↔ 7",
            r"4 ↔ 4"
        ], key="r3_2", label_visibility="collapsed")
        
        st.markdown("**Questão 3:** Por que razão a contagem combinatória do número 5 exige uma frequência obrigatoriamente par?")
        r3_3 = st.radio("", [
            "Porque é um número ímpar.",
            "Porque apenas pode emparelhar consigo próprio para atingir a soma 10.",
            "Porque é o vértice central de Euler."
        ], key="r3_3", label_visibility="collapsed")
        
        if r3_1 == "Fica isolado e bloqueia o progresso do jogo.": score3 += 3.33
        if r3_2 == r"3 ↔ 7": score3 += 3.33
        if r3_3 == "Porque apenas pode emparelhar consigo próprio para atingir a soma 10.": score3 += 3.34
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("✅ Submeter Exame do Módulo 3", key="b3"):
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.metric("🎯 A tua Nota Final", f"{round(score3, 1)}/10")
                if score3 >= 8:
                    st.success("🏆 Excelente! Dominas a lógica do Number Match!")
                elif score3 >= 5:
                    st.warning("📚 Bom trabalho! Revê alguns conceitos para melhorar.")
                else:
                    st.error("💪 Continua a estudar! Revê a matéria e tenta novamente.")

# ==============================================================================
# MÓDULO 4: PADRÕES DOS PRIMOS
# ==============================================================================
elif page == "🟣 Padrões dos Primos":
    render_module_header("🟣", "MÓDULO 4: PADRÕES DOS PRIMOS")
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa & Aplicações", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("📘 4.1 A Natureza e Distribuição Irregular dos Números Primos", expanded=False):
            st.markdown("""
            ### Explicação Teórica Exaustiva
            
            A Teoria dos Números revela estruturas profundas e padrões inesperados. A matemática pura 
            possui uma beleza intrínseca precisamente porque revela **ordem onde antes se supunha irregularidade**.
            
            Os números primos são fundamentais na aritmética: o **Teorema Fundamental da Aritmética** 
            estabelece que qualquer número inteiro positivo pode ser decomposto de forma única num 
            produto de primos.
            
            A distribuição dos primos é notoriamente irregular. Essa oscilação entre ordem e caos levou 
            à introdução da **função zeta complexa** e à formulação da célebre **Hipótese de Riemann**, 
            segundo a qual todas as raízes não triviais dessa função têm parte real igual a $$\\frac{1}{2}$$.
            """)
            
        with st.expander("🌀 4.2 A Espiral de Ulam e Padrões Inesperados", expanded=False):
            st.markdown("""
            ### Explicação Teórica Exaustiva
            
            A visualização na **Espiral de Ulam** revelou que os números primos se alinham em 
            **diagonais longas e bem definidas**.
            
            As diagonais da espiral correspondem a expressões quadráticas do tipo $$an^2 + bn + c$$. 
            O exemplo mais famoso é o **polinómio de Euler**:
            """)
            
            st.latex(r"P(n) = n^2 + n + 41")
            
            st.markdown("Este polinómio produz números primos para todos os inteiros de $$n = 0$$ a $$n = 39$$.")
            
            st.markdown("---")
            
            st.markdown("#### 🎛️ Laboratório: Gerador de Primos de Euler")
            
            n_slider = st.slider("Altere o valor de n para validar o polinómio:", 0, 39, 0, key="euler_slider")
            res_euler = (n_slider**2) + n_slider + 41
            
            def is_prime(n):
                if n < 2:
                    return False
                for i in range(2, int(n**0.5) + 1):
                    if n % i == 0:
                        return False
                return True
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(f"P({n_slider})", int(res_euler))
            with col2:
                if is_prime(res_euler):
                    st.success("✅ É primo!")
                else:
                    st.error("❌ Não é primo")
            
        with st.expander("φ 4.3 A Função Totiente de Euler", expanded=False):
            st.markdown("""
            ### Explicação Teórica
            
            A função totiente $$\\varphi(n)$$, introduzida por Euler, conta quantos naturais até $$n$$ 
            são **coprimos** com $$n$$ (ou seja, cujo máximo divisor comum com $$n$$ é 1).
            
            ### Fórmula Multiplicativa Geral
            
            Se $$n = p_1^{a_1} p_2^{a_2} \\dots p_k^{a_k}$$ em que $$p_1, p_2, \\dots, p_k$$ são os 
            fatores primos distintos de $$n$$, então:
            """)
            
            st.latex(r"\varphi(n) = n \prod_{i=1}^{k} \left(1 - \frac{1}{p_i}\right)")
            
            st.markdown("""
            ### Propriedades Fundamentais
            
            | Propriedade | Fórmula |
            |-------------|---------|
            | Totiente de um número primo $$p$$ | $$\\varphi(p) = p - 1$$ |
            | Totiente de uma potência de primo | $$\\varphi(p^k) = p^k - p^{k-1}$$ |
            
            Esta função é central na **criptografia moderna**, nomeadamente no algoritmo **RSA**.
            """)
            
            st.markdown("---")
            
            st.markdown("#### 🔢 Calculadora do Totiente")
            
            num_input = st.number_input("Introduz um valor para calcular φ(n):", min_value=2, max_value=500, value=12, key="tot_input")
            
            def phi_alg(n):
                result = n
                p = 2
                temp_n = n
                while p * p <= temp_n:
                    if temp_n % p == 0:
                        while temp_n % p == 0:
                            temp_n //= p
                        result -= result // p
                    p += 1
                if temp_n > 1:
                    result -= result // temp_n
                return result
            
            phi_result = phi_alg(num_input)
            st.metric(f"φ({num_input})", phi_result)

    with tab2:
        st.markdown("### 🧠 Questionário de Avaliação — Módulo 4")
        
        score4 = 0
        
        st.markdown("**Questão 1:** O que postula a célebre Hipótese de Riemann?")
        r4_1 = st.radio("", [
            "Que todas as diagonais quadráticas geram primos.",
            "Que todas as raízes não triviais da função zeta complexa têm parte real igual a 1/2.",
            "Que a função totiente é constante."
        ], key="r4_1", label_visibility="collapsed")
        
        st.markdown("**Questão 2:** Quanto vale a função totiente de Euler para n=12?")
        r4_2 = st.radio("", ["12", "6", "4", "2"], key="r4_2", label_visibility="collapsed")
        
        st.markdown("**Questão 3:** Qual a propriedade fundamental de um número primo p em relação ao seu totiente?")
        r4_3 = st.radio("", [
            "φ(p) = p",
            "φ(p) = p - 1",
            "φ(p) = 1"
        ], key="r4_3", label_visibility="collapsed")
        
        if r4_1 == "Que todas as raízes não triviais da função zeta complexa têm parte real igual a 1/2.": score4 += 3.33
        if r4_2 == "4": score4 += 3.33
        if r4_3 == "φ(p) = p - 1": score4 += 3.34
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("✅ Submeter Exame do Módulo 4", key="b4"):
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.metric("🎯 A tua Nota Final", f"{round(score4, 1)}/10")
                if score4 >= 8:
                    st.success("🏆 Excelente! Dominas os padrões dos primos!")
                elif score4 >= 5:
                    st.warning("📚 Bom trabalho! Revê alguns conceitos para melhorar.")
                else:
                    st.error("💪 Continua a estudar! Revê a matéria e tenta novamente.")

# ==============================================================================
# MÓDULO 5: PADRÕES NUMÉRICOS
# ==============================================================================
elif page == "🟡 Padrões Numéricos":
    render_module_header("🟡", "MÓDULO 5: PADRÕES NUMÉRICOS")
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa & Gráficos", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("📐 5.1 Números Triangulares e Contagem Geométrica", expanded=False):
            st.markdown("""
            ### Explicação Teórica
            
            Os números triangulares pertencem ao grupo dos **números figurados**, que se caracterizam 
            por serem números que podem ser representados através de arranjos geométricos de pontos regulares.
            
            Eles representam a quantidade de pontos necessária para construir um **triângulo equilátero** 
            com um determinado número de linhas. Como cada nova linha adiciona sempre mais um ponto do 
            que a linha anterior, um número triangular corresponde diretamente à **soma dos primeiros 
            números naturais**:
            """)
            
            st.latex(r"T_n = 1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2}")
            
            st.markdown("""
            Esta fórmula pode ser explicada através de um raciocínio geométrico atribuído a **Gauss**: 
            se escrevermos a sequência da soma na sua ordem direta e inversa, cada par de termos 
            resulta em $$n+1$$. Como existem $$n$$ termos, a soma total das duas linhas é $$2T_n = n(n+1)$$.
            
            ---
            
            ### Aplicação Prática
            
            Os números triangulares modelam problemas de contagem em redes. Se tivermos **6 pessoas** 
            e quisermos saber quantos **apertos de mão únicos** ocorrem se todas se cumprimentarem:
            """)
            
            st.latex(r"T_5 = \frac{5 \times 6}{2} = 15 \text{ apertos de mão}")
            
            if GRAFICOS_ATIVOS:
                st.markdown("#### 📐 Triângulo Pitagórico (3, 4, 5)")
                
                fig_tri, ax_tri = plt.subplots(figsize=(4, 4))
                fig_tri.patch.set_facecolor('#0f0f23')
                ax_tri.set_facecolor('#0f0f23')
                
                x_tri = [0, 4, 0, 0]
                y_tri = [0, 0, 3, 0]
                ax_tri.plot(x_tri, y_tri, color='#667eea', linewidth=2.5)
                ax_tri.fill([0, 4, 0], [0, 0, 3], color='#667eea', alpha=0.2)
                
                ax_tri.text(2, -0.4, "4", fontsize=12, ha='center', color='white', fontweight='bold')
                ax_tri.text(-0.4, 1.5, "3", fontsize=12, va='center', color='white', fontweight='bold')
                ax_tri.text(2.2, 1.8, "5", fontsize=12, ha='center', color='white', fontweight='bold')
                
                ax_tri.plot([0, 0.3, 0.3, 0], [0, 0, 0.3, 0], color='#f093fb', linewidth=1.5)
                
                ax_tri.axis('equal')
                ax_tri.axis('off')
                st.pyplot(fig_tri)
            
        with st.expander("✨ 5.2 Números Perfeitos e Harmonia de Divisores", expanded=False):
            st.markdown("""
            ### Explicação Teórica Exaustiva
            
            Um **número perfeito** define-se como um número inteiro positivo que é exatamente igual 
            à soma de todos os seus **divisores próprios** (divisores menores que o próprio número).
            
            Esta definição remonta aos *Elementos de Euclides*, refletindo o interesse por propriedades 
            estéticas de equilíbrio e harmonia aritmética.
            
            ---
            
            ### Exemplos Clássicos
            
            | Número | Divisores Próprios | Soma |
            |--------|-------------------|------|
            | **6** | 1, 2, 3 | 1 + 2 + 3 = **6** ✓ |
            | **28** | 1, 2, 4, 7, 14 | 1 + 2 + 4 + 7 + 14 = **28** ✓ |
            
            ---
            
            ### Relação com os Primos de Mersenne
            
            Os números perfeitos pares têm uma ligação direta com os **Primos de Mersenne** ($$2^p - 1$$). 
            Euclides demonstrou que quando $$2^p - 1$$ é primo, gera-se um número perfeito par:
            """)
            
            st.latex(r"n = 2^{p-1}(2^p - 1)")
            
        with st.expander("9️⃣ 5.3 Exploração do Número 9 na Base Decimal", expanded=False):
            st.markdown("""
            ### Explicação Teórica Exaustiva
            
            O número **9** ocupa um lugar de destaque na aritmética elementar devido à organização do 
            nosso sistema de numeração em **base 10**. Pelo facto de $$9 = 10 - 1$$, cria-se um conjunto 
            único de simetrias e regras de divisibilidade.
            
            ### Propriedade Modular
            
            Qualquer número inteiro positivo é sempre **congruente com a soma dos seus dígitos** em módulo 9:
            """)
            
            st.latex(r"n \equiv \text{soma dos dígitos de } n \pmod{9}")
            
            st.markdown("""
            Esta propriedade justifica o **critério de divisibilidade por 9**.
            
            ### Simetria na Tabuada do 9
            
            Os resultados da tabuada formam um **espelho numérico**:
            - $$9 \\times 2 = 18$$ ↔ $$9 \\times 9 = 81$$
            - $$9 \\times 3 = 27$$ ↔ $$9 \\times 8 = 72$$
            - $$9 \\times 4 = 36$$ ↔ $$9 \\times 7 = 63$$
            
            Em todos os produtos, a **soma dos dígitos é sempre 9**.
            """)
            
            st.markdown("---")
            
            st.markdown("#### 🔄 Laboratório de Redução Digital (Módulo 9)")
            
            num_9_input = st.text_input("Introduz um número inteiro:", value="432", key="num_9_input")
            
            if num_9_input.isdigit() and int(num_9_input) > 0:
                n_atual = int(num_9_input)
                passos = [str(n_atual)]
                
                while n_atual > 9:
                    soma_digitos = sum(int(d) for d in str(n_atual))
                    passos.append(str(soma_digitos))
                    n_atual = soma_digitos
                
                caminho_setas = " → ".join(passos)
                
                st.info(f"**Cadeia de Colapso:** {caminho_setas}")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Raiz Digital", n_atual)
                with col2:
                    resto_mod = int(num_9_input) % 9
                    st.metric("Resto (mod 9)", resto_mod if resto_mod != 0 else 9)
                
                if n_atual == 9:
                    st.success(f"🟩 O número {num_9_input} é múltiplo de 9!")
                else:
                    st.warning(f"🟨 O número não é múltiplo de 9. Resto: {resto_mod if resto_mod != 0 else 9}")
            else:
                st.error("Introduz apenas números inteiros positivos.")
            
        with st.expander("∞ 5.4 O Último Teorema de Fermat", expanded=False):
            st.markdown("""
            ### Explicação Teórica
            
            O **Último Teorema de Fermat** ilustra como pequenas alterações numa expressão matemática 
            podem fazer com que um padrão de soluções infinitas **desapareça por completo**.
            
            Para $$n = 2$$, a equação de Pitágoras admite infinitas soluções inteiras (triplas pitagóricas):
            """)
            
            st.latex(r"a^2 + b^2 = c^2 \quad \text{(ex: } 3^2 + 4^2 = 5^2 \text{)}")
            
            st.markdown("""
            Contudo, Fermat afirmou que a equação geral:
            """)
            
            st.latex(r"a^n + b^n = c^n")
            
            st.markdown("""
            **não admite qualquer solução inteira não trivial** para $$n > 2$$.
            
            A prova definitiva foi alcançada por **Andrew Wiles** em 1995, utilizando conceitos 
            sofisticados como **curvas elípticas** e **formas modulares**.
            """)
            
            if GRAFICOS_ATIVOS:
                st.markdown("#### 📊 Comparação das Curvas de Fermat")
                
                n_input_txt = st.text_input("Expoente n (> 2) para comparar com n=2:", value="3.0", key="fermat_n")
                
                try:
                    n_fermat = float(n_input_txt)
                    if n_fermat <= 2:
                        st.warning("Introduz um valor > 2 para ver a diferença.")
                        n_fermat = 3.0
                except ValueError:
                    st.error("Introduz um valor numérico válido.")
                    n_fermat = 3.0
                
                a_grid = np.linspace(0.01, 5, 400)
                b_grid = np.linspace(0.01, 5, 400)
                A, B = np.meshgrid(a_grid, b_grid)
                
                fig_fer, ax_fer = plt.subplots(figsize=(6, 6))
                fig_fer.patch.set_facecolor('#0f0f23')
                ax_fer.set_facecolor('#0f0f23')
                
                C2 = A**2 + B**2
                ax_fer.contour(A, B, C2, levels=[25], colors=['#4facfe'], linewidths=2.5)
                
                Cn = A**n_fermat + B**n_fermat
                ax_fer.contour(A, B, Cn, levels=[25], colors=['#f093fb'], linestyles='--', linewidths=2.5)
                
                ax_fer.scatter([3], [4], color='#00f2fe', s=100, zorder=5, edgecolors='white', linewidth=2)
                ax_fer.annotate('(3, 4)', (3, 4), xytext=(3.3, 4.3), color='white', fontsize=10)
                
                ax_fer.set_xlabel("a", fontsize=12, color='white')
                ax_fer.set_ylabel("b", fontsize=12, color='white')
                ax_fer.tick_params(colors='white')
                ax_fer.grid(alpha=0.2, color='white')
                
                for spine in ax_fer.spines.values():
                    spine.set_color('white')
                    spine.set_alpha(0.3)
                
                from matplotlib.lines import Line2D
                handles = [
                    Line2D([0], [0], color='#4facfe', lw=2.5, linestyle='-'),
                    Line2D([0], [0], color='#f093fb', lw=2.5, linestyle='--')
                ]
                labels = ["n = 2", f"n = {n_fermat:.1f}"]
                ax_fer.legend(handles, labels, loc="upper right", fontsize=10, 
                             facecolor='#1a1a3e', edgecolor='white', labelcolor='white')
                
                st.pyplot(fig_fer)

    with tab2:
        st.markdown("### 🧠 Questionário de Avaliação — Módulo 5")
        
        score5 = 0
        
        st.markdown("**Questão 1:** Qual a expressão utilizada para calcular o n-ésimo número triangular?")
        r5_1 = st.radio("", [
            "Tₙ = n(n+1)/2",
            "Tₙ = 2ⁿ - 1",
            "Tₙ = n² + n + 41"
        ], key="r5_1", label_visibility="collapsed")
        
        st.markdown("**Questão 2:** Qual a relação matemática que define se um número é perfeito?")
        r5_2 = st.radio("", [
            "σ(n) = n",
            "σ(n) = 2n",
            "σ(n) = n - 1"
        ], key="r5_2", label_visibility="collapsed")
        
        st.markdown("**Questão 3:** A partir de que expoente n deixa de existir qualquer solução inteira não trivial segundo Fermat?")
        r5_3 = st.radio("", [
            "n > 1",
            "n > 2",
            "n > 5"
        ], key="r5_3", label_visibility="collapsed")
        
        if r5_1 == "Tₙ = n(n+1)/2": score5 += 3.33
        if r5_2 == "σ(n) = 2n": score5 += 3.33
        if r5_3 == "n > 2": score5 += 3.34
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("✅ Submeter Exame do Módulo 5", key="b5"):
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.metric("🎯 A tua Nota Final", f"{round(score5, 1)}/10")
                if score5 >= 8:
                    st.success("🏆 Excelente! Dominas os padrões numéricos!")
                elif score5 >= 5:
                    st.warning("📚 Bom trabalho! Revê alguns conceitos para melhorar.")
                else:
                    st.error("💪 Continua a estudar! Revê a matéria e tenta novamente.")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
render_divider()
st.markdown("""
<div style="text-align: center; opacity: 0.5; padding: 2rem 0;">
    <p>© 2024 MathXplore — ISCTE Sintra</p>
    <p style="font-size: 0.8rem;">Fundamentos de Matemática • Licenciatura em MATD</p>
</div>
""", unsafe_allow_html=True)
