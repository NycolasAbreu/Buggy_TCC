from machine import Pin, Timer
import time

class SensorLinha:
    """Classe para controlar os sensores de linha"""
    
    # Pinos dos sensores de linha
    R_TCRT = 26
    L_TCRT = 25
    
    # Contagem para o debounce
    CONTAGEM = 100
    
    def __init__(self):
        self.sensor_direita = Pin(self.R_TCRT, Pin.IN)
        self.sensor_esquerda = Pin(self.L_TCRT, Pin.IN)
    
        self.estado_direita = 0
        self.estado_esquerda = 0
        self.amostras_direita = self.CONTAGEM
        self.amostras_esquerda = self.CONTAGEM

        self.tim1 = Timer(1)
        self.init_timer()
    
    def _recebe_valores(self, t):
        if (self.sensor_direita.value() != self.estado_direita):
            # Se contagem = 0, debounce terminado
            self.amostras_direita -= 1
            if (self.amostras_direita <= 0):
                self.estado_direita = self.sensor_direita.value()
        else:
            self.amostras_direita = self.CONTAGEM

        if (self.sensor_esquerda.value() != self.estado_esquerda):
            # Se contagem = 0, debounce terminado
            self.amostras_esquerda -= 1
            if (self.amostras_esquerda <= 0):
                self.estado_esquerda = self.sensor_esquerda.value()
        else:
            self.amostras_esquerda = self.CONTAGEM

    def direita(self):
        return self.estado_direita
    
    def esquerda(self):
        return self.estado_esquerda

    def init_timer(self, period_ms = 10):  # Cria um timer para atualizar o pulse_time a cada 500ms
        self.tim1.init(period=period_ms, mode=Timer.PERIODIC, callback=self._recebe_valores)
    
if __name__ == '__main__':
    sensores = SensorLinha()
    while(1):
        time.sleep(0.5)
        print("ESTADO DIREITA = ", sensores.direita())
        print("ESTADO ESQUERDA = ", sensores.esquerda())