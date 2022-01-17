import random

health = 100

counter_1 = 0
counter_2 = 0

while health > 0:

	for i in range(100):
	
		r = random.randint(0,1)

		if r == 0:

			counter_1 += 1

		else:

			counter_2 += 1

	if counter_1 > counter_2:

		print("You are dead")

		health -= 1

		if health == 0:

			print("Game Over")

	elif counter_1 < counter_2:

		print("You are alive")

	else:

		pass

print(counter_1, counter_2)