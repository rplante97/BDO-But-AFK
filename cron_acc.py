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
success_chance = [0.745, 0.5, 0.405, 0.3] #This equates to stacks 27, 40, 44, 100

# print(tet_cost)

#Simulation
<<<<<<< HEAD
total_cost = 0
=======
cost = 0 #20 bil
>>>>>>> parent of 8515ae9... Biohack failstack method calcs
enhance_level = 0
stack_costs = [10.5, 116, 116, 1800]
stack_usage = [0, 0, 0, 0]
fail_counter = [0, 0, 0, 0]
<<<<<<< HEAD
downgrade_counter = [0,0,0,0]
acc_price = float(sys.argv[1])
reward = float(sys.argv[2])
cron = [False, False, False, False]
if sys.argv[4] == "cron":
    cron = [True, True, True, True]

sell_level = int(sys.argv[3])
clicks = [0,0,0,0]
rip = 0
trials = 1000

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
=======
trials = 100000

for i in range(trials):
    enhance_level = 0 #Reset enhance to 0 after each run
    while enhance_level < 4:
        #Cost per tap is always just the price of disto + amount of crons used
        cost = cost + disto_price + crons[enhance_level]
>>>>>>> parent of 8515ae9... Biohack failstack method calcs
        if random.random() < success_chance[enhance_level]:
            #Enhance success
            stack_usage[enhance_level] += 1 #reflect usage of stack on success
            enhance_level += 1 #increment our enhance level
            
        else:
            #Enhance failure
<<<<<<< HEAD
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
=======
            if random.random() < downgrade_chance:
                #Enhancement caused downgrade
                fail_counter[enhance_level] += 1
                if enhance_level > 0: #Downgrade unless we failed a tap for PRI
                    enhance_level -= 1
>>>>>>> parent of 8515ae9... Biohack failstack method calcs

for i in range(len(clicks)):
    clicks[i] = clicks[i]/trials

print(stack_usage)
overall_stack_cost = 0
for i in range(len(stack_costs)):
    overall_stack_cost += stack_usage[i]*stack_costs[i]
print("average stack costs: ", overall_stack_cost/trials)
print("Total Trials: " + str(trials))
<<<<<<< HEAD
print("average Cost in accs: " + str(total_cost/trials))
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
print("Profit per acc: ", str(reward*0.85 - total_cost/trials - overall_stack_cost/trials))
print(stack_used)
print(downgrade_rate)
print(failure_rate)
print("[success rate]          " + "PRI: " + str(stack_usage[0]/trials/clicks[0]) + " | DUO: " + str(stack_usage[1]/trials/clicks[1]) + " | TRI: " + str(stack_usage[2]/trials/clicks[2]) + " | TET: " + str(stack_usage[3]/trials/clicks[3]))
#print("Num Attempts Costing > 50 Bil: " + str(rip))
=======
print("Average Cost: " + str(cost/trials))
print("[Stacks Used (Avg)] " + "PRI: " + str(stack_usage[0]/trials) + " | DUO: " + str(stack_usage[1]/trials) + " | TRI: " + str(stack_usage[2]/trials) + " | TET: " + str(stack_usage[3]/trials))
print("[Downgrade Rate]    " + "PRI: " + str(fail_counter[0]/trials) + " | DUO: " + str(fail_counter[1]/trials) + " | TRI: " + str(fail_counter[2]/trials) + " | TET: " + str(fail_counter[3]/trials))

>>>>>>> parent of 8515ae9... Biohack failstack method calcs

    