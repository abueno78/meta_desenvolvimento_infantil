"""Página Sobre"""
import streamlit as st
import os

st.markdown("## Sobre Este Dashboard")

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

#### Indicadores Avaliados

O sistema avalia 5 indicadores principais para crianças de 0 a 2 anos atendidas na Atenção Primária à Saúde:

#### **Meta 1 - 1ª Consulta Presencial**
- **Descrição:** Ter a 1ª consulta presencial realizada por médica(o) ou enfermeira(o), até o 30º dia de vida.
- **Variáveis utilizadas:** `Data da primeira consulta`, `Data de nascimento`
- **Cálculo:** Verifica se a diferença entre a data da primeira consulta e a data de nascimento é ≤ 30 dias
- **Formatação:** Conversão de datas para formato datetime, cálculo de diferença em dias

#### **Meta 2 - Consultas Presenciais ou Remotas**
- **Descrição:** Ter pelo menos 09 (nove) consultas presenciais ou remotas realizadas por médica(o) ou enfermeira(o) até dois anos de vida.
- **Variáveis utilizadas:** `Quantidade de consultas até 24 meses`
- **Cálculo:** Verifica se a quantidade de consultas é ≥ 9
- **Formatação:** Conversão de valores numéricos, tratamento de valores nulos

#### **Meta 3 - Registros de Peso e Altura**
- **Descrição:** Ter pelo menos 09 (nove) registros simultâneos de peso e altura até os dois anos de vida.
- **Variáveis utilizadas:** `Quantidade de medições de peso/altura simultâneas até 24 meses`
- **Cálculo:** Verifica se a quantidade de medições simultâneas é ≥ 9
- **Formatação:** Conversão de valores numéricos, tratamento de valores nulos

#### **Meta 4 - Visitas Domiciliares**
- **Descrição:** Ter pelo menos 02 (duas) visitas domiciliares realizadas por ACS/TACS, sendo a primeira até os primeiros 30(trinta) dias de vida e a segunda até os 06 (seis) meses de vida.
- **Variáveis utilizadas:** `Data da primeira visita domiciliar`, `Data da segunda visita domiciliar`, `Data de nascimento`
- **Cálculo:** Verifica se:
  - Primeira visita ocorreu até 30 dias após o nascimento (diferença ≤ 30 dias)
  - Segunda visita ocorreu até 6 meses após o nascimento (diferença ≤ 180 dias)
  - Ambas as datas estão preenchidas
- **Formatação:** Conversão de datas para formato datetime, cálculo de diferenças em dias, validação de ambas as condições

#### **Meta 5 - Vacinação Completa**
- **Descrição:** Ter vacinas contra difteria, tétano, coqueluche, hepatite B, infecções causadas por Haemophilus influenza e tipo b, poliomielite, sarampo, caxumba e rubéola, pneumocócica, registradas com todas as doses recomendadas.
- **Variáveis utilizadas:**
  - `Difteria, Tétano, Pertusis, Hepatite B, Haemophilus Influenza B` (Penta - 3 doses)
  - `Poliomielite` (VIP - 3 doses)
  - `Sarampo, Caxumba, Rubéola` (SCR - 1 dose)
  - `Pneumocócica` (VPC10 - 3 doses)
- **Cálculo:** Verifica se todas as doses recomendadas foram registradas:
  - Penta com 3 doses
  - VIP com 3 doses
  - SCR com 1 dose
  - VPC10 com 3 doses
- **Formatação:** Parsing de strings com informações de doses, contagem de doses por vacina, validação de conformidade com calendário nacional

#### Metodologia de Cálculo

Cada indicador é calculado como um valor booleano (Conforme/Não-conforme):
- **Conforme (✓):** Criança atende aos critérios da meta
- **Não-conforme (✗):** Criança não atende aos critérios da meta

A **conformidade percentual** de cada meta é calculada como:
```
Conformidade (%) = (Quantidade de Conformes / Total de Crianças) × 100
```

#### Análises Disponíveis

O dashboard apresenta análises segmentadas por:
- **Sexo:** Masculino, Feminino, Não informado
- **Raça/Cor:** Conforme categorias do IBGE
- **Bolsa Família:** Beneficiários e não-beneficiários
- **Microárea:** Divisões territoriais da unidade de saúde

Para cada segmento, são exibidos:
- Valores absolutos (quantidade de crianças)
- Valores relativos (percentual de conformidade)

---

### Tecnologias Utilizadas

- **Streamlit** - Framework para aplicações web em Python
- **Pandas** - Manipulação e análise de dados
- **Plotly** - Visualizações interativas
- **Python 3.11** - Linguagem de programação

---

### Documentação

Abaixo estão disponíveis os documentos de referência utilizados no desenvolvimento deste dashboard:

""")

# Seção de Downloads
st.markdown("#### 📥 Downloads de Documentos")

# Diretório de assets
assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")

# Verificar e oferecer downloads
docs = {
    "Nota Metodológica C2 - Cuidado no Desenvolvimento Infantil": 
        os.path.join(assets_dir, "Nota Metodológica C2 - Cuidado no desenvolvimento infantil.pdf"),
    "Calendário Nacional de Vacinação - Criança": 
        os.path.join(assets_dir, "CalendárioNacionaldeVacinação-Criança.pdf")
}

col1, col2 = st.columns(2)

with col1:
    if os.path.exists(docs["Nota Metodológica C2 - Cuidado no Desenvolvimento Infantil"]):
        with open(docs["Nota Metodológica C2 - Cuidado no Desenvolvimento Infantil"], "rb") as f:
            st.download_button(
                label="📄 Nota Metodológica C2",
                data=f,
                file_name="Nota_Metodologica_C2.pdf",
                mime="application/pdf",
                key="download_nota_c2"
            )
    else:
        st.warning("Arquivo Nota Metodológica C2 não encontrado")

with col2:
    if os.path.exists(docs["Calendário Nacional de Vacinação - Criança"]):
        with open(docs["Calendário Nacional de Vacinação - Criança"], "rb") as f:
            st.download_button(
                label="📄 Calendário Vacinal",
                data=f,
                file_name="Calendario_Vacinal.pdf",
                mime="application/pdf",
                key="download_calendario"
            )
    else:
        st.warning("Arquivo Calendário Vacinal não encontrado")

st.markdown("""
---

**Versão:** 3.0.0  
**Data:** Dezembro de 2025  
**Instituição:** PUCRS - Escola de Ciências da Saúde e da Vida
""")
