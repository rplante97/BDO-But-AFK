''' how to use 

command line call: python failstack_theory_cost.py <stack>

stack = 44 or 110. no other stack is supported


'''

import itertools
import sys

db = {}

strategy_og = [('pri_reblath', 2, 3), ('duo_reblath', 1 , 4), ('pri_boss',2, 3), ('duo_reblath', 2, 4), ('duo_boss', 2, 4), ('tri_reblath', 4, 5), ('valks', 10, 1), ('tri_boss', 3, 5), ('tet_reblath', 3, 5)]

strategy_44 = [('pri_reblath', 3, 3), ('duo_reblath', 1, 4), ('pri_boss', 2, 3), ('duo_reblath', 1, 4)]

strategy_110 = [('pri_reblath', 3, 3), ('duo_reblath', 1 , 4), ('pri_boss',2, 3), ('duo_reblath', 1, 4), ('duo_boss', 2, 4), ('tri_reblath', 4, 5), ('valks', 10, 1), ('tri_boss', 4, 5), ('tet_reblath', 3, 5)]

strategy_130 = [('pri_reblath', 3, 3), ('duo_reblath', 1 , 4), ('pri_boss',2, 3), ('duo_reblath', 1, 4), ('duo_boss', 2, 4), ('tri_reblath', 4, 5), ('valks', 10, 1), ('tri_boss', 4, 5), ('tet_reblath', 3, 5), ('tet_boss', 3, 6)]


strategy_250 = [('pri_reblath', 3, 3), ('duo_reblath', 1 , 4), ('pri_boss',2, 3), ('duo_reblath', 1, 4), ('duo_boss', 2, 4), ('tri_reblath', 4, 5), ('valks', 10, 1), ('tri_boss', 4, 5), ('tet_reblath', 3, 5), ('tet_boss', 15, 6)]

reblath_15 = 3.63
reblath_16 = 4.04
reblath_17 = 4.4
reblath_18 = 4.95
reblath_19 = 5.46

meme_frag = 1.8
hard_conc = 2.25
start_stack = 17

end_stack = int(sys.argv[-1])

strategy = strategy_44

if end_stack == 44:
	strategy = strategy_44

elif end_stack == 110:
	strategy = strategy_110

elif end_stack == 130:
	strategy = strategy_130

elif end_stack == 250:
	strategy = strategy_250 
	
db['pri_reblath'] = [0, 'duo_reblath', .0769, .0077, hard_conc, .012, 3, 'pri_reblath', 82, .00155] #cost, name_of_success, base_chance, chance_growth, click_cost, stack_growth, down-grade name, stack softcap, post softcap gfain
db['duo_reblath'] = [0, 'tri_reblath', .0625, .00625, hard_conc, .012, 4, 'pri_reblath', 102, .00125]
db['tri_reblath'] = [0, 'tet_reblath', .02, .002, hard_conc, .012, 5, 'duo_reblath', 340, 0]
db['tet_reblath'] = [0, 'pen_reblath', .003, .0003, hard_conc, .012, 6, 'tri_reblath', 2324, 0]
db['pen_reblath'] = [1026, 'NA', 0, 0, 0, 0, None]

db['pri_boss'] = [0, 'duo_boss', .0769, .0077, hard_conc, 10*meme_frag, 3, 'pri_boss', 82, .00155] #cost, name_of_success, base_chance, chance_growth, click_cost, stack_growth, down-grade name, stack softcap, post softcap gfain
db['duo_boss'] = [41.5, 'tri_boss', .0625, .00625, hard_conc, 10*meme_frag, 4, 'pri_boss', 102, .00125]
db['tri_boss'] = [102, 'tet_boss', .02, .002, hard_conc, 10*meme_frag, 5, 'duo_boss', 340, 0]
db['tet_boss'] = [1440, 'pen_boss', .003, .0003, hard_conc, 10*meme_frag, 6, 'tri_boss', 2324, 0]
db['pen_boss'] = [18000, 'NA', 0, 0, 0, 0, None]

db['valks'] = [0, 'valks', 1, 0, 0, 0, 1, 'valks', 0, 0]

total_clicks = 0
for i in range(len(strategy)):
	total_clicks

def convert_strategy_to_dict(strategy, start_stack):
	strat_dict = {}
	stack = start_stack
	break_flag = 0
	for i in range(len(strategy)):
		num_enhance = strategy[i][1]
		while num_enhance > 0:
			strat_dict[stack] = strategy[i][0]
			num_enhance -= 1
			stack += strategy[i][2]
			if stack >= end_stack:
				break_flag = 1
				break

		if break_flag == 1:
			break

	return strat_dict

def fail_stack_calculator(start, start_cost, stack, strategy, print_bool=True):
	strat_dict = convert_strategy_to_dict(strategy,17)

	#print(strat_dict)

	#keep track of (percent chance, cost)

	paths = []

	running_chance = 1 
	running_cost = start_cost
	stack = start
	debug = 1
	end_stack_one_shot_cost = 0

	end = 2
	count = 0
	for i in strat_dict.keys():
		if strat_dict[i] == 'valks':
			stack += 1
			continue
		#get enhance rate info by using name from strat_dict in the db
		base_chance = db[strat_dict[i]][2]
		gain_chance = db[strat_dict[i]][3]
		stack_gain = db[strat_dict[i]][6]
		success_rate = base_chance + gain_chance*stack
		fail_rate = 1 - success_rate

		#get enhance cost info
		click_cost = db[strat_dict[i]][4]
		repair_cost = db[strat_dict[i]][5]

		#reset succ and fail variables:
		succ_path_chance = 0
		succ_path_cost = 0
		fail_path_chance = 0
		fail_path_cost = 0

		#success
		succ_path_chance = running_chance * success_rate
		succ_path_cost = running_cost + click_cost
		if debug == 1:
			print("running chance: ", running_chance)
			print("success path rate:", success_rate)
			print("succ path chance: ", succ_path_chance)
			print("succ path cost: ", succ_path_cost)
		#save to path - teerminates because we succeeded an enhancement
		paths.append((stack, round(succ_path_cost,2), round(success_rate,3), strat_dict[i],  succ_path_chance) )

		#fail - stack goes up
		fail_path_chance = running_chance * fail_rate
		fail_path_cost = running_cost + click_cost + repair_cost
		end_stack_one_shot_cost += click_cost + repair_cost
		if debug == 1:
			print("")
			print("fail path rate:", fail_rate)
			print("fail path chance: ", fail_path_chance)
			print("fail path cost: ", fail_path_cost)

			print("----------")
		#update running_chance and running_cost <- same as #fail section
		running_chance = fail_path_chance
		running_cost = fail_path_cost
		stack += stack_gain

		if stack >= end_stack:
			break
		#count += 1
		#if count >= end:
		#		break

	formatt = ['stack', 'cost', 'chance', 'item', 'running chance']
	end_fail_chance = 0
	weighted_fail_cost = 0
	if print_bool == True:
		print("\t".join(formatt))
		print("-------------------------------------------------------------")

	for i in range(len(paths)):
		end_fail_chance += paths[i][-1]
		weighted_fail_cost += paths[i][-1]*paths[i][1]
		if print_bool == True:
			print("\t".join(str(x) for x in paths[i]))

	stack_chance = []
	last_name = paths[0][3]
	running_chance_fail_all = 1
	running_chance_get_item = 0
	cost_list = []
	running_chance_list = []
	clicks = 0
	for i in range(len(paths)):
		if paths[i][3] != last_name:
			'''
			how to compute teh cost of the next item, duo from pri reblath based on 3 clicks of pri:

			duo_reblath = path_1_cost*(path_1_chance/sum of all chances) + ... + path_3_cost*(path_3_chance/sum of all chances) / (sum of all chances)

			thought process: assume you get the item in the numberator. so you rescale the costs by the relative chances of all clicks (sum of all chances), then you divide by the sum of all chances to remove the assumption that you get the item.

			'''
			cost_next_item = 0
			chance_next_item_sum = sum(running_chance_list)
			for j in range(len(cost_list)):
				cost_next_item += cost_list[j]*running_chance_list[j]/chance_next_item_sum
			cost_next_item /= chance_next_item_sum

			stack_chance.append((last_name, str(clicks), str(round(running_chance_fail_all,4)),str(round(running_chance_get_item,4)), str(round(cost_next_item,4))))

			last_name = paths[i][3]
			running_chance_fail_all = 1
			running_chance_get_item = 0
			cost_list = []
			running_chance_list = []
			clicks = 0

		running_chance_fail_all *= (1-paths[i][2])
		running_chance_get_item += (paths[i][-1])
		cost_list.append(paths[i][1])
		running_chance_list.append(paths[i][-1])
		clicks += 1

		if i+1 == len(paths):
			stack_chance.append((last_name, str(clicks), str(round(running_chance_fail_all,4)),str(round(running_chance_get_item,4))))
	formatt = ['name', 'clicks', '\t fail all', '\t chance to get item', '\t cost of next item']
	if print_bool == True:
		print("")
		print("\t".join(formatt))
		print("--------------------------------------------------------------")
		for i in range(len(stack_chance)):
			print("\t".join(stack_chance[i]))

		print("")
		print("chance u get the end stack: ", 1-end_fail_chance)
		print("avg fail cost: ", weighted_fail_cost)
		print('attempts to get end stack: ', 1/(1-end_fail_chance))
		print('end_stack_one_shot: ', end_stack_one_shot_cost)
		print('cost of end stack: ', weighted_fail_cost*1/(1-end_fail_chance) + end_stack_one_shot_cost)

	return weighted_fail_cost*1/(1-end_fail_chance) + end_stack_one_shot_cost, stack, 1-end_fail_chance

def item_optimizer(item_name,strategy):
	'''
	purpose: to find the cheapest stacking method for a particular item

	inputs:
		item_name: name of the item you want to click
		strategy: clicking strategy that SHOULD NOT include the name of the item
				also assumes the num_clicks in each item in strategy is set to 1
				also assumes there are no unused items in the strategy


	method:
		linearly searches for a stacking method starting at 1 click per previous item.
		simply looks at all cominations, increasing the click of each item by 1 at a time.

		For example: if you are trying to enhance a tri reblath, assume that creating a stack for that tri reblath
		requires clicking of pri and duo reblath. 

		start with 1 pri, 1 duo and search:

		1 pri 2 duo
		1 pri 3 duo
		1 pri 4 duo
		2 pri 1 duo
		2 pri 2 duo
		2 pri 3 duo
		...
		4 pri 4 duo
	'''

	#convert tuple to strategy
	#strategy_og = [('pri_reblath', 2, 3), ('duo_reblath', 1 , 4), ('pri_boss',2, 3), ('duo_reblath', 2, 4), ('duo_boss', 2, 4), ('tri_reblath', 4, 5), ('valks', 10, 1), ('tri_boss', 3, 5), ('tet_reblath', 3, 5)]
	reblath = [(15,reblath_15),(16,reblath_16),(17,reblath_17),(18,reblath_18),(19,reblath_19)]
	num_items = len(strategy)
	combinations = list(itertools.product([0,1,2,3,4], repeat=num_items))
	i = 0
	while i < (len(combinations)):
		if combinations[i][0] == 0:
			del combinations[i]
		else:
			i += 1

	end_list = []
	strategy = []
	item_order = [('pri_reblath',3), ('duo_reblath',4), ('tri_reblath',5)]
	for i in range(len(combinations)):
		strategy = []
		for j in range(len(combinations[i])):
			strategy.append((item_order[j][0],combinations[i][j],item_order[j][1]))
		for k in reblath:
			cost, stack, chance = fail_stack_calculator(k[0],k[1],44,strategy,print_bool = False)
			end_list.append((cost , stack, chance, k[0], strategy))

	end_list.sort(key = lambda x:x[1])

	last_stack = end_list[0][1]
	for i in end_list:
		if i[1] != last_stack:
			print("---------------------------------")
			last_stack = i[1]

		print(i)





def main():
	fail_stack_calculator(17, reblath_17, end_stack, strategy, print_bool = True)
	#strategy = [('pri_reblath', 1, 3)]
	#strategy = [('pri_reblath', 1, 3), ('duo_reblath', 1, 4)]
	#item_optimizer('test',strategy)

main()