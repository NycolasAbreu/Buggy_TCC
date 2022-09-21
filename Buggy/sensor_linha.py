from machine import Pin, Timer
import time

class SensorLinha:
    """Classe para controlar os sensores de linha"""

    def __init__(self):
        # Pinos dos sensores de linha
        self.R_TCRT = 26
        self.L_TCRT = 25

        self.sensor_direita = Pin(self.R_TCRT, Pin.IN)
        self.sensor_esquerda = Pin(self.L_TCRT, Pin.IN)
    
        self.estado_direita = 0
        self.estado_esquerda = 0
        self.amostras_direita = 100
        self.amostras_esquerda = 100
        self.amostras_filtro = 100

        self.tim1 = Timer(1)
        self.init_timer()
    
    def _recebe_valores(self, t):
        #print("direita = ", self.sensor_direita.value())
        #print(self.amostras_direita);
        if (self.sensor_direita.value() != self.estado_direita):
            # Se contagem = 0, debounce terminado
            self.amostras_direita -= 1
            if (self.amostras_direita <= 0):
                self.estado_direita = self.sensor_direita.value()
        else:
            self.amostras_direita = self.amostras_filtro

        #print("esquerda = ", self.sensor_esquerda.value())
        #print(self.amostras_esquerda);
        if (self.sensor_esquerda.value() != self.estado_esquerda):
            # Se contagem = 0, debounce terminado
            self.amostras_esquerda -= 1
            if (self.amostras_esquerda <= 0):
                self.estado_esquerda = self.sensor_esquerda.value()
        else:
            self.amostras_esquerda = self.amostras_filtro

    def direita(self):
        return self.estado_direita
    
    def esquerda(self):
        return self.estado_esquerda

    def init_timer(self, period_ms = 5):  # Cria um timer para atualizar o pulse_time a cada 500ms
        self.tim1.init(period=period_ms, mode=Timer.PERIODIC, callback=self._recebe_valores)
    
if __name__ == '__main__':
    sensores = SensorLinha()
    while(1):
        time.sleep_us(100);
        print("ESTADO DIREITA = ", sensores.direita())
        print("ESTADO ESQUERDA = ", sensores.esquerda())

        
