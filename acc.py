import numpy as np
import sys

base_price = sys.argv[1]
pri_price = sys.argv[2]
duo_price = sys.argv[3]
tri_price = sys.argv[4]
tet_price = sys.argv[5]

prices = np.asarray([float(base_price), float(pri_price),float(duo_price),float(tri_price)])

compare_prices = np.asarray([float(pri_price),float(duo_price),float(tri_price),float(tet_price)])
odds = np.asarray([0.7, 0.5, 0.4, 0.3])

stack_costs = np.asarray([6, 95, 95, 3000])
expected = 1/odds

profit = []
for i,j in zip(range(len(prices)), range(len((expected)))):
	profit_i= (prices[i]+ float(base_price))*expected[j] + stack_costs[i]
	if i != len(prices) - 1 and profit_i < prices[i+1]:
		prices[i+1] = profit_i
	profit.append(profit_i)

profit = np.asarray(profit)


print("margins: ", compare_prices - profit)