from gpiozero import LEDBoard
from time import sleep
from signal import pause

print ('Lightwater mine')

ledPins = ["J8:11", "J8:12","J8:13","J8:15","J8:16","J8:18","J8:22","J8:3","J8:5","J8:24"]

leds = LEDBoard(*ledPins, active_high=False)

on_led = 0

def on_off(leds, led_id, stime=0.2):
	leds[led_id].on()
	sleep(stime)
	leds[led_id].off()

# escalera
# while(True):

		# on_off(leds, on_led)
		# # print(on_led)
		# on_led =  (on_led + 2) % 10

		# on_off(leds, on_led)
		# # print(on_led)
		# on_led =  (on_led - 1) % 10

		# on_off(leds, on_led)
		# # print(on_led)
		
# ping-pong
# while True:
	# for led in range(len(ledPins)):
		# on_off(leds, led)
	
	# for led in range(len(ledPins)-2,0,-1):
		# on_off(leds, led)

# to the center
# counter = 0
# while True:
	
	# for led in range(len(ledPins)):
		# if led % 2 == 0 and led != 0:
			# led = int(led / 2)
		# elif led % 2 == 1 :
			# led = 10 - led + counter
			# counter += 1
		# # print(led)
		# on_off(leds, led)
	# counter = 0


# snake
# led_matrix = [
	# [1,0,0,0,0,0,0,0,0,0],
	# [1,1,0,0,0,0,0,0,0,0],
	# [1,1,1,0,0,0,0,0,0,0],
	# [0,1,1,1,0,0,0,0,0,0],
	# [0,0,1,1,1,0,0,0,0,0],
	# [0,0,0,1,1,1,0,0,0,0],
	# [0,0,0,0,1,1,1,0,0,0],
	# [0,0,0,0,0,1,1,1,0,0],
	# [0,0,0,0,0,0,1,1,1,0],
	# [0,0,0,0,0,0,0,1,1,1],
	# [0,0,0,0,0,0,0,0,1,1],
	# [0,0,0,0,0,0,0,0,0,1]
# ]



# while True:
	# for section in led_matrix:
		# for led,state in enumerate(section):
			# if state == 1:
				# leds[led].on()
			# else:
				# leds[led].off()
			# sleep(0.1)

	
# snake2
# works better, but still has to declare a specific matrix
# state_matrix = [
	# [0],
	# [0,1],
	# [0,1,2],
	# [1,2,3],
	# [2,3,4],
	# [3,4,5],
	# [4,5,6],
	# [5,6,7],
	# [6,7,8],
	# [7,8,9],
	# [8,9,0],
	# [9,0,1]
# ]
	
	
# prev_state = []
# first_pass = True
# counter = 0
# while True: 
	
	# for state in state_matrix:
		# for led in state:
			# leds[led].on()
			
		# for led in prev_state:
			# if not led in state:
				# leds[led].off()
		# prev_state = state
		# sleep(0.2)
	
	# if first_pass:
		# _ = state_matrix.pop(0)
		# _ = state_matrix.pop(0)
		# first_pass = not first_pass
				
			
# snake3

def generate_next_state(counter, size, total_size=10):
	
	return [i % total_size for i in range(counter, counter+size, 1)]


size = 3

counter = 0
starting_counter = 1
prev_state = []
starting = True

if size > 10:
	raise ValueError("size should be smaller than 10.")

while True:
	
	# generate state
	if starting:
		state = generate_next_state(0, starting_counter)
	else:
		state = generate_next_state(counter, size)
	
	# operate leds
	for led in state:
		leds[led].on()
		
	for led in prev_state:
		if not led in state:
			leds[led].off()
	prev_state = state
	
	
	if starting:
		starting_counter += 1
		
		if starting_counter >= size:
			starting = not starting
	else:
		counter = (counter + 1) % 10
	sleep(0.1)
	
	
		
	
	
	
	


pause()







