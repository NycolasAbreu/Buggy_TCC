from machine import Pin
import machine
from time import time

class Encoder:
    """Classe para controlar os Encoders de velocidade"""
    
    IRQ = 20  # Num de interrupções por revolução
    INTERVALO = 0.5  # Frequencia que sera calculado o rpm
    
    # Recebe o pino do encoder pelo construtor
    def __init__(self, pinEncoder):
        self.time0 = time() # Tempo para fazer o calculo da velocidade
        self.counter = 0
        self.rpm = 0.0
        self.freq = 0
    
        # Definindo o pino do encoder como interrupção na borda de subida
        self.irq = Pin(pinEncoder, Pin.IN, Pin.PULL_UP)
        self.irq.irq(trigger=Pin.IRQ_RISING, handler=self.handle_interrupt)

    def handle_interrupt(self, channel):
        self.counter +=1

    def monitorRPM(self):
        if (time() - self.time0) > self.INTERVALO:
          state = machine.disable_irq()
          self.freq = self.counter/(time() - self.time0)
          self.rpm = self.freq/self.IRQ*60
          self.counter = 0  # Reseta o counter para a próxima revolução
          self.time0 = time()  # Reseta o timer para próximo intervalo
          machine.enable_irq(state)
        return self.rpm

if __name__ == "__main__":
    encoder1 = Encoder(15)
    encoder2 = Encoder(4)
    while True:
        print("rpm1:{0} rpm2:{1}".format(encoder1.monitorRPM(), encoder2.monitorRPM()))