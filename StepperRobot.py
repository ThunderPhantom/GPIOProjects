import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pins = [17, 27, 22, 23]

GPIO.setup(pins, GPIO.OUT)
l=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
rl = [(0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0)]
#rotation = int(input('How many times do you want the motor to rotate?'))
##angle = int(500/360 * rotation)
##
anglechoice = input("Do you want a 90, 180, 270, or 360 turn?")
def t90():
    print('turning...')
    s = int(500/360 * 90*2)
    for r in range(0, s, 1):
        for x in l:
            GPIO.output(pins,x)
            time.sleep(0.002)
    print('Done!')
def t180():
    
    print('turning...')
    s = int(550/360 * 180*2)
    for r in range(0, s, 1):
        for x in l:
            GPIO.output(pins,x)
            time.sleep(0.002)
    print('Done!')
def t270():
    

    print('turning...')
    s = int(550/360 * 270*2)
    for r in range(0, s, 1):
        for x in l:
            GPIO.output(pins,x)
            time.sleep(0.002)
    print('Done!')
def t360():
    

    print('turning...')
    s = int(550/360 * 360*2)
    for r in range(0, s, 1):
        for x in l:
            GPIO.output(pins,x)
            time.sleep(0.002)
    print('Done!')
'''print('turning...')
t = rotation * 500
for r in range(0, t, 1):
    for x in l:
        GPIO.output(pins,x)
        time.sleep(0.002)
print('Done!')'''
if anglechoice == 90:
    t90()
elif anglechoice == 180:
        t180()
elif anglechoice == 270:
        t270()
elif anglechoice == 360:
        t360()
