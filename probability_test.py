import random
import numpy as np
import matplotlib.pyplot as plt
num_tries = 1000
succ_chance = 0.4
i = 0
avg_tries = []
while(i < num_tries):
	tries = 0
	while(True):
		roll = random.random()
		tries += 1
		if roll > (1-succ_chance):
			break
	avg_tries.append(tries)
	i += 1

print("empirical: ", np.median(avg_tries))
print("logarithm: ", np.log(0.5)/np.log(1-succ_chance))
print(" division: ", 1/succ_chance)

plt.hist(avg_tries,bins=20)
plt.show()