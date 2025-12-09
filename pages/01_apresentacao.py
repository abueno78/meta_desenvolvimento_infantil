"""Página de Apresentação"""
import streamlit as st

st.markdown("## Bem-vindo ao Dashboard")

st.markdown("""
### Monitoramento de Desenvolvimento Infantil

Este dashboard foi desenvolvido para monitorar e avaliar indicadores de qualidade do cuidado 
no desenvolvimento infantil, baseado na Nota Metodológica C2 do Ministério da Saúde.

---
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background-color: #f5f7fa; padding: 20px; border-radius: 8px; border-left: 4px solid #0066cc;">
        <h4 style="color: #003d82; margin-top: 0;">Objetivo</h4>
        <p style="margin: 0; font-size: 14px;">Avaliar a qualidade do cuidado infantil na Atenção Primária à Saúde através de 5 indicadores principais.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background-color: #f5f7fa; padding: 20px; border-radius: 8px; border-left: 4px solid #00a8e8;">
        <h4 style="color: #003d82; margin-top: 0;">Indicadores</h4>
        <p style="margin: 0; font-size: 14px;">5 metas monitoradas com 20 pontos cada, totalizando 100 pontos de conformidade.
         
        </p>
    </div>
    """, unsafe_allow_html=True)
