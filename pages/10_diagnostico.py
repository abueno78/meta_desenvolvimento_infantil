"""Página de Diagnóstico"""
import streamlit as st

st.markdown("## Diagnóstico do Arquivo")

if "df_upload" not in st.session_state or st.session_state.df_upload is None:
    st.warning("Nenhum arquivo carregado. Faça upload primeiro na seção 'Upload'.")
else:
    df = st.session_state.df_upload
    
    if df is None or len(df) == 0:
        st.warning("Arquivo vazio ou inválido.")
    else:
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
        st.dataframe(df.head(5), use_container_width=True)
