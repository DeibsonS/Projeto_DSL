
from loguru import logger
import operator

MAX_ITERETIONS = 100

class Interpreter:
    def __init__(self, car):
        self.car = car
        self.ops = {
            "<": operator.lt,
            ">": operator.gt,
            "==": operator.eq,
            "<=": operator.le,
            ">=": operator.ge
        }

    def evaluate_condition(self, condition):
        sensor_name, op_str, target_value = condition
        current_value = self.car.get_sensor(sensor_name)
        op_func = self.ops.get(op_str)
        result = op_func(current_value, target_value)
        return result

    def run(self, ast):
        for action in ast:
            self.execute_action(action)

    def execute_action(self, action):
        cmd = action[0]
        
        if cmd == "acelerar":
            self.car.acelerar(action[1])
        elif cmd == "frear":
            self.car.frear(action[1])
        elif cmd == "virar":
            self.car.virar(action[1], action[2])
        elif cmd == "parar":
            self.car.parar()
        elif cmd == "manter_velocidade":
            self.car.manter_velocidade()
        elif cmd == "se":
            cond = action[1]
            then_block = action[2]
            else_block = None
            if len(action) > 3:
                else_block = action[3]
            
            if self.evaluate_condition(cond):
                self.run(then_block)
            elif else_block:
                self.run(else_block)
                
        elif cmd == "enquanto":
            cond = action[1]
            loop_block = action[2]

            iters = 0
            while self.evaluate_condition(cond) and iters < MAX_ITERETIONS:
                self.run(loop_block)
                self.car.update_environment() # Simulate time passing
                iters += 1
            if iters == MAX_ITERETIONS:
                logger.warning("[WARNING] Loop 'enquanto' atingiu o limite de iteracoes! Finalizando aplicacao.")
