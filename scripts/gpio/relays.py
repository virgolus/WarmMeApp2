import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# rel 1
GPIO.setup(19, GPIO.OUT)
# rel 2
GPIO.setup(26, GPIO.OUT)
# rel 3
GPIO.setup(16, GPIO.OUT)
# rel 4
GPIO.setup(20, GPIO.OUT)

# rel 1
sleep(0.1)
GPIO.output(19, GPIO.HIGH)
sleep(0.1)
GPIO.output(19, GPIO.LOW)

# rel 2
GPIO.output(26, GPIO.HIGH)
sleep(0.1)
GPIO.output(26, GPIO.LOW)

# rel 3
sleep(0.1)
GPIO.output(16, GPIO.LOW)
sleep(0.1)
GPIO.output(16, GPIO.HIGH)
sleep(0.1)
GPIO.output(16, GPIO.HIGH)
sleep(0.1)
GPIO.output(16, GPIO.LOW)
sleep(0.1)
GPIO.output(16, GPIO.HIGH)
sleep(0.1)
GPIO.output(16, GPIO.LOW)
sleep(0.1)
GPIO.output(16, GPIO.HIGH)
sleep(0.1)
GPIO.output(16, GPIO.LOW)
sleep(0.1)
GPIO.output(16, GPIO.HIGH)

# rel 1
sleep(0.1)
GPIO.output(19, GPIO.HIGH)
sleep(0.1)
GPIO.output(19, GPIO.LOW)

# rel 2
GPIO.output(26, GPIO.HIGH)
sleep(0.1)
GPIO.output(26, GPIO.LOW)

# rel 3
sleep(0.1)
GPIO.output(16, GPIO.LOW)
sleep(0.1)
GPIO.output(16, GPIO.HIGH)

GPIO.output(16, GPIO.HIGH)
sleep(0.1)
GPIO.output(16, GPIO.LOW)

# shutdown
GPIO.output(16, GPIO.HIGH)
GPIO.output(19, GPIO.HIGH)
GPIO.output(26, GPIO.HIGH)
GPIO.output(20, GPIO.HIGH)
