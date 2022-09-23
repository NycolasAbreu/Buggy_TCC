from motor import Motor
from bateria import Baterias
from encoder import Encoder
from sensor_linha import SensorLinha
from ultrassom import Ultrassom
import time

PIN_ENC1 = 2
PIN_ENC2 = 4

def mostrar_sensores(ultrassom, sensoresLinha, encoder1, encoder2, baterias):
    print("BAT1: {0}V BAT2: {1}V".format(baterias.bateria1(), baterias.bateria2()))
    print("rpm1: {0} rpm2: {1}".format(encoder1.monitorRPM(), encoder2.monitorRPM()))
    print("ESTADO DIREITA = ", sensoresLinha.direita())
    print("ESTADO ESQUERDA = ", sensoresLinha.esquerda())
    print("Distancia = ", ultrassom.distancia_cm())

if __name__ == '__main__':
    motores = Motor()
    baterias = Baterias()
    encoder1 = Encoder(PIN_ENC1)
    encoder2 = Encoder(PIN_ENC2)
    sensoresLinha = SensorLinha()
    ultrassom = Ultrassom()
    
    print('Bem vindo Ao Buggy')
    print('Digite a direção para mover: ')
    print('p: parar')
    print('w: frente')
    print('s: ré')
    print('a: esquerda')
    print('d: direita')
    print('q: sair')
    
    motores.parar()
    
    while (dir != 'q' and dir != 'Q'):
        dir = input()

        if dir == 'p' or dir == 'P':
            motores.parar()
        if dir == 'w' or dir == 'W':
            motores.mover_frente(30)
        if dir == 's' or dir == 'S':
            motores.mover_re(30)
        if dir == 'a' or dir == 'A':
            motores.mover_esquerda(40)
        if dir == 'd' or dir == 'D':
            motores.mover_direita(40)
            
        time.sleep(1)
        motores.parar()
        
    mostrar_sensores(ultrassom, sensoresLinha, encoder1, encoder2, baterias)