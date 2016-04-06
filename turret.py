#http://computers.tutsplus.com/tutorials/controlling-dc-motors-using-python-with-a-raspberry-pi--cms-20051
#xxx!
import RPi.GPIO as GPIO
from time import sleep

def move_up(degrees):
	pass

def move_down(degrees):
	pass

def move_right(degrees):
	pass

def move_left(degrees):
	pass

def shoot_short():
	pass

def shoot_long(time):
	pass
 
GPIO.setmode(GPIO.BOARD)
 
GPIO_port1 = 16
GPIO_port2 = 18
GPIO_port3 = 22

# 
Motor1A = GPIO_port1
# 
Motor1B = GPIO_port2
#enable pin - no motors on unless this is on
Motor1E = GPIO_port3
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
print "Turning motor on"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(2)
 
print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)
 
GPIO.cleanup()
