import RPi.GPIO as GPIO
import time

servo_pin = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
p = GPIO.PWM(servo_pin, 50)
p.start(0)

try:
	p.ChangeDutyCycle(7)
	time.sleep(1)
	p.ChangeDutyCycle(5)
	time.sleep(1)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()