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

/* =========================================
   APP
========================================= */

.stApp {
    background: #0f0f23;
}

/* =========================================
   TEXTO GLOBAL
========================================= */

html, body, [class*="css"] {
    color: rgba(255,255,255,0.92);
}

p, label, div {
    color: rgba(255,255,255,0.88);
}

h1, h2, h3 {
    color: #b388ff;
    font-weight: 700;
}

/* =========================================
   INPUTS GERAIS
========================================= */

div[data-baseweb="input"] {
    background: rgba(255,255,255,0.06) !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    overflow: hidden;
}

/* caixa interior */
div[data-baseweb="input"] input {
    background: rgba(255,255,255,0.06) !important;
    color: white !important;
    font-size: 1.2rem !important;
    font-weight: 600 !important;
}

/* placeholder */
div[data-baseweb="input"] input::placeholder {
    color: rgba(255,255,255,0.5) !important;
}

/* focus */
div[data-baseweb="input"]:focus-within {
    border: 1px solid #8b5cf6 !important;
    box-shadow: 0 0 12px rgba(139,92,246,0.35);
}

/* =========================================
   NUMBER INPUT BOTÕES + -
========================================= */

button[data-testid="stNumberInputStepUp"],
button[data-testid="stNumberInputStepDown"] {
    background: rgba(255,255,255,0.08) !important;
    color: white !important;
    border: none !important;
}

button[data-testid="stNumberInputStepUp"]:hover,
button[data-testid="stNumberInputStepDown"]:hover {
    background: #8b5cf6 !important;
}

/* =========================================
   SELECTBOX
========================================= */

div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.06) !important;
    border-radius: 14px !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
}

/* texto */
div[data-baseweb="select"] span {
    color: white !important;
}

/* dropdown */
ul[role="listbox"] {
    background: #1b1b35 !important;
}

/* opções */
li[role="option"] {
    color: white !important;
}

/* hover */
li[role="option"]:hover {
    background: rgba(139,92,246,0.3) !important;
}

/* =========================================
   SLIDER
========================================= */

.stSlider {
    color: white !important;
}

/* =========================================
   EXPANDERS
========================================= */

details {
    background: rgba(255,255,255,0.04) !important;
    border-radius: 16px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    padding: 0.5rem;
}

/* header */
summary {
    color: white !important;
    font-weight: 600;
}

/* conteúdo */
details div {
    color: rgba(255,255,255,0.9) !important;
}

/* =========================================
   TABS
========================================= */

button[data-baseweb="tab"] {
    color: white !important;
    background: transparent !important;
    border-radius: 12px 12px 0 0 !important;
}

/* ativa */
button[aria-selected="true"] {
    background: rgba(139,92,246,0.18) !important;
}

/* =========================================
   BOTÕES
========================================= */

.stButton button {
    background: linear-gradient(135deg,#7c3aed,#8b5cf6);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 600;
}

.stButton button:hover {
    transform: translateY(-1px);
    box-shadow: 0 0 14px rgba(139,92,246,0.4);
}

/* =========================================
   MÉTRICAS / CARDS
========================================= */

[data-testid="stMetric"] {
    background: rgba(255,255,255,0.04);
    padding: 1rem;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.08);
}



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

def render_module_header(title, color_class="primary"):
    """Renderiza um header de módulo premium"""
    st.markdown(f"""
    <div class="modulo-header">
        <h2>{title}</h2>
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
            "Grupos de Simetria",
            "17 Grupos Cristalográficos",
            "Lógica do Number Match",
            "Padrões dos Primos",
            "Padrões Numéricos"
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
        <h1 class="hero-title">MathXplore</h1>
        <div class="hero-subtitle">
            Plataforma interativa com conhecimentos nas mais vastas áreas da matemática. Explore conceitos através de visualizações dinâmicas, simuladores e quizzes.
        </div>
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
    
    st.markdown("""
    ### Sobre a Plataforma

    Esta plataforma digital foi desenvolvida para integrar a totalidade dos conteúdos teóricos presentes nos cinco projetos académicos desenvolvidos nos relatórios.

    A nossa abordagem converte a teoria exaustiva dos relatórios em componentes de aprendizagem dinâmicos, estruturados rigorosamente sob a metodologia de **Explicação Teórica**,  
    **Aplicação Prática** e **Questionários Gerais com Pontuação** automática.
    """)

    

# ==============================================================================
# MÓDULO 1: GRUPOS DE SIMETRIA
# ==============================================================================
elif page == "Grupos de Simetria":
    render_divider()
    render_module_header( "MÓDULO 1: GRUPOS DE SIMETRIA")
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("📘 Introdução à Simetria e Teoria de Grupos", expanded=True):
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
        with st.expander("📐 1. Geometria dos Polígonos e Sólidos Platónicos", expanded=False):
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
            
        with st.expander("🔢 2. Teoria de Grupos: Estrutura Abstrata", expanded=False):
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
        with st.expander("🦠 3. Estruturas Virais Icosaédricas", expanded=False):
            st.markdown("""
    ### Estruturas Virais Icosaédricas

    Muitos vírus ditos “esféricos” apresentam, na verdade, uma estrutura altamente organizada baseada no **icosaedro**, um dos sólidos platónicos mais simétricos.

    A geometria icosaédrica oferece vantagens excecionais:

    - **Simetria Rotacional Avançada**: A maioria dos vírus esféricos possui uma estrutura baseada no icosaedro, com múltiplos eixos de simetria rotacional de ordem **2, 3 e 5**.
    - **Eficiência Estrutural**: Permite que subunidades proteicas idênticas (chamadas **capsómeros**) se encaixem perfeitamente, formando uma cápsula (capsídeo) fechada, estável e de grande resistência.
    - **Eficiência Genética**: Esta organização repetitiva permite que o vírus utilize um **único gene** para codificar uma pequena proteína, que através de rotações se multiplica para formar uma estrutura grande e complexa.

    Exemplos clássicos incluem o **adenovírus**, o **poliovírus** e o **vírus Zika**. Esta arquitetura viral é elegantemente descrita pelo modelo de **Caspar–Klug** (Flint et al., *Principles of Virology*).
    """)
        with st.expander("🧬 4. Estruturas Helicoidais e Simetria Quaternária", expanded=False):
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
    with st.expander("🎨 5. Simetria na Arte de M. C. Escher", expanded=False):
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
            st.image("Regular-division-31.jpg", 
                    caption="M. C. Escher - Regular Division of the Plane nº 31 (1950)",
                    use_container_width=True)
        except:
            st.error("Não foi possível carregar a imagem. Verifique o caminho do ficheiro.")

    with st.expander("🔭 6. O Caleidoscópio e a Força Unificadora da Simetria", expanded=False):
        st.markdown("""
    ### O Caleidoscópio: Simetria em Ação

    O **caleidoscópio** é uma das demonstrações mais belas e intuitivas de como simetrias simples podem gerar padrões complexos e hipnóticos.

    O efeito visual resulta de **múltiplas reflexões** entre espelhos dispostos em triângulo, produzindo:

    - **Simetrias Rotacionais** de ângulo 360°/n
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
elif page == "17 Grupos Cristalográficos":
    render_divider()
    render_module_header( "MÓDULO 2: 17 GRUPOS CRISTALOGRÁFICOS")
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("📖 Introdução aos 17 Grupos Cristalográficos", expanded=True):
            st.markdown("""
            ### Introdução aos 17 Grupos Cristalográficos

            No trabalho anterior explorámos os conceitos fundamentais de simetria e as isometrias do plano — **translações, rotações, reflexões e reflexões deslizantes** —, tal como descritas classicamente por Grünbaum e Shephard em *Tilings and Patterns* (1987), uma das obras de referência no estudo das tesselações.

            Esta base teórica permite agora avançar para uma classificação mais completa e estruturada: **os 17 Grupos Cristalográficos do Plano** (também conhecidos como *Wallpaper Groups*). A apresentação moderna destes grupos segue, entre outros, o trabalho de Conway, Burgiel e Goodman-Strauss em *The Symmetries of Things* (2008).

            ---

            Apesar da enorme variedade de padrões que observamos em azulejos, cristais, tecidos ou nas obras de **M. C. Escher** (amplamente analisadas por Schattschneider em *Visions of Symmetry*, 2004), a Matemática demonstra que **apenas 17 tipos distintos de simetria** podem pavimentar o plano de forma regular e periódica.

            Esta limitação geométrica resulta das combinações possíveis entre as isometrias estudadas anteriormente e das restrições impostas pela repetição periódica no plano, conforme discutido por Holden em *Shapes, Space and Symmetry* (1991).

            ---

            Neste módulo apresentamos uma visão geral dos **17 grupos cristalográficos** e, de seguida, analisamos com maior detalhe três grupos específicos, destacando as suas propriedades geométricas e exemplos representativos.

            O objetivo é aprofundar a compreensão das simetrias do plano e consolidar a ligação entre a teoria abstrata e as suas múltiplas aplicações visuais e estruturais.
            """)
        with st.expander("📘 1. Grupos de Simetria e Tesselações Periódicas", expanded=False):
            st.markdown("""
            ### Grupos de Simetria e Tesselações Periódicas

            As **tesselações periódicas** são padrões que cobrem o plano de forma contínua e repetem-se indefinidamente através de translações. A definição formal e a análise estrutural destas tesselações estão detalhadamente exploradas na obra clássica *Tilings and Patterns* de Grünbaum e Shephard.

            Cada tesselação possui um **grupo de simetria**, isto é, o conjunto de todas as isometrias que deixam o padrão inalterado. Esta abordagem, que combina Geometria com Teoria de Grupos, é apresentada de forma acessível e visual por Conway, Burgiel e Goodman-Strauss em *The Symmetries of Things*.

            ---

            ### O que distingue os diferentes grupos?

            A presença ou ausência de:
            - Eixos de reflexão
            - Centros de rotação de diferentes ordens (2, 3, 4 ou 6)
            - Reflexões deslizantes

            permite distinguir padrões que, à primeira vista, podem parecer semelhantes. Esta distinção é frequentemente ilustrada nas análises das obras de **M. C. Escher** feitas por Schattschneider (2004).

            A Teoria de Grupos fornece a linguagem formal necessária para descrever estas simetrias e compreender como diferentes combinações de isometrias originam estruturas geométricas distintas.

            ---

            ### Um dos Resultados Mais Importantes

            Um dos resultados mais notáveis deste estudo é que existem **exatamente 17 grupos cristalográficos do plano**. Este resultado aparece tanto em obras de geometria recreativa (como a de Holden), como em textos mais formais de cristalografia, tais como *The Basics of Crystallography and Diffraction* de Hammond (2015).
            """)
        with st.expander("📋 2. Visão Geral dos 17 Grupos Cristalográficos", expanded=False):
            st.markdown("""
            ### Visão Geral dos 17 Grupos Cristalográficos do Plano

            Os **grupos cristalográficos do plano** (também chamados *Wallpaper Groups*) constituem a classificação completa de todas as tesselações periódicas possíveis. Esta classificação segue a abordagem moderna apresentada por Conway, Burgiel e Goodman-Strauss em *The Symmetries of Things* (2008).

            Apesar da enorme variedade de padrões que observamos na arte, arquitetura e natureza, a Matemática demonstra que **existem apenas 17 tipos distintos de simetria** capazes de pavimentar o plano de forma periódica e regular. Esta limitação geométrica foi rigorosamente demonstrada por Grünbaum e Shephard em *Tilings and Patterns* (1987) e explorada por Holden em *Shapes, Space and Symmetry* (1991).

            ---

            ### Tabela dos 17 Grupos Cristalográficos

            A tabela seguinte apresenta os 17 grupos, organizados segundo as simetrias que os caracterizam:
            """)
            
            # Tabela em DataFrame (mais bonita no Streamlit)
            data = {
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
            st.dataframe(data, use_container_width=True, hide_index=True)

            st.markdown("""
            **Tabela 1:** Classificação dos 17 grupos cristalográficos do plano.

            ---

            Cada um destes grupos descreve um tipo único de organização periódica. Por exemplo, padrões com rotações de ordem 4 pertencem aos grupos **p4**, **p4m** ou **p4g**, enquanto padrões com simetria hexagonal surgem nos grupos **p6** e **p6m** — uma simetria frequentemente observada em estruturas naturais (Hammond, 2015).

            Na secção seguinte, analisamos em maior detalhe três destes grupos, destacando as suas características geométricas, exemplos e aplicações.
            """)
            
        with st.expander("🔍 3. Análise Detalhada dos 3 Grupos Cristalográficos", expanded=False):
            st.markdown("""
            ### Análise Detalhada dos 3 Grupos Cristalográficos

            Nesta secção analisamos em detalhe três grupos cristalográficos representativos: **p4**, **p6** e **pm**. 
            Estes grupos foram selecionados por apresentarem diferentes combinações de simetrias (rotações, reflexões e translações), 
            permitindo ilustrar a rica diversidade estrutural das tesselações periódicas do plano.
            """)

            # ====================== GRUPO p4 ======================
            st.markdown("#### 3.1 Grupo p4 (Simetria Quadrada)")
            st.markdown("""
            O grupo **p4** caracteriza-se pela presença de rotações de ordem 4, mas pela **ausência total de eixos de reflexão**. 
            Esta combinação torna-o único entre os grupos com simetria quadrada.
            """)
            
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown("""
                **Principais simetrias:**
                - Rotações de ordem 4 (90°, 180°, 270°)
                - Rotações de ordem 2
                - Translações ortogonais (rede quadrada)
                - **Não possui** reflexões nem reflexões deslizantes
                """)
            with col2:
                st.info("**Rede:** Quadrada  \n**Reflexões:** Ausentes")

            # ====================== GRUPO p6 ======================
            st.markdown("#### 3.2 Grupo p6 (Simetria Hexagonal)")
            st.markdown("""
            O grupo **p6** apresenta a mais elevada ordem de rotação entre todos os grupos cristalográficos. 
            Está fortemente associado a padrões naturais, como os favos de mel.
            """)
            
            col3, col4 = st.columns([2, 1])
            with col3:
                st.markdown("""
                **Principais simetrias:**
                - Rotações de ordem 6 (60°, 120°, 180°, 240°, 300°)
                - Rotações de ordem 3 e 2
                - Translações em rede hexagonal
                - **Não possui** reflexões
                """)
            with col4:
                st.success("**Rede:** Hexagonal  \n**Reflexões:** Ausentes")

            # ====================== GRUPO pm ======================
            st.markdown("#### 3.3 Grupo pm (Simetria Axial)")
            st.markdown("""
            O grupo **pm** é um dos exemplos mais simples de simetria com reflexões. 
            Caracteriza-se pela presença de eixos de reflexão paralelos.
            """)
            
            col5, col6 = st.columns([2, 1])
            with col5:
                st.markdown("""
                **Principais simetrias:**
                - Reflexões (eixos paralelos)
                - Translações perpendiculares aos eixos
                - **Não possui** rotações nem reflexões deslizantes
                """)
            with col6:
                st.warning("**Rede:** Retangular  \n**Reflexões:** Paralelas")

            # ====================== COMPARAÇÃO ======================
            st.markdown("#### 3.4 Comparação entre os 3 Grupos")
            
            comparison_data = {
                "Grupo": ["p4", "p6", "pm"],
                "Rotações": ["Ordem 4 e 2", "Ordem 6, 3 e 2", "Não"],
                "Reflexões": ["Não", "Não", "Sim (paralelas)"],
                "Rede de Translação": ["Quadrada", "Hexagonal", "Retangular"],
                "Simetria Dominante": ["Rotacional", "Rotacional forte", "Reflexão"]
            }
            
            st.dataframe(comparison_data, use_container_width=True, hide_index=True)
            
            st.markdown("""
            **Tabela 2:** Comparação entre os grupos cristalográficos p4, p6 e pm.

            Esta comparação evidencia como diferentes combinações de isometrias originam padrões geométricos visualmente distintos, 
            mesmo quando obedecem às mesmas restrições de repetição periódica.
            """)
            
            st.markdown("#### Explorador Interativo de Grupos")
            
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
elif page == "Lógica do Number Match":
    render_divider()
    render_module_header( "MÓDULO 3: LÓGICA DO NUMBER MATCH")
    
    tab1, tab2 = st.tabs(["💡 Teoria completa & Simulador", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("📖 Introdução ao Number Match", expanded=True):
            st.markdown("""
            ### Introdução ao Number Match

            O **Number Match** é um jogo de lógica e aritmética que ganhou grande popularidade em plataformas digitais, graças às suas regras simples e à dinâmica envolvente do tabuleiro.

            Apesar de aparentar baixa complexidade, o jogo pode ser analisado de forma rigorosa através de conceitos fundamentais da **Matemática Discreta**. As decisões do jogador dependem simultaneamente de:

            - **Condições lógicas**
            - **Propriedades aritméticas elementares** (igualdade, soma e paridade)

            que influenciam diretamente a evolução do jogo (Rosen, 2012).

            ---

            Estes conceitos não se manifestam apenas nas regras, mas sobretudo nas **dinâmicas do sistema**, à medida que o tabuleiro se transforma após cada jogada.

            A formalização das condições de jogada pode ser feita recorrendo à **lógica proposicional**, permitindo descrever de forma precisa quando uma jogada é válida. Esta abordagem baseia-se em ferramentas da lógica formal, adequadas à modelação de um sistema discreto finito (Boolos, Burgess & Jeffrey, 2007).

            Adicionalmente, o tabuleiro pode ser representado como um **grafo dinâmico**, no qual os números correspondem a vértices e as relações de jogada válida a arestas. Nesta perspetiva, o jogo torna-se um processo iterativo de remoção de vértices e arestas, cuja estrutura evolui ao longo do tempo — uma ideia amplamente explorada na Teoria de Grafos (West, 2001).

            ---

            **Objetivo deste módulo:** Analisar matematicamente o Number Match através de três pilares fundamentais:

            - **Lógica Proposicional**
            - **Teoria de Grafos**
            - **Combinatória**

            Esta abordagem demonstra como jogos do quotidiano podem constituir contextos ricos para a compreensão de conceitos matemáticos essenciais, utilizando modelos baseados em relações, grafos e argumentos de contagem.
            """)
        with st.expander("📘 1. Formalização Lógica do Jogo", expanded=False):
            st.markdown("""
            ### Formalização Lógica do Jogo

            A **lógica proposicional** constitui uma ferramenta poderosa para descrever formalmente sistemas baseados em regras bem definidas, como é o caso do Number Match.

            No Number Match, uma jogada válida ocorre quando dois números \(a\) e \(b\) satisfazem simultaneamente uma **condição numérica** e uma **condição estrutural de acessibilidade**.
            """)

            st.latex(r"""
            \text{JogadaVálida}(a, b) \iff (a = b \lor a + b = 10) \land \text{Conectados}(a, b)
            """)

            st.markdown("""
            Esta expressão representa uma **fórmula booleana composta**, na qual as condições aritméticas e estruturais são combinadas através dos conectivos lógicos usuais.

            **Condições Numéricas:**
            - \(a = b\) (os dois números são iguais)
            - \(a + b = 10\) (relação aritmética complementar)

            Estas condições podem ser interpretadas como predicados lógicos simples. Além disso, a jogada só é permitida se os dois números estiverem **conectados** no tabuleiro segundo as regras do jogo.

            ---

            #### Exemplo Prático
            Se existirem dois números adjacentes com valores **3 e 7**, a condição \(a + b = 10\) é satisfeita. Caso estejam conectados, a jogada é válida. No entanto, se duas ocorrências do número **5** não estiverem conectadas, a jogada é inválida apesar da condição aritmética ser cumprida.
            """)

            # === SIMULADOR INTERATIVO (mantido e melhorado) ===
            st.markdown("#### 🕹️ Simulador de Validação Lógica")

            col1, col2, col3 = st.columns(3)
            with col1:
                s_a = st.number_input("Valor da Carta A", 1, 9, 5, key="s_a_logic")
            with col2:
                s_b = st.number_input("Valor da Carta B", 1, 9, 5, key="s_b_logic")
            with col3:
                s_con = st.checkbox("Conectados / Adjacentes?", value=True, key="s_con_logic")

            c_num = (s_a == s_b) or (s_a + s_b == 10)
            c_valida = c_num and s_con

            if c_valida:
                st.success(f"🟩 **JOGADA VÁLIDA!** O par ({s_a}, {s_b}) cumpre todas as condições e pode ser eliminado.")
            else:
                reasons = []
                if not c_num:
                    reasons.append(f"Os valores não são iguais nem somam 10 ({s_a} + {s_b} = {s_a + s_b})")
                if not s_con:
                    reasons.append("As cartas não estão conectadas")
                st.error(f"🟥 **JOGADA INVÁLIDA!** Razões: {'; '.join(reasons)}")
                
        with st.expander("📊 2. Modelação em Teoria de Grafos", expanded=False):
            st.markdown("""
            ### Modelação em Teoria de Grafos

            O tabuleiro do Number Match pode ser representado como um **grafo dinâmico não dirigido**:

            - **Vértices** → Cada número no tabuleiro
            - **Arestas** → Cada par de números que pode ser eliminado (jogada válida)

            Esta modelação permite analisar como o tabuleiro evolui ao longo do tempo através da remoção sucessiva de vértices e arestas.
            """)

            st.markdown("**Elemento Crítico:**")
            st.info("**Vértices de grau zero** (números isolados) bloqueiam o progresso do jogo.")
            
            st.markdown("""
            A Teoria de Grafos revela-se assim uma ferramenta extremamente eficaz para compreender as dinâmicas do jogo, prever bloqueios e desenvolver estratégias mais eficazes.
            """)
        with st.expander("🔢 3. Análise Combinatória", expanded=False):
            st.markdown("""
            ### Análise Combinatória

            A **combinatória** desempenha um papel central na análise do Number Match, permitindo estudar a existência e a quantidade de pares elimináveis, bem como prever situações de bloqueio no tabuleiro.

            As técnicas combinatórias baseiam-se em princípios de contagem, análise de frequências e argumentos de paridade, sendo particularmente adequadas ao estudo de sistemas discretos finitos como este jogo (Grimaldi, 2004).
            """)

            st.markdown("""
            #### 1. Pares por Igualdade

            Se um número aparece exatamente **2k** vezes no tabuleiro, é possível formar **k pares** válidos por igualdade. 

            Por outro lado, se um número aparece um **número ímpar** de vezes, pelo menos um exemplar ficará necessariamente isolado. Este é um resultado direto do princípio da paridade e constitui uma das principais causas de bloqueio no jogo (Stanley, 2011).
            """)

            st.markdown("""
            #### 2. Pares por Soma 10

            Cada número entre 1 e 9 possui exatamente um parceiro que permite obter a soma 10:

            - 1 ↔ 9
            - 2 ↔ 8
            - 3 ↔ 7
            - 4 ↔ 6
            - **5 ↔ 5** (caso especial)

            O número **5** é particularmente crítico: a sua frequência no tabuleiro deve ser **par** para permitir a eliminação completa. Caso contrário, sobrará pelo menos um 5 isolado.
            """)

            st.markdown("""
            #### 3. Distribuição dos Números e Probabilidade de Jogadas Válidas

            A probabilidade de existirem jogadas válidas depende fortemente da **distribuição dos números**. 

            Distribuições desiguais (em que certos números aparecem com frequência muito superior a outros) reduzem o número de emparelhamentos possíveis. Números raros tendem a ficar isolados mais facilmente, aumentando o risco de bloqueio do tabuleiro.

            Assim, argumentos combinatórios baseados em contagem, paridade e distribuição explicam matematicamente as dificuldades enfrentadas pelo jogador em determinadas configurações do jogo.
            """)

            # Imagem (se tiveres)
            # st.image("caminho/para/figura2.jpg", caption="Figura 2: Distribuições desiguais que impossibilitam combinações", use_container_width=True)
        with st.expander("🎯 4. Estratégia Matemática", expanded=False):
            st.markdown("""
            ### Estratégia Matemática

            A análise matemática permite não apenas compreender o jogo, mas desenvolver **estratégias racionais** que aumentam significativamente a probabilidade de sucesso.
            """)

            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **1. Minimizar números isolados**  
                Evitar criar vértices de grau zero no grafo.

                **2. Eliminar números raros**  
                Priorizar números com baixa frequência.
                """)
            
            with col2:
                st.markdown("""
                **3. Controlar a expansão**  
                Gerir com cuidado o crescimento do tabuleiro.

                **4. Tratar o 5 com cuidado**  
                Manter a quantidade de 5s sempre par.
                """)
    
        import streamlit as st
        import random
        from collections import deque

        with st.expander("🎮 Number Match (Jogo Interativo)", expanded=False):

            st.markdown("""
            ### Regras do Jogo

            Seleciona dois números que:

            - sejam **iguais** ou cuja **soma seja 10**
            - estejam ligados por um **caminho livre** seja em linha, coluna ou diagonal
        
            Por isso, jogadas que parecem diagonais podem funcionar!
            """)

            COLS = 9
            SIZE = 45

            # -------- ESTADO --------
            if "grid" not in st.session_state:
                st.session_state.grid = [random.randint(1, 9) for _ in range(SIZE)]

            if "selected" not in st.session_state:
                st.session_state.selected = []

            if "msg" not in st.session_state:
                st.session_state.msg = ""

            grid = st.session_state.grid

            # -------- FUNÇÃO CAMINHO (BFS COMPLETO) --------
            def valid_move(i, j, grid, cols):

                if i == j:
                    return False

                a, b = grid[i], grid[j]

                if a is None or b is None:
                    return False

                if not (a == b or a + b == 10):
                    return False

                rows = len(grid) // cols

                visited = {i}
                queue = deque([i])

                while queue:
                    current = queue.popleft()

                    if current == j:
                        return True

                    r, c = divmod(current, cols)

                    neighbors = []

# ortogonais
                    if r > 0:
                        neighbors.append((r-1)*cols + c)
                    if r < rows - 1:
                        neighbors.append((r+1)*cols + c)
                    if c > 0:
                        neighbors.append(r*cols + (c-1))
                    if c < cols - 1:
                        neighbors.append(r*cols + (c+1))

                    # diagonais
                    if r > 0 and c > 0:
                        neighbors.append((r-1)*cols + (c-1))
                    if r > 0 and c < cols - 1:
                        neighbors.append((r-1)*cols + (c+1))
                    if r < rows - 1 and c > 0:
                        neighbors.append((r+1)*cols + (c-1))
                    if r < rows - 1 and c < cols - 1:
                        neighbors.append((r+1)*cols + (c+1))

                    for n in neighbors:
                        if n in visited:
                            continue

                        if grid[n] is None or n == j:
                            visited.add(n)
                            queue.append(n)

                return False

            # -------- LÓGICA --------
            def select_number(idx):

                if idx in st.session_state.selected:
                    return

                st.session_state.selected.append(idx)

                if len(st.session_state.selected) == 2:
                    i, j = st.session_state.selected

                    if valid_move(i, j, grid, COLS):
                        grid[i] = None
                        grid[j] = None
                        st.session_state.msg = "✅ Jogada válida!"
                    else:
                        st.session_state.msg = "❌ Estes números não podem ser combinados."

                    st.session_state.selected = []
                    st.rerun()

            # -------- ESTILO (SÓ GRELHA) --------
            st.markdown("""
            <style>
            .grid-button button {
                width: 55px !important;
                height: 55px !important;
                font-size: 20px !important;
                border-radius: 12px !important;
                background: linear-gradient(135deg, #667eea, #764ba2) !important;
                color: white !important;
                border: none !important;
                font-weight: bold !important;
            }

            .grid-button button:hover {
                outline: 3px solid #00f2fe !important;
            }
            </style>
            """, unsafe_allow_html=True)

            # -------- GRELHA --------
            rows = SIZE // COLS

            for r in range(rows):
                cols = st.columns(COLS)

                for c in range(COLS):
                    idx = r * COLS + c

                    if idx >= len(grid):
                        continue

                    val = grid[idx]

                    with cols [c]:
                        if val is None:
                            st.markdown("<div style='height:55px'></div>", unsafe_allow_html=True)
                        else:
                            st.markdown('<div class="grid-button">', unsafe_allow_html=True)
                            if st.button(str(val), key=f"grid_{idx}"):
                                select_number(idx)
                            st.markdown("</div>", unsafe_allow_html=True)

            # -------- MENSAGEM --------
            if st.session_state.msg:
                if "❌" in st.session_state.msg:
                    st.warning(st.session_state.msg)
                else:
                    st.success(st.session_state.msg)

            # -------- BOTÃO REINICIAR --------
            if st.button("🔄 Reiniciar"):
                st.session_state.grid = [random.randint(1, 9) for _ in range(SIZE)]
                st.session_state.selected = []
                st.session_state.msg = ""
                st.rerun()




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
elif page == "Padrões dos Primos":
    render_divider()
    render_module_header("MÓDULO 4: PADRÕES DOS PRIMOS: DA ESPIRAL Á TOTIENTE")
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        import streamlit as st

    with st.expander("🔢 Introdução", expanded=True):

        st.markdown("""
        #### Distribuição dos Números e Probabilidade de Jogadas Válidas

        A probabilidade de existirem jogadas válidas depende fortemente da **distribuição dos números**. 

        Distribuições desiguais (em que certos números aparecem com frequência muito superior a outros) reduzem o número de emparelhamentos possíveis. Números raros tendem a ficar isolados mais facilmente, aumentando o risco de bloqueio do tabuleiro.

        Assim, argumentos combinatórios baseados em contagem, paridade e distribuição explicam matematicamente as dificuldades enfrentadas pelo jogador em determinadas configurações do jogo.
        """)

        st.markdown("---")

        st.markdown("""
        ### Contexto Teórico: Teoria dos Números

        A **Teoria dos Números** é um dos ramos mais antigos e fascinantes da matemática. Apesar de lidar com objetos aparentemente simples, os números inteiros, revela estruturas profundas e padrões inesperados.

        Esta ideia é destacada por **G. H. Hardy** na sua obra *A Mathematician’s Apology* (1940), onde defende que a matemática pura possui uma beleza intrínseca, comparável à arte, precisamente porque revela ordem onde antes se supunha irregularidade.

        Hardy, um dos maiores teóricos dos números do século XX, via nesta área um exemplo perfeito de como estruturas elegantes podem emergir de objetos aparentemente elementares.

        A distribuição dos números primos, irregular à primeira vista mas repleta de padrões subtis, é um dos casos mais emblemáticos dessa visão.
        """)

        st.markdown("""
        #### Objetivos deste estudo

        Este trabalho explora dois eixos fundamentais onde esses padrões se tornam visíveis:

        - A **distribuição dos números primos**, analisada através da **Espiral de Ulam**, uma representação visual que revela alinhamentos surpreendentes.  
        - A **função totiente de Euler**, que descreve a estrutura multiplicativa modular dos inteiros e evidencia regularidades aritméticas.

        O objetivo é mostrar que, mesmo em contextos onde a aleatoriedade parece dominar, surgem padrões que revelam a profundidade estrutural dos números.
        """)

    with st.expander("🌀 1. A Espiral de Ulam e Padrões Inesperados", expanded=False):

        st.markdown("""
        ### 1. Números Primos e a sua Natureza

        Os **números primos** são fundamentais na aritmética. O Teorema Fundamental da Aritmética estabelece que qualquer número inteiro positivo pode ser decomposto de forma **única** num produto de primos.

        Apesar desta importância estrutural, a sua distribuição é **aparentemente irregular**. 

        Este comportamento cria um contraste fascinante:
        - **Aleatoriedade aparente** na distribuição dos primos  
        - **Determinismo** em certas expressões algébricas que os geram  

        Este contraste está no centro da investigação matemática há séculos.
        """)

        st.markdown("""
        ### 2. A Espiral de Ulam

        Em 1963, **Stanislaw Ulam** representou os números naturais numa espiral quadrada:

        - 1 no centro  
        - Crescimento em espiral (sentido horário)  
        - Primos destacados  

        Resultado surpreendente:

        Os números primos alinham-se em **diagonais longas e bem definidas**.
        """)
        st.markdown("---")

        st.markdown("### Visualização Interativa: Espiral de Ulam")

        st.markdown("""
        Move o slider para ver como os **números primos se organizam em padrões diagonais**.
        """)
        # Função primo
        import streamlit as st
        import matplotlib.pyplot as plt
        import numpy as np

        # -------- Primo --------
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        # -------- Espiral fixa --------
        MAX_GLOBAL = 1000

        def ulam_spiral_full(n):
            size = int(np.ceil(np.sqrt(n)))
            if size % 2 == 0:
                size += 1

            grid = np.zeros((size, size), dtype=int)

            x = y = size // 2
            dx, dy = 1, 0
            steps = 1
            num = 1

            while num <= n:
                for _ in range(2):
                    for _ in range(steps):
                        if num <= n:
                            grid[y][x] = num
                            num += 1
                        x += dx
                        y += dy
                    dx, dy = -dy, dx
                steps += 1

            return grid

        # -------- gerar espiral fixa --------
        grid = ulam_spiral_full(MAX_GLOBAL)
        size = grid.shape[0]

        # -------- UI --------
        st.markdown("### Espiral de Ulam")

        n_max = st.slider("Quantidade de números:", 10, MAX_GLOBAL, 200)

        # -------- fundo (igual ao teu) --------
        Y, X = np.ogrid[:size, :size]
        center = size // 2
        dist = np.sqrt((X - center)**2 + (Y - center)**2)

        fig, ax = plt.subplots(figsize=(7, 7))
        fig.patch.set_facecolor('#0f0f23')
        ax.set_facecolor('#0f0f23')

        # fundo colorido bonito
        ax.imshow(dist, cmap='magma', alpha=0.6)

        # -------- agora números em vez de bolinhas --------
        for i in range(size):
            for j in range(size):
                num = grid[i, j]

                if num <= n_max and is_prime(num):
                    ax.text(
                        j, i, str(num),
                        color='#ffffff',   # texto branco forte (melhor contraste)
                        fontsize=6,
                        ha='center',
                        va='center',
                        fontweight='bold'
                    )

        # título
        ax.set_title("Espiral de Ulam (números primos)", color='white')
        ax.axis('off')

        st.pyplot(fig)




        st.markdown("---")

        st.markdown("""
        ### 3. Interpretação Matemática

        As diagonais da espiral estão associadas a **polinómios quadráticos** do tipo:
        """)

        st.latex(r"an^2 + bn + c")

        st.markdown("""
        Algumas destas expressões geram muitos números primos consecutivos.

        O exemplo mais famoso é o polinómio de Euler:
        """)

        st.latex(r"P(n) = n^2 + n + 41")

        st.markdown("""
        Este polinómio produz números primos para todos os inteiros de:

        **n = 0 até n = 39**
        """)

        st.markdown("""
        #### Interpretação

        - Cada diagonal corresponde a uma expressão matemática  
        - Algumas geram muitos primos → **diagonais densas**  
        - Outras geram poucos → **diagonais vazias**

        A espiral não cria primos — apenas revela padrões escondidos.
        """)

        st.markdown("---")

        st.markdown("### Laboratório Interativo: Gerador de Primos de Euler")

        n_slider = st.slider(
            "Altere o valor de n para testar o polinómio:",
            0, 50, 0,  # aumentei para veres quando deixa de ser primo
            key="euler_slider"
        )

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

        st.info("""
        Observação: O polinómio gera primos até n = 39. 
        A partir daí, começam a surgir números compostos — mostrando os limites destas expressões.
        """)
            

    with st.expander("φ 2. A Função Totiente de Euler", expanded=False):

        st.markdown("""
        ### 1. Definição e Significado

        A função totiente $$\\varphi(n)$$, introduzida por Euler, conta quantos números naturais até $$n$$ 
        são **coprimos** com $$n$$, ou seja:
        """)

        st.latex(r"gcd(a,n) = 1")

        st.markdown("""
        Esta função revela a **estrutura multiplicativa dos inteiros** e depende diretamente dos 
        fatores primos de $$n$$.

        #### Exemplo

        Para $$n = 12$$, os coprimos são: 1, 5, 7, 11
        """)

        st.latex(r"\varphi(12) = 4")

        st.markdown("---")

        st.markdown("""
        ### 2. Propriedades Fundamentais

        | Propriedade | Fórmula |
        |-------------|---------|
        | Primo $$p$$ | $$\\varphi(p) = p - 1$$ |
        | Potência de primo | $$\\varphi(p^k) = p^k - p^{k-1}$$ |
        | Multiplicatividade | $$\\varphi(ab) = \\varphi(a)\\varphi(b), \\; gcd(a,b)=1$$ |
        """)

        st.markdown("""
        #### Interpretação

        - Números primos → valor máximo  
        - Muitos fatores primos → valor baixo  
        - Potências de primos → valores relativamente altos  
        """)

        st.markdown("---")

        st.markdown("""
        ### 3. Fórmula Multiplicativa Geral

        Se:
        """)

        st.latex(r"n = p_1^{a_1} p_2^{a_2} \dots p_k^{a_k}")

        st.markdown("então:")

        st.latex(r"\varphi(n) = n \prod_{i=1}^{k} \left(1 - \frac{1}{p_i}\right)")

        st.markdown("""
        O valor de $$\\varphi(n)$$ depende apenas dos **fatores primos** de $$n$$.
        """)

        st.markdown("---")

        st.markdown("### 4. Visualização da Função Totiente")

        n_max = st.slider("Escolhe o intervalo:", 10, 200, 100)

        def phi(n):
            count = 0
            for k in range(1, n + 1):
                if math.gcd(n, k) == 1:
                    count += 1
            return count

        x = list(range(1, n_max + 1))
        y = [phi(i) for i in x]

        fig, ax = plt.subplots()
        ax.scatter(x, y, s=10)
        ax.set_title("Função Totiente φ(n)")
        ax.set_xlabel("n")
        ax.set_ylabel("φ(n)")

        st.pyplot(fig)

        st.markdown("""
        #### Observações

        - Primos formam a "linha superior"  
        - Estrutura irregular → depende da fatorização  
        - Sem periodicidade  
        """)

        st.markdown("---")

        st.markdown("### 5. Calculadora do Totiente")

        num_input = st.number_input(
            "Introduz um valor:",
            min_value=2,
            max_value=500,
            value=12
        )

        def phi_fast(n):
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

        phi_result = phi_fast(num_input)
        st.metric(f"φ({num_input})", phi_result)

        st.markdown("---")

        st.markdown("""
        ### 6. Aplicação: Criptografia RSA

        A função totiente é essencial no algoritmo **RSA**.

        #### Ideia base:

        - Escolhem-se primos grandes $$p$$ e $$q$$  
        - Calcula-se $$n = pq$$  
        - $$\\varphi(n) = (p-1)(q-1)$$  

        A segurança depende da dificuldade de fatorizar $$n$$.

        Sem conhecer os fatores primos, calcular $$\\varphi(n)$$ é extremamente difícil.
        """)
        

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
elif page == "Padrões Numéricos":
    render_divider()
    render_module_header( "MÓDULO 5: PADRÕES NUMÉRICOS E ESTRUTURAS ARITMÉTICAS: DOS TRIÂNGULARES A FERMAT")
    
    tab1, tab2 = st.tabs(["📖 Matéria Completa & Gráficos", "🧠 Quiz Geral do Módulo"])
    
    with tab1:
        with st.expander("📖 Introdução à Teoria dos Números", expanded=True):

            st.markdown("""
            ### Introdução

            A **Teoria dos Números** é uma das áreas mais antigas da Matemática, tendo como principal objetivo o estudo dos números inteiros e a identificação das suas propriedades e regularidades.

            Desde a Antiguidade, o ser humano procura encontrar **ordem no comportamento dos números**, estabelecendo ligações entre a aritmética abstrata e representações mais visuais, como a geometria.

            ---

            ### Objetivo do Trabalho

            Neste trabalho, exploram-se diferentes **padrões numéricos** e estruturas fundamentais:

            #### Números Figurados
            Começamos pelos **números triangulares**, onde a geometria permite visualizar somas aritméticas através de pontos organizados.

            #### Números Perfeitos
            De seguida, analisam-se os **números perfeitos**, que representam uma forma de equilíbrio matemático, sendo iguais à soma dos seus divisores próprios.

            #### O Número 9 na Base Decimal
            Explora-se também o comportamento do número **9**, evidenciando simetrias e padrões que resultam do sistema de numeração decimal.

            #### Último Teorema de Fermat
            Por fim, estuda-se o **Último Teorema de Fermat**, destacando o contraste entre:

            - O caso do expoente 2 → com infinitas soluções (triplas pitagóricas)  
            - O caso de expoentes superiores a 2 → sem soluções inteiras  

            ---

            ### Ideia Central

            O objetivo global é mostrar que, mesmo quando os números parecem comportar-se de forma irregular, existem **padrões profundos e estruturas matemáticas** que revelam ordem e beleza.

            A Teoria dos Números permite assim transformar o aparente caos em **compreensão estruturada**.
            """)

        with st.expander("📐 1. Números Triangulares e Contagem Geométrica", expanded=False):

            st.markdown("""
            ### Explicação Teórica

            Os **números triangulares** pertencem ao grupo dos chamados **números figurados**, que se caracterizam por serem números que podem ser representados através de arranjos geométricos de pontos regulares.

            Esta abordagem visual é extremamente importante, pois transforma problemas abstratos de contagem numa perceção geométrica intuitiva.

            No caso dos números triangulares, eles representam a quantidade de pontos necessária para construir um **triângulo equilátero** com um determinado número de linhas.
            """)

            st.latex(r"T_n = 1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2}")

            st.markdown("""
            ---
            ### Demonstração (Gauss)
            
            A fórmula pode ser obtida somando a sequência na ordem direta e inversa, formando pares com valor **n + 1**:
            """)

            st.latex(r"2T_n = n(n+1)")

            st.latex(r"T_n = \frac{n(n+1)}{2}")

            st.markdown("---")

            st.markdown("""
            ### Representação Geométrica
            """)

            st.image("Números_triangulares.png", use_container_width=True)
            st.caption("Figura 1: Representação geométrica dos primeiros 6 números triangulares")

            st.markdown("""
            Nesta representação observam-se os primeiros valores da sequência:

            - T₁ = 1  
            - T₂ = 3  
            - T₃ = 6  
            - T₄ = 10  
            - T₅ = 15  
            - T₆ = 21  

            Cada novo nível adiciona mais pontos, formando um triângulo crescente.
            """)

            st.markdown("---")

            st.markdown("""
            ### Exemplo Prático

            Para calcular o quarto número triangular:
            """)

            st.latex(r"T_4 = \frac{4(4+1)}{2} = \frac{20}{2} = 10")

            st.markdown("""
            ✔ Isto coincide com:
            
            **1 + 2 + 3 + 4 = 10**
            """)

            st.markdown("---")

            st.markdown("""
            ### Aplicações

            Um exemplo clássico é o problema dos **apertos de mão**.

            Se 6 pessoas se cumprimentarem todas uma vez:
            """)

            st.latex(r"T_5 = \frac{5 \cdot 6}{2} = 15")

            st.markdown("""
            Aplica-se a redes, ligações e contagens de pares únicos.

            ---
            **Ideia-chave:**  
            Os números triangulares mostram como a matemática pode ser simultaneamente 
            **visual e algébrica**, revelando padrões de crescimento simples mas profundos.
            """)


        with st.expander("✨ 2. Números Perfeitos e Harmonia de Divisores", expanded=False):

            st.markdown("""
            ### Definição e Significado

            Um **número perfeito** é um número inteiro positivo que é exatamente igual à soma dos seus 
            **divisores próprios**, ou seja, todos os divisores menores do que ele.

            Esta definição remonta aos *Elementos de Euclides*, refletindo o interesse dos matemáticos 
            da Antiguidade por números que exibem **equilíbrio e harmonia aritmética**.
            """)

            st.markdown("---")

            st.markdown("""
            ### Exemplos Clássicos

            | Número | Divisores Próprios | Soma |
            |--------|-------------------|------|
            | **6**  | 1, 2, 3           | 1 + 2 + 3 = **6** ✓ |
            | **28** | 1, 2, 4, 7, 14    | 1 + 2 + 4 + 7 + 14 = **28** ✓ |

            Em ambos os casos, a soma dos divisores próprios é exatamente igual ao número original.
            """)

            st.markdown("---")

            st.markdown("""
            ### Relação com Primos de Mersenne

            Os números perfeitos pares estão diretamente ligados aos chamados **Primos de Mersenne**, 
            que têm a forma:
            """)

            st.latex(r"2^p - 1")

            st.markdown("""
            Euclides demonstrou que, sempre que $$2^p - 1$$ é primo, então podemos gerar um número perfeito 
            através da fórmula:
            """)

            st.latex(r"n = 2^{p-1}(2^p - 1)")

            st.markdown("""
            #### Exemplos

            - Para **p = 3**:
            """)

            st.latex(r"n = 2^{2}(2^3 - 1) = 4 \times 7 = 28")

            st.markdown("""
            - Para **p = 5**:
            """)

            st.latex(r"n = 2^{4}(2^5 - 1) = 16 \times 31 = 496")

            st.markdown("""
            Esta construção gera **todos os números perfeitos pares conhecidos**.
            """)

            st.markdown("---")

            st.markdown("""
            ### Formulação com a Função σ(n)

            A definição também pode ser expressa recorrendo à função soma dos divisores:

            """)

            st.latex(r"\sigma(n) = \text{soma de todos os divisores de } n")

            st.markdown("Um número é perfeito se:")

            st.latex(r"\sigma(n) = 2n")

            st.markdown("""
            #### Exemplo:

            Para n = 6:

            - Divisores: 1, 2, 3, 6  
            - Soma:
            """)

            st.latex(r"\sigma(6) = 12 = 2 \times 6")

            st.markdown("---")

            st.markdown("""
            ### Ligação aos Números Triangulares

            Um facto surpreendente é que **todos os números perfeitos pares conhecidos são também números triangulares**.

            #### Exemplo:
            """)

            st.latex(r"T_7 = \frac{7 \times 8}{2} = 28")

            st.markdown("""
            Isto mostra uma ligação profunda entre diferentes áreas da Teoria dos Números.
            """)

            st.markdown("---")

            st.markdown("""
            ### Problema em Aberto

            Permanece uma grande questão na matemática:

            **Existem números perfeitos ímpares?**

            Até hoje:
            - Nenhum foi encontrado  
            - Nenhuma prova mostra que não existe  

            Estudos indicam que, a existir, um número perfeito ímpar teria de:
            - Ser extremamente grande  
            - Ter uma estrutura muito complexa de divisores  

            Este continua a ser um dos problemas clássicos ainda em aberto.
            """)

            st.markdown("""
            ---
            **Ideia-chave:**  
            Os números perfeitos representam um raro exemplo de **equilíbrio absoluto na aritmética**, 
            ligando divisores, primos e até estruturas geométricas como os números triangulares.
            """)

            
        with st.expander("9️⃣ 3. Exploração do Número 9 na Base Decimal", expanded=False):

            st.markdown("""
            ### Explicação Teórica

            O número **9** ocupa um lugar de destaque na aritmética devido à estrutura do sistema de numeração **decimal (base 10)**.

            Como $$9 = 10 - 1$$, surgem padrões matemáticos extremamente regulares, incluindo:
            
            - Simetrias numéricas  
            - Regras simples de divisibilidade  
            - Padrões visuais previsíveis  

            ---

            ### Propriedade Modular

            Qualquer número inteiro positivo é sempre **congruente com a soma dos seus dígitos módulo 9**:
            """)

            st.latex(r"n \equiv \text{soma dos dígitos de } n \pmod{9}")

            st.markdown("""
            Esta propriedade está na base do **critério de divisibilidade por 9**.

            #### Exemplos

            - Para **432**:
            """)

            st.latex(r"4 + 3 + 2 = 9")

            st.markdown("""
            Como 9 é múltiplo de 9, então 432 também é.

            - Para **981**:
            """)

            st.latex(r"9 + 8 + 1 = 18 \rightarrow 1 + 8 = 9")

            st.markdown("""
            Qualquer múltiplo de 9 acaba por “colapsar” no valor 9 através da soma repetida dos dígitos.
            """)

            st.markdown("---")

            st.markdown("""
            ### Simetria na Tabuada do 9

            A tabuada do 9 apresenta uma estrutura de **espelho numérico**:

            - $$9 \\times 2 = 18$$ ↔ $$9 \\times 9 = 81$$  
            - $$9 \\times 3 = 27$$ ↔ $$9 \\times 8 = 72$$  
            - $$9 \\times 4 = 36$$ ↔ $$9 \\times 7 = 63$$  

            Em todos os casos, a **soma dos dígitos é sempre 9**.

            Isto reflete a complementaridade entre dezenas e unidades no sistema decimal.
            """)

            st.markdown("---")

            st.markdown("""
            ### Potências de 9 e Estrutura Algébrica

            O comportamento do número 9 também se explica pela identidade:

            """)

            st.latex(r"9^n = (10 - 1)^n")

            st.markdown("""
            Ao expandir esta expressão (Binómio de Newton), observa-se que quase todos os termos são múltiplos de 10.

            Isso explica os padrões nas potências de 9.

            #### Exemplos:

            - $$9^1 = 9$$  
            - $$9^2 = 81$$ → soma = 9  
            - $$9^3 = 729$$ → soma = 7+2+9 = 18 → 9  
            - $$9^4 = 6561$$ → soma = 18 → 9  

            As potências de 9 exibem um comportamento cíclico na soma dos dígitos.
            """)

            st.markdown("---")

            st.markdown("### Laboratório de Redução Digital")

            num_9_input = st.text_input(
                "Introduz um número inteiro:",
                value="432",
                key="num_9_input"
            )

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

            st.markdown("""
            ---
            **Ideia-chave:**  
            O número 9 revela como a estrutura da base 10 cria padrões previsíveis, transformando 
            operações aritméticas em comportamentos visuais e regulares.
            """)
            
        with st.expander("∞ 4. O Último Teorema de Fermat", expanded=False):

            st.markdown("""
            ### Introdução e Enquadramento

            O **Último Teorema de Fermat** constitui um dos resultados mais emblemáticos da Teoria dos Números, 
            pois ilustra como pequenas alterações numa expressão matemática podem fazer desaparecer um padrão 
            inteiro de soluções.

            ---

            ### Caso Clássico: n = 2

            Para $$n = 2$$, obtemos a equação de Pitágoras:
            """)

            st.latex(r"a^2 + b^2 = c^2")

            st.markdown("""
            Esta equação admite **infinitas soluções inteiras positivas**, conhecidas como 
            **triplas pitagóricas**.

            #### Exemplo clássico:
            """)

            st.latex(r"3^2 + 4^2 = 9 + 16 = 25 = 5^2")

            st.markdown("""
            ### Representação Geométrica
            """)

            st.image("triangulo.png", use_container_width=True)
            st.caption("Figura 2: Representação geométrica do caso clássico n = 2")

            st.markdown("""
            Este triângulo retângulo ilustra visualmente a relação entre os três lados, mostrando como 
            a soma dos quadrados dos catetos corresponde ao quadrado da hipotenusa.

            Estas soluções podem ser geradas pelas **fórmulas de Euclides**:
            """)

            st.latex(r"a = m^2 - n^2,\quad b = 2mn,\quad c = m^2 + n^2")

            st.markdown("""
            Este caso representa um sistema com estrutura regular e infinitas soluções.

            ---

            ### Mudança Radical: n > 2

            Fermat afirmou que a equação geral:
            """)

            st.latex(r"a^n + b^n = c^n")

            st.markdown("""
            **não admite soluções inteiras não triviais para qualquer valor de $$n > 2$$.**

            Ou seja:
            - Para $$n = 2$$ → infinitas soluções  
            - Para $$n > 2$$ → nenhuma solução  

            Esta mudança mostra um contraste profundo na estrutura dos números.

            ---

            ### História e Demonstração

            No século XVII, **Pierre de Fermat** escreveu que tinha uma demonstração 
            "verdadeiramente maravilhosa", mas nunca a registou.

            Durante mais de **350 anos**, o problema permaneceu em aberto:

            - **Euler** → resolveu o caso $$n = 3$$  
            - **Sophie Germain** → contribuições importantes  
            - **Kummer** → avanços significativos  

            A prova final foi alcançada por **Andrew Wiles (1994/1995)**, usando:

            - Curvas elípticas  
            - Formas modulares  

            ---

            ### Interpretação Matemática

            Este teorema mostra que:

            - Pequenas alterações podem mudar completamente o comportamento  
            - Padrões matemáticos têm limites inesperados  
            - O simples pode esconder enorme profundidade  

            Passamos de infinitas soluções para nenhuma apenas alterando o expoente.
            """)

            if GRAFICOS_ATIVOS:
                st.markdown("#### Comparação Gráfica")

                import numpy as np
                import matplotlib.pyplot as plt

                n_input_txt = st.text_input(
                    "Expoente n (> 2):",
                    value="3.0",
                    key="fermat_n"
                )

                try:
                    n_fermat = float(n_input_txt)
                    if n_fermat <= 2:
                        st.warning("Introduz n > 2.")
                        n_fermat = 3.0
                except ValueError:
                    st.error("Valor inválido.")
                    n_fermat = 3.0

                a = np.linspace(0.01, 5, 400)
                b = np.linspace(0.01, 5, 400)
                A, B = np.meshgrid(a, b)

                fig, ax = plt.subplots(figsize=(6, 6))
                fig.patch.set_facecolor('#0f0f23')
                ax.set_facecolor('#0f0f23')

                ax.contour(A, B, A**2 + B**2, levels=[25], colors=['#4facfe'], linewidths=2.5)
                ax.contour(A, B, A**n_fermat + B**n_fermat, levels=[25], colors=['#f093fb'], linestyles='--')

                ax.scatter([3], [4], color='#00f2fe', s=100)
                ax.annotate("(3,4)", (3, 4), color='white')

                ax.set_xlabel("a", color='white')
                ax.set_ylabel("b", color='white')
                ax.tick_params(colors='white')
                ax.grid(alpha=0.2)

                st.pyplot(fig)

            st.markdown("""
            ---
            **Ideia-chave:**  
            O Último Teorema de Fermat revela que nem todos os padrões matemáticos são contínuos: 
            alguns têm limites absolutos que só se tornam visíveis quando se altera ligeiramente a estrutura.
            """)


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
