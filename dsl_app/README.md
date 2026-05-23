
# Autonomous Car DSL Application

Esta aplicação implementa uma infraestrutura base para uma DSL de comportamento de carros autônomos.

## Estrutura do Projeto

- `parser.py`: Utiliza a biblioteca `pyparsing` para transformar o código da DSL em uma Árvore de Sintaxe Abstrata (AST).
- `simulator.py`: Simula um carro com sensores (`distancia_frente`, `velocidade`, etc.) e atuadores (`acelerar`, `frear`, `virar`).
- `interpreter.py`: Percorre a AST e executa as ações no simulador, tratando lógica de decisão (`se`) e repetição (`enquanto`).
- `main.py`: Ponto de entrada que lê um arquivo `.car` e executa a simulação.

## Como Usar

1. Certifique-se de ter o Python instalado.
2. Instale a dependência `pyparsing` (se necessário):
   ```bash
   pip install pyparsing
   ```
3. Execute o programa:
   ```bash
   python dsl_app/main.py
   ```

## Exemplo de Código DSL

```bnf
acelerar(50)
se (distancia_frente < 30) entao {
    frear(20)
    virar(esquerda, 90)
} senao {
    acelerar(10)
}

enquanto (velocidade > 0) {
    frear(15)
    se (velocidade < 10) entao {
        parar
    }
}
```
