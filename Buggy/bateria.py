from machine import Pin, Timer, ADC
import time

class Baterias:
    """Classe para controlar as baterias"""
    
    # Pinos das baterias
    BAT1 = 32
    BAT2 = 33
    
    # Fator de correção do ADC
    FATOR_ADC = 3.3 / 4095
    
    def __init__(self):
        self.bat1 = ADC(Pin(self.BAT1))
        self.bat2 = ADC(Pin(self.BAT2))

        self.bat1_volts = 0
        self.bat2_volts = 0
        
        # Atenuação para ler até 3.3V (Máx. do esp32)
        self.bat1.atten(ADC.ATTN_11DB)  
        self.bat2.atten(ADC.ATTN_11DB)

        self.tim2 = Timer(2)
        self.init_timer()
    
    def _recebe_valores(self, t):
        self.bat1_volts = self.bat1.read()
        self.bat2_volts = self.bat2.read()

    def bateria1(self):
        return self.bat1_volts * self.FATOR_ADC
    
    def bateria2(self):
        return self.bat2_volts * self.FATOR_ADC

    def init_timer(self, period_ms = 5000):  # Cria um timer para atualizar os valores a cada 5s
        self.tim2.init(period=period_ms, mode=Timer.PERIODIC, callback=self._recebe_valores)
    
if __name__ == '__main__':
    baterias = Baterias()
    while(1):
        time.sleep(1)
        print("bateria1 = ", baterias.bateria1())
        print("bateria2 = ", baterias.bateria2())