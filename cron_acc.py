#how to run this program from the command line:

#python cron_acc.py base_price sell_price sell_level "cron"


#base_price - base price of the item in terms of mil, so 10,000,000 should be set in as 10
#sell_price - sell price of the item also in mil (see above)
#sell_level - 1 = pri, 2 = duo, 3 = tri, 4 = tet
#"cron", type "cron" in if you want to use cron, otherwise leave it blank

import random
import sys
random.seed(None)
downgrade_chance = 0.3

crons = [62, 187, 562, 1562]
crons1 = [24, 74, 224, 625]
#0.275
success_chance = [0.745, 0.5, 0.405, 0.3] #This equates to stacks 27, 40, 44, 110

# print(tet_cost)

#Simulation
total_cost = 0
enhance_level = 0
stack_costs = [10.5, 116, 116, 1800]
stack_usage = [0, 0, 0, 0]
fail_counter = [0, 0, 0, 0]
downgrade_counter = [0,0,0,0]
acc_price = float(sys.argv[1])
reward = float(sys.argv[2])
cron = [False, False, False, False]
if sys.argv[4] == "cron":
    cron = [True, True, True, True]

sell_level = int(sys.argv[3])
clicks = [0,0,0,0]
rip = 0
trials = 100000

for i in range(trials):
    enhance_level = 0 #Reset enhance to 0 after each run
    cost = 0 
    while enhance_level < sell_level:
        #Cost per tap is always just the price of disto + amount of crons used
        cost = cost + acc_price
        clicks[enhance_level] += 1
        if cron[enhance_level] == True:
            cost += crons[enhance_level]
        #print(str(cost) + " | " + str(crons[enhance_level]))
        if random.random() < success_chance[enhance_level]:
            #Enhance success
            stack_usage[enhance_level] += 1 #reflect usage of stack on success
            enhance_level += 1 #increment our enhance level
            
        else:
            #Enhance failure
            fail_counter[enhance_level] += 1
            if cron[enhance_level] == True:
                if random.random() < downgrade_chance:
                    #Enhancement caused downgrade
                    downgrade_counter[enhance_level] += 1
                    if enhance_level > 0: #Downgrade unless we failed a tap for PRI
                        enhance_level -= 1
            else:
                enhance_level = 0

        #print(enhance_level)
        
    total_cost = total_cost + cost

for i in range(len(clicks)):
    clicks[i] = clicks[i]/trials

print(clicks)
overall_stack_cost = 0
for i in range(len(stack_costs)):
    overall_stack_cost += stack_usage[i]/trials*stack_costs[i]
print("stack costs: ", overall_stack_cost)
print("Total Trials: " + str(trials))
print("Average Cost: " + str(total_cost/trials))
levels = ['PRI', 'DUO', 'TRI', 'TET']
stack_used = "[Stacks Used (Avg)]: "
downgrade_rate = "[Downgrade Rate]    "
failure_rate = "[Failutre Rate]    "
i = 0
while(i < sell_level):
    stack_used += levels[i]+" "+str(stack_usage[i]/trials) + " || "
    downgrade_rate += levels[i] + " " +str(downgrade_counter[i]/trials/clicks[i]) + " || "
    failure_rate += levels[i] + " " + str(fail_counter[i]/trials/clicks[i]) + " || "
    i += 1
print("Profit: ", str((reward * .85) - (total_cost/trials+overall_stack_cost)))
print(stack_used)
print(downgrade_rate)
print(failure_rate)
print("[success rate]          " + "PRI: " + str(stack_usage[0]/trials/clicks[0]) + " | DUO: " + str(stack_usage[1]/trials/clicks[1]) + " | TRI: " + str(stack_usage[2]/trials/clicks[2]) + " | TET: " + str(stack_usage[3]/trials/clicks[3]))
#print("Num Attempts Costing > 50 Bil: " + str(rip))

