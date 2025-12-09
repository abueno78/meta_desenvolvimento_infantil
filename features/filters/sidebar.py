"""
Módulo para componentes de filtro na sidebar
"""

import streamlit as st
import pandas as pd
from config.settings import FILTROS, FAIXAS_ETARIAS


def criar_filtros_sidebar(df: pd.DataFrame) -> dict:
    """
    Cria os componentes de filtro na sidebar.
    
    Args:
        df: DataFrame com os dados
        
    Returns:
        Dicionário com os filtros selecionados
    """
    st.sidebar.title("🔍 Filtros")
    
    filtros = {}
    
    # Filtro de sexo
    sexo_opcoes = FILTROS["sexo"]
    filtros["sexo"] = st.sidebar.selectbox(
        "Sexo",
        sexo_opcoes,
        key="filtro_sexo"
    )
    
    # Filtro de raça/cor
    raca_opcoes = FILTROS["raca_cor"]
    filtros["raca_cor"] = st.sidebar.selectbox(
        "Raça/Cor",
        raca_opcoes,
        key="filtro_raca"
    )
    
    # Filtro de faixa etária
    faixa_opcoes = ["Todos"] + list(FAIXAS_ETARIAS.keys())
    filtros["faixa_etaria"] = st.sidebar.selectbox(
        "Faixa Etária",
        faixa_opcoes,
        key="filtro_faixa"
    )
    
    # Filtro de bairro
    bairros_disponiveis = sorted(df["Bairro"].dropna().unique())
    bairros_disponiveis = [b for b in bairros_disponiveis if b != "-"]
    filtros["bairro"] = st.sidebar.multiselect(
        "Bairro",
        bairros_disponiveis,
        key="filtro_bairro"
    )
    
    # Filtro de status
    status_opcoes = FILTROS["status"]
    filtros["status"] = st.sidebar.selectbox(
        "Status Geral",
        status_opcoes,
        key="filtro_status"
    )
    
    # Filtro por indicador específico
    st.sidebar.markdown("---")
    st.sidebar.subheader("Filtrar por Indicador")
    
    indicadores = ["Todos", "A", "B", "C", "D", "E"]
    filtros["indicador"] = st.sidebar.selectbox(
        "Indicador",
        indicadores,
        key="filtro_indicador"
    )
    
    # Botão de reset
    st.sidebar.markdown("---")
    if st.sidebar.button("🔄 Limpar Filtros"):
        st.session_state.clear()
        st.rerun()
    
    return filtros


def aplicar_filtros(df: pd.DataFrame, filtros: dict) -> pd.DataFrame:
    """
    Aplica os filtros selecionados ao DataFrame.
    
    Args:
        df: DataFrame com os dados
        filtros: Dicionário com os filtros selecionados
        
    Returns:
        DataFrame filtrado
    """
    df_filtrado = df.copy()
    
    # Filtro de sexo
    if filtros["sexo"] != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Sexo"] == filtros["sexo"]]
    
    # Filtro de raça/cor
    if filtros["raca_cor"] != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Raça/cor"] == filtros["raca_cor"]]
    
    # Filtro de faixa etária
    if filtros["faixa_etaria"] != "Todos":
        min_meses, max_meses = FAIXAS_ETARIAS[filtros["faixa_etaria"]]
        df_filtrado = df_filtrado[
            (df_filtrado["Idade_meses"] >= min_meses) &
            (df_filtrado["Idade_meses"] < max_meses)
        ]
    
    # Filtro de bairro
    if filtros["bairro"]:
        df_filtrado = df_filtrado[df_filtrado["Bairro"].isin(filtros["bairro"])]
    
    # Filtro de status
    if filtros["status"] != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Status_geral"] == filtros["status"]]
    
    # Filtro por indicador
    if filtros["indicador"] != "Todos":
        coluna_indicador = f"Indicador_{filtros['indicador']}"
        df_filtrado = df_filtrado[df_filtrado[coluna_indicador] == True]
    
    return df_filtrado
