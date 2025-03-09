import Jetson.GPIO as GPIO # Uso con Jetson Nano
#import RPi.GPIO as GPIO # Uso con Raspberry Pi
import time

GPIO.setmode(GPIO.BOARD)


pines_MotorX = [10,12,11,13] #Motor X
pines_MotorY = [8,7,5,3] #Motor Y
pines_MotorZ = [16, 18, 22, 24]  # Motor Z

bajo, medio, alto, lampara = 16, 12, 10, 8
Relee = [bajo, medio, alto, lampara]

Fc = [40, 38, 36]

class __Version__:
    def __init__(self):
        print("Beta 0.0.1")

class StepMotor: 
    # Clase para controlar motores paso a paso
    # pines: lista de pines del motor
    # fc: pin de fin de carrera (opcional)(pull-up)
    # Esta clse permite controlar motores paso a paso
    # con la posibilidad de vincularlo a un fin de carrera

    def __init__(self, pines, fc = None):
        self.pines = pines
        self.cont = 0
        self.fc = fc
        
        self.seq = [[1, 0, 0, 1],  # Paso 1
                    [1, 0, 0, 0],  # Paso 2
                    [1, 1, 0, 0],  # Paso 3
                    [0, 1, 0, 0],  # Paso 4
                    [0, 1, 1, 0],  # Paso 5
                    [0, 0, 1, 0],  # Paso 6
                    [0, 0, 1, 1],  # Paso 7
                    [0, 0, 0, 1]]  # Paso 8

        self.inv = self.seq[::-1]
        
        for pin in self.pines:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

        if fc is not None:
            GPIO.setup(self.fc, GPIO.IN)
        
    def step(self, pasos, direccion):

        if self.fc is not None:
            if direccion == 1:
                for i in range(pasos):
                    if GPIO.input(self.fc) != 0:
                        self.cont += 1
                        for paso in self.seq:
                            self.cont += 1
                            for i in range(4):
                                GPIO.output(self.pines[i], paso[i])
                            time.sleep(0.001)

            elif direccion == -1:
                for i in range(pasos):
                    if  GPIO.input(self.fc) != 0:
                        self.cont -= 1
                        for paso in self.seq:
                            self.cont += 1
                            for i in range(4):
                                GPIO.output(self.pines[i], paso[i])
                            time.sleep(0.001)

        else:
            if direccion == 1:
                for i in range(pasos):
                    for paso in self.seq:
                        self.cont += 1
                        for i in range(4):
                            GPIO.output(self.pines[i], paso[i])
                        time.sleep(0.001)

            elif direccion == -1:
                for i in range(pasos):
                    self.cont -= 1
                    for paso in self.seq:
                        self.cont += 1
                        for i in range(4):
                            GPIO.output(self.pines[i], paso[i])
                        time.sleep(0.001)

    def origen(self):
        if self.fc is not None:
            while GPIO.input(self.fc) != 0:
                for h in range(8):
                    for pin in range(4):
                        GPIO.output(self.pines[pin], self.seq[h][pin])
                    time.sleep(0.001)
            self.cont = 0
        else:
            print("No se ha definido fin de carrera, no se puede regresar al origen")

    def reset(self):
        self.cont = 0

class Light_var:
    def __init__(self, pines):
        self.pines = pines
        self.status = False
        for pin in self.pines:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

    def encender(self, intensidad):
        if intensidad == 1:
            GPIO.output(self.pines[1], 1)
            time.sleep(0.001)
            GPIO.output(self.pines[2], 1)
            time.sleep(0.001)
            GPIO.output(self.pines[0], 0)
            self.status = True
        
        elif intensidad == 2:
            GPIO.output(self.pines[0], 1)
            time.sleep(0.001)
            GPIO.output(self.pines[2], 1)
            time.sleep(0.001)
            GPIO.output(self.pines[1], 0)
            self.status = True
        
        elif intensidad == 3:
            GPIO.output(self.pines[0], 1)
            time.sleep(0.001)
            GPIO.output(self.pines[1], 1)
            time.sleep(0.001)
            GPIO.output(self.pines[2], 0)
            self.status = True

    def apagar(self):
        for pin in self.pines:
            GPIO.output(pin, 1)
            time.sleep(0.001)
        self.status = False

    def estado(self):
        return self.status
    

def liberate():
    GPIO.cleanup()

