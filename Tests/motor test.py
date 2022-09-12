from machine import Pin, PWM
import time

def DutyPercentage(percentage):
    return int((percentage * 1023) / 100)

def main():
    
    frequency = 1000
    m1  = PWM(Pin(21), frequency)
    m1n = PWM(Pin(22), frequency)
    m2  = PWM(Pin(18), frequency)
    m2n = PWM(Pin(19), frequency)
    
    m1.duty(DutyPercentage(50))
    m1n.duty(DutyPercentage(0))
    m2.duty(DutyPercentage(50))
    m2n.duty(DutyPercentage(0))
    print(m1)
    print(m1n)
    print(m2)
    print(m2n)
    time.sleep(3)

if __name__ == '__main__':
    main()
