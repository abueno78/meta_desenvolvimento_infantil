"""Página da Meta 4"""
import streamlit as st
import pandas as pd
from data.loader import carregar_dados, limpar_dados
from data.processor import processar_dados, calcular_estatisticas
from features.visualizations.charts import (
    criar_grafico_conformidade_por_variavel,
)
from config.settings import DATA_CONFIG

st.markdown("## Meta 4 - Visitas Domiciliares")
st.info("Ter pelo menos 02 (duas) visitas domiciliares realizadas por ACS/TACS, sendo a primeira até os primeiros 30(trinta) dias de vida e a segunda até os 06 (seis) meses de vida.")

try:
    # Carregar dados
    df = st.session_state.get("df_upload")
    if df is None:
        df = carregar_dados(DATA_CONFIG["csv_path"])
        df = limpar_dados(df)
    
    if df is not None and len(df) > 0:
        df = processar_dados(df)
        
        # Métricas Meta 4
        st.markdown("### Métricas - Meta 4")
        
        total = len(df)
        conformes = df["Indicador_D"].sum() if total > 0 else 0
        nao_conformes = total - conformes
        percentual = (conformes / total * 100) if total > 0 else 0
        
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        with metric_col1:
            st.metric("Conforme", int(conformes))
        with metric_col2:
            st.metric("Não-conforme", int(nao_conformes))
        with metric_col3:
            st.metric("Conformidade", f"{percentual:.1f}%")
        
        st.markdown("---")
        
        # Gráficos por variáveis de filtro com valores absolutos e relativos
        st.markdown("### Análise por Variáveis")
        
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(
                criar_grafico_conformidade_por_variavel(df, "Sexo", "Indicador_D"),
                use_container_width=True
            )
        with col2:
            st.plotly_chart(
                criar_grafico_conformidade_por_variavel(df, "Raça/cor", "Indicador_D"),
                use_container_width=True
            )
        
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(
                criar_grafico_conformidade_por_variavel(df, "Beneficiário do programa Bolsa Família", "Indicador_D"),
                use_container_width=True
            )
        with col2:
            st.plotly_chart(
                criar_grafico_conformidade_por_variavel(df, "Microárea", "Indicador_D"),
                use_container_width=True
            )
        
        st.markdown("---")
        
        # Tabela de dados das crianças
        st.markdown("### Dados das Crianças")
        
        # Preparar tabela com colunas solicitadas
        colunas_exibicao = ["Nome", "CPF", "CNS", "Telefone celular", "Telefone residencial", "Telefone de contato", "Indicador_D"]
        colunas_exibicao = [c for c in colunas_exibicao if c in df.columns]
        
        df_tabela = df[colunas_exibicao].copy()
        
        # Renomear coluna Indicador_D para "D"
        df_tabela = df_tabela.rename(columns={"Indicador_D": "D"})
        
        # Converter booleanos para símbolos
        df_tabela["D"] = df_tabela["D"].apply(lambda x: "✓" if x else "✗")
        
        if len(df_tabela) > 0:
            st.dataframe(df_tabela, use_container_width=True, hide_index=True)
        else:
            st.warning("Nenhum dado disponível.")
    
    else:
        st.warning("Nenhum arquivo carregado. Faça upload de dados na seção 'Upload'.")

except Exception as e:
    st.error(f"Erro ao exibir dados: {str(e)}")
    import traceback
    st.warning(traceback.format_exc())
