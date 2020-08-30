#!/usr/bin/env python
import RPi.GPIO as GPIO
import time 

colors = [0xFF00, 0x00FF, 0x0FF0, 0xF00F]
pins = (11, 12) #pins is a dict

GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location 
GPIO.setup(pins, GPIO.OUT) # set pin's  mode is out
GPIO.output(pins, GPIO.LOW) # set pins to LOW(0 Volt) to off led

p_R = GPIO.PWM(pins[0], 2000) # set frequence to 2KHz
p_G = GPIO.PWM(pins[1], 2000)

P_R.start(0) # initial duty Cycle = 0(led off)
p_G = GPIO.PWM(pins[1], 2000) 

def map(x, in_min, in_max, out_min, out_max):
	return (x-in_min)/(in_max-in_min)*(out_max-out_min) + out_min
	
def setColor(col): # for example: col = 0x1122
	R_val = col >> 8
	G_val = col & 0x00FF
	
	R_val = map(R_val, 0, 255, 0, 100)
	G_val = map(R_val, 0, 255, 0, 100)
	
	p_R.ChangeDutyCycle(R_val) #change duty cycle
	p_G.ChangeDutyCycle(R_val) #change duty cycle

def loop():
	while True:
		for col in colors:
			SetColor(col)
			time.sleep(0.5)

def destroy():
	p_R.stop()
	p_G.stop()
	GPIO.output(pins, GPIO.LOW) #Turn off all leds
	GPIO.cleanup()

If __name__ == "__main__":
	try:
		loop()
	except KeyboardInterrup:
		destroy()
