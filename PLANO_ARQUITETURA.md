# Plano de Arquitetura - Dashboard Streamlit

## Objetivo
Criar um dashboard modular para monitoramento de indicadores de desenvolvimento infantil baseado na metodologia C2 do Ministério da Saúde.

## Estrutura Modular

```
dashboard_streamlit/
├── app.py                          # Arquivo principal da aplicação
├── requirements.txt                # Dependências do projeto
├── config/
│   ├── __init__.py
│   └── settings.py                 # Configurações globais
├── data/
│   ├── __init__.py
│   ├── loader.py                   # Carregamento e limpeza de dados
│   └── processor.py                # Processamento e cálculo de indicadores
├── features/
│   ├── __init__.py
│   ├── indicators/
│   │   ├── __init__.py
│   │   ├── calculator.py           # Cálculo dos 5 indicadores
│   │   └── definitions.py          # Definições dos indicadores
│   ├── filters/
│   │   ├── __init__.py
│   │   └── sidebar.py              # Componentes de filtro
│   └── visualizations/
│       ├── __init__.py
│       ├── charts.py               # Gráficos e visualizações
│       └── metrics.py              # Cards de métricas
├── pages/
│   ├── __init__.py
│   ├── home.py                     # Página inicial/resumo
│   ├── indicators.py               # Detalhamento dos indicadores
│   └── children.py                 # Listagem de crianças
└── utils/
    ├── __init__.py
    └── helpers.py                  # Funções auxiliares
```

## Módulos Principais

### 1. **config/settings.py**
- Configurações globais (cores, temas, constantes)
- Definições de parâmetros dos indicadores

### 2. **data/loader.py**
- Carregamento do CSV com tratamento de encoding
- Limpeza e normalização de dados
- Conversão de tipos

### 3. **data/processor.py**
- Processamento de datas
- Cálculo de idade
- Agregações por grupos

### 4. **features/indicators/calculator.py**
Cálculo dos 5 indicadores:
- **A**: 1ª consulta presencial até 30º dia
- **B**: Mínimo 9 consultas até 2 anos
- **C**: Mínimo 9 registros de peso/altura
- **D**: Mínimo 2 visitas domiciliares
- **E**: Vacinação completa

### 5. **features/filters/sidebar.py**
- Filtros por sexo, raça/cor, bairro
- Filtro por faixa etária
- Filtro por status de indicadores

### 6. **features/visualizations/charts.py**
- Gráficos de distribuição dos indicadores
- Gráficos de série temporal
- Heatmaps de conformidade

### 7. **pages/home.py**
- KPIs principais (% de conformidade)
- Resumo dos 5 indicadores
- Distribuição geral

### 8. **pages/indicators.py**
- Detalhamento de cada indicador
- Crianças em conformidade vs não-conformidade
- Análises por grupo demográfico

### 9. **pages/children.py**
- Tabela interativa de crianças
- Filtros avançados
- Detalhes individuais

## Indicadores a Calcular

| Indicador | Métrica | Cálculo |
|-----------|---------|---------|
| A | 1ª consulta até 30º dia | % de crianças com 1ª consulta ≤ 30 dias |
| B | 9+ consultas até 2 anos | % de crianças com ≥ 9 consultas |
| C | 9+ medições peso/altura | % de crianças com ≥ 9 registros simultâneos |
| D | 2+ visitas domiciliares | % de crianças com ≥ 2 visitas |
| E | Vacinação completa | % de crianças com esquema vacinal completo |

## Filtros Interativos

1. **Sexo**: Masculino, Feminino, Todos
2. **Raça/Cor**: BRANCA, PARDA, PRETA, INDÍGENA, AMARELA, Todos
3. **Bairro**: Seleção múltipla
4. **Faixa Etária**: 0-6 meses, 6-12 meses, 12-24 meses, Todos
5. **Status Indicador**: Conforme, Não-conforme, Todos

## Visualizações Principais

1. **KPI Cards**: % de conformidade por indicador
2. **Gráfico de Barras**: Distribuição de conformidade
3. **Gráfico de Pizza**: Proporção conforme vs não-conforme
4. **Heatmap**: Conformidade por indicador e grupo demográfico
5. **Tabela Interativa**: Listagem de crianças com detalhes
6. **Gráfico de Série Temporal**: Evolução das consultas ao longo do tempo

## Tecnologias

- **Streamlit**: Framework web
- **Pandas**: Processamento de dados
- **Plotly**: Visualizações interativas
- **Python 3.11**: Linguagem

## Fluxo de Dados

1. Carregamento do CSV (data/loader.py)
2. Processamento (data/processor.py)
3. Cálculo de indicadores (features/indicators/calculator.py)
4. Aplicação de filtros (features/filters/sidebar.py)
5. Geração de visualizações (features/visualizations/charts.py)
6. Renderização em páginas (pages/*.py)
