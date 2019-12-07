import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pins = [17, 27, 22, 23, 20, 12, 16, 21, 26, 6, 13]
GPIO.setup(pins, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
GPIO.setup(19, GPIO.IN)
three=[23, 21, 20, 13, 16, 26]
l=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
rl = [(0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0)]
rotate=0
while True:
##    j = GPIO.input(19)
##    print(j)
##    i = GPIO.input(24)
##    #print(i)
##    if i == 0:
##        rotate=0
##        s = int(550/360 * 180)
##        if rotate==0:
##            for r in range(0, s, 1):
##                for x in l:
##                    GPIO.output(pins,x)
##                    time.sleep(0.002)
##            rotate=1
##        if i == 1:
##            s = int(550/360 * 180)
##            if rotate==0:
##                for r in range(0, s, 1):
##                    for x in rl:
##                        GPIO.output(pins,x)
##                        time.sleep(0.002)
##            rotate=1
##            GPIO.output(pins, GPIO.HIGH)
##            time.sleep(1)

    GPIO.output([12, 6], GPIO.HIGH)
    GPIO.output(three, GPIO.LOW)
    time.sleep(1)
            
        #GPIO.cleanup()
