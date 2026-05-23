
import random
from loguru import logger

class Car:
    def __init__(self):
        self.velocity = 0
        self.distance_frente = 100
        self.distance_lateral = 50
        self.obstaculo = 0  # 0: no, 1: yes
        self.direction = 0  # degrees
        self.is_running = True

    def acelerar(self, valor):
        self.velocity += valor
        logger.info(f"[CAR] Acelerando: +{valor} | Velocidade Atual: {self.velocity}")

    def frear(self, valor):
        self.velocity = max(0, self.velocity - valor)
        logger.info(f"[CAR] Freando: -{valor} | Velocidade Atual: {self.velocity}")

    def virar(self, direcao, valor):
        if direcao == "esquerda":
            self.direction = (self.direction - valor) % 360
        else:
            self.direction = (self.direction + valor) % 360
        
        # Simulação: ao virar, o sensor frontal para de ler o obstáculo antigo
        self.distance_frente += valor 
        logger.info(f"[CAR] Virando para {direcao}: {valor} graus | Direção Atual: {self.direction:.1f}°")

    def parar(self):
        self.velocity = 0
        logger.info("[CAR] Parado.")

    def manter_velocidade(self):
        logger.info(f"[CAR] Mantendo velocidade atual: {self.velocity}")

    def get_sensor(self, name):
        # In a real simulator, these would come from the environment.
        # Here we simulate some variability.
        if name == "distancia_frente":
            # Simulate getting closer to something if moving
            self.distance_frente = max(0, self.distance_frente - (self.velocity // 10))
            return self.distance_frente
        elif name == "distancia_lateral":
            return self.distance_lateral
        elif name == "velocidade":
            return self.velocity
        elif name == "obstaculo":
            if self.distance_frente < 10:
                self.obstaculo = 1
            else:
                self.obstaculo = 0
            return self.obstaculo
        return 0

    def update_environment(self):
        """Randomly change environment to test logic."""
        if random.random() < 0.1:
            self.distance_frente = random.randint(5, 150)
            logger.info(f"[ENV] Sensor de frente atualizado: {self.distance_frente}")
