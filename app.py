"""
Dashboard Streamlit - Monitoramento de Desenvolvimento Infantil
Aplicação principal com st.navigation() e menu aninhado apenas para Metas
"""

import streamlit as st
from config.settings import PAGE_CONFIG

# Configurar página
st.set_page_config(**PAGE_CONFIG)

# Aplicar estilos CSS com cores PUCRS
st.markdown("""
<style>
    /* Cores PUCRS */
    :root {
        --pucrs-blue: #003d82;
        --pucrs-light-blue: #0066cc;
        --white: #ffffff;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #003d82;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Texto da sidebar */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: white !important;
    }
    
    /* Botões da navegação */
    [data-testid="stSidebar"] button {
        color: white !important;
    }
    
    /* Links */
    [data-testid="stSidebar"] a {
        color: white !important;
    }
    
    /* Página principal */
    .main {
        background-color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# Header customizado na sidebar (no topo - ANTES da navegação)
st.sidebar.markdown("""
<div style="padding: 20px 0; border-bottom: 2px solid rgba(255,255,255,0.3); margin-bottom: 20px; text-align: center;">
    <h2 style="color: white; margin: 0; font-size: 20px; font-weight: bold;">Cuidado no Desenvolvimento Infantil</h2>
    <p style="color: rgba(255,255,255,0.8); margin: 10px 0 0 0; font-size: 12px;">Cuidado no desenvolvimento infantil na Atenção Primária à Saúde</p>
</div>
""", unsafe_allow_html=True)

# Definir páginas com st.navigation()
# TODAS as páginas devem estar em listas
# Streamlit automaticamente oculta o submenu para itens com apenas uma página
pages = {
    "Principal": [
        st.Page("pages/01_apresentacao.py", title="Apresentação"),
        st.Page("pages/02_passo_a_passo.py", title="Passo a Passo"),
        st.Page("pages/03_upload.py", title="Upload"),
        st.Page("pages/10_diagnostico.py", title="Diagnóstico arquivo"),
    ],
    "Metas": [
        st.Page("pages/04_visao_geral.py", title="Visão geral"),
        st.Page("pages/05_meta_1.py", title="Meta 1 - 1ª Consulta Presencial"),
        st.Page("pages/06_meta_2.py", title="Meta 2 - Consultas Presenciais/Remotas"),
        st.Page("pages/07_meta_3.py", title="Meta 3 - Medições Peso/Altura"),
        st.Page("pages/08_meta_4.py", title="Meta 4 - Visitas Domiciliares"),
        st.Page("pages/09_meta_5.py", title="Meta 5 - Vacinação Completa"),
    ],
    "Sobre": [
        st.Page("pages/11_sobre.py", title="Sobre"),
    ],
}

# Verificar se há dados carregados
df_upload = st.session_state.get("df_upload")
has_data = df_upload is not None and len(df_upload) > 0

# Se não há dados, remover o menu Metas
if not has_data:
    pages_filtered = {
        "Principal": pages["Principal"],
        "Sobre": pages["Sobre"],
    }
    
    # Mostrar aviso na sidebar
    st.sidebar.warning("⚠️ Faça upload de dados na seção 'Upload' para acessar as Metas")
else:
    pages_filtered = pages

# Renderizar navegação
pg = st.navigation(pages_filtered)

# Executar página
pg.run()
