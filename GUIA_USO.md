# Guia de Uso - Dashboard de Desenvolvimento Infantil

## Começando

### 1. Iniciar a Aplicação

```bash
cd /home/ubuntu/dashboard_streamlit
source venv/bin/activate
streamlit run app.py
```

A aplicação abrirá automaticamente no navegador em `http://localhost:8501`.

### 2. Interface Principal

O dashboard é dividido em três áreas principais:

```
┌─────────────────────────────────────────────────────────────┐
│                      TÍTULO E DESCRIÇÃO                      │
├──────────────┬──────────────────────────────────────────────┤
│              │                                              │
│   FILTROS    │          CONTEÚDO PRINCIPAL                │
│   (Sidebar)  │                                              │
│              │  - Resumo Executivo                         │
│              │  - Indicadores                              │
│              │  - Gráficos                                 │
│              │  - Tabelas                                  │
│              │                                              │
└──────────────┴──────────────────────────────────────────────┘
```

## Usando os Filtros

### Filtro de Sexo

1. Clique no campo "Sexo" na sidebar
2. Selecione uma opção:
   - **Todos:** Exibe todas as crianças
   - **Masculino:** Exibe apenas meninos
   - **Feminino:** Exibe apenas meninas

**Efeito:** O dashboard atualiza automaticamente mostrando apenas dados das crianças selecionadas.

### Filtro de Raça/Cor

1. Clique no campo "Raça/Cor"
2. Selecione uma opção:
   - **Todos:** Todas as raças/cores
   - **BRANCA, PARDA, PRETA, INDÍGENA, AMARELA:** Categorias específicas

**Efeito:** Filtra crianças pela raça/cor informada.

### Filtro de Faixa Etária

1. Clique no campo "Faixa Etária"
2. Selecione uma opção:
   - **Todos:** Todas as idades
   - **0-6 meses:** Recém-nascidos até 6 meses
   - **6-12 meses:** 6 meses até 1 ano
   - **12-24 meses:** 1 ano até 2 anos

**Efeito:** Mostra apenas crianças na faixa etária selecionada.

### Filtro de Bairro

1. Clique no campo "Bairro"
2. Digite para buscar ou selecione múltiplos bairros
3. Pressione Enter ou clique fora para aplicar

**Efeito:** Filtra crianças pelos bairros selecionados.

### Filtro de Status Geral

1. Clique no campo "Status Geral"
2. Selecione:
   - **Todos:** Todas as crianças
   - **Conforme:** Crianças com 100 pontos (todos os indicadores)
   - **Não-conforme:** Crianças com menos de 100 pontos

**Efeito:** Mostra apenas crianças com o status selecionado.

### Filtro por Indicador

1. Clique no campo "Indicador" (em "Filtrar por Indicador")
2. Selecione:
   - **Todos:** Sem filtro por indicador
   - **A, B, C, D, E:** Mostra apenas crianças conformes naquele indicador

**Efeito:** Filtra crianças que atendem ao indicador específico.

### Limpar Todos os Filtros

1. Clique no botão **"🔄 Limpar Filtros"**
2. O dashboard volta ao estado inicial com todos os dados

## Entendendo as Visualizações

### Resumo Executivo

Mostra três métricas principais:

| Métrica | Significado |
|---------|-------------|
| **Total de Crianças** | Quantidade de crianças no filtro atual |
| **Conformes** | Crianças com 100 pontos (todos os indicadores atendidos) |
| **Não-conformes** | Crianças com menos de 100 pontos |

### Indicadores de Conformidade

Cinco cards mostram cada indicador:

```
┌─────────────────────────────────────┐
│ Indicador A                         │
│ 1ª Consulta Presencial              │
│ 66.1%                               │
│ 41 de 62 crianças                   │
└─────────────────────────────────────┘
```

**O que significa:**
- **66.1%:** Percentual de crianças que tiveram 1ª consulta até 30º dia
- **41 de 62:** 41 crianças atenderam, 62 é o total

### Gráfico de Conformidade por Indicador

Gráfico de barras mostrando o percentual de conformidade de cada indicador.

**Como ler:**
- Eixo X: Indicadores (A, B, C, D, E)
- Eixo Y: Percentual de conformidade (0-100%)
- Barras mais altas = melhor conformidade

**Exemplo:**
```
100% ┤
  80% ┤     ████
  60% ┤ ████    ████
  40% ┤
  20% ┤        ██
   0% ┤────────────
       A  B  C  D  E
```

### Gráfico de Status Geral

Gráfico de pizza mostrando proporção de conformes vs não-conformes.

**Como ler:**
- Fatia verde = Crianças conformes
- Fatia vermelha = Crianças não-conformes
- Percentual ao lado de cada fatia

### Distribuição por Faixa Etária

Gráfico de barras mostrando quantas crianças em cada faixa etária.

**Útil para:** Entender a distribuição etária do grupo.

### Distribuição por Sexo

Gráfico de pizza mostrando proporção de meninos vs meninas.

**Útil para:** Verificar equilíbrio de gênero na amostra.

### Heatmap de Conformidade

Tabela colorida mostrando conformidade de cada indicador por faixa etária.

**Como ler:**
- Cores mais verdes = maior conformidade
- Cores mais vermelhas = menor conformidade
- Números mostram percentual exato

**Exemplo:**
```
        A    B    C    D    E
0-6m   92%  12%  0%   83%  0%
6-12m  51%  8%   0%   81%  49%
12-24m 0%   0%   0%   100% 100%
```

## Trabalhando com a Tabela de Crianças

### Visualizar Dados

A tabela mostra todas as crianças com as seguintes colunas:

| Coluna | Descrição |
|--------|-----------|
| Nome | Identificador da criança |
| Data de nascimento | Data de nascimento |
| Idade | Idade em formato legível |
| Sexo | Masculino/Feminino |
| Raça/cor | Raça/cor informada |
| Bairro | Bairro de residência |
| A, B, C, D, E | ✓ (conforme) ou ✗ (não-conforme) |
| Pontuação | Total de pontos (0-100) |
| Status | Conforme ou Não-conforme |

### Buscar na Tabela

1. Clique no campo "Type to search" acima da tabela
2. Digite o nome da criança ou qualquer valor
3. A tabela filtra em tempo real

### Exportar Dados

1. Clique no botão **"📥 Exportar CSV"**
2. Um arquivo CSV será baixado com os dados filtrados
3. Abra em Excel, Google Sheets ou outro programa

## Interpretando os Indicadores

### Indicador A: 1ª Consulta Presencial
- **Meta:** 1ª consulta até 30º dia de vida
- **Pontos:** 20
- **Conforme se:** Data da 1ª consulta ≤ 30 dias após nascimento
- **Importância:** Detecção precoce de problemas

### Indicador B: Consultas Presenciais/Remotas
- **Meta:** Mínimo 9 consultas até 2 anos
- **Pontos:** 20
- **Conforme se:** Quantidade de consultas ≥ 9
- **Importância:** Acompanhamento contínuo do desenvolvimento

### Indicador C: Medições Peso/Altura
- **Meta:** Mínimo 9 registros simultâneos até 2 anos
- **Pontos:** 20
- **Conforme se:** Quantidade de medições ≥ 9
- **Importância:** Monitoramento do crescimento

### Indicador D: Visitas Domiciliares
- **Meta:** Mínimo 2 visitas domiciliares
- **Pontos:** 20
- **Conforme se:** Quantidade de visitas ≥ 2
- **Importância:** Avaliação do ambiente familiar

### Indicador E: Vacinação Completa
- **Meta:** Todas as vacinas obrigatórias
- **Pontos:** 20
- **Conforme se:** Todas as vacinas registradas
- **Importância:** Proteção contra doenças preveníveis

## Análises Comuns

### 1. Qual indicador tem pior desempenho?

1. Olhe o gráfico "Conformidade por Indicador"
2. A barra mais baixa é o indicador com pior desempenho
3. Clique no filtro de Indicador e selecione aquele indicador
4. Veja quais crianças não estão conformes

### 2. Há diferença entre meninos e meninas?

1. Filtre por Sexo = Masculino
2. Anote os percentuais dos indicadores
3. Limpe o filtro e filtre por Sexo = Feminino
4. Compare os percentuais

### 3. Qual faixa etária tem melhor conformidade?

1. Olhe o heatmap de conformidade
2. Procure a linha com mais cores verdes
3. Ou filtre por Faixa Etária e observe os percentuais

### 4. Quais crianças precisam de atenção urgente?

1. Filtre por Status Geral = Não-conforme
2. Ordene pela Pontuação (mais baixas primeiro)
3. Veja quais crianças têm menos pontos
4. Identifique quais indicadores estão faltando

## Dicas e Truques

### Combinar Filtros

Você pode combinar múltiplos filtros:
- Sexo = Feminino + Faixa Etária = 0-6 meses
- Bairro = [selecione vários] + Status = Não-conforme
- Indicador = A + Raça/Cor = BRANCA

### Usar Heatmap para Análise Rápida

O heatmap mostra padrões rapidamente:
- Coluna vermelha = indicador com problema geral
- Linha vermelha = faixa etária com problema
- Célula vermelha = combinação específica com problema

### Exportar para Análise Posterior

1. Aplique os filtros desejados
2. Clique "Exportar CSV"
3. Abra em Excel para análises adicionais
4. Crie gráficos e relatórios personalizados

### Compartilhar Visualizações

1. Aplique os filtros desejados
2. Tire screenshot da visualização
3. Compartilhe com a equipe
4. Ou compartilhe o link do dashboard

## Problemas Comuns

### "Nenhuma criança encontrada"

Isso significa que nenhuma criança atende aos critérios dos filtros aplicados.

**Solução:** Clique "🔄 Limpar Filtros" para resetar.

### Números não fazem sentido

Verifique se os filtros estão aplicados corretamente:
1. Olhe a mensagem azul que diz "Exibindo X de Y crianças"
2. Verifique cada filtro na sidebar
3. Clique "🔄 Limpar Filtros" se necessário

### Gráficos não aparecem

Isso pode acontecer se:
1. Nenhuma criança atende aos filtros (veja acima)
2. A aplicação está carregando (aguarde alguns segundos)
3. Há um erro (verifique o console do navegador)

## Próximos Passos

Após explorar o dashboard:

1. **Identificar problemas:** Quais indicadores têm baixa conformidade?
2. **Analisar causas:** Por que certas crianças não estão conformes?
3. **Planejar ações:** O que fazer para melhorar a conformidade?
4. **Acompanhar progresso:** Volte ao dashboard periodicamente para ver melhorias

## Suporte

Se tiver dúvidas:
1. Consulte a seção "Próximas Melhorias" do README
2. Verifique a documentação técnica em PLANO_ARQUITETURA.md
3. Revise o código em `app.py` e módulos relacionados

---

**Última atualização:** 08 de dezembro de 2025
