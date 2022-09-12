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
        
        self.m1  = PWM(Pin(M1), pwm_freq)
        self.m1n = PWM(Pin(M1N), pwm_freq)
        self.m2  = PWM(Pin(M2), pwm_freq)
        self.m2n = PWM(Pin(M2N), pwm_freq)
        
        self.parar()
        
    def parar(self):        
        # Todos desligados
        self.m1.deinit()
        self.m1n.deinit()
        self.m2.deinit()
        self.m2n.deinit()
        
    def porcentagem_duty(porcentagem):
        return int((porcentagem * 1023) / 100)
        
    def mover_frente(self, porcentagem):
        
        self.parar()
        
        if (porcentagem > 0) and (porcentagem <= 100):
            duty = self.porcentagem_duty(porcentagem)
            self.m1.duty(duty)
            self.m2.duty(duty)
        
    def mover_re(self, porcentagem):
        
        self.parar()
        
        if (porcentagem > 0) and (porcentagem <= 100):
            duty = self.porcentagem_duty(porcentagem)
            self.m1n.duty(duty)
            self.m2n.duty(duty)
        
    def mover_esquerda(self, porcentagem):
        
        self.parar()
        
        if (porcentagem > 0) and (porcentagem <= 100):
            duty = self.porcentagem_duty(porcentagem)
            self.m1.duty(duty)
            self.m2n.duty(duty)
        
    def mover_direita(self, porcentagem):
        
        self.parar()
        
        if (porcentagem > 0) and (porcentagem <= 100):
            duty = self.porcentagem_duty(porcentagem)
            self.m1n.duty(duty)
            self.m2.duty(duty)