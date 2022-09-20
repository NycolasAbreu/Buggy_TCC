from machine import Pin, PWM
import time

class Motor:
    """Classe para controlar os motores do buggy"""
    
    # Pinos do PWM
    M1 = 21
    M1N = 22
    M2 = 18
    M2N = 19
       
    # Frequencia PWM
    pwm_freq = 1000
    
    def __init__(self):
        self.m1  = PWM(Pin(self.M1), self.pwm_freq)
        self.m1n = PWM(Pin(self.M1N), self.pwm_freq)
        self.m2  = PWM(Pin(self.M2), self.pwm_freq)
        self.m2n = PWM(Pin(self.M2N), self.pwm_freq)

        self.parar()
        
    def parar(self):
        self.m1.duty(0)
        self.m1n.duty(0)
        self.m2.duty(0)
        self.m2n.duty(0)
        
    def porcentagem_duty(self, porcentagem):
        return int((porcentagem * 1023) / 100)
        
    def mover_frente(self, porcentagem):
        self.parar()
        time.sleep(1)
        if (porcentagem > 0) and (porcentagem <= 100):
            duty = self.porcentagem_duty(porcentagem)
            self.m1.duty(duty)
            self.m2.duty(duty)
        
    def mover_re(self, porcentagem):
        self.parar()
        time.sleep(1)
        if (porcentagem > 0) and (porcentagem <= 100):
            duty = self.porcentagem_duty(porcentagem)
            self.m1n.duty(duty)
            self.m2n.duty(duty)
        
    def mover_esquerda(self, porcentagem):
        self.parar()
        time.sleep(1)
        if (porcentagem > 0) and (porcentagem <= 100):
            duty = self.porcentagem_duty(porcentagem)
            self.m1.duty(duty)
            self.m2n.duty(duty)
        
    def mover_direita(self, porcentagem):
        self.parar()
        time.sleep(1)
        if (porcentagem > 0) and (porcentagem <= 100):
            duty = self.porcentagem_duty(porcentagem)
            self.m1n.duty(duty)
            self.m2.duty(duty)

if __name__ == '__main__':
    motores = Motor()
    motores.mover_frente(50)
    time.sleep(3)
    motores.mover_re(50)
    time.sleep(3)
    motores.mover_direita(50)
    time.sleep(3)
    motores.mover_esquerda(50)
    time.sleep(3)
    motores.parar()
