# Dashboard Streamlit - Monitoramento de Desenvolvimento Infantil

## Visão Geral

Este dashboard foi desenvolvido para monitorar e avaliar indicadores de **cuidado no desenvolvimento infantil** baseado na **Nota Metodológica C2 do Ministério da Saúde**. A aplicação permite visualizar dados de 62 crianças (0-2 anos) e acompanhar 5 indicadores principais de qualidade do cuidado.

## Indicadores Monitorados

O dashboard avalia 5 indicadores principais, cada um valendo 20 pontos (total de 100 pontos):

| Indicador | Descrição | Meta |
|-----------|-----------|------|
| **A** | 1ª Consulta Presencial | Realizada até 30º dia de vida |
| **B** | Consultas Presenciais/Remotas | Mínimo 9 consultas até 2 anos |
| **C** | Medições Peso/Altura | Mínimo 9 registros simultâneos até 2 anos |
| **D** | Visitas Domiciliares | Mínimo 2 visitas (ACS/TACS) |
| **E** | Vacinação Completa | Difteria, Tétano, Coqueluche, Hepatite B, Haemophilus |

## Resultados Atuais

- **Total de Crianças:** 62
- **Conformes (100 pontos):** 0 (0.0%)
- **Não-conformes:** 62 (100.0%)

### Conformidade por Indicador

- **Indicador A:** 66.1% (41 crianças)
- **Indicador B:** 9.7% (6 crianças)
- **Indicador C:** 0.0% (0 crianças)
- **Indicador D:** 82.3% (51 crianças)
- **Indicador E:** 30.6% (19 crianças)

## Estrutura do Projeto

```
dashboard_streamlit/
├── app.py                          # Arquivo principal da aplicação
├── requirements.txt                # Dependências do projeto
├── dados_utf8.csv                  # Dados das crianças
├── PLANO_ARQUITETURA.md           # Documentação de arquitetura
├── README.md                       # Este arquivo
├── config/
│   ├── __init__.py
│   └── settings.py                 # Configurações globais
├── data/
│   ├── __init__.py
│   ├── loader.py                   # Carregamento de dados
│   └── processor.py                # Processamento e cálculo de indicadores
├── features/
│   ├── __init__.py
│   ├── filters/
│   │   ├── __init__.py
│   │   └── sidebar.py              # Componentes de filtro
│   └── visualizations/
│       ├── __init__.py
│       ├── charts.py               # Gráficos e visualizações
│       └── metrics.py              # Cards de métricas
└── venv/                           # Ambiente virtual Python
```

## Instalação e Execução

### Pré-requisitos

- Python 3.11+
- pip (gerenciador de pacotes Python)

### Passos para Executar

1. **Clonar ou copiar o projeto:**
   ```bash
   cd /home/ubuntu/dashboard_streamlit
   ```

2. **Criar e ativar ambiente virtual (se não existir):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Executar a aplicação:**
   ```bash
   streamlit run app.py
   ```

5. **Acessar no navegador:**
   - Local: `http://localhost:8501`
   - Rede: O Streamlit mostrará a URL da rede

## Funcionalidades

### Filtros Interativos

A sidebar esquerda oferece diversos filtros para análise segmentada:

- **Sexo:** Todos, Masculino, Feminino
- **Raça/Cor:** Todos, BRANCA, PARDA, PRETA, INDÍGENA, AMARELA
- **Faixa Etária:** Todos, 0-6 meses, 6-12 meses, 12-24 meses
- **Bairro:** Seleção múltipla de bairros
- **Status Geral:** Todos, Conforme, Não-conforme
- **Indicador:** Filtrar por indicador específico (A, B, C, D, E)

### Visualizações

1. **Resumo Executivo**
   - Cards com total de crianças, conformes e não-conformes
   - Métricas principais em destaque

2. **Indicadores de Conformidade**
   - Cards individuais para cada indicador
   - Percentual de conformidade
   - Quantidade de crianças conformes

3. **Gráficos Interativos**
   - Gráfico de barras: Conformidade por indicador
   - Gráfico de pizza: Status geral (conforme/não-conforme)
   - Gráfico de barras: Distribuição por faixa etária
   - Gráfico de pizza: Distribuição por sexo
   - Heatmap: Conformidade por indicador e faixa etária

4. **Listagem de Crianças**
   - Tabela interativa com dados detalhados
   - Busca e filtros de coluna
   - Opção de exportar para CSV

5. **Resumo Detalhado**
   - Interpretação textual dos indicadores
   - Metas e objetivos de cada indicador

## Módulos Principais

### `config/settings.py`
Centraliza todas as configurações:
- Cores e tema do dashboard
- Definições dos 5 indicadores
- Limites e metas
- Faixas etárias
- Configurações de página e dados

### `data/loader.py`
Responsável pelo carregamento e limpeza inicial:
- Carrega CSV com tratamento de encoding (ISO-8859-1 → UTF-8)
- Converte tipos de dados (datas, números)
- Normaliza colunas
- Função auxiliar para extrair idade em meses

### `data/processor.py`
Processa dados e calcula indicadores:
- Calcula idade em meses
- Determina faixa etária
- Calcula cada um dos 5 indicadores
- Calcula pontuação total (0-100)
- Determina status geral (conforme/não-conforme)
- Gera estatísticas agregadas

### `features/filters/sidebar.py`
Componentes de filtro interativos:
- Cria controles na sidebar
- Aplica filtros ao DataFrame
- Suporta múltiplos tipos de filtros

### `features/visualizations/charts.py`
Gráficos e visualizações:
- Gráficos de barras, pizza, heatmap
- Tabelas formatadas
- Todos os gráficos são interativos (Plotly)

### `features/visualizations/metrics.py`
Exibição de métricas e cards:
- Métricas principais em destaque
- Cards individuais de indicadores
- Resumo textual dos indicadores

### `app.py`
Arquivo principal que orquestra tudo:
- Configura página Streamlit
- Carrega e processa dados
- Cria filtros
- Renderiza visualizações
- Gerencia estado da aplicação

## Fluxo de Dados

```
CSV (dados_utf8.csv)
    ↓
loader.py (carrega e limpa)
    ↓
processor.py (processa e calcula indicadores)
    ↓
sidebar.py (aplica filtros)
    ↓
charts.py + metrics.py (gera visualizações)
    ↓
app.py (renderiza no Streamlit)
```

## Cálculo dos Indicadores

### Indicador A: 1ª Consulta Presencial
```python
Conforme se: (Data da 1ª consulta - Data de nascimento) <= 30 dias
```

### Indicador B: Consultas Presenciais/Remotas
```python
Conforme se: Quantidade de consultas até 24 meses >= 9
```

### Indicador C: Medições Peso/Altura
```python
Conforme se: Quantidade de medições simultâneas até 24 meses >= 9
```

### Indicador D: Visitas Domiciliares
```python
Conforme se: Quantidade de visitas domiciliares até 24 meses >= 2
```

### Indicador E: Vacinação Completa
```python
Conforme se: Todas as vacinas obrigatórias foram registradas
  - Difteria, Tétano, Pertusis, Hepatite B, Haemophilus (PENTA)
  - Poliomielite (VIP)
  - Sarampo, Caxumba, Rubéola (SCR)
  - Pneumocócica (VPC10)
```

## Pontuação Total

A pontuação total é calculada como:
```
Pontuação = (A × 20) + (B × 20) + (C × 20) + (D × 20) + (E × 20)
Máximo: 100 pontos
```

Uma criança é considerada **conforme** apenas se tiver **100 pontos** (todos os 5 indicadores atendidos).

## Tecnologias Utilizadas

- **Streamlit:** Framework web para criar dashboards interativos
- **Pandas:** Processamento e manipulação de dados
- **Plotly:** Gráficos interativos
- **Python 3.11:** Linguagem de programação

## Dependências

```
streamlit==1.28.1
pandas==2.0.3
plotly==5.17.0
python-dateutil==2.8.2
```

## Customizações Possíveis

### Alterar Cores
Edite `config/settings.py` na seção `COLORS`:
```python
COLORS = {
    "primary": "#1f77b4",
    "success": "#2ca02c",
    # ... outras cores
}
```

### Modificar Limites dos Indicadores
Edite `config/settings.py` na seção `INDICATOR_LIMITS`:
```python
INDICATOR_LIMITS = {
    "A": {"dias": 30},
    "B": {"consultas": 9},
    # ... outros limites
}
```

### Adicionar Novos Filtros
Edite `features/filters/sidebar.py` e `config/settings.py`:
1. Adicione a opção em `FILTROS`
2. Crie o controle na função `criar_filtros_sidebar()`
3. Implemente a lógica de filtro em `aplicar_filtros()`

### Adicionar Novos Gráficos
Crie uma função em `features/visualizations/charts.py` e chame-a em `app.py`:
```python
def criar_novo_grafico(df: pd.DataFrame) -> go.Figure:
    # Implementar gráfico
    pass
```

## Troubleshooting

### Erro: "Arquivo não encontrado: dados_utf8.csv"
- Certifique-se de que o arquivo `dados_utf8.csv` está no mesmo diretório que `app.py`
- Ou atualize o caminho em `config/settings.py`

### Erro de Encoding
- O arquivo CSV original está em ISO-8859-1
- Já foi convertido para UTF-8 em `dados_utf8.csv`
- Se precisar reconverter: `iconv -f ISO-8859-1 -t UTF-8 arquivo.csv > dados_utf8.csv`

### Aplicação Lenta
- Aumente o cache em `app.py` ajustando o decorator `@st.cache_data`
- Reduza o tamanho do dataset se necessário

## Próximas Melhorias

- [ ] Adicionar exportação em PDF
- [ ] Implementar gráficos de série temporal
- [ ] Criar relatórios automáticos por período
- [ ] Adicionar análise de tendências
- [ ] Integrar com banco de dados
- [ ] Implementar autenticação de usuários
- [ ] Adicionar mais indicadores
- [ ] Criar alertas para crianças fora da conformidade

## Suporte e Documentação

Para mais informações sobre:
- **Streamlit:** https://docs.streamlit.io
- **Pandas:** https://pandas.pydata.org/docs
- **Plotly:** https://plotly.com/python

## Licença

Este projeto foi desenvolvido para fins educacionais e de monitoramento de saúde pública.

## Autor

Desenvolvido como parte do projeto de Dashboard Streamlit para Monitoramento de Desenvolvimento Infantil.

---

**Última atualização:** 08 de dezembro de 2025
