"""
Módulo para estilos CSS customizados do dashboard
"""

import streamlit as st


def aplicar_estilos_profissionais():
    """Aplica estilos CSS profissionais ao dashboard."""
    st.markdown("""
    <style>
    /* Variáveis de cor */
    :root {
        --primary-color: #003d82;
        --secondary-color: #0066cc;
        --accent-color: #00a8e8;
        --success-color: #27ae60;
        --warning-color: #f39c12;
        --danger-color: #e74c3c;
        --light-gray: #f5f7fa;
        --dark-gray: #2c3e50;
        --border-color: #e0e6ed;
    }
    
    /* Remover elementos infantis */
    .stApp {
        background-color: #ffffff;
    }
    
    /* Sidebar profissional */
    [data-testid="stSidebar"] {
        background-color: var(--primary-color);
        color: white;
    }
    
    [data-testid="stSidebar"] .stRadio > label {
        color: white;
        font-weight: 500;
        font-size: 14px;
    }
    
    [data-testid="stSidebar"] .stRadio > div {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 12px;
    }
    
    /* Títulos profissionais */
    h1 {
        color: var(--primary-color);
        font-weight: 700;
        font-size: 32px;
        margin-bottom: 8px;
    }
    
    h2 {
        color: var(--primary-color);
        font-weight: 600;
        font-size: 24px;
        margin-top: 24px;
        margin-bottom: 16px;
        border-bottom: 3px solid var(--accent-color);
        padding-bottom: 8px;
    }
    
    h3 {
        color: var(--dark-gray);
        font-weight: 600;
        font-size: 18px;
    }
    
    /* Cards de métrica */
    [data-testid="metric-container"] {
        background-color: var(--light-gray);
        border-radius: 8px;
        border-left: 4px solid var(--secondary-color);
        padding: 16px;
    }
    
    /* Botões */
    .stButton > button {
        background-color: var(--secondary-color);
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: 600;
        padding: 10px 24px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: var(--primary-color);
        box-shadow: 0 4px 12px rgba(0, 61, 130, 0.3);
    }
    
    /* Selectbox e inputs */
    .stSelectbox, .stMultiSelect {
        border-radius: 6px;
    }
    
    /* Info box */
    .stInfo {
        background-color: #e3f2fd;
        border-left: 4px solid var(--secondary-color);
        border-radius: 6px;
    }
    
    /* Success box */
    .stSuccess {
        background-color: #e8f5e9;
        border-left: 4px solid var(--success-color);
        border-radius: 6px;
    }
    
    /* Warning box */
    .stWarning {
        background-color: #fff3e0;
        border-left: 4px solid var(--warning-color);
        border-radius: 6px;
    }
    
    /* Error box */
    .stError {
        background-color: #ffebee;
        border-left: 4px solid var(--danger-color);
        border-radius: 6px;
    }
    
    /* Tabelas */
    .stDataFrame {
        border-radius: 8px;
        border: 1px solid var(--border-color);
    }
    
    /* Separadores */
    hr {
        border: none;
        border-top: 2px solid var(--border-color);
        margin: 24px 0;
    }
    
    /* Links */
    a {
        color: var(--secondary-color);
        text-decoration: none;
        font-weight: 500;
    }
    
    a:hover {
        color: var(--primary-color);
        text-decoration: underline;
    }
    
    /* Texto */
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
            'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
            sans-serif;
        color: var(--dark-gray);
    }
    
    /* Logo na sidebar */
    .sidebar-logo {
        text-align: center;
        padding: 20px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 20px;
    }
    
    .sidebar-logo h1 {
        color: white;
        font-size: 20px;
        margin: 0;
    }
    
    .sidebar-logo p {
        color: rgba(255, 255, 255, 0.8);
        font-size: 12px;
        margin: 4px 0 0 0;
    }
    
    /* Submenu dropdown */
    .submenu-container {
        background-color: var(--light-gray);
        border-radius: 8px;
        border: 1px solid var(--border-color);
        overflow: hidden;
    }
    
    .submenu-header {
        background-color: var(--secondary-color);
        color: white;
        padding: 12px 16px;
        cursor: pointer;
        font-weight: 600;
        display: flex;
        justify-content: space-between;
        align-items: center;
        user-select: none;
    }
    
    .submenu-header:hover {
        background-color: var(--primary-color);
    }
    
    .submenu-content {
        padding: 12px 0;
    }
    
    .submenu-item {
        padding: 10px 16px;
        color: var(--dark-gray);
        cursor: pointer;
        border-left: 4px solid transparent;
        transition: all 0.2s ease;
    }
    
    .submenu-item:hover {
        background-color: #e8f1f8;
        border-left-color: var(--secondary-color);
        padding-left: 20px;
    }
    
    .submenu-item.active {
        background-color: #e8f1f8;
        border-left-color: var(--secondary-color);
        font-weight: 600;
        color: var(--secondary-color);
    }
    
    /* Container profissional */
    .main-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 20px;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #999;
        font-size: 12px;
        padding: 20px;
        border-top: 1px solid var(--border-color);
        margin-top: 40px;
    }
    
    /* Logo PUCRS */
    .pucrs-logo {
        text-align: center;
        margin: 20px 0;
    }
    
    .pucrs-logo img {
        max-width: 300px;
        height: auto;
    }
    
    /* Texto sobre */
    .about-text {
        font-size: 15px;
        line-height: 1.8;
        color: var(--dark-gray);
        margin: 16px 0;
    }
    
    .about-highlight {
        background-color: var(--light-gray);
        padding: 16px;
        border-left: 4px solid var(--secondary-color);
        border-radius: 6px;
        margin: 16px 0;
    }
    
    </style>
    """, unsafe_allow_html=True)
