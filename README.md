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

## Instalação e Execução

### Pré-requisitos

- Python 3.11+
- pip (gerenciador de pacotes Python)

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

## Suporte e Documentação

Para mais informações sobre:
- **Streamlit:** https://docs.streamlit.io
- **Pandas:** https://pandas.pydata.org/docs
- **Plotly:** https://plotly.com/python

## Licença

Este projeto foi desenvolvido para fins educacionais e de monitoramento de saúde pública.

## Autores

André Scolare Bueno, Aline Zorzi, Ana Clara Araujo, Cássia Vieira Stravalacci, Celina Fagundes Silva, Geisiane Souza Soares, Larissa Silva, Luiza Cunha Oliveira, Maiara Vargas Cardoso, Marinice Ferreira Rosa, Raissa Cervelin Garcia e Raquel Pienis Garcia.

---

**Última atualização:** 08 de dezembro de 2025
