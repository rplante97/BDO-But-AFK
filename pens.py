import random
import numpy as np

#Simulate cost of enhancing pens, assumes infinite supply of base reblath and infinite supply of stack slots

#Taps stuff until we hit a PEN
#Returns: Total cost of pen boss gear, number of reblath pieces at each enhance level when pen is tapped

#Enhances pri grunil until end_stack target is reached

#----- GLOBALS -----#
conc_cost = 2150000
reblath_repair_cost = 12900
boss_repair_cost = 10 * 1300000
base_stack_cost = 5150000
cron_cost = 429000000
debug = 0
#temp global
succeed_duo = 0
fail_duo = 0

#keeps track of applied modifications
modification_tracker = {}
modification_tracker['pri_reblath'] = 0
modification_tracker['duo_reblath'] = 0
modification_tracker['duo_reblath_2'] = 0
modification_tracker['tri_reblath'] = 0
modification_tracker['tet_reblath'] = 0
modification_tracker['valks'] = 0
modification_tracker['pri_boss'] = 0
modification_tracker['duo_boss'] = 0
modification_tracker['tri_boss'] = 0
modification_tracker['tet_boss'] = 0

#bounds for editing base num clicks
bounds_num_clicks = {}
bounds_num_clicks['pri_reblath'] = (-1, 2)
bounds_num_clicks['duo_reblath'] = (-1, 1)
bounds_num_clicks['duo_reblath_2'] = (-1, 1)
bounds_num_clicks['tri_reblath'] = (-1, 1)
bounds_num_clicks['tet_reblath'] = (-1, 1)
bounds_num_clicks['valks'] = (0, 0)
bounds_num_clicks['pri_boss'] = (-1, 1)
bounds_num_clicks['duo_boss'] = (-1, 1)
bounds_num_clicks['tri_boss'] = (-1, 1)
bounds_num_clicks['tet_boss'] = (0, 0)



def enhance_pri(stack, reblath_arr, stack_arr):
    global succeed_duo
    global fail_duo
    #Constants
    base_chance = .0769
    increase_per_stack = 0.00770
    fs_gain_per_attempt = 3
    cost = 0

    #We always remove the stack from the stack list, if stack grows we reinsert new stack
    stack_arr.remove(stack)
    
    if random.random() < (base_chance + (stack * increase_per_stack)):
        #Success: enhanced piece of gear
        reblath_arr[0] += 1 #add duo
        cost = conc_cost
        if debug == 1:
                print("")
                print("Succeeded pri reblath")
                print("")
    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + reblath_repair_cost
        if debug == 1:
                print("")
                print("Failed pri reblath")
                print("")

    return cost

#-------------------------------------------------------------------------#

def enhance_duo(stack, reblath_arr, stack_arr):
    #Constants
    global succeed_duo
    global fail_duo
    base_chance = 0.0625
    increase_per_stack = 0.00625
    fs_gain_per_attempt = 4
    cost = 0

    #We always remove the stack from the stack list, if stack grows we reinsert new stack
    stack_arr.remove(stack)

    if random.random() < (base_chance + (stack * increase_per_stack)):
        #Success: enhanced piece of gear
        reblath_arr[1] += 1 #add tri
        reblath_arr[0] -= 1 #subtract duo
        cost = conc_cost
        if debug == 1:
                print("")
                print("Succeeded duo reblath")
                print("")
    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + reblath_repair_cost
        reblath_arr[0] -= 1 #subtract duo
        if debug == 1:
                print("")
                print("Failed duo reblath")
                print("")

    return cost


#-------------------------------------------------------------------------#

def enhance_tri(stack, reblath_arr, stack_arr):
    #Constants
    global succeed_duo
    global fail_duo
    base_chance = 0.02
    increase_per_stack = 0.002
    fs_gain_per_attempt = 5
    cost = 0

    #We always remove the stack from the stack list, if stack grows we reinsert new stack
    stack_arr.remove(stack)

    if random.random() < (base_chance + (stack * increase_per_stack)):
        #Success: enhanced piece of gear
        reblath_arr[2] += 1 #add tet
        reblath_arr[1] -= 1 #subtract tri
        cost = conc_cost
        if debug == 1:
                print("")
                print("Succeeded tri reblath")
                print("")

    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + reblath_repair_cost
        reblath_arr[1] -= 1 #subtract tri
        reblath_arr[0] += 1 #add duo
        if debug == 1:
                print("")
                print("Failed tri reblath")
                print("")

    return cost


#-------------------------------------------------------------------------#

def enhance_tet(stack, reblath_arr, stack_arr):
    #Constants
    base_chance = 0.003
    increase_per_stack = 0.0003
    fs_gain_per_attempt = 6
    cost = 0

    #We always remove the stack from the stack list, if stack grows we reinsert new stack
    stack_arr.remove(stack)

    if random.random() < (base_chance + (stack * increase_per_stack)):
        #Success: enhanced piece of gear
        reblath_arr[3] += 1 #add pen
        reblath_arr[2] -= 1 #subtract tet
        cost = conc_cost
        if debug == 1:
                print("")
                print("Succeeded Tet reblath")
                print("")
    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + reblath_repair_cost
        reblath_arr[2] -= 1 #subtract tet
        reblath_arr[1] += 1 #add tri
        if debug == 1:
                print("")
                print("Failed tet reblath")
                print("")

    return cost

#-------------------------------------------------------------------------#

def enhance_pri_boss(stack, boss_arr, stack_arr):
    base_chance = .0769
    increase_per_stack = 0.00770
    fs_gain_per_attempt = 3
    cost = 0

    #We always remove the stack from the stack list, if stack grows we reinsert new stack
    stack_arr.remove(stack)
    
    if random.random() < (base_chance + (stack * increase_per_stack)):
        #Success: enhanced piece of gear
        boss_arr[0] += 1 #add duo
        cost = conc_cost
        if debug == 1:
                print("")
                print("Succeeded pri boss")
                print("")
    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + boss_repair_cost
        if debug == 1:
                print("")
                print("failed pri boss")
                print("")
    
    return cost

#-------------------------------------------------------------------------#

def enhance_duo_boss(stack, boss_arr, stack_arr):
    #Constants
    base_chance = 0.0625
    increase_per_stack = 0.00625
    fs_gain_per_attempt = 4
    cost = 0

    #We always remove the stack from the stack list, if stack grows we reinsert new stack
    stack_arr.remove(stack)

    if random.random() < (base_chance + (stack * increase_per_stack)):
        #Success: enhanced piece of gear
        boss_arr[1] += 1 #add tri
        boss_arr[0] -= 1 #subtract duo
        cost = conc_cost
        if debug == 1:
                print("")
                print("Succeeded duo boss")
                print("")
    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + boss_repair_cost
        boss_arr[0] -= 1 #subtract duo
        if debug == 1:
                print("")
                print("Failed duo boss")
                print("")

    return cost


#-------------------------------------------------------------------------#

def enhance_tri_boss(stack, boss_arr, stack_arr):
    #Constants
    base_chance = 0.02
    increase_per_stack = 0.002
    fs_gain_per_attempt = 5
    cost = 0

    #We always remove the stack from the stack list, if stack grows we reinsert new stack
    stack_arr.remove(stack)

    if random.random() < (base_chance + (stack * increase_per_stack)):
        #Success: enhanced piece of gear
        boss_arr[2] += 1 #add tet
        boss_arr[1] -= 1 #subtract tri
        cost = conc_cost
        if debug == 1:
                print("")
                print("Succeeded tri boss")
                print("")
    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + boss_repair_cost
        boss_arr[1] -= 1 #lose tri
        boss_arr[0] += 1 #add duo
        if debug == 1:
                print("")
                print("Failed tri boss")
                print("")

    return cost


#-------------------------------------------------------------------------#

def enhance_tet_boss(stack, boss_arr, stack_arr):
    #Constants
    base_chance = 0.003
    increase_per_stack = 0.0003
    fs_gain_per_attempt = 6
    cost = 0
    #We always remove the stack from the stack list, if stack grows we reinsert new stack
    stack_arr.remove(stack)

    if random.random() < (base_chance + (stack * increase_per_stack)):
        #Success: enhanced piece of gear
        boss_arr[3] += 1 #add pen
        boss_arr[2] -= 1 #subtract tet
        cost = conc_cost
        hit = True
        if debug == 1:
                print("")
                print("Succeeded tet boss")
                print("")
    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + boss_repair_cost
        boss_arr[2] -= 1
        boss_arr[1] += 1 #add tri
        if debug == 1:
                print("")
                print("Failed tet boss")
                print("")

    return cost


#-------------------------------------------------------------------------#

def cron_tet_boss(stack, boss_arr, stack_arr):
    #Constants
    base_chance = 0.003
    increase_per_stack = 0.0003
    cost = 0
    hitPen = False
    
    #Remove stack from list, we are cronning so we know we will use it
    stack_arr.remove(stack)

    while hitPen is False:

        if random.random() < (base_chance + (stack * increase_per_stack)):
            #Success: enhanced w/ crons
            boss_arr[3] += 1 #add pen
            boss_arr[2] -= 1 #subtract tet
            cost += conc_cost + cron_cost
            hitPen = True
            if debug == 1:
                print("")
                print("Succeeded cronning tet boss")
                print("")
        else: 
            #Failed: add to stack
            cost += conc_cost + boss_repair_cost + cron_cost
            if debug == 1:
                print("")
                print("Failed cronning tet boss")
                print("")

    return cost

#-------------------------------------------------------------------------#

def gen_item_stacks(strategy, num_clicks, stack_gain):
    item_stacks = {}
    cur_stack = 15
    for item in strategy:
        #print(item)
        item_stacks[item] = (cur_stack, cur_stack + (num_clicks[item]-1)*stack_gain[item])
        cur_stack = cur_stack + (num_clicks[item])*stack_gain[item]
    
    return item_stacks

def find_highest_usable_stack(available_stack_list, strategy_rev, item_stacks, array_index_dict, boss_array, reblath_array):
    stack = 15
    cur_item = 0
    while(cur_item < len(strategy_rev)):
        item = strategy_rev[cur_item]

        item_arr = []
        if "boss" in item or item == "valks":
            item_arr = boss_array
        else:
            item_arr = reblath_array
        array_index = array_index_dict[item]
        
        #checks if I have an item of that enhance
        if item_arr[array_index] > 0:
            stack_limits = item_stacks[item]
            possible_stacks = list(x for x in available_stack_list if stack_limits[0] <= x <= stack_limits[1])
            possible_stacks.sort(reverse=True)

            #no possible stacks
            if len(possible_stacks) == 0:
                cur_item += 1
                continue
            stack = possible_stacks[0]
            break
        cur_item += 1
    return stack

def update_num_clicks(base_num_clicks, click_modification):
    for key in base_num_clicks:
        if key == "valks" or key == "tet_boss":
            continue
        else:
            base_num_clicks[key] = max(1,int(base_num_clicks[key] + click_modification[key]))

    for key in click_modification:
        click_modification[key] = 0

    return base_num_clicks
'''
def update_stack_counters(reblath_stack_array, boss_stack_array, available_stack_list, item_stacks, array_index_dict):
    for i in available_stack_list:
        for key in item_stacks:
            lower = item_stacks[key][0]
            upper = item_stacks[key][1]
            if i >= lower and i <= upper:
                index = array_index_dict[key]
                if "boss" in key or key == "valks":
                    boss_stack_array[index] += 1
                else:
                    reblath_stack_array[index] += 1
    return reblath_stack_array, boss_stack_array
'''

def update_click_modifications(available_stack_list, item_stacks, boss_array, reblath_array, array_index_dict, click_modification):
    edit_dict = {}
    threshold = 5
    edit_dict['duo_reblath'] = 'pri_reblath'
    edit_dict['pri_boss'] = 'duo_reblath'
    edit_dict['duo_reblath_2'] = 'pri_boss'
    edit_dict['duo_boss'] = 'duo_reblath_2'
    edit_dict['tri_reblath'] = 'duo_boss'
    edit_dict['tri_boss'] = 'tri_reblath'
    edit_dict['tet_reblath'] = 'tri_boss'
    edit_dict['tet_boss'] = 'tet_reblath'
    debug = 0
    
    for key in click_modification:
        if key == "valks" or key == "pri_reblath":
            continue
        index = array_index_dict[key]
        edit_key = edit_dict[key]
        item_arr = reblath_array
        if "boss" in key or "valks" in key:
            item_arr = boss_array

        #print("stack arr: ", available_stack_list)
        #print([item for item in available_stack_list if item < 30 and item > 0])
        num_viable_stacks = len([item for item in available_stack_list if item <= item_stacks[key][1] and item >= item_stacks[key][0]])
        if (item_arr[index] - num_viable_stacks) > threshold and (modification_tracker[edit_key] - 1) >= bounds_num_clicks[edit_key][0]:
            if debug == 1:
                print("item arr: ", item_arr[index])
                print("stack arr: ", available_stack_list)
                print("")
                print("Decreased", edit_key, "clicks by 1")
                print("")
                print("can lower without going below bound of: ", bounds_num_clicks[edit_key][0])
                stall = input("hit any button")
            click_modification[edit_key] -= 1
            modification_tracker[edit_key] -= 1
        elif (num_viable_stacks - item_arr[index]) > threshold and (modification_tracker[edit_key] + 1) <= bounds_num_clicks[edit_key][1]:
            if debug == 1:
                print("item arr: ", item_arr[index])
                print("stack arr: ", available_stack_list)
                print("")
                print("Increased", edit_key, "clicks by 1")
                print("")
                print("can increase without going above bound of: ", bounds_num_clicks[edit_key][1])
                stall = input("hit any button")
            click_modification[edit_key] += 1
            modification_tracker[edit_key] += 1

    return click_modification




def enhance_pen(reblath_array, boss_array, cost, available_stack_list):

    strategy = ['pri_reblath', 'duo_reblath', 'pri_boss', 'duo_reblath_2', 'duo_boss', 'tri_reblath', 'valks', 'tri_boss', 'tet_reblath', 'tet_boss']

    strategy_rev = [ele for ele in reversed(strategy)] 

    #editable to account for over production of a certain stack or item
    base_num_clicks = {}
    base_num_clicks['pri_reblath'] = 3
    base_num_clicks['duo_reblath'] = 1
    base_num_clicks['duo_reblath_2'] = 2
    base_num_clicks['tri_reblath'] = 4
    base_num_clicks['tet_reblath'] = 3
    base_num_clicks['valks'] = 10
    base_num_clicks['pri_boss'] = 1
    base_num_clicks['duo_boss'] = 2
    base_num_clicks['tri_boss'] = 5
    base_num_clicks['tet_boss'] = 100

    #do not edit. stack gains are not editable
    stack_gain = {}
    stack_gain['pri_reblath'] = 3
    stack_gain['duo_reblath'] = 4
    stack_gain['duo_reblath_2'] = 4
    stack_gain['tri_reblath'] = 5
    stack_gain['tet_reblath'] = 6
    stack_gain['valks'] = 1
    stack_gain['pri_boss'] = 3
    stack_gain['duo_boss'] = 4
    stack_gain['tri_boss'] = 5
    stack_gain['tet_boss'] = 6

    #logic based on threshold X:
    #if a certain number of items exceeds X:
    #   then we decrease the number of clicks of creating that item by 1
    #if a certain number of stacks exceeds X:
    #   then we increase the number of clicks on that stack by 1
    click_modification = {}
    click_modification['pri_reblath'] = 0
    click_modification['duo_reblath'] = 0
    click_modification['duo_reblath_2'] = 0
    click_modification['tri_reblath'] = 0
    click_modification['tet_reblath'] = 0
    click_modification['pri_boss'] = 0
    click_modification['duo_boss'] = 0
    click_modification['tri_boss'] = 0

    #valks and tet_boss should never change
    click_modification['tet_boss'] = 0
    click_modification['valks'] = 0

    refrac = 0 #refractory perdiod of when u can change a value in the click modification, default set to every 10 iterations

    num_clicks = update_num_clicks(base_num_clicks, click_modification)
    item_stacks = gen_item_stacks(strategy, num_clicks, stack_gain)

    array_index_dict = {}
    array_index_dict['pri_reblath'] = 4
    array_index_dict['duo_reblath'] = 0
    array_index_dict['duo_reblath_2'] = 0
    array_index_dict['tri_reblath'] = 1
    array_index_dict['tet_reblath'] = 2
    array_index_dict['pen_reblath'] = 3

    array_index_dict['duo_boss'] = 0
    array_index_dict['tri_boss'] = 1
    array_index_dict['tet_boss'] = 2
    array_index_dict['pen_boss'] = 3
    array_index_dict['pri_boss'] = 4

    array_index_dict['valks'] = 5



    hitPen = False
    #edited these two arrays so that we ALWAYS have pri reblath, and we ALWAYS have valks and pri_boss. Do not edit those values from '1'
    # reblath_array = [0, 0, 0, 0, 1] #Duo, Tri, Tet, Pen, pri
    # boss_array = [0, 0, 0, 0, 1, 1] #Duo, Tri, Tet, Pen, pri, valks
    # cost = 0
    # available_stack_list = [15] #Starting stack we initiall click on
    #current_stack_index = 0

    # #Temp, needed to make looping work, otherwise next time we attempt tet boss function will think it succeeded in pen no matter what
    # boss_array[3] = 0

    while not hitPen:

        #TEMP SMARTER STACKING CODE

        #available_stack_list.extend([89,24,28,45,80,150,29, 24, 40, 57,70])
        #reblath_stack_array, boss_stack_array = update_stack_counters(reblath_stack_array, boss_stack_array, available_stack_list, item_stacks, array_index_dict)

        click_modification = update_click_modifications(available_stack_list, item_stacks, boss_array, reblath_array, array_index_dict, click_modification)

        num_clicks = update_num_clicks(base_num_clicks, click_modification)
        item_stacks = gen_item_stacks(strategy, num_clicks, stack_gain)

        available_stack_list.sort(reverse=True)
        #print("Stack: ", stack)
        print("---------------------------------")
        print("Cost (Millions): ", cost/1000000)
        print("strategy: ", item_stacks)
        print("Stacks List: ")
        print(*available_stack_list, sep=", ")
        print("Reblath Gear: ")
        print("duo_reblath: ", reblath_array[0], "| tri_reblath: ", reblath_array[1], "| tet_reblath: ", reblath_array[2], "| pen_reblath: ", reblath_array[3], )
        print("Boss Gear: ")
        print("duo_boss: ", boss_array[0], "| tri_boss: ", boss_array[1], "| tet_boss: ", boss_array[2], "| pen_boss: ", boss_array[3], )
        print("")

        if boss_array[3] > 0:
            hitPen = True
            break

        #If we have no stacks then add another 15 (base) stack 
        if not available_stack_list:
            #print("adding 15 stack stack list")
            available_stack_list = [15]
            cost += base_stack_cost
            if debug == 1:
                print("")
                print("Added new 15 stack")
                print("")
        
        #If all availble stacks are too high to tap PRI reblath on add a base stack in case it is needed
        #print("smallest stack: ", min(available_stack_list))
        if min(available_stack_list) > item_stacks['pri_reblath'][1]:
            available_stack_list.append(15)
            cost += base_stack_cost
            if debug == 1:
                print("")
                print("Added new 15 stack")
                print("")
            #print("adding 15 stack #2")

        #Pick biggest stack that MAY be useable
        #stack = available_stack_list[current_stack_index]
        stack = find_highest_usable_stack(available_stack_list, strategy_rev, item_stacks, array_index_dict, boss_array, reblath_array)
        #print("stack: ", stack)

        #Tap Pri reblath
        if item_stacks['pri_reblath'][0] <= stack <= item_stacks['pri_reblath'][1]:
            #Assume inf supply of PRI reblath, aka we can always click it
            cost += enhance_pri(stack, reblath_array, available_stack_list)
            #Reset current stack index
            #current_stack_index = 0
            

        #Tap Duo reblath
        elif item_stacks['duo_reblath'][0] <= stack <= item_stacks['duo_reblath'][1] or item_stacks['duo_reblath_2'][0] <= stack <= item_stacks['duo_reblath_2'][1]:
            #Test if suitable gear to click on proposed stack exists
            if reblath_array[0] > 0:
                cost += enhance_duo(stack, reblath_array, available_stack_list)
            else:
                continue
        
        #Tap Pri boss
        elif item_stacks['pri_boss'][0] <= stack <= item_stacks['pri_boss'][1]:
            #Assume inf pri boss supply
            cost += enhance_pri_boss(stack, boss_array, available_stack_list)
            #current_stack_index = 0
        #Tap Duo boss
        elif item_stacks['duo_boss'][0] <= stack <= item_stacks['duo_boss'][1]:
            #Test if suitable gear to click on proposed stack exists
            if boss_array[0] > 0:
                cost += enhance_duo_boss(stack, boss_array, available_stack_list)
                #current_stack_index = 0
            else:
                #Click on this stack not possible, try next highest stack
                #current_stack_index += 1
                continue
        
        #Tap Tri reblath
        elif item_stacks['tri_reblath'][0] <= stack <= item_stacks['tri_reblath'][1]:
            #Test if suitable gear to click on proposed stack exists
            if reblath_array[1] > 0:
                cost += enhance_tri(stack, reblath_array, available_stack_list)
                #current_stack_index = 0
            else:
                #Click on this stack not possible, try next highest stack
                #current_stack_index += 1
                continue

        #Valks +10
        elif item_stacks['valks'][0] <= stack <= item_stacks['valks'][1]:
            available_stack_list.remove(stack)
            available_stack_list.append(stack + 10)
            cost += 30000000 #10 valks ~30 mil value based on costumes
            if debug == 1:
                    print("")
                    print("added valks")
                    print("")

        #Tap Tri boss
        elif item_stacks['tri_boss'][0] <= stack <= item_stacks['tri_boss'][1]:
            #Test if suitable gear to click on proposed stack exists
            if boss_array[1] > 0:
                cost += enhance_tri_boss(stack, boss_array, available_stack_list)
                #current_stack_index = 0
            else:
                #Click on this stack not possible, try next highest stack
                #current_stack_index += 1
                continue

        # #Tap Tet reblath
        elif item_stacks['tet_reblath'][0] <= stack <= item_stacks['tet_reblath'][1]:
            #Test if suitable gear to click on proposed stack exists
            if reblath_array[2] > 0:
                cost += enhance_tet(stack, reblath_array, available_stack_list)
                #current_stack_index = 0
            else:
                #Click on this stack not possible, try next highest stack
                #current_stack_index += 1
                continue

        #Tap Tet boss
        elif item_stacks['tet_boss'][0] <= stack <= item_stacks['tet_boss'][1]:
            
            num_pens_before_tap = boss_array[3]

            #Test if second largest stack is large enough to cron
            #print("Second largest stack: ", available_stack_list[1])
            if(available_stack_list[1] >= 100):
                #print("Cronning tet boss")
                cost += cron_tet_boss(available_stack_list[1], boss_array, available_stack_list)
            else:
                cost += enhance_tet_boss(stack, boss_array, available_stack_list)
                if boss_array[3] > num_pens_before_tap or boss_array[3] > 1:
                    hitPen = True



            # if boss_array[2] > 0:
            #     cost += enhance_tet_boss(stack, boss_array, available_stack_list)
            #     #current_stack_index = 0
            #     if boss_array[3] > 0:
            #         hitPen = True
            # else:
            #     #Click on this stack not possible, try next highest stack
            #     #current_stack_index += 1
            #     #Check to see if we hit a pen
            #     continue

        #Error condition
        else:
            print(stack)
            print("strategy: ", item_stacks)
            print("Stack: ", stack)
            print("Cost (Millions): ", cost/1000000)
            print("Stacks List: ")
            print(*available_stack_list, sep=", ")
            print("Reblath Gear: ")
            print("duo_reblath: ", reblath_array[0], "| tri_reblath: ", reblath_array[1], "| tet_reblath: ", reblath_array[2], "| pen_reblath: ", reblath_array[3], )
            print("Boss Gear: ")
            print("duo_boss: ", boss_array[0], "| tri_boss: ", boss_array[1], "| tet_boss: ", boss_array[2], "| pen_boss: ", boss_array[3], )
            exit(1)

        if debug == 1:
            next = input("hit any button for next: ")

        #print("Cost: ", cost/1000000)

    #This code is reachable only after a PEN boss item is enhanced
    print("Stack: ", stack)
    print("strategy: ", item_stacks)
    print("Cost (Millions): ", cost/1000000)
    print("Stacks List: ")
    print(*available_stack_list, sep=", ")
    print("Reblath Gear: ")
    print("duo_reblath: ", reblath_array[0], "| tri_reblath: ", reblath_array[1], "| tet_reblath: ", reblath_array[2], "| pen_reblath: ", reblath_array[3], )
    print("Boss Gear: ")
    print("duo_boss: ", boss_array[0], "| tri_boss: ", boss_array[1], "| tet_boss: ", boss_array[2], "| pen_boss: ", boss_array[3], )

    return reblath_array, boss_array, cost, available_stack_list



def main(iterations):
    #enhance_pen()
    reblath_array = [0, 1, 0, 0, 1] #Duo, Tri, Tet, Pen, pri
    boss_array = [2, 0, 0, 0, 1, 1] #Duo, Tri, Tet, Pen, pri, valks
    #reblath_stack_array = [0, 0, 0, 0, 0] #duo, tri, tet, pen, pri
    #boss_stack_array = [0, 0, 0, 0, 0, 0] #duo, tri, tet, pen, pri, valks
    cost = 0
    available_stack_list = [39,24,24,24,24,24,24,24,24,24,15] #Starting stack we initiall click on

    cost_list = []
    for i in range(iterations):
        print("-------------------------------------------------------------------------------------------------------------")
        print()
        reblath_array, boss_array, cost, available_stack_list =  enhance_pen(reblath_array, boss_array, 0, available_stack_list)
        cost_list.append(cost/1000000)
        print("-------------------------------------------------------------------------------------------------------------")

    # cost_mil = cost/1000000
    # avg_cost = cost_mil/iterations
    print(cost_list)
    print(sum(cost_list))
    print(len(cost_list))
    #print("Avg Cost: ", sum(cost_list)/iterations)
    print("Avg Cost Per Pen: ", sum(cost_list)/boss_array[3])


#RUN MAIN
main(1)