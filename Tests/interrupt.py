import machine
 
interruptCounter = 0
totalInterruptsCounter = 0
 
def callback(pin):
  global interruptCounter
  interruptCounter = interruptCounter+1
 
p4 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
 
p4.irq(trigger=machine.Pin.IRQ_RISING, handler=callback)
 
while True:
 
  if interruptCounter>0:
 
    state = machine.disable_irq()
    interruptCounter = interruptCounter-1
    machine.enable_irq(state)
 
    totalInterruptsCounter = totalInterruptsCounter+1
    print("Interrupt has occurred: " + str(totalInterruptsCounter))

