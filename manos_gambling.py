import numpy as np
import random
random.seed(None)
def generate_matrix(n=10):
	overall = np.zeros((2**n,n))
	num = 0
	while num < 2**n:
		overall[num,:] = convert_to_np(num,n)
		num += 1
	return overall

def convert_to_np(number,maxx):
	binary = []
	count = 0
	while number != 0:
	    bit = number % 2
	    binary.append(bit)
	    count += 1
	    number = number // 2

	while count < maxx:
		#print(count)
		binary.append(0)
		count += 1

	binary.reverse()

	#print(binary)

	return np.reshape(np.asarray(binary),(1,maxx))

def compute_odds(matrix, succeed_chance, payment, reward):
	weighted_sum = 0
	row = 0
	while(row < matrix.shape[0]):
		col = 0
		odds = 1
		money = 0
		while(col < matrix.shape[1]):
			if matrix[row,col] == 0: #0 = failure
				odds *= 1-succeed_chance
				money += payment
			elif matrix[row,col] == 1:
				odds *= succeed_chance
				money += reward + payment
			col += 1
		weighted_sum += odds*money
		row += 1

	print(weighted_sum)


def simulate(success_chance, cost, reward, number,starting):
	tris_made = 0
	money = starting
	avg_tries = 0
	pri_success_chance = success_chance[0]
	duo_success_chance = success_chance[1]
	tri_success_chance = success_chance[2]

	base_cost = cost[0]
	pri_concs_cost = cost[1]
	duo_concs_cost = cost[2]
	tri_concs_cost = cost[3]

	while(tris_made < number):
		pri_failed = False
		clicks = 0
		money += base_cost
		while(True): 
			if money < 0: #if i go negative, reset everything and try again
				return -1,-1
			pri_roll = random.random()
			clicks += 1
			money += pri_concs_cost
			if pri_roll <= 1 - pri_success_chance:
				continue

			duo_roll = random.random()
			clicks += 1
			money += duo_concs_cost
			if duo_roll <= 1 - duo_success_chance:
				continue

			tri_roll = random.random()
			clicks += 1
			money += tri_concs_cost
			if tri_roll <= 1 - tri_success_chance:
				continue

			break
		avg_tries += clicks
		money += reward
		tris_made += 1


	return money, avg_tries/number

concs_price = 7.85
starting_money = 6000
lives = 10000
cur = 0
deaths = 0
avg_net = []
while (cur < lives):
	money, avgg = simulate([.7,.5,.3],[-250,concs_price * -10,concs_price * -12,concs_price * -13], 4000*.85, number=100,starting=starting_money)
	if money == -1 and avgg == -1:
		deaths += 1
	else:
		avg_net.append(money-starting_money)
	cur += 1
print("died: ", deaths, " out of: ", lives)

neg_count = 0
i = 0
while(i < len(avg_net)):
	if avg_net[i] < 0:
		neg_count += 1
	i += 1

print("lost money on: ", neg_count, " out of ", lives-deaths)