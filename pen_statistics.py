import random
import numpy as np
import matplotlib.pyplot as plt
random.seed(None)

def simulate(num_make, odds, starting, stack_cost, tet_cost, reward, click_cost):
	money = starting
	base = stack_cost + tet_cost
	pen_made = 0
	click_list = []
	while(pen_made < num_make):
		clicks = 0
		money += base
		#print(money)
		#exit(1)
		while(True):
			if money < 0:
				return -1,-1
			roll = random.random()
			clicks += 1
			money += click_cost
			#print(roll)
			if roll <= 1 - odds:
				continue
			money += reward
			#exit(1)
			break
		pen_made += 1
		click_list.append(clicks)
	return money,click_list

num_made = 200
odds = 0.05
starting = 100000
stack_cost = -3609
tet_cost = -1910
reward = 18300*.85
percentile = .90
click_cost = -15 + (-429)
end_index = int(percentile*num_made)

lives = 1000
cur = 0
avg_net = []
deaths = 0
while(cur < lives):
	money,click_list = simulate(num_made, odds, starting, stack_cost, tet_cost, reward, click_cost)
	if money == -1:
		deaths += 1
	else:
		avg_net.append(money-starting)
	cur += 1
print("died: ", deaths, " out of: ", lives)
print("average net: ", sum(avg_net)/(lives-deaths))
neg_count = 0
i = 0
while(i < len(avg_net)):
	if avg_net[i] < 0:
		neg_count += 1
	i += 1

print("lost money on: ", neg_count, " out of ", lives-deaths)
# print("----------Statistics-------------")
# print("Number of pens made: ", num_made)
# print("Success chance: ", odds)
# print("Average number of clicks: ", np.average(pen_clicks))
# print("Median number of clicks: ", pen_clicks[int(pen_clicks.shape[0]/2)])
# print(percentile, "th percentile: ", pen_clicks[0],"to", pen_clicks[end_index])
# print("Quartiles: ", np.percentile(pen_clicks,0), np.percentile(pen_clicks,25), np.percentile(pen_clicks,50), np.percentile(pen_clicks,75), np.percentile(pen_clicks,100))
# plt.hist(pen_clicks,bins=100)
# plt.show()

