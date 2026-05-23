from pyparsing import (
    Word, nums, Keyword, OneOrMore, Group, Optional, 
    Forward, Suppress, Literal, pythonStyleComment
)

def get_parser():
    # Basic tokens
    LPAR = Suppress("(")
    RPAR = Suppress(")")
    LBRACE = Suppress("{")
    RBRACE = Suppress("}")
    COMMA = Suppress(",")
    
    valor = Word(nums).setParseAction(lambda t: int(t[0]))
    direcao = Keyword("esquerda") | Keyword("direita")
    sensor = Keyword("distancia_frente") | Keyword("distancia_lateral") | \
             Keyword("velocidade") | Keyword("obstaculo")
    operador = Literal("<=") | Literal(">=") | Literal("==") | Literal("<") | Literal(">")

    # Forward declaration for nested structures
    acao = Forward()
    lista_acoes = OneOrMore(acao)

    # Movement Actions
    acelerar = Group(Keyword("acelerar") + LPAR + valor + RPAR)
    frear = Group(Keyword("frear") + LPAR + valor + RPAR)
    virar = Group(Keyword("virar") + LPAR + direcao + COMMA + valor + RPAR)
    
    # Control Actions
    parar = Group(Keyword("parar"))
    manter_velocidade = Group(Keyword("manter_velocidade"))

    # Conditions
    condicao = Group(sensor + operador + valor)

    # Decisions
    decisao = Group(
        Keyword("se") + LPAR + condicao + RPAR + Suppress(Keyword("entao")) + 
        LBRACE + Group(lista_acoes) + RBRACE + 
        Optional(Suppress(Keyword("senao")) + LBRACE + Group(lista_acoes) + RBRACE)
    )

    # Loops
    loop = Group(
        Keyword("enquanto") + LPAR + condicao + RPAR + 
        LBRACE + Group(lista_acoes) + RBRACE
    )

    # Combine all actions
    acao << (acelerar | frear | virar | parar | manter_velocidade | decisao | loop)

    # Program is one or more actions
    programa = OneOrMore(acao).setParseAction(lambda t: t.asList())
    programa.ignore(pythonStyleComment)
    
    return programa

def parse_code(code):
    parser = get_parser()
    return parser.parseString(code, parseAll=True)

if __name__ == "__main__":
    # Small test
    test_code = """
    # Comentario inicial
    acelerar(10)
    se (distancia_frente < 20) entao {
        frear(5)
        parar
    } senao {
        manter_velocidade
    }
    """
    try:
        result = parse_code(test_code)
        print("Parse successful!")
        print(result.asList())
    except Exception as e:
        print(f"Parse error: {e}")
