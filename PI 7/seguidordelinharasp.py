#import GPIO library
import RPi.GPIO as GPIO


#Warnings de troca de channel para GPIO

def segLinha()
    GPIO.setwarnings(False)

    sensorIR1 = 29
    sensorIR2 = 31

    rodaR1 = 16
    rodaR2 = 18

    rodaL1 = 13
    rodaL2 = 15

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(29,GPIO.IN)
    GPIO.setup(31,GPIO.IN)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)


    try:
        while True:
            if GPIO.input(29):
                GPIO.output(16,False)
                GPIO.output(18,False)
            else:
                GPIO.output(16,True)
                GPIO.output(18,False)
            if GPIO.input(31):
                GPIO.output(13,False)
                GPIO.output(15,False)
            else:
                GPIO.output(13,True)
                GPIO.output(15,False)
            
            
    finally:
        GPIO.cleanup()
            #GPIO.output(35,True)
            

segLinha()


























































































































GPIO.setmode(GPIO.BOARD)
GPIO.setup(rodaR1,GPIO.OUT)
GPIO.setup(rodaR2,GPIO.OUT)
GPIO.setup(rodaL1,GPIO.OUT)
GPIO.setup(rodaL2,GPIO.OUT)
GPIO.setup(12,GPIO.IN)
GPIO.setup(16,GPIO.IN)


#set GPIO numbering mode and define input and output pins

try:
    while True:
        if GPIO.input(12):
            GPIO.output(11,True)
            GPIO.output(7,False)
        else:
            GPIO.output(11,False)
            GPIO.output(7,True)
        if GPIO.input(16):
            GPIO.output(15,True)
            GPIO.output(13,False)
        else:
            GPIO.output(15,False)
            GPIO.output(13,True)
             
finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()
