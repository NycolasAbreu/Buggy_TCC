import machine, time
from machine import Pin, Timer

class Ultrassom:
    """Classe para controlar o ultrassom do buggy"""
    # Pinos do PWM
    TRIG0 = 27
    ECHO0 = 14
    
    # Tempo de resposta máximo
    ECHO_TIMEOUT = 10000
    
    def __init__(self):
        self.pulse_time = 0
        
        self.trigger = Pin(self.TRIG0, mode=Pin.OUT, pull=None)
        self.trigger.value(0)

        self.echo = Pin(self.ECHO0, mode=Pin.IN, pull=None)
        
        self.tim0 = Timer(0)
        self._init_timer()

    def _envia_pulso_e_espera(self, t):
        self.trigger.value(0) # Aguarda a estabilizacao do sensor
        time.sleep_us(5)
        self.trigger.value(1) # Envia pulso por 10us
        time.sleep_us(10)
        self.trigger.value(0)
        self.pulse_time = machine.time_pulse_us(self.echo, 1, self.ECHO_TIMEOUT)

    def distancia_cm(self):
        # Calculo da distância é pulse_time / 2 (o pulso vai e volta)
        # e dividido por 29,13 porque a velocidade do som no ar é 0.034320 cm/us
        # que é 1 cm cada 29.13us
        cms = (self.pulse_time / 2) / 29.1375
        return cms

    def _init_timer(self, period_ms = 500):  # Cria um timer para atualizar o pulse_time a cada 500ms
        self.tim0.init(period=period_ms, mode=Timer.PERIODIC, callback=self._envia_pulso_e_espera)

if __name__ == '__main__':
    ultrassom = Ultrassom()
    while (1):
        time.sleep(1)
        print(ultrassom.distancia_cm())
