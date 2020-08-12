import random
disto_price = 295
downgrade_chance = 0.3

crons = [62, 187, 562, 1562]
#0.275
success_chance = [0.745, 0.5, 0.405, 0.3] #This equates to stacks 27, 40, 44, 100

# print(tet_cost)

#Simulation
cost = 0 #20 bil
enhance_level = 0
stack_usage = [0, 0, 0, 0]
fail_counter = [0, 0, 0, 0]
trials = 100000

for i in range(trials):
    enhance_level = 0 #Reset enhance to 0 after each run
    while enhance_level < 4:
        #Cost per tap is always just the price of disto + amount of crons used
        cost = cost + disto_price + crons[enhance_level]
        if random.random() < success_chance[enhance_level]:
            #Enhance success
            stack_usage[enhance_level] += 1 #reflect usage of stack on success
            enhance_level += 1 #increment our enhance level
            
        else:
            #Enhance failure
            if random.random() < downgrade_chance:
                #Enhancement caused downgrade
                fail_counter[enhance_level] += 1
                if enhance_level > 0: #Downgrade unless we failed a tap for PRI
                    enhance_level -= 1

print("Total Trials: " + str(trials))
print("Average Cost: " + str(cost/trials))
print("[Stacks Used (Avg)] " + "PRI: " + str(stack_usage[0]/trials) + " | DUO: " + str(stack_usage[1]/trials) + " | TRI: " + str(stack_usage[2]/trials) + " | TET: " + str(stack_usage[3]/trials))
print("[Downgrade Rate]    " + "PRI: " + str(fail_counter[0]/trials) + " | DUO: " + str(fail_counter[1]/trials) + " | TRI: " + str(fail_counter[2]/trials) + " | TET: " + str(fail_counter[3]/trials))


    