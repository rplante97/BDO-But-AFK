import numpy as np
import random
import matplotlib.pyplot as plt
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


def simulate(success_chance, cost, reward, number, starting, level, stack_costs = [0,0,0,0], cron=[False,False,False,False], crons_req = [0,0,0,0]):
	tris_made = 0
	money = starting
	avg_tries = 0
	pri_success_chance = success_chance[0]
	duo_success_chance = success_chance[1]
	tri_success_chance = success_chance[2]
	tet_success_chance = success_chance[3]

	base_cost = cost[0]
	pri_concs_cost = cost[1]
	duo_concs_cost = cost[2]
	tri_concs_cost = cost[3]
	tet_concs_cost = cost[4]

	pri_stack_cost = stack_costs[0]
	duo_stack_cost = stack_costs[1]
	tri_stack_cost = stack_costs[2]
	tet_stack_cost = stack_costs[3]

	cron_pri = cron[0]
	cron_duo = cron[1]
	cron_tri = cron[2]
	cron_tet = cron[3]

	cron_base_amount = crons_req[0]
	cron_pri_amount = crons_req[1]
	cron_duo_amount = crons_req[2]
	cron_tri_amount = crons_req[3]

	while(tris_made < number):
		pri_failed = False
		clicks = 0
		state = 0
		while(True): 
			if state == 0:
				#print("bought base")
				money += base_cost
				state = 1
			#print(money)
			if money < 0: #if i go negative, reset everything and try again
				return -1,-1
			if state == 1:
				#print("rolling for pri...", end ='')
				pri_roll = random.random()
				clicks += 1
				money += pri_concs_cost
				if pri_roll <= 1 - pri_success_chance:
					#print("failed with ", pri_roll)
					if cron_pri == True:
						money += cron_base_amount
						downgrade_roll = random.random()
						if downgrade_roll < 0.7:
							state = 1
						else:
							state = 1
							#print("downgraded to state: ", state)
					else:
						state = 0
					continue
				else:
					#print("succeeded!")
					state = 2
			if state == 2:
				#print("rolling for duo...", end ='')
				money += pri_stack_cost
				duo_roll = random.random()
				clicks += 1
				money += duo_concs_cost
				pri_expected = (base_cost + base_cost)/pri_success_chance
				if duo_roll <= 1 - duo_success_chance:
					#print("failed with ", duo_roll)
					if cron_duo == True:
						money += cron_pri_amount
						downgrade_roll = random.random()
						if downgrade_roll < 0.7:
							state = 2
							money -= pri_expected
						else:
							state = 1
							#print("downgraded to state: ", state)
					else:
						state = 0
					continue
				else:
					#print("succeeded!")
					state = 3
			if state == 3:
				#print("rolling for tri...", end ='')
				money += duo_stack_cost
				tri_roll = random.random()
				clicks += 1
				money += tri_concs_cost
				if tri_roll <= 1 - tri_success_chance:
					#print("failed with ", tri_roll)
					if cron_tri == True:
						money += cron_duo_amount
						downgrade_roll = random.random()
						if downgrade_roll < 0.7:
							state = 3
						else:
							state = 2
							#print("downgraded to state: ", state)
					else:
						state = 0
					continue
				else:
					#print("succeeded!")
					state = 4

			if state == 4:
				#print("rolling for tet...", end ='')
				money += tri_stack_cost
				#print(money)
				tet_roll = random.random()
				clicks += 1
				money += tet_concs_cost
				if tet_roll <= 1 - tet_success_chance:
					#print("failed with ", tri_roll)
					if cron_tet == True:
						money += cron_tri_amount
						downgrade_roll = random.random()
						if downgrade_roll < 0.7:
							state = 4
						else:
							state = 3
							#print("downgraded to state: ", state)
					else:
						state = 0
					continue
				else:
					#print("succeeded!")
					money += tet_stack_cost
			break
		avg_tries += clicks
		money += reward
		tris_made += 1


	return money, avg_tries/number

concs_price = 7.85
black_gem = .480
starting_money = 50000
lives = 1000
cur = 0
base_acc_price = -288
tet_acc_price = 18200
deaths = 0
avg_net = []
stack_costs = [-27, -90, -150, -3000.4]
while (cur < lives):
	#money, avgg = simulate([.75,.45,.3],[-250,concs_price * -10,concs_price * -12,concs_price * -13], 4000*.85, number=100,starting=starting_money)
	#money, avgg = simulate([.70,.40,.3,.2],[-1,black_gem*-1,black_gem* -2,black_gem* -3,black_gem*-4], 47*.85, number=100,starting=starting_money,level=4)
	money, avgg = simulate([0.77, 0.5, 0.4, 0.3], [base_acc_price, base_acc_price, base_acc_price, base_acc_price, base_acc_price], tet_acc_price * 0.85, number = 100, level=4, stack_costs=stack_costs,starting=starting_money, cron=[True,True,True, True], crons_req = [-62, -187, -562, -1562])
	#exit(1)
	if money == -1 and avgg == -1:
		deaths += 1
	else:
		avg_net.append(money-starting_money)
	cur += 1
print("died: ", deaths, " out of: ", lives)
if lives != deaths:
	print("average net: ", sum(avg_net)/(lives-deaths))

neg_count = 0
i = 0
while(i < len(avg_net)):
	if avg_net[i] < 0:
		neg_count += 1
	i += 1

print("lost money on: ", neg_count, " out of ", lives-deaths)

plt.hist(avg_net,bins=20)
plt.show()