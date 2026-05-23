class SemanticError(Exception):
    pass

class SemanticAnalyzer:
    def __init__(self):
        self.valid_sensors = ["distancia_frente", "distancia_lateral", "velocidade", "obstaculo"]
        self.valid_directions = ["esquerda", "direita"]

    def validate(self, ast):
        """Valida a Arvore Sintatica Abstrata (AST) recursivamente."""
        for action in ast:
            self._validate_action(action)

    # [acao, valor]
    def _validate_action(self, action):
        cmd = action[0]
        
        if cmd == "acelerar" or cmd == "frear":
            valor = action[1]
            if valor < 0:
                raise SemanticError(f"Erro no comando '{cmd}': O valor {valor} nao pode ser negativo")
            if cmd == "acelerar" and valor > 100:
                raise SemanticError(f"Erro no comando 'acelerar': Aceleracao de {valor} excede o limite de seguranca de 100")
        
        elif cmd == "virar":
            direcao = action[1]
            valor = action[2]
            if direcao not in self.valid_directions:
                raise SemanticError(f"Erro no comando 'virar': Direcao '{direcao}' invalida. Use 'esquerda' ou 'direita'")
            if valor < 0:
                raise SemanticError(f"Erro no comando 'virar': O valor {valor} nao pode ser negativo")

        elif cmd == "se":
            condicao = action[1]
            self._validate_condition(condicao)
            then_block = action[2]
            self.validate(then_block)
            if len(action) > 3:
                else_block = action[3]
                self.validate(else_block)

        elif cmd == "enquanto":
            condicao = action[1]
            self._validate_condition(condicao)
            loop_block = action[2]
            self.validate(loop_block)

        elif cmd in ["parar", "manter_velocidade"]:
            pass
        
        else:
            raise SemanticError(f"Erro semantico: Comando '{cmd}' nao e reconhecido pela linguagem")

    def _validate_condition(self, condition):
        sensor_name = condition[0]
        if sensor_name not in self.valid_sensors:
            raise SemanticError(f"Erro na condicao: Sensor '{sensor_name}' nao reconhecido.")