import random
import sys
random.seed(None)
downgrade_chance = 0.3

crons = [62, 187, 562, 1562]
crons1 = [24, 74, 224, 625]
#0.275
success_chance = [0.75, 0.5, 0.405, 0.3] #This equates to stacks 27, 40, 44, 110

# print(tet_cost)

#Simulation
total_cost = 0
enhance_level = 0
stack_costs = [10,110,110,1800]
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
trials = 10000
total_acc_used = 0
for i in range(trials):
    enhance_level = 0 #Reset enhance to 0 after each run
    cost = 0 
    acc_used = 0
    while enhance_level < sell_level:
        #Cost per tap is always just the price of disto + amount of crons used
        cost = cost + acc_price
        acc_used += 1
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

        
    total_cost = total_cost + cost
    total_acc_used += acc_used
    #print(cost)
    if enhance_level == sell_level:
        if cost > 60000:
            rip += 1

for i in range(len(clicks)):
    clicks[i] = clicks[i]/trials
overall_stack_cost = 0
for i in range(len(stack_costs)):
    overall_stack_cost += stack_usage[i]/trials*stack_costs[i]
print("Total Trials: " + str(trials))
print("Average Cost: " + str(total_cost/trials + overall_stack_cost))
print("Average acc used: " + str(total_acc_used/trials))
print("Average money in Acc: ", str(total_acc_used/trials*acc_price))
print("Average money in Crons: ", str(total_cost/trials - total_acc_used/trials*acc_price))
levels = ['PRI', 'DUO', 'TRI', 'TET']
stack_used = "[Stacks Used (Avg)]: "
downgrade_rate = "[Downgrade Rate]    "
failure_rate = "[Failutre Rate]    "

print("Profit: ", str((reward * .85) - (total_cost/trials + overall_stack_cost)))
print(stack_used)
print(downgrade_rate)
print(failure_rate)
print("Average Cost: " + str(total_cost/trials))
print("[Stacks Used (Avg)]          " + "PRI: " + str(stack_usage[0]/trials) + " | DUO: " + str(stack_usage[1]/trials) + " | TRI: " + str(stack_usage[2]/trials) + " | TET: " + str(stack_usage[3]/trials))
print("[Failed Attempt + Downgrade] " + "PRI: " + str(fail_counter[0]/trials) + " | DUO: " + str(fail_counter[1]/trials) + " | TRI: " + str(fail_counter[2]/trials) + " | TET: " + str(fail_counter[3]/trials))
print("Num Attempts Costing > 50 Bil: " + str(rip))

