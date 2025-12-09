"""Página de Upload de Dados"""
import streamlit as st
import pandas as pd

st.markdown("## Carregar Arquivo de Dados")

st.info("Selecione um arquivo CSV com os dados das crianças para análise.")

uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"], key="file_uploader_main")

if uploaded_file is not None:
    try:
        df = None
        
        # Tentativa 1: ISO-8859-1 com skiprows=24
        try:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, sep=";", encoding="iso-8859-1", skiprows=24)
            if len(df) > 0:
                st.success("Arquivo carregado com sucesso!")
        except:
            pass
        
        # Tentativa 2: ISO-8859-1 com engine=python
        if df is None or len(df) == 0:
            try:
                uploaded_file.seek(0)
                df = pd.read_csv(uploaded_file, sep=";", encoding="iso-8859-1", engine="python", skiprows=24)
                if len(df) > 0:
                    st.success("Arquivo carregado com sucesso!")
            except:
                pass
        
        # Tentativa 3: ISO-8859-1 sem skiprows
        if df is None or len(df) == 0:
            try:
                uploaded_file.seek(0)
                df = pd.read_csv(uploaded_file, sep=";", encoding="iso-8859-1")
                if len(df) > 0:
                    st.success("Arquivo carregado com sucesso!")
            except:
                pass
        
        # Tentativa 4: UTF-8
        if df is None or len(df) == 0:
            try:
                uploaded_file.seek(0)
                df = pd.read_csv(uploaded_file, sep=";", encoding="utf-8", skiprows=24)
                if len(df) > 0:
                    st.success("Arquivo carregado com sucesso!")
            except:
                pass
        
        # Tentativa 5: Sem encoding
        if df is None or len(df) == 0:
            try:
                uploaded_file.seek(0)
                df = pd.read_csv(uploaded_file, sep=";")
                if len(df) > 0:
                    st.success("Arquivo carregado com sucesso!")
            except:
                pass
        
        if df is None or len(df) == 0:
            st.error("Não foi possível carregar o arquivo. Verifique se é um CSV válido.")
        else:
            df = df.dropna(how='all')
            df = df.dropna(axis=1, how='all')
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            
            if len(df) == 0:
                st.error("Arquivo vazio ou sem dados válidos após limpeza.")
            else:
                st.write(f"**Total de linhas:** {len(df)}")
                st.write(f"**Total de colunas:** {len(df.columns)}")
                
                st.session_state.df_upload = df
                
                st.markdown("---")
                st.markdown("### Primeiras Linhas do Arquivo")
                st.dataframe(df.head(10), use_container_width=True)
                
                st.success("Arquivo carregado com sucesso!")
    except Exception as e:
        st.error(f"Erro ao carregar arquivo: {str(e)[:150]}")
