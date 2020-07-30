import requests
import random
import time
import pickle
import sys

reblath_18 = 6.09
reblath_21 = 8.049 #mil
reblath_24 = 10.549 #mil

db = {}
db['pri_grunil'] = [30.2, 'duo_grunil', .0769, .0077, 2, 3, None, 82, .00155] #cost, name_of_success, base_chance, chance_growth, click_cost, stack_growth, down-grade name, stack softcap, post softcap gfain
db['duo_grunil'] = [41.5, 'tri_grunil', .0625, .00625, 2, 4, 'pri_grunil', 102, .00125]
db['tri_grunil'] = [102, 'tet_grunil', .02, .002, 2, 5, 'duo_grunil', 340, 0]
db['tet_grunil'] = [455, 'pen_grunil', .003, .0003, 2, 6, 'tri_grunil', 2324, 0]
db['pen_grunil'] = [2840, 'NA', 0, 0, 0, 0, None]

db['pri_leebur'] = [520, 'duo_leebur', .077, .0077, 2+10*1.3, 3, None, 82, .00155] #cost, name_of_success, base_chance, chance_growth, click_cost, stack_growth
db['pri_dimtree'] = [520, 'duo_dimtree', .077, .0077, 2+10*1.3, 3, None, 82, .00155]
db['pri_bheg'] = [520, 'duo_bheg', .077, .0077, 2+10*1.3, 3, None, 82, .00155]
db['pri_giath'] = [520, 'duo_giath', .077, .0077, 2+10*1.3, 3, None, 82, .00155]
db['pri_urugon'] = [520, 'duo_rednose', .077, .0077, 2+10*1.3, 3, None, 82, .00155]
db['pri_rednose'] = [520, 'duo_rednose', .077, .0077, 2+10*1.3, 3, None, 82, .00155]
db['pri_muskan'] = [520, 'duo_muskan', .077, .0077, 2+10*1.3, 3, None, 82, .00155]
db['pri_griffon'] = [520, 'duo_muskan', .077, .0077, 2+10*1.3, 3, None, 82, .00155]

db['duo_leebur'] = [615, 'tri_leebur', .0625, .00625, 2+10*1.3, 4, 'pri_leebur', 102, .00125]
db['duo_dimtree'] = [615, 'tri_dimtree', .0625, .00625, 2+10*1.3, 4, 'pri_dimtree', 102, .00125]
db['duo_bheg'] = [615, 'tri_bheg', .0625, .00625, 2+10*1.3, 4, 'pri_bheg', 102, .00125]
db['duo_giath'] = [615, 'tri_giath', .0625, .00625, 2+10*1.3, 4, 'pri_giath', 102, .00125]
db['duo_urugon'] = [615, 'tri_urugon', .0625, .00625, 2+10*1.3, 4, 'pri_urugon', 102, .00125]
db['duo_rednose'] = [615, 'tri_rednose', .0625, .00625, 2+10*1.3, 4, 'pri_rednose', 102, .00125]
db['duo_muskan'] = [615, 'tri_muskan', .0625, .00625, 2+10*1.3, 4, 'pri_muskan', 102, .00125]
db['duo_griffon'] = [615, 'tri_muskan', .0625, .00625, 2+10*1.3, 4, 'pri_muskan', 102, .00125]

db['tri_leebur'] = [720, 'tet_leebur', .02, .002, 2+10*1.3, 5, 'duo_leebur', 340, 0]
db['tri_dimtree'] = [720, 'tet_dimtree', .02, .002, 2+10*1.3, 5, 'duo_dimtree', 340, 0]
db['tri_bheg'] = [720, 'tet_bheg', .02, .002, 2+10*1.3, 5, 'duo_bheg', 340, 0]
db['tri_giath'] = [720, 'tet_giath', .02, .002, 2+10*1.3, 5, 'duo_giath', 340, 0]
db['tri_urugon'] = [720, 'tet_urugon', .02, .002, 2+10*1.3, 5, 'duo_urugon', 340, 0]
db['tri_rednose'] = [720, 'tet_rednose', .02, .002, 2+10*1.3, 5, 'duo_rednose', 340, 0]
db['tri_muskan'] = [720, 'tet_muskan', .02, .002, 2+10*1.3, 5, 'duo_muskan', 340, 0]
db['tri_griffon'] = [720, 'tet_muskan', .02, .002, 2+10*1.3, 5, 'duo_muskan', 340, 0]

db['tet_leebur'] = [1990, 'pen_leebur', .003, .0003, 2+10*1.3, 6, 'tri_leebur', 2324, 0]
db['tet_dimtree'] = [1990, 'pen_dimtree', .003, .0003, 2+10*1.3, 6, 'tri_dimtree', 2324, 0]
db['tet_bheg'] = [1990, 'pen_bheg', .003, .0003, 2+10*1.3, 6, 'tri_bheg', 2324, 0]
db['tet_giath'] = [1990, 'pen_giath', .003, .0003, 2+10*1.3, 6, 'tri_giath', 2324, 0]
db['tet_urugon'] = [1990, 'pen_urugon', .003, .0003, 2+10*1.3, 6, 'tri_urugon', 2324, 0]
db['tet_rednose'] = [1990, 'pen_rednose', .003, .0003, 2+10*1.3, 6, 'tri_rednose', 2324, 0]
db['tet_muskan'] = [1990, 'pen_muskan', .003, .0003, 2+10*1.3, 6, 'tri_muskan', 2324, 0]
db['tet_griffon'] = [1990, 'pen_muskan', .003, .0003, 2+10*1.3, 6, 'tri_muskan', 2324, 0]

db['pen_leebur'] = [17900, 'NA', 0, 0, 0, 0]
db['pen_dimtree'] = [17900, 'NA', 0, 0, 0, 0]
db['pen_bheg'] = [17900, 'NA', 0, 0, 0, 0]
db['pen_giath'] = [17900, 'NA', 0, 0, 0, 0]
db['pen_urugon'] = [17900, 'NA', 0, 0, 0, 0]
db['pen_rednose'] = [17900, 'NA', 0, 0, 0, 0]
db['pen_muskan'] = [17900, 'NA', 0, 0, 0, 0]
db['pen_griffon'] = [17900, 'NA', 0, 0, 0, 0]


pen_db = {}
#cost, name_of_success, base_chance, chance_growth, click_cost, stack_growth, down-grade name, stack softcap, post softcap gfain, pen price, cron(mil)
pen_db['tet_leebur'] = [1850, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 17700, -429*.8725]
pen_db['tet_urugon'] = [2390, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 17200, -493*.8725]
pen_db['tet_muskan'] = [1550, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 15700, -429*.8725]
pen_db['tet_dimtree'] = [2010, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 18400, -493*.8725]
pen_db['tet_rednose'] = [1630, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 17300, -429*.8725]
pen_db['tet_kzarka'] = [1430, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 16100, -531*.8725]
pen_db['tet_dande'] = [1670, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 15500, -611*.8725]
pen_db['tet_kutum'] = [1800, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 18600, -531*.8725]
pen_db['tet_nouver'] = [1590, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 14100, -531*.8725]
pen_db['tri_blackstar'] = [3000, 'pen_boss', .0051, .0005, 2+20*1.3, 5, 'duo_blackstar', 2324, 0, 15000, -591*.8725]

def update_db(database, prices):
	'''
	database = db variable above
	prices = prices dictionary from udpate_prices
	'''
	for i in database.keys():
		if i in prices:
			database[i][0] = prices[i]/1000000

def update_pen_db(database, prices):
	for i in database.keys():
		if i in prices:
			database[i][0] = prices[i]/1000000
		if i[4:] != 'blackstar':
			pen = 'pen_'+i[4:]
			if pen in prices:
				database[i][9] = prices[pen]/1000000

# Grab up to date prices from API
def update_prices(filename):
	prices = {}

	print("Updating Grunil prices...")
	prices['pri_grunil'] = requests.get("https://omegapepega.com/na/Grunil%20Helmet/16", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['duo_grunil'] = requests.get("https://omegapepega.com/na/Grunil%20Helmet/17", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tri_grunil'] = requests.get("https://omegapepega.com/na/Grunil%20Helmet/18", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tet_grunil'] = requests.get("https://omegapepega.com/na/Grunil%20Helmet/19", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pen_grunil'] = requests.get("https://omegapepega.com/na/Grunil%20Helmet/20", headers={'Connection': 'close'}).json()['pricePerOne']

	print("Updating Griffon prices...")
	prices['pri_griffon'] = requests.get("https://omegapepega.com/na/Griffon's%20Helmet/16", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['duo_griffon'] = requests.get("https://omegapepega.com/na/Griffon's%20Helmet/17", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tri_griffon'] = requests.get("https://omegapepega.com/na/Griffon's%20Helmet/18", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tet_griffon'] = requests.get("https://omegapepega.com/na/Griffon's%20Helmet/19", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pen_griffon'] = requests.get("https://omegapepega.com/na/Griffon's%20Helmet/20", headers={'Connection': 'close'}).json()['pricePerOne']

	print("Updating Giath prices...")
	prices['pri_giath'] = requests.get("https://omegapepega.com/na/Giath's%20Helmet/16", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['duo_giath'] = requests.get("https://omegapepega.com/na/Giath's%20Helmet/17", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tri_giath'] = requests.get("https://omegapepega.com/na/Giath's%20Helmet/18", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tet_giath'] = requests.get("https://omegapepega.com/na/Giath's%20Helmet/19", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pen_giath'] = requests.get("https://omegapepega.com/na/Giath's%20Helmet/20", headers={'Connection': 'close'}).json()['pricePerOne']

	print("Updating Red Nose prices...")
	prices['pri_rednose'] = requests.get("https://omegapepega.com/na/Red%20Nose's%20Armor/16", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['duo_rednose'] = requests.get("https://omegapepega.com/na/Red%20Nose's%20Armor/17", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tri_rednose'] = requests.get("https://omegapepega.com/na/Red%20Nose's%20Armor/18", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tet_rednose'] = requests.get("https://omegapepega.com/na/Red%20Nose's%20Armor/19", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pen_rednose'] = requests.get("https://omegapepega.com/na/Red%20Nose's%20Armor/20", headers={'Connection': 'close'}).json()['pricePerOne']

	print("Updating Dim Tree prices...")
	prices['pri_dimtree'] = requests.get("https://omegapepega.com/na/Dim%20Tree%20Spirit's%20Armor/16", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['duo_dimtree'] = requests.get("https://omegapepega.com/na/Dim%20Tree%20Spirit's%20Armor/17", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tri_dimtree'] = requests.get("https://omegapepega.com/na/Dim%20Tree%20Spirit's%20Armor/18", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tet_dimtree'] = requests.get("https://omegapepega.com/na/Dim%20Tree%20Spirit's%20Armor/19", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pen_dimtree'] = requests.get("https://omegapepega.com/na/Dim%20Tree%20Spirit's%20Armor/20", headers={'Connection': 'close'}).json()['pricePerOne']

	print("Updating Muskan prices...")
	prices['pri_muskan'] = requests.get("https://omegapepega.com/na/Muskan's%20Shoes/16", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['duo_muskan'] = requests.get("https://omegapepega.com/na/Muskan's%20Shoes/17", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tri_muskan'] = requests.get("https://omegapepega.com/na/Muskan's%20Shoes/18", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tet_muskan'] = requests.get("https://omegapepega.com/na/Muskan's%20Shoes/19", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pen_muskan'] = requests.get("https://omegapepega.com/na/Muskan's%20Shoes/20", headers={'Connection': 'close'}).json()['pricePerOne']

	print("Updating Urugon prices...")
	prices['pri_urugon'] = requests.get("https://omegapepega.com/na/Urugon's%20Shoes/16", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['duo_urugon'] = requests.get("https://omegapepega.com/na/Urugon's%20Shoes/17", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tri_urugon'] = requests.get("https://omegapepega.com/na/Urugon's%20Shoes/18", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tet_urugon'] = requests.get("https://omegapepega.com/na/Urugon's%20Shoes/19", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pen_urugon'] = requests.get("https://omegapepega.com/na/Urugon's%20Shoes/20", headers={'Connection': 'close'}).json()['pricePerOne']

	print("Updating Bheg prices...")
	prices['pri_bheg'] = requests.get("https://omegapepega.com/na/Bheg's%20Gloves/16", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['duo_bheg'] = requests.get("https://omegapepega.com/na/Bheg's%20Gloves/17", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tri_bheg'] = requests.get("https://omegapepega.com/na/Bheg's%20Gloves/18", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tet_bheg'] = requests.get("https://omegapepega.com/na/Bheg's%20Gloves/19", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pen_bheg'] = requests.get("https://omegapepega.com/na/Bheg's%20Gloves/20", headers={'Connection': 'close'}).json()['pricePerOne']

	print("Updating Leebur prices...")
	prices['pri_leebur'] = requests.get("https://omegapepega.com/na/Leebur's%20Gloves/16", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['duo_leebur'] = requests.get("https://omegapepega.com/na/Leebur's%20Gloves/17", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tri_leebur'] = requests.get("https://omegapepega.com/na/Leebur's%20Gloves/18", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tet_leebur'] = requests.get("https://omegapepega.com/na/Leebur's%20Gloves/19", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pen_leebur'] = requests.get("https://omegapepega.com/na/Leebur's%20Gloves/20", headers={'Connection': 'close'}).json()['pricePerOne']

	with open(filename, 'wb') as file_handler:
	    pickle.dump(prices, file_handler)

	#print(prices)

#prices_file = 'prices.pk'
# ONLY RUN TO UPDATE STALE PRICES
#update_prices(prices_file) #API is SLOW ~1 min to fetch all prices




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
			if "grunil" not in order[current_index] or "pen_" in order[current_index]:
				current_index += 1
				continue
			current_list = db[order[current_index]]
			over_soft_cap = max(0,cur_stack - current_list[7])
			current_success_chance = over_soft_cap*current_list[8] + (cur_stack-over_soft_cap)*current_list[3] + current_list[2]
			current_success_cost = current_list[4] + stack_cost - (db[current_list[1]][0]*tax - current_list[0])
			#print("succ: cost", current_success_cost)
			current_fail_cost = current_list[4]
			if 'grunil' in order[current_index]:
				current_fail_cost += 0.35

			if current_list[6] != None: #aka item can downgrade upon failure
				current_fail_cost += (current_list[0] - db[current_list[6]][0])
			#print("fail: cost", current_fail_cost)
			#cost_to_add = (stack_cost + current_fail_cost)/(1-current_success_chance) - (current_success_chance/(1-current_success_chance)*current_success_cost)
			current_cost = ((current_success_chance*current_success_cost + (1 - current_success_chance)*current_fail_cost))/(1-current_success_chance)/current_list[5]

			#if order[current_index] == 'pri_grunil':
			#print("")
			#print(" name: ", order[current_index], " cost: ", round(current_cost,2))
			#print(" succ_chance: ", current_success_chance)
			#print(" succ_cost: ", current_success_cost)
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

#cost_dict = grunil_break_points(order = ['pri_boss', 'duo_boss', 'tet_boss','pri_grunil', 'duo_grunil', 'tri_grunil', 'tet_grunil'])

def cron_pen(cost_dict, pen_details):
	#db['tet_boss'] = [1990, 'pen_boss', .003, .0003, 2+10*1.3, 6, 'tri_boss', 2324, 0]
	best_stack = 0
	best_profit = 0
	best_clicks = 0
	best_cost = 0
	first = True
	for i in cost_dict.keys():
		cur_odds = i*pen_details[3] + pen_details[2]
		#print(i)
		cost = pen_details[10] - 2 - 13
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

def acc(cost_dict, acc_details ,cron=False):
	best_stack = 0
	best_profit = 0
	best_clicks = 0
	best_cost = 0
	first = True
	for i in cost_dict.keys():
		cur_odds = i*pen_details[3] + pen_details[2]
		#print(i)
		cost = pen_details[10] - 2 - 13
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

def main():
	command = sys.argv[1]
	prices = {}
	if command == "update_prices":
		update_prices('prices.pk')
		exit(1)
	prices_file = 'prices.pk'
	with open(prices_file, 'rb') as file_handler:
		prices = pickle.load(file_handler)
	print("before update")
	for keys in db:
		if "grunil" in keys:
			print(keys,":",db[keys])
	#update_db(db,prices)
	update_pen_db(pen_db, prices)
	print("after update")
	for keys in db:
		if "grunil" in keys:
			print(keys,":",db[keys])
	#print(pen_db)
	if command == "rank_pens":
		print(list(db.keys()))
		cost_dict = grunil_break_points(order = list(db.keys()))
		rank_pens(pen_db,cost_dict)

main()