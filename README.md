# Implementação de uma Linguagem de Domínio Específico para Comportamento de Carros Autônomos

## Sobre o Projeto

Este projeto apresenta o desenvolvimento de uma **DSL (Domain-Specific Language)** voltada para a modelagem de comportamentos de veículos autônomos em ambientes simulados.

A linguagem foi criada como trabalho da disciplina de **Teoria da Computação e Compiladores**, aplicando conceitos de:

- Gramáticas Formais
- Análise Léxica
- Análise Sintática
- Análise Semântica
- Interpretação de Linguagens
- Hierarquia de Chomsky

A DSL permite criar regras de comportamento para veículos utilizando comandos simples e específicos do domínio automotivo, abstraindo detalhes complexos de implementação presentes em linguagens de propósito geral.

---

# Objetivos

A linguagem proposta tem como objetivo permitir a especificação declarativa de comportamentos autônomos por meio de regras de alto nível.

## Funcionalidades principais:

- Leitura de sensores simulados
- Controle de velocidade
- Frenagem e aceleração
- Tomada de decisão condicional
- Controle de direção
- Estruturas de repetição
- Execução de regras automáticas

---

# Motivação

Linguagens de propósito geral como Python ou C++ exigem que o desenvolvedor lide com detalhes técnicos que não pertencem diretamente ao domínio de veículos autônomos.

A DSL proposta simplifica esse processo utilizando comandos semânticos específicos, como:

```dsl
acelerar(30)
frear(20)
virar(direita, 15)
```

Dessa forma:

- O código se torna mais legível
- As regras ficam mais fáceis de validar
- O sistema se torna mais seguro
- O desenvolvimento fica mais próximo do domínio automotivo

---

# Estrutura do Projeto

```bash
.
├── lexer/              # Análise léxica
├── parser/             # Parser e AST
├── semantic/           # Análise semântica
├── interpreter/        # Interpretador da DSL
├── examples/           # Exemplos de programas
├── docs/               # Documentação
├── tests/              # Testes
├── main.py             # Arquivo principal
└── README.md
```

---

# Funcionalidades da DSL

A linguagem oferece suporte para:

## Movimentação
- `acelerar(valor)`
- `frear(valor)`
- `virar(direcao, valor)`

## Controle
- `parar`
- `manter_velocidade`

## Decisão
- `se`
- `senao`

## Repetição
- `enquanto`

## Sensores
- `distancia_frente`
- `distancia_lateral`
- `velocidade`
- `obstaculo`

---

# Exemplo de Código na DSL

```dsl
acelerar(30)

enquanto (distancia_frente > 5) {

    manter_velocidade

    se (distancia_lateral < 3) entao {

        virar(direita, 20)

    } senao {

        virar(esquerda, 10)

    }
}

frear(50)
parar
```

---

# Gramática Formal (BNF)

```bnf
<programa> ::= <acao>
             | <acao> <programa>

<acao> ::= <movimento>
          | <controle>
          | <decisao>
          | <loop>

<movimento> ::= "acelerar" "(" <valor> ")"
              | "frear" "(" <valor> ")"
              | "virar" "(" <direcao> "," <valor> ")"

<controle> ::= "parar"
             | "manter_velocidade"

<decisao> ::= "se" "(" <condicao> ")" "entao"
              "{" <lista_acoes> "}"

            | "se" "(" <condicao> ")" "entao"
              "{" <lista_acoes> "}" "senao"
              "{" <lista_acoes> "}"

<loop> ::= "enquanto" "(" <condicao> ")"
           "{" <lista_acoes> "}"
```

---

# Exemplo de Saída

```bash
[INFO] Acelerando para 30 km/h
[INFO] Mantendo velocidade
[INFO] Distância lateral detectada
[ACTION] Virando à direita
[INFO] Obstáculo distante
[INFO] Freando veículo
[INFO] Veículo parado
```

---

# Classificação na Hierarquia de Chomsky

A DSL foi definida utilizando uma **Gramática Livre de Contexto (CFG)**, pertencente à:

## Classe 2 — Hierarquia de Chomsky

Características:

- Uso de recursão
- Estruturas condicionais
- Blocos aninhados
- Análise via parsers LL/LR

---

# Etapas do Interpretador

## Análise Léxica
Transforma o código-fonte em tokens.

Exemplos:
- PALAVRA_RESERVADA
- IDENTIFICADOR
- NÚMERO
- OPERADOR

---

## Análise Sintática
Valida a estrutura da linguagem utilizando a gramática BNF.

---

## Análise Semântica
Responsável por:

- Validar comandos
- Verificar sensores
- Garantir parâmetros válidos
- Evitar estruturas inválidas

---

## Interpretação
Executa os comandos da DSL simulando o comportamento do veículo.

---

# Tecnologias Utilizadas

- Python
- PyParsing
- Git
- GitHub

---

# Como Executar

## Clone o repositório

```bash
git clone https://github.com/DeibsonS/Projeto_DSL.git
```

## Entre na pasta do projeto

```bash
cd Projeto_DSL
```

## Execute o interpretador

```bash
python main.py examples/exemplo.dsl
```

---

# Fundamentação Teórica

O projeto foi baseado em conceitos clássicos de:

- Linguagens Formais
- Compiladores
- DSLs
- Autômatos
- Parsing
- AST (Abstract Syntax Tree)

---

# Referências

- Fowler, Martin — *Domain-Specific Languages*
- Aho, Lam, Sethi e Ullman — *Compilers: Principles, Techniques, and Tools*
- Hudak — *Modular Domain-Specific Languages and Tools*
- Shalev-Shwartz — *Safe and Scalable Self-driving Cars*

---

# Autores

- Bruno da Silva Godoy
- Deibson dos Santos Lima
- Gabriel Rodrigues da Silva

---

# Disciplina

Teoria da Computação e Compiladores  
FHO — Fundação Hermínio Ometto