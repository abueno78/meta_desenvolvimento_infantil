"""Página de Guia de Uso"""
import streamlit as st

st.markdown("## Como Usar o Dashboard")

st.markdown("""
### 📋 Extração de Dados do E-SUS

Siga os passos abaixo para extrair os dados de desenvolvimento infantil do E-SUS e carregar no dashboard:

---
""")

# Função para criar cards lado a lado
def criar_card_passo(titulo, acao, orientacao):
    """Cria um card com dois blocos lado a lado"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div style="
            background-color: #f0f7ff;
            border-left: 4px solid #0066cc;
            padding: 20px;
            border-radius: 4px;
            height: 100%;
        ">
            <h4 style="color: #0066cc; margin-top: 0;">Ação</h4>
            <p style="margin: 0;">{acao}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background-color: #f0f7ff;
            border-left: 4px solid #0066cc;
            padding: 20px;
            border-radius: 4px;
            height: 100%;
        ">
            <h4 style="color: #0066cc; margin-top: 0;">Orientação</h4>
            <p style="margin: 0;">{orientacao}</p>
        </div>
        """, unsafe_allow_html=True)

# Passo 1
st.markdown("### Passo 1️⃣: Acessar E-SUS")
criar_card_passo(
    "Acessar E-SUS",
    "Abra seu navegador e acesse o E-SUS da sua unidade",
    "Digite o endereço do E-SUS em seu navegador, faça login com suas credenciais e você será direcionado ao painel principal"
)
st.divider()

# Passo 2
st.markdown("### Passo 2️⃣: Acessar Módulo de Acompanhamentos")
criar_card_passo(
    "Acessar Acompanhamentos",
    "No menu principal, clique em 'Acompanhamentos'",
    "Este módulo contém todos os registros de acompanhamento das crianças. Você verá uma lista de opções relacionadas ao monitoramento"
)
st.divider()

# Passo 3
st.markdown("### Passo 3️⃣: Acessar Condições de Saúde")
criar_card_passo(
    "Selecionar Condições de Saúde",
    "Dentro de Acompanhamentos, clique em 'Condições de Saúde'",
    "Este submenu agrupa os dados por condições de saúde específicas. Você terá acesso a diferentes listas temáticas"
)
st.divider()

# Passo 4
st.markdown("### Passo 4️⃣: Selecionar Lista Temática 'Desenvolvimento Infantil'")
criar_card_passo(
    "Clicar em Desenvolvimento Infantil",
    "Procure pela lista temática 'Desenvolvimento Infantil'",
    "Esta lista contém todos os registros de crianças de 0 a 2 anos. Você verá uma tabela com informações como: Nome, Data de Nascimento, Sexo, Raça/Cor, etc."
)
st.divider()

# Passo 5
st.markdown("### Passo 5️⃣: Exportar para CSV")
criar_card_passo(
    "Clicar em Exportar CSV",
    "Ao final da página, procure pelo botão 'Exportar'",
    "Selecione a opção 'CSV' (Comma Separated Values). O arquivo será baixado em seu computador com extensão .csv contendo todos os dados da lista"
)
st.divider()

# Passo 6
st.markdown("### Passo 6️⃣: Carregar Dados no Dashboard")
criar_card_passo(
    "Fazer upload do arquivo",
    "Volte ao dashboard e clique no menu 'Upload'",
    "Clique em 'Procurar arquivos' ou arraste o arquivo CSV. Selecione o arquivo que você baixou do E-SUS. Aguarde o processamento. O menu 'Metas' aparecerá automaticamente"
)

st.divider()

st.markdown("""
---

## ✅ Pronto para Análise!

Após carregar os dados, você terá acesso a:

### 📊 **Visão Geral**
- Resumo de todas as metas
- Gráficos comparativos
- Análise por variáveis demográficas

### 🎯 **Metas Individuais (1 a 5)**
- Análise detalhada de cada indicador
- Gráficos segmentados por sexo, raça/cor, Bolsa Família e microárea
- Tabelas com dados de contato das crianças
- Para Meta 5: Análise refinada de vacinação com doses faltantes

### 📚 **Documentação**
- Acesse a seção "Sobre" para:
  - Metodologia completa de cálculo
  - Descrição de variáveis utilizadas
  - Download da Nota Metodológica C2
  - Download do Calendário Nacional de Vacinação

---

## 💡 Dicas Importantes

- **Formato do arquivo:** O arquivo deve estar em formato CSV (exportado do E-SUS)
- **Encoding:** Certifique-se de que o arquivo está em UTF-8
- **Atualização:** Você pode carregar novos arquivos a qualquer momento
- **Filtros:** Use os filtros para segmentar análises por características específicas
- **Gráficos:** Todos os gráficos são interativos - passe o mouse para ver detalhes

---

## ❓ Dúvidas Frequentes

**P: O arquivo não é reconhecido. O que fazer?**
- R: Verifique se o arquivo está em formato CSV
- Verifique se o arquivo foi exportado corretamente do E-SUS
- Tente abrir o arquivo em um editor de texto para confirmar o formato

**P: Posso usar dados de diferentes unidades?**
- R: Sim, você pode fazer upload de dados de diferentes unidades
- Cada upload substitui os dados anteriores

**P: Os dados são salvos no servidor?**
- R: Não, os dados são processados localmente na sua sessão
- Quando você fecha o navegador, os dados são descartados
""")
