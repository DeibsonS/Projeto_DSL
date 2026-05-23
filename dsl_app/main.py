from semantic import SemanticAnalyzer, SemanticError
from interpreter import Interpreter
from parser import parse_code
from simulator import Car
from loguru import logger
import sys

def run_app(file_path):
    try:
        with open(file_path, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        logger.error(f"Erro: Arquivo '{file_path}' nao encontrado.")
        return

    logger.debug("Iniciando Parser (Análise Sintática)")
    try:
        ast = parse_code(code)
        logger.success("Sintaxe validada com sucesso!")
    except Exception as e:
        logger.error(f"Erro de sintaxe na DSL:\n{e}")
        return

    logger.debug("Iniciando Analisador Semântico")
    try:
        analyzer = SemanticAnalyzer()
        analyzer.validate(ast)
        logger.success("Semântica validada com sucesso!")
    except SemanticError as e:
        logger.error(f"Erro semântico na DSL: {e}")
        return
    except Exception as e:
        logger.error(f"Erro inesperado na análise semântica: {e}")
        return

    logger.debug("Iniciando Interpretador e Simulação")
    car = Car()
    interpreter = Interpreter(car)
    
    interpreter.run(ast)
    logger.info("Simulação Finalizada")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_app(sys.argv[1])
    else:
        logger.info("Uso: python main.py <arquivo_dsl.car>")
        logger.debug("Executando 'exemplo.car' padrão...")
        # Garantir que o exemplo no arquivo esteja correto
        with open('exemplo.car', 'w') as f:
            f.write("""

# GP de Monaco - Volta Rapida

# Largada na Sainte-Devote
acelerar(100)

enquanto (velocidade > 0) {
    # Alerta de Colisao (Outros carros ou Muros da Piscine)
    se (obstaculo == 1) entao {
        frear(90)
        virar(esquerda, 30)
    }

    # Curva Loews (Hairpin) - A curva mais lenta da Formula 1
    # Detectada por baixissima distancia frontal
    se (distancia_frente < 10) entao {
        frear(95)
        virar(direita, 120) # Curva em 'U'
        acelerar(40)
    } senao {
        # Curvas de Media Velocidade (Ex: Mirabeau ou Rascasse)
        se (distancia_frente < 30) entao {
            frear(50)
            virar(direita, 45)
            acelerar(30)
        } senao {
            # Secao de Alta: Tunel e Reta dos Boxes
            se (velocidade < 100) entao {
                acelerar(20)
            } senao {
                manter_velocidade
            }
        }
    }

    # Controle de Linha de Corrida
    se (distancia_lateral < 3) entao {
        virar(esquerda, 5) # Pequeno ajuste para o centro da pista
    }
}

frear(100)
parar
            """)
        run_app('exemplo.car')