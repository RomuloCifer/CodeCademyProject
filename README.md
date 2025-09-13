# Insurance Cost Analysis Tool

Este projeto é uma ferramenta de análise de dados de custos de seguros de saúde, permitindo filtrar e analisar informações sobre segurados com base em diversos critérios como idade, IMC, região, hábito de fumar e custos.

## 📊 Conjunto de Dados

O projeto utiliza um dataset (`insurance.csv`) que contém as seguintes informações:
- `age`: Idade do segurado
- `sex`: Gênero do segurado
- `bmi`: Índice de Massa Corporal
- `children`: Número de dependentes
- `smoker`: Status de fumante (yes/no)
- `region`: Região geográfica (northeast/northwest/southeast/southwest)
- `charges`: Custos do seguro

## 🚀 Funcionalidades

1. **Filtros Individuais**: Filtrar dados por qualquer campo com operadores de comparação
2. **Filtros Múltiplos**: Aplicar múltiplos filtros simultaneamente (AND)
3. **Filtro Regional**: Filtrar segurados por região específica
4. **Análise de Fumantes**: Separar e analisar dados de fumantes e não fumantes
5. **Cálculo de Médias**: Calcular média de custos para qualquer conjunto filtrado
6. **Reset de Dados**: Opção para voltar ao dataset completo

## 💻 Como Usar

1. Certifique-se de ter Python instalado em seu sistema
2. Clone este repositório
3. Execute o script principal:
```bash
python Insurance_costs.py
```

### Menu de Opções

- `[1]` Filtrar por uma condição
- `[2]` Filtrar por várias condições (AND)
- `[3]` Filtrar por região
- `[4]` Filtrar fumantes/não fumantes
- `[5]` Calcular média de custos do conjunto atual
- `[6]` Resetar para o dataset completo
- `[0]` Sair

### Exemplo de Uso

```python
# Filtrar pessoas com mais de 30 anos
Campo: age
Operador: >
Valor: 30

# Filtrar por região
Região: northeast

# Ver média de custos
[5] Média de charges do conjunto atual
```

## 🛠 Requisitos

- Python 3.x
- Módulo CSV (built-in)

## 📝 Estrutura do Código

O código está organizado em várias funções principais:

- `filtrar_valor()`: Filtra registros por valor específico
- `filtrar_local()`: Filtra por região
- `filtrar_fumantes()`: Filtra fumantes/não fumantes
- `contar_fumantes()`: Conta quantidade de fumantes
- `filtrar_and()`: Aplica múltiplos filtros
- `media_charges()`: Calcula média de custos
- `main()`: Loop principal do programa

## 👥 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Enviar pull requests

## 📄 Licença

Este projeto é open source e disponível sob a licença MIT.

### README feito pelo copilot <3