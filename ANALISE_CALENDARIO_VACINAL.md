# Análise do Calendário Nacional de Vacinação

## Vacinas Obrigatórias para Indicador E (até 2 anos)

Com base no Calendário Nacional de Vacinação - Criança (0 a 9 anos, 11 meses e 29 dias), as vacinas obrigatórias para o indicador E até 2 anos de idade são:

### 1. **Penta (DTP + Hib + HB)** - Difteria, Tétano, Coqueluche, Hepatite B, Haemophilus
- **Doses até 2 anos:** 3 doses
- **Cronograma:**
  - 1ª dose: 2 meses
  - 2ª dose: 4 meses
  - 3ª dose: 6 meses

### 2. **Poliomielite Inativada (VIP)**
- **Doses até 2 anos:** 3 doses
- **Cronograma:**
  - 1ª dose: 2 meses
  - 2ª dose: 4 meses
  - 3ª dose: 6 meses

### 3. **Pneumocócica 10-valente (VPC10)**
- **Doses até 2 anos:** 3 doses
- **Cronograma:**
  - 1ª dose: 2 meses
  - 2ª dose: 4 meses
  - 3ª dose: 6 meses
  - 1 dose reforço: 12 meses

### 4. **Tríplice Viral (SCR)** - Sarampo, Caxumba, Rubéola
- **Doses até 2 anos:** 1 dose
- **Cronograma:**
  - 1ª dose: 12 meses

### 5. **Hepatite B**
- **Doses até 2 anos:** 1 dose
- **Cronograma:**
  - Ao nascer (dose 0)
  - Mais 2 doses no esquema Penta (2 e 4 meses)

## Doses Mínimas Recomendadas até 2 Anos

| Vacina | Doses Mínimas |
|--------|---------------|
| Penta (DTP + Hib + HB) | 3 doses |
| Poliomielite Inativada (VIP) | 3 doses |
| Pneumocócica 10-valente | 3 doses |
| Tríplice Viral (SCR) | 1 dose |
| **Total de aplicações** | **10 doses** |

## Interpretação para o Indicador E

Uma criança é considerada **conforme no Indicador E** quando tem registradas:

✓ **Mínimo 3 doses de Penta** (DTP + Hib + HB)
✓ **Mínimo 3 doses de Poliomielite Inativada (VIP)**
✓ **Mínimo 3 doses de Pneumocócica 10-valente**
✓ **Mínimo 1 dose de Tríplice Viral (SCR)**

## Observações Importantes

1. **Hepatite B:** A dose ao nascer é importante, mas as doses 2 e 3 estão incluídas na Penta
2. **Reforços:** Não são contados para o indicador até 2 anos (são após 12 meses)
3. **Variações:** O calendário permite variações conforme notas de rodapé, mas as doses mínimas acima são o padrão
4. **Intervalo:** Deve haver intervalo mínimo de 30 dias entre as doses

## Validação de Dados no Dashboard

Para validar se uma criança está conforme no Indicador E:

1. Contar doses de **Penta** (DTP/HepB/Hib) - deve ter ≥ 3
2. Contar doses de **VIP** (Poliomielite) - deve ter ≥ 3
3. Contar doses de **VPC10** (Pneumocócica) - deve ter ≥ 3
4. Verificar se tem **SCR** (Sarampo, Caxumba, Rubéola) - deve ter ≥ 1

Se todas as condições acima forem atendidas = **Conforme**
Se alguma condição não for atendida = **Não-conforme**

## Mapeamento de Colunas do CSV

Baseado no CSV fornecido, as colunas relevantes são:

- `Difteria, Tétano, Pertusis, Hepatite B, Haemophilus Influenza B` → **Penta**
- `Poliomielite` → **VIP**
- `Sarampo, Caxumba, Rubéola` → **SCR**
- `Pneumocócica` → **VPC10**

Cada coluna contém um texto com as doses registradas no formato:
```
D - [data] - [nome da vacina] | D1 - [data] - [nome da vacina] | D2 - [data] - [nome da vacina] | ...
```

Onde:
- `D` = Dose ao nascer
- `D1`, `D2`, `D3` = 1ª, 2ª, 3ª doses
- `REF` = Reforço
