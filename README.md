# Autômato Celular de 1 Dimensão

Um autômato celular de 1 dimensão é um modelo matemático simples que consiste em um conjunto de células organizadas linearmente, onde cada célula pode estar em um estado específico. Essas células evoluem de acordo com regras predefinidas, influenciadas pelos estados de suas células vizinhas.

Este projeto implementa um autômato celular de 1 dimensão em Python, permitindo a geração e evolução de conjuntos de células ao longo do tempo, seguindo uma regra binária definida pelo usuário.

## Funcionamento do Autômato Celular

### Definição
O autômato celular é definido por:

- **Número máximo de gerações:** Determina por quantas iterações o autômato evoluirá.
- **Número de células:** Define o tamanho do conjunto de células.
- **Regra binária:** Um número decimal que representa a regra de transição para a próxima geração de células.

### Implementação
O código Python utiliza uma representação de matriz para armazenar as células. Cada célula pode ter um estado binário (0 ou 1). A regra de transição é aplicada a cada célula e suas vizinhas para determinar o próximo estado das células na geração seguinte.

## Como é utilizado

1. **Parâmetros de Entrada**
    - Durante a execução, o programa solicitará os seguintes parâmetros:
        - Número máximo de gerações.
        - Número de células.
        - Número decimal que representa a regra binária.

2. **Visualização**
    - O programa exibirá a evolução do autômato celular ao longo das gerações.

## Exemplo de Uso

Suponha que queiramos executar o autômato celular com 10 gerações, 20 células e a regra binária 30:

```
Número máximo de gerações: 10
Número de células: 20
Número decimal que representa a regra binária: 30
```

O programa exibirá a evolução das células ao longo das 10 gerações de acordo com a regra definida.

```
Geração 0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Geração 1: [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
Geração 2: [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
Geração 3: [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
Geração 4: [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
Geração 5: [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0]
Geração 6: [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
Geração 7: [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0]
Geração 8: [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0]
Geração 9: [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1]
Geração 10: [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0]
```
---
