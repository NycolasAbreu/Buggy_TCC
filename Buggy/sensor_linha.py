from machine import Pin
import time

class SensorLinha:
    """Classe para controlar os sensores de linha"""
    
    # Pinos dos sensores de linha
    R_TCRT = 26
    L_TCRT = 25
    
    estado_esquerda = 1
    estado_direita = 1
    
    def __init__(self):
        self.sensor_direita = Pin(self.R_TCRT, Pin.IN)
        self.sensor_esquerda = Pin(self.L_TCRT, Pin.IN)
        
    def direita(self):
        time.sleep(0.01)
        self.estado_direita = self.sensor_direita.value()
        return self.estado_direita
    
    def esquerda(self):
        time.sleep(0.01)
        self.estado_esquerda = self.sensor_esquerda.value()
        return self.estado_esquerda
    
if __name__ == '__main__':
    sensores = SensorLinha()
    while(1):
        print("direita = ", sensores.direita())
        print("esquerda =", sensores.esquerda())
