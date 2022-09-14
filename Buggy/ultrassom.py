import machine, time
from machine import Pin

class Ultrassom:
    """Classe para controlar o ultrassom do buggy"""

    # Pinos do PWM
    TRIG0 = 33
    ECHO0 = 32

    def __init__(self, echo_timeout_us=6000):
        self.echo_timeout_us = echo_timeout_us  # Timeout para a resposta do echo
                                                # 6000us é aproximadamente 1 metro
        self.trigger = Pin(self.TRIG0, mode=Pin.OUT, pull=None)
        self.trigger.value(0)

        self.echo = Pin(self.ECHO0, mode=Pin.IN, pull=None)

    def _send_pulse_and_wait(self):
        self.trigger.value(0) # Aguarda a estabilizacao do sensor
        time.sleep_us(2)
        self.trigger.value(1) # Envia pulso por 10us
        time.sleep_us(10)
        self.trigger.value(0)
        pulse_time = machine.time_pulse_us(self.echo, 1, self.echo_timeout_us)
        return pulse_time     # Retorna o tempo de retorno do pulso em us

    def distance_cm(self):
        pulse_time = self._send_pulse_and_wait()

        # Calculo da distância é pulse_time / 2 (o pulso vai e volta)
        # e dividido por 29,1 porque a velocidade do som no ar é 0.034320 cm/us
        # que é 1 cm cada 29.1us
        cms = (pulse_time / 2) / 29.1
        return cms

if __name__ == '__main__':
    ultrassom = Ultrassom()
    print(ultrassom.distance_cm())