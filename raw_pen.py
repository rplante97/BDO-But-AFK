import math
import sys
import numpy as np
import random
import matplotlib.pyplot as plt

random.seed(None)
base_chance = .003
growth = .0003
start_stack = 110
stack_gain = 6


cur = 0
trials = 10000
total_clicks = []
stack_popped = []

while(cur < trials):
	stack = start_stack
	clicks = 0
	while(True):
		chance = base_chance + growth*stack
		roll = random.random()
		clicks += 1
		if (roll < 1 - chance):
			stack += stack_gain
		else:
			stack_popped.append(stack)
			total_clicks.append(clicks)
			break
	cur += 1

print(np.sum(total_clicks)/len(total_clicks))
plt.hist(total_clicks,bins=30)
plt.show()

plt.hist(stack_popped)
plt.show()


