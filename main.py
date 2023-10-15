import RPi.GPIO as GPIO
from time import sleep

# Configurar os pinos GPIO
GPIO.setmode(GPIO.BCM)

# Definir os pinos para os semáforos
semaforo1_pino_1 = 10
semaforo1_pino_2 = 8
semaforo2_pino_1 = 1
semaforo2_pino_2 = 18

# Definir os pinos para os botões de pedestres
botao_pedestre_1 = 23
botao_pedestre_2 = 24

# Definir os pinos para os sensores
sensos_via_aux_1 = 25
sensos_via_aux_2 = 12
sensos_via_pri_1 = 16
sensos_via_pri_2 = 20

#Definir Buzzer
buzzer = 21

# Configurar os pinos como saídas (semáforos) e entradas (botões)
GPIO.setup(semaforo1_pino_1, GPIO.OUT)
GPIO.setup(semaforo1_pino_2, GPIO.OUT)
GPIO.setup(semaforo2_pino_1, GPIO.OUT)
GPIO.setup(semaforo2_pino_2, GPIO.OUT)

GPIO.setup(botao_pedestre_1, GPIO.IN)
GPIO.setup(botao_pedestre_2, GPIO.IN)

GPIO.setup(sensos_via_aux_1, GPIO.IN)
GPIO.setup(sensos_via_aux_2, GPIO.IN)
GPIO.setup(sensos_via_pri_1, GPIO.IN)
GPIO.setup(sensos_via_pri_2, GPIO.IN)

GPIO.setup(buzzer, GPIO.OUT)

def setDefault():
    GPIO.output(semaforo1_pino_1, GPIO.LOW)
    GPIO.output(semaforo1_pino_1, GPIO.LOW)
    GPIO.output(semaforo2_pino_1, GPIO.LOW)
    GPIO.output(semaforo2_pino_2, GPIO.LOW)
    GPIO.output(botao_pedestre_1, GPIO.HIGH)
    GPIO.output(botao_pedestre_2, GPIO.HIGH)

def handlePedButton1():
    if GPIO.input(botao_pedestre_2) == GPIO.LOW:
        print("Botão de pedestre 1 acionado")
        GPIO.output(semaforo1_pino_1, GPIO.HIGH)
        GPIO.output(semaforo1_pino_2, GPIO.HIGH)
        sleep(0.5)

def handlePedButton2():
    if GPIO.input(botao_pedestre_1) == GPIO.LOW:
        print("Botão de pedestre 2 acionado")
        GPIO.output(semaforo2_pino_1, GPIO.HIGH)
        GPIO.output(semaforo2_pino_2, GPIO.HIGH)
        sleep(0.5)

GPIO.add_event_detect(botao_pedestre_1, GPIO.RISING)
GPIO.add_event_detect(botao_pedestre_2, GPIO.RISING)

try:
    while True:
        setDefault();
        # Exemplo: Simulação de semáforo na via principal
        if GPIO.event_detected(botao_pedestre_1):
            handlePedButton1()
            sleep(0.7)
            GPIO.output(semaforo1_pino_1, GPIO.LOW)
            GPIO.output(semaforo1_pino_2, GPIO.HIGH)
            
        if GPIO.event_detected(botao_pedestre_2):
            handlePedButton2()
            sleep(0.7)
            GPIO.output(semaforo2_pino_1, GPIO.LOW)
            GPIO.output(semaforo2_pino_2, GPIO.HIGH)

except KeyboardInterrupt:
    # Ctrl+C foi pressionado
    pass
 
GPIO.cleanup()