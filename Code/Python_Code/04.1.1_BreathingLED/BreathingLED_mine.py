from gpiozero import PWMLED
from time import sleep

led = PWMLED(18)

# sleep_value = 0.2

# while True:
	# led.value = 0.0
	# sleep(sleep_value)
	
	# led.value =0.5
	# sleep(sleep_value)
	
	# led.value = 1.0
	# sleep(sleep_value)
	
	
# breathing

while True:
	
	for duty_cycle in range(0,100,1):
		led.value = duty_cycle / 100
		sleep(0.01)
	sleep(0.2)
	
	for duty_cycle in range(100, -1, -1):
		led.value = duty_cycle / 100
		sleep(0.01)
	sleep(0.4)
