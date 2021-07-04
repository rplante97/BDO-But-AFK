''' how to use 

command line call: python failstack_theory_cost.py <stack>

stack = 44 or 110. no other stack is supported


'''

import sys

db = {}

strategy_og = [('pri_reblath', 2, 3), ('duo_reblath', 1 , 4), ('pri_boss',2, 3), ('duo_reblath', 2, 4), ('duo_boss', 2, 4), ('tri_reblath', 4, 5), ('valks', 10, 1), ('tri_boss', 3, 5), ('tet_reblath', 3, 5)]

strategy_44 = [('pri_reblath', 4, 3), ('duo_reblath', 3, 4)]

strategy_110 = [('pri_reblath', 4, 3), ('duo_reblath', 0 , 4), ('pri_boss',0, 3), ('duo_reblath', 4, 4), ('duo_boss', 0, 4), ('tri_reblath', 4, 5), ('valks', 10, 1), ('tri_boss', 0, 5), ('tet_reblath', 6, 5)]

reblath_17 = 4.4
meme_frag = 1.8
hard_conc = 2.25
start_stack = 17

end_stack = int(sys.argv[-1])

strategy = None

if end_stack != 44 and end_stack != 110:
	print("needs to be 44 or 110 end stack")
	sys.exit(1)

if end_stack == 44:
	strategy = strategy_44

elif end_stack == 110:
	strategy = strategy_110

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
			if stack >= 110:
				break_flag = 1
				break

		if break_flag == 1:
			break

	return strat_dict

strat_dict = convert_strategy_to_dict(strategy,17)

#print(strat_dict)

#keep track of (percent chance, cost)

paths = []

running_chance = 1 
running_cost = reblath_17
stack = start_stack
debug = 0
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
print("\t".join(formatt))
print("-------------------------------------------------------------")
for i in range(len(paths)):
	end_fail_chance += paths[i][-1]
	weighted_fail_cost += paths[i][-1]*paths[i][1]
	print("\t".join(str(x) for x in paths[i]))

print("")
stack_chance = []
last_name = paths[0][3]
running_chance = 1
clicks = 0
for i in range(len(paths)):
	if paths[i][3] != last_name:
		stack_chance.append((last_name, str(clicks), str(running_chance)))
		last_name = paths[i][3]
		running_chance = 1
		clicks = 0

	running_chance *= (1-paths[i][2])
	clicks += 1

	if i+1 == len(paths):
		stack_chance.append((last_name, str(clicks), str(running_chance)))

formatt = ['name', 'clicks', '\t fail all']
print("\t".join(formatt))
print("--------------------------------------------------------------")
for i in range(len(stack_chance)):
	print("\t".join(stack_chance[i]))

print("")
print("chance u dont get the end stack: ", end_fail_chance)
print("avg fail cost: ", weighted_fail_cost)
print('attempts to get end stack: ', 1/(1-end_fail_chance))
print('end_stack_one_shot: ', end_stack_one_shot_cost)
print('cost of end stack: ', weighted_fail_cost*1/(1-end_fail_chance) + end_stack_one_shot_cost)