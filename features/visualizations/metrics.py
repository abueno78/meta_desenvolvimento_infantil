"""
Módulo para exibição de métricas e cards
"""

import streamlit as st
from config.settings import INDICATORS, COLORS, PARAMETROS


def exibir_metricas_principais(stats: dict):
    """
    Exibe as métricas principais em cards.
    
    Args:
        stats: Dicionário com estatísticas dos indicadores
    """
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Total de Crianças",
            value=stats["total_criancas"],
            delta=None,
        )
    
    with col2:
        st.metric(
            label="Conformes",
            value=stats["conformes"],
            delta=f"{stats['percentual_conforme']:.1f}%",
        )
    
    with col3:
        st.metric(
            label="Não-conformes",
            value=stats["nao_conformes"],
            delta=f"{100 - stats['percentual_conforme']:.1f}%",
        )


def exibir_cards_indicadores(stats: dict):
    """
    Exibe cards com conformidade de cada indicador e parâmetros.
    
    Args:
        stats: Dicionário com estatísticas dos indicadores
    """
    st.subheader("🎯 Metas e Indicadores")
    
    col1, col2, col3 = st.columns(3)
    
    # Indicador A
    with col1:
        _exibir_card_indicador(
            "A",
            INDICATORS["A"]["nome"],
            stats["indicador_a"]["conformes"],
            stats["total_criancas"],
            stats["indicador_a"]["percentual"],
            INDICATORS["A"]["cor"],
        )
    
    # Indicador B
    with col2:
        _exibir_card_indicador(
            "B",
            INDICATORS["B"]["nome"],
            stats["indicador_b"]["conformes"],
            stats["total_criancas"],
            stats["indicador_b"]["percentual"],
            INDICATORS["B"]["cor"],
        )
    
    # Indicador C
    with col3:
        _exibir_card_indicador(
            "C",
            INDICATORS["C"]["nome"],
            stats["indicador_c"]["conformes"],
            stats["total_criancas"],
            stats["indicador_c"]["percentual"],
            INDICATORS["C"]["cor"],
        )
    
    col1, col2, col3 = st.columns(3)
    
    # Indicador D
    with col1:
        _exibir_card_indicador(
            "D",
            INDICATORS["D"]["nome"],
            stats["indicador_d"]["conformes"],
            stats["total_criancas"],
            stats["indicador_d"]["percentual"],
            INDICATORS["D"]["cor"],
        )
    
    # Indicador E
    with col2:
        _exibir_card_indicador(
            "E",
            INDICATORS["E"]["nome"],
            stats["indicador_e"]["conformes"],
            stats["total_criancas"],
            stats["indicador_e"]["percentual"],
            INDICATORS["E"]["cor"],
        )
    
    # Legenda de Parâmetros
    with col3:
        st.markdown("### Parâmetros de Avaliação")
        for param_key, param in PARAMETROS.items():
            cor_param = param["cor"]
            label_param = param["label"]
            min_val = param["min"]
            max_val = param["max"]
            st.markdown(
                f"""<div style="background-color: {cor_param}20; border-left: 4px solid {cor_param}; padding: 8px; margin: 5px 0; border-radius: 3px;"><b>{label_param}</b>: {min_val} - {max_val}%</div>""",
                unsafe_allow_html=True
            )


def _exibir_card_indicador(
    letra: str,
    nome: str,
    conformes: int,
    total: int,
    percentual: float,
    cor: str,
):
    """
    Exibe um card individual de indicador com parâmetro de avaliação.
    
    Args:
        letra: Letra do indicador (A, B, C, D, E)
        nome: Nome do indicador
        conformes: Quantidade de crianças conformes
        total: Total de crianças
        percentual: Percentual de conformidade
        cor: Cor do indicador
    """
    # Determinar parâmetro
    parametro = "regular"
    if percentual > 75:
        parametro = "otimo"
    elif percentual > 50:
        parametro = "bom"
    elif percentual > 25:
        parametro = "suficiente"
    
    param = PARAMETROS[parametro]
    
    html_content = f"""
    <div style="
        background-color: {cor}20;
        border-left: 4px solid {cor};
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 10px;
    ">
        <h4 style="margin: 0 0 10px 0; color: {cor};">Meta {letra}</h4>
        <p style="margin: 0 0 5px 0; font-size: 12px; color: #666;">{nome}</p>
        <h3 style="margin: 0; color: {cor};">{percentual:.1f}%</h3>
        <p style="margin: 5px 0 0 0; font-size: 11px; color: #999;">
            {conformes} de {total} crianças
        </p>
        <p style="margin: 8px 0 0 0; font-size: 10px; padding: 5px; background-color: {param['cor']}30; border-radius: 3px; color: {param['cor']}; font-weight: bold;">
            {param['label']}
        </p>
    </div>
    """
    
    st.markdown(html_content, unsafe_allow_html=True)


def exibir_resumo_indicadores(stats: dict):
    """
    Exibe um resumo textual dos indicadores.
    
    Args:
        stats: Dicionário com estatísticas dos indicadores
    """
    st.markdown("---")
    st.subheader("📋 Resumo dos Indicadores")
    
    resumo = f"""
    **Meta A - 1ª Consulta Presencial:**
    - {stats['indicador_a']['conformes']} de {stats['total_criancas']} crianças ({stats['indicador_a']['percentual']:.1f}%)
    - Objetivo: 1ª consulta até 30º dia de vida
    
    **Meta B - Consultas Presenciais/Remotas:**
    - {stats['indicador_b']['conformes']} de {stats['total_criancas']} crianças ({stats['indicador_b']['percentual']:.1f}%)
    - Objetivo: Mínimo 9 consultas até 2 anos
    
    **Meta C - Medições Peso/Altura:**
    - {stats['indicador_c']['conformes']} de {stats['total_criancas']} crianças ({stats['indicador_c']['percentual']:.1f}%)
    - Objetivo: Mínimo 9 registros simultâneos até 2 anos
    
    **Meta D - Visitas Domiciliares:**
    - {stats['indicador_d']['conformes']} de {stats['total_criancas']} crianças ({stats['indicador_d']['percentual']:.1f}%)
    - Objetivo: 2 visitas (1ª até 30 dias, 2ª até 6 meses)
    
    **Meta E - Vacinação Completa:**
    - {stats['indicador_e']['conformes']} de {stats['total_criancas']} crianças ({stats['indicador_e']['percentual']:.1f}%)
    - Objetivo: Penta (3), VIP (3), VPC10 (3), SCR (1)
    """
    
    st.markdown(resumo)
