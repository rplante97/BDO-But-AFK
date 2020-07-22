import random
reblath_18 = 6.09
reblath_21 = 8.049 #mil
reblath_24 = 10.549 #mil

db = {}
db['pri_grunil'] = [30.2, 'duo_grunil', .0769, .0077, 2, 3, None, 82, .00155] #cost, name_of_success, base_chance, chance_growth, click_cost, stack_growth, down-grade name, stack softcap, post softcap gfain
db['duo_grunil'] = [41.5, 'tri_grunil', .0625, .00625, 2, 4, 'pri_grunil', 102, .00125]
db['tri_grunil'] = [102, 'tet_grunil', .02, .002, 2, 5, 'duo_grunil', 340, 0]
db['tet_grunil'] = [455, 'pen_grunil', .003, .0003, 2, 6, 'tri_grunil', 2324, 0]
db['pen_grunil'] = [2840, 'NA', 0, 0, 0, 0, None]

db['pri_boss'] = [520, 'duo_boss', .077, .0077, 2+10, 3, None, 82, .00155] #cost, name_of_success, base_chance, chance_growth, click_cost, stack_growth
db['duo_boss'] = [615, 'tri_boss', .0625, .00625, 2+10, 4, 'pri_boss', 102, .00125]
db['tri_boss'] = [720, 'tet_boss', .02, .002, 2+10, 5, 'duo_boss', 340, 0]
db['tet_boss'] = [1990, 'pen_boss', .003, .0003, 2+10, 6, 'tri_boss', 2324, 0]
db['pen_boss'] = [17900, 'NA', 0, 0, 0, 0]

def grunil_break_points(order):
	tax = 0.85
	fail_repair_cost = 0.34
	cur_stack = 18
	stack_cost = reblath_18
	cost_dict = {}
	while(cur_stack < 200):
		current_index = 0
		best_index = 0
		best_cost = 0
		best_list = []
		while(current_index < len(order)):
			current_list = db[order[current_index]]
			over_soft_cap = max(0,cur_stack - current_list[7])
			current_success_chance = over_soft_cap*current_list[8] + (cur_stack-over_soft_cap)*current_list[3] + current_list[2]
			current_success_cost = current_list[4] + stack_cost - (db[current_list[1]][0]*tax - current_list[0])
			#print("succ: cost", current_success_cost)
			current_fail_cost = current_list[4]
			if 'boss' in order[current_index]:
				current_fail_cost += 10
			elif 'grunil' in order[current_index]:
				current_fail_cost += 0.35

			if current_list[6] != None: #aka item can downgrade upon failure
				current_fail_cost += (current_list[0] - db[current_list[6]][0])
			#print("fail: cost", current_fail_cost)
			#cost_to_add = (stack_cost + current_fail_cost)/(1-current_success_chance) - (current_success_chance/(1-current_success_chance)*current_success_cost)
			current_cost = ((current_success_chance*current_success_cost + (1 - current_success_chance)*current_fail_cost))/(1-current_success_chance)/current_list[5]

			#if order[current_index] == 'pri_grunil':
		#		print("")
		#		print(" name: ", order[current_index], " cost: ", round(current_cost,2))
	#			print(" succ_chance: ", current_success_chance)
#				print(" succ_cost: ", current_success_cost)
				#print(" fail_cost: ", current_fail_cost)
			if current_index == 0:
				best_index = 0
				best_cost = current_cost
				best_list = current_list
			else:
				if current_cost < best_cost:
					#print("swapping ", order[best_index], " for ", order[current_index])
					best_cost = current_cost
					best_index = current_index
					best_list = current_list
					#best_cost_to_add = cost_to_add
			current_index += 1

		print(cur_stack, " costs: ", round(stack_cost,2), " || ", order[best_index], "= ", round(best_cost,2), "mil per stack ||")
		if cur_stack > 100:
			cost_dict[cur_stack] = stack_cost
		cur_stack += best_list[5]
		stack_cost += best_cost*best_list[5]
	return cost_dict

cost_dict = grunil_break_points(order = ['pri_boss', 'duo_boss', 'tet_boss','pri_grunil', 'duo_grunil', 'tri_grunil', 'tet_grunil'])

def cron_pen(cost_dict, pen_details):
	#db['tet_boss'] = [1990, 'pen_boss', .003, .0003, 2+10, 6, 'tri_boss', 2324, 0]
	best_stack = 0
	best_profit = 0
	best_clicks = 0
	best_cost = 0
	first = True
	for i in cost_dict.keys():
		cur_odds = i*pen_details[3] + pen_details[2]
		#print(cur_odds)
		cost = pen_details[10] - 2 -10
		reward = pen_details[-2]

		expected_cost = cost / cur_odds

		additional_expenses = -cost_dict[i] - pen_details[0]*.85

		overall_cost = expected_cost + additional_expenses

		#print("cost: ", overall_cost)

		profit = reward * .85  + overall_cost

		#print("profit: ", profit)

		if first == True:
			best_stack = i
			best_profit = profit
			best_clicks = 1/cur_odds
			best_cost = -1*overall_cost
			first = False
		else:
			if best_profit < profit:
				#print(best_profit, profit)
				best_profit = profit
				best_stack = i
				best_clicks = 1/cur_odds
				best_cost = -1*overall_cost
	return best_profit, best_cost, best_clicks, best_stack


pen_db = {}
#cost, name_of_success, base_chance, chance_growth, click_cost, stack_growth, down-grade name, stack softcap, post softcap gfain, pen price, cron(mil)
pen_db['leebur'] = [1850, 'pen_boss', .003, .0003, 2+10, 6, 'tri_boss', 2324, 0, 18100, -429]
pen_db['urugon'] = [2390, 'pen_boss', .003, .0003, 2+10, 6, 'tri_boss', 2324, 0, 17200, -493]
pen_db['muskan'] = [1550, 'pen_boss', .003, .0003, 2+10, 6, 'tri_boss', 2324, 0, 17700, -429]
pen_db['dim tree'] = [2010, 'pen_boss', .003, .0003, 2+10, 6, 'tri_boss', 2324, 0, 18400, -493]
pen_db['red nose'] = [1630, 'pen_boss', .003, .0003, 2+10, 6, 'tri_boss', 2324, 0, 17300, -429]
pen_db['kzarka'] = [1430, 'pen_boss', .003, .0003, 2+10, 6, 'tri_boss', 2324, 0, 16100, -531]
pen_db['dande'] = [1670, 'pen_boss', .003, .0003, 2+10, 6, 'tri_boss', 2324, 0, 15500, -611]
pen_db['kutum'] = [1800, 'pen_boss', .003, .0003, 2+10, 6, 'tri_boss', 2324, 0, 18600, -531]
pen_db['nouver'] = [1590, 'pen_boss', .003, .0003, 2+10, 6, 'tri_boss', 2324, 0, 14100, -531]

#cron_pen(cost_dict, pen_db['leebur'])

def rank_pens(pen_db, cost_dict):
	over_all_list = []
	for i in pen_db.keys():
		profit, cost, clicks, stack = cron_pen(cost_dict, pen_db[i])
		cur_list = [i, profit, cost, clicks, stack]
		over_all_list.append(cur_list)
	over_all_list.sort(key = lambda x: x[1])
	over_all_list.reverse()

	for i in over_all_list:
		print(i)

rank_pens(pen_db, cost_dict)
#order = ['pri_grunil', 'duo_grunil', 'tri_grunil', 'tet_grunil', 'pen_grunil']

