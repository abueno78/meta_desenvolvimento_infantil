"""Página de Visão Geral das Metas"""
import streamlit as st
import pandas as pd
from data.loader import carregar_dados, limpar_dados
from data.processor import processar_dados, calcular_estatisticas
from features.visualizations.metrics import exibir_metricas_principais, exibir_cards_indicadores
from features.visualizations.charts import (
    criar_grafico_indicadores,
    criar_grafico_indicadores_bolsa_familia,
    criar_grafico_status_geral,
    criar_grafico_distribuicao_idade,
    criar_grafico_sexo,
    criar_heatmap_indicadores,
    criar_tabela_crianças,
)
from config.settings import DATA_CONFIG
import plotly.graph_objects as go
import plotly.express as px

st.markdown("## Visão Geral - Todas as Metas")

try:
    # Tentar carregar dados do session_state primeiro
    df = st.session_state.get("df_upload")
    
    # Se não houver dados no session_state, carregar do arquivo padrão
    if df is None:
        try:
            df = carregar_dados(DATA_CONFIG["csv_path"])
            df = limpar_dados(df)
        except:
            st.warning("Nenhum arquivo carregado. Faça upload de dados na seção 'Upload'.")
            st.stop()
    
    if df is not None and len(df) > 0:
        # Processar dados
        df = processar_dados(df)
        
        # Iniciar com Resumo Geral
        st.markdown("### Resumo Geral")
        stats = calcular_estatisticas(df)
        exibir_metricas_principais(stats)
        
        st.markdown("---")
        
        # Layout lado a lado: Filtros à esquerda (reduzido), Metas à direita
        # Proporção: 0.5 (filtros) vs 1.5 (metas)
        col_filtros, col_metas = st.columns([0.5, 1.5])
        
        # COLUNA ESQUERDA: FILTROS (REDUZIDA)
        with col_filtros:
            st.markdown("### Filtros")
            
            # Obter valores únicos com tratamento de NaN
            sexo_values = ["Todos"] + [x for x in df["Sexo"].dropna().unique().tolist() if pd.notna(x)]
            raca_values = ["Todos"] + [x for x in df["Raça/cor"].dropna().unique().tolist() if pd.notna(x)]
            microarea_values = ["Todos"] + [x for x in df["Microárea"].dropna().unique().tolist() if pd.notna(x)]
            bolsa_familia_values = ["Todos", "Sim", "Não"]
            
            # Usar selectbox (dropdown de única escolha) em vez de multiselect
            sexo_filter = st.selectbox(
                "Sexo",
                options=sexo_values,
                index=0,
                key="sexo_filter_visao"
            )
            
            raca_filter = st.selectbox(
                "Raça/Cor",
                options=raca_values,
                index=0,
                key="raca_filter_visao"
            )
            
            microarea_filter = st.selectbox(
                "Microárea",
                options=microarea_values,
                index=0,
                key="microarea_filter_visao"
            )
            
            bolsa_familia_filter = st.selectbox(
                "Bolsa Família",
                options=bolsa_familia_values,
                index=0,
                key="bolsa_filter_visao"
            )
        
        # COLUNA DIREITA: METAS E INDICADORES (DESTAQUE)
        with col_metas:
            
            # Aplicar filtros
            df_filtrado = df.copy()
            
            if sexo_filter != "Todos":
                df_filtrado = df_filtrado[df_filtrado["Sexo"] == sexo_filter]
            
            if raca_filter != "Todos":
                df_filtrado = df_filtrado[df_filtrado["Raça/cor"] == raca_filter]
            
            if microarea_filter != "Todos":
                df_filtrado = df_filtrado[df_filtrado["Microárea"] == microarea_filter]
            
            if bolsa_familia_filter != "Todos":
                df_filtrado = df_filtrado[df_filtrado["Beneficiário do programa Bolsa Família"] == bolsa_familia_filter]
            
            # Calcular estatísticas filtradas
            stats_filtrado = calcular_estatisticas(df_filtrado)
            
            # Exibir cards reduzidos
            exibir_cards_indicadores(stats_filtrado)
        
        st.info(f"Exibindo {len(df_filtrado)} de {len(df)} crianças com os filtros aplicados")
        
        st.markdown("---")
        
        st.markdown("### Visualizações")
        
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(criar_grafico_indicadores_bolsa_familia(df_filtrado), use_container_width=True)
        with col2:
            st.plotly_chart(criar_grafico_status_geral(df_filtrado), use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(criar_grafico_distribuicao_idade(df_filtrado), use_container_width=True)
        with col2:
            st.plotly_chart(criar_grafico_sexo(df_filtrado), use_container_width=True)
        
        st.markdown("---")
        st.markdown("### Análise Detalhada")
        
        # Gráfico de calor com Raça/Cor
        st.subheader("Conformidade por Raça/Cor")
        
        # Criar tabela de conformidade por raça/cor
        if "Raça/cor" in df_filtrado.columns:
            conformidade_raca = pd.DataFrame()
            
            for raca in df_filtrado["Raça/cor"].dropna().unique():
                df_raca = df_filtrado[df_filtrado["Raça/cor"] == raca]
                
                if len(df_raca) > 0:
                    conformidade_raca = pd.concat([conformidade_raca, pd.DataFrame({
                        "Raça/Cor": [raca],
                        "Meta 1": [(df_raca["Indicador_A"].sum() / len(df_raca) * 100) if len(df_raca) > 0 else 0],
                        "Meta 2": [(df_raca["Indicador_B"].sum() / len(df_raca) * 100) if len(df_raca) > 0 else 0],
                        "Meta 3": [(df_raca["Indicador_C"].sum() / len(df_raca) * 100) if len(df_raca) > 0 else 0],
                        "Meta 4": [(df_raca["Indicador_D"].sum() / len(df_raca) * 100) if len(df_raca) > 0 else 0],
                        "Meta 5": [(df_raca["Indicador_E"].sum() / len(df_raca) * 100) if len(df_raca) > 0 else 0],
                    })], ignore_index=True)
            
            if len(conformidade_raca) > 0:
                # Criar heatmap
                conformidade_raca_pivot = conformidade_raca.set_index("Raça/Cor")[["Meta 1", "Meta 2", "Meta 3", "Meta 4", "Meta 5"]]
                
                fig_heatmap = go.Figure(data=go.Heatmap(
                    z=conformidade_raca_pivot.values,
                    x=conformidade_raca_pivot.columns,
                    y=conformidade_raca_pivot.index,
                    colorscale="RdYlGn",
                    text=conformidade_raca_pivot.values.round(1),
                    texttemplate="%{text:.1f}%",
                    textfont={"size": 12},
                    colorbar=dict(title="Conformidade (%)")
                ))
                
                fig_heatmap.update_layout(
                    title="Conformidade das Metas por Raça/Cor",
                    xaxis_title="Metas",
                    yaxis_title="Raça/Cor",
                    height=400
                )
                
                st.plotly_chart(fig_heatmap, use_container_width=True)
        
        # Heatmap original de indicadores
        st.plotly_chart(criar_heatmap_indicadores(df_filtrado), use_container_width=True)
        
        st.markdown("---")
        st.markdown("### Dados das Crianças")
        st.dataframe(criar_tabela_crianças(df_filtrado), use_container_width=True)
    else:
        st.warning("Nenhum arquivo carregado. Faça upload de dados na seção 'Upload'.")

except Exception as e:
    st.error(f"Erro ao exibir dados: {str(e)}")
    st.warning("Nenhum arquivo carregado. Faça upload de dados na seção 'Upload'.")
