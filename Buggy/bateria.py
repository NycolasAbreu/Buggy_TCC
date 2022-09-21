from machine import Pin, ADC
from time import sleep

bat1 = ADC(Pin(32))
bat1.atten(ADC.ATTN_11DB)

bat2 = ADC(Pin(33))
bat2.atten(ADC.ATTN_11DB)

conversion_factor = 3.3 / 4095

while True:
  bat1_value = bat1.read() * conversion_factor
  print(bat1_value)
  bat2_value = bat2.read() * conversion_factor
  print(bat2_value)
  sleep(1)