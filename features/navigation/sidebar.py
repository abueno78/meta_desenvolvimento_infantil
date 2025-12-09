"""
Módulo para navegação e sidebar da aplicação
"""

import streamlit as st
import pandas as pd
from config.settings import FILTROS, SIDEBAR_TEXTS


def criar_sidebar_navegacao():
    """
    Cria a sidebar com navegação estruturada.
    
    Returns:
        tuple: (seção principal, opção de meta se aplicável)
    """
    with st.sidebar:
        # Logo/Título profissional
        st.markdown("""
        <div style="text-align: center; padding: 20px 0; border-bottom: 1px solid rgba(255,255,255,0.2); margin-bottom: 20px;">
            <h2 style="color: white; margin: 0; font-size: 20px;">📊 Dashboard Infantil</h2>
            <p style="color: rgba(255,255,255,0.8); font-size: 12px; margin: 4px 0 0 0;">Monitoramento de Saúde</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Menu principal
        secao = st.radio(
            "Navegação",
            [
                "🏠 Início",
                "📋 Guia de Uso",
                "📤 Upload de Dados",
                "🎯 Análise de Metas",
                "🔍 Diagnóstico",
                "ℹ️ Sobre",
            ],
            key="menu_principal"
        )
        
        st.markdown("---")
        
        return secao


def exibir_apresentacao():
    """Exibe a seção de apresentação profissional."""
    st.markdown("## 📊 Dashboard de Monitoramento Infantil")
    
    st.markdown("""
    ### Bem-vindo ao Sistema de Acompanhamento
    
    Este dashboard foi desenvolvido para monitorar e avaliar indicadores de qualidade do cuidado 
    no desenvolvimento infantil, baseado na **Nota Metodológica C2** do Ministério da Saúde.
    
    ---
    """)
    
    # Cards informativos
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #f5f7fa; padding: 20px; border-radius: 8px; border-left: 4px solid #0066cc;">
            <h4 style="color: #003d82; margin-top: 0;">🎯 Objetivo</h4>
            <p style="margin: 0; font-size: 14px;">Avaliar a qualidade do cuidado infantil na Atenção Primária à Saúde através de 5 indicadores principais.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #f5f7fa; padding: 20px; border-radius: 8px; border-left: 4px solid #00a8e8;">
            <h4 style="color: #003d82; margin-top: 0;">📈 Indicadores</h4>
            <p style="margin: 0; font-size: 14px;">5 metas monitoradas com 20 pontos cada, totalizando 100 pontos de conformidade.</p>
        </div>
        """, unsafe_allow_html=True)


def exibir_passo_a_passo():
    """Exibe o guia passo a passo."""
    st.markdown("## 📋 Como Usar o Dashboard")
    
    st.markdown("""
    ### Passo 1️⃣: Carregar Dados
    Acesse a seção **"Upload de Dados"** e selecione seu arquivo CSV com os dados das crianças.
    
    ### Passo 2️⃣: Aplicar Filtros
    Na tela principal, use os filtros para segmentar os dados:
    - **Sexo** - Filtrar por gênero
    - **Raça/Cor** - Filtrar por etnia
    - **Bolsa Família** - Filtrar por beneficiários
    - **Microárea** - Filtrar por localização
    
    ### Passo 3️⃣: Analisar Metas
    Visualize os cards das 5 metas com seus indicadores e parâmetros de avaliação.
    
    ### Passo 4️⃣: Explorar Gráficos
    Analise os gráficos interativos para insights mais profundos sobre os dados.
    
    ### Passo 5️⃣: Exportar Dados
    Exporte os dados filtrados em formato CSV para análises adicionais.
    """)


def exibir_upload_dados():
    """Exibe a seção de upload de dados."""
    st.markdown("## 📤 Carregar Arquivo de Dados")
    
    st.info("Selecione um arquivo CSV com os dados das crianças para análise.")
    
    uploaded_file = st.file_uploader(
        "Escolha um arquivo CSV",
        type=["csv"],
        key="file_uploader"
    )
    
    if uploaded_file is not None:
        try:
            df = None
            
            # Tentativa 1: ISO-8859-1 com skiprows=24
            try:
                uploaded_file.seek(0)
                df = pd.read_csv(uploaded_file, sep=";", encoding="iso-8859-1", skiprows=24)
                if len(df) > 0:
                    st.success("✓ Arquivo carregado com sucesso!")
            except:
                pass
            
            # Tentativa 2: ISO-8859-1 com engine=python e skiprows=24
            if df is None or len(df) == 0:
                try:
                    uploaded_file.seek(0)
                    df = pd.read_csv(uploaded_file, sep=";", encoding="iso-8859-1", engine="python", skiprows=24)
                    if len(df) > 0:
                        st.success("✓ Arquivo carregado com sucesso!")
                except:
                    pass
            
            # Tentativa 3: ISO-8859-1 sem skiprows
            if df is None or len(df) == 0:
                try:
                    uploaded_file.seek(0)
                    df = pd.read_csv(uploaded_file, sep=";", encoding="iso-8859-1")
                    if len(df) > 0:
                        st.success("✓ Arquivo carregado com sucesso!")
                except:
                    pass
            
            # Tentativa 4: UTF-8 com skiprows=24
            if df is None or len(df) == 0:
                try:
                    uploaded_file.seek(0)
                    df = pd.read_csv(uploaded_file, sep=";", encoding="utf-8", skiprows=24)
                    if len(df) > 0:
                        st.success("✓ Arquivo carregado com sucesso!")
                except:
                    pass
            
            # Tentativa 5: Sem especificar encoding
            if df is None or len(df) == 0:
                try:
                    uploaded_file.seek(0)
                    df = pd.read_csv(uploaded_file, sep=";")
                    if len(df) > 0:
                        st.success("✓ Arquivo carregado com sucesso!")
                except:
                    pass
            
            # Se ainda não conseguiu carregar
            if df is None or len(df) == 0:
                st.error("Não foi possível carregar o arquivo. Verifique se é um CSV válido.")
                return None
            
            # Remover linhas completamente vazias
            df = df.dropna(how='all')
            
            # Remover colunas completamente vazias
            df = df.dropna(axis=1, how='all')
            
            # Filtrar colunas que são só "Unnamed"
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            
            if len(df) == 0:
                st.error("Arquivo vazio ou sem dados válidos após limpeza.")
                return None
            
            st.write(f"**Total de linhas:** {len(df)}")
            st.write(f"**Total de colunas:** {len(df.columns)}")
            
            # Armazenar no session state
            st.session_state.df_upload = df
            
            return df
        except Exception as e:
            st.error(f"Erro ao carregar arquivo: {str(e)[:150]}")
            return None
    
    return None


def exibir_analise_metas():
    """Exibe o menu de análise de metas com submenu dropdown."""
    st.markdown("## 🎯 Análise de Metas")
    
    # Usar selectbox em vez de radio para comportamento dropdown
    opcoes_metas = st.selectbox(
        "Selecione uma meta para análise:",
        [
            "📊 Visão Geral",
            "🔹 Meta 1 - 1ª Consulta Presencial",
            "🔹 Meta 2 - Consultas Presenciais/Remotas",
            "🔹 Meta 3 - Medições Peso/Altura",
            "🔹 Meta 4 - Visitas Domiciliares",
            "🔹 Meta 5 - Vacinação Completa",
        ],
        key="opcoes_metas"
    )
    
    return opcoes_metas


def exibir_diagnostico():
    """Exibe a seção de diagnóstico."""
    st.markdown("## 🔍 Diagnóstico do Arquivo")
    
    # Verificar se tem arquivo carregado
    if "df_upload" not in st.session_state or st.session_state.df_upload is None:
        st.warning("Nenhum arquivo carregado. Faça upload primeiro na seção 'Upload de Dados'.")
        return
    
    df = st.session_state.df_upload
    
    # Verificar se dataframe é válido
    if df is None or len(df) == 0:
        st.warning("Arquivo vazio ou inválido.")
        return
    
    st.markdown("### Informações do Arquivo")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total de Registros", len(df))
    
    with col2:
        st.metric("Total de Colunas", len(df.columns))
    
    with col3:
        if len(df) > 0 and len(df.columns) > 0:
            total_cells = len(df) * len(df.columns)
            null_cells = df.isnull().sum().sum()
            completude = (1 - null_cells / total_cells) * 100
            st.metric("Dados Completos", f"{completude:.1f}%")
        else:
            st.metric("Dados Completos", "N/A")
    
    st.markdown("### Colunas Disponíveis")
    st.write(df.columns.tolist())
    
    st.markdown("### Primeiras Linhas")
    st.dataframe(df.head(5))


def exibir_sobre():
    """Exibe a seção sobre com logo PUCRS."""
    st.markdown("## ℹ️ Sobre Este Dashboard")
    
    # Logo PUCRS
    st.markdown("""
    <div style="text-align: center; margin: 20px 0;">
        <img src="https://www.pucrs.br/eventos/wp-content/uploads/sites/73/2023/09/Escola-de-Ciencias-da-Saude-e-da-Vida_Azul-01.png" 
             style="max-width: 300px; height: auto;">
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### Desenvolvimento Acadêmico
    
    Este dashboard foi desenvolvido como projeto prático da disciplina de **"Tecnologia em Saúde e Ciência de Dados"**, 
    ministrada pelo **Prof. André Scolare Bueno** na especialização **"Saúde Coletiva com Ênfase em Saúde da Família"** 
    da Pontifícia Universidade Católica do Rio Grande do Sul (PUCRS).
    
    ---
    
    ### Objetivo e Metodologia
    
    O dashboard foi desenvolvido para monitorar e avaliar indicadores de qualidade do cuidado no desenvolvimento infantil, 
    baseado na **Nota Metodológica C2** do Ministério da Saúde do Brasil.
    
    Utiliza dados de crianças de 0 a 2 anos atendidas na Atenção Primária à Saúde, avaliando 5 indicadores principais:
    
    - **Meta A:** 1ª Consulta Presencial (até 30º dia de vida)
    - **Meta B:** Consultas Presenciais/Remotas (mínimo 9 até 2 anos)
    - **Meta C:** Medições Peso/Altura (mínimo 9 registros simultâneos até 2 anos)
    - **Meta D:** Visitas Domiciliares (2 visitas: 1ª até 30 dias, 2ª até 6 meses)
    - **Meta E:** Vacinação Completa (conforme Calendário Nacional)
    
    ---
    
    ### Tecnologias Utilizadas
    
    - **Streamlit** - Framework para aplicações web em Python
    - **Pandas** - Manipulação e análise de dados
    - **Plotly** - Visualizações interativas
    - **Python 3.11** - Linguagem de programação
    
    ---
    
    ### Parâmetros de Avaliação
    
    Os indicadores são avaliados conforme os seguintes parâmetros:
    
    | Parâmetro | Intervalo | Significado |
    |-----------|-----------|-------------|
    | 🟢 Ótimo | > 75 e ≤ 100 | Excelente desempenho |
    | 🔵 Bom | > 50 e ≤ 75 | Bom desempenho |
    | 🟠 Suficiente | > 25 e ≤ 50 | Desempenho aceitável |
    | 🔴 Regular | ≤ 25 | Desempenho insuficiente |
    
    ---
    
    **Versão:** 2.0.0  
    **Data:** Dezembro de 2025  
    **Instituição:** PUCRS - Escola de Ciências da Saúde e da Vida
    """)


def criar_filtros_principais(df: pd.DataFrame) -> dict:
    """
    Cria filtros na tela principal (não na sidebar).
    
    Args:
        df: DataFrame com os dados
        
    Returns:
        Dicionário com os filtros selecionados
    """
    st.markdown("## 🔍 Filtros")
    
    col1, col2, col3, col4 = st.columns(4)
    
    filtros = {}
    
    with col1:
        filtros["sexo"] = st.selectbox(
            "Sexo",
            FILTROS["sexo"],
            key="filtro_sexo_principal"
        )
    
    with col2:
        filtros["raca_cor"] = st.selectbox(
            "Raça/Cor",
            FILTROS["raca_cor"],
            key="filtro_raca_principal"
        )
    
    with col3:
        # Mapear valores de Bolsa Família
        bolsa_opcoes = FILTROS["bolsa_familia"]
        filtros["bolsa_familia"] = st.selectbox(
            "Bolsa Família",
            bolsa_opcoes,
            key="filtro_bolsa_principal"
        )
    
    with col4:
        # Microáreas disponíveis
        try:
            microareas = sorted(df["Microárea"].dropna().unique())
            microareas = ["Todas"] + [str(m) for m in microareas if m != "-"]
        except:
            microareas = ["Todas"]
        
        filtros["microarea"] = st.selectbox(
            "Microárea",
            microareas,
            key="filtro_microarea_principal"
        )
    
    return filtros


def aplicar_filtros_principais(df: pd.DataFrame, filtros: dict) -> pd.DataFrame:
    """
    Aplica os filtros da tela principal ao DataFrame.
    
    Args:
        df: DataFrame com os dados
        filtros: Dicionário com os filtros selecionados
        
    Returns:
        DataFrame filtrado
    """
    df_filtrado = df.copy()
    
    # Filtro de sexo
    if filtros["sexo"] != "Todos":
        if "Sexo" in df_filtrado.columns:
            df_filtrado = df_filtrado[df_filtrado["Sexo"] == filtros["sexo"]]
    
    # Filtro de raça/cor
    if filtros["raca_cor"] != "Todos":
        if "Raça/cor" in df_filtrado.columns:
            df_filtrado = df_filtrado[df_filtrado["Raça/cor"] == filtros["raca_cor"]]
    
    # Filtro de Bolsa Família
    if filtros["bolsa_familia"] != "Todos":
        if "Beneficiário do programa Bolsa Família" in df_filtrado.columns:
            valor_bolsa = "Sim" if filtros["bolsa_familia"] == "Sim" else "Não"
            df_filtrado = df_filtrado[df_filtrado["Beneficiário do programa Bolsa Família"] == valor_bolsa]
    
    # Filtro de Microárea
    if filtros["microarea"] != "Todas":
        if "Microárea" in df_filtrado.columns:
            df_filtrado = df_filtrado[df_filtrado["Microárea"] == filtros["microarea"]]
    
    return df_filtrado
