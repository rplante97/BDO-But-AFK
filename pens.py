import random

#Simulate cost of enhancing pens, assumes infinite supply of base reblath and infinite supply of stack slots

#Taps stuff until we hit a PEN
#Returns: Total cost of pen boss gear, number of reblath pieces at each enhance level when pen is tapped

#Enhances pri grunil until end_stack target is reached

#----- GLOBALS -----#
conc_cost = 2150000
reblath_repair_cost = 12900
boss_repair_cost = 10 * 1300000
base_stack_cost = 5150000

#temp global
succeed_duo = 0
fail_duo = 0

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
    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + reblath_repair_cost

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
    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + reblath_repair_cost
        reblath_arr[0] -= 1 #subtract duo

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

    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + reblath_repair_cost
        reblath_arr[1] -= 1 #subtract tri
        reblath_arr[0] += 1 #add duo

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
    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + reblath_repair_cost
        reblath_arr[2] -= 1 #subtract tet
        reblath_arr[1] += 1 #add tri

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
    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + boss_repair_cost
    
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
    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + boss_repair_cost
        boss_arr[0] -= 1 #subtract duo

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
    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + boss_repair_cost
        boss_arr[1] -= 1 #lose tri
        boss_arr[0] += 1 #add duo

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
    else: 
        #Failed: add to stack
        stack_arr.append(stack + fs_gain_per_attempt)
        cost = conc_cost + boss_repair_cost
        boss_arr[2] -= 1
        boss_arr[1] += 1 #add tri

    return cost


#-------------------------------------------------------------------------#

def enhance_pen():
    global succeed_duo
    global fail_duo

    hitPen = False
    reblath_array = [0, 0, 0, 0] #Duo, Tri, Tet, Pen
    boss_array = [0, 0, 0, 0] #Duo, Tri, Tet, Pen
    cost = 0
    available_stack_list = [15] #Starting stack we initiall click on
    current_stack_index = 0

    num_pri_tap = 4
    num_duo_tap = 1
    num_duo_tap_2 = 2
    num_tri_tap = 4
    num_tet_tap = 3

    num_pri_boss_tap = 1
    num_duo_boss_tap = 2
    num_tri_boss_tap = 3

    pri_start = 15
    pri_gain = 3

    duo_start = pri_start + num_pri_tap * pri_gain
    duo_gain = 4

    pri_boss_start = duo_start + num_duo_tap *duo_gain
    pri_boss_gain = 3

    duo_start_two = pri_boss_start + num_pri_boss_tap * pri_boss_gain
    duo_gain_two = 4

    duo_boss_start = duo_start_two + num_duo_tap_2 * duo_gain_two
    duo_boss_gain = 4

    tri_start = duo_boss_start + num_duo_boss_tap * duo_boss_gain
    tri_gain = 5

    valks_start = tri_start + num_tri_tap*tri_gain

    tri_boss_start = valks_start + 10
    tri_boss_gain = 5   

    tet_start = tri_boss_start + num_tri_boss_tap*tri_boss_gain
    tet_gain = 6

    tet_boss_start = tet_start + num_tet_tap*tet_gain

    print("pri ", pri_start)
    print("duo ", duo_start)
    print("pri boss", pri_boss_start)
    print("duo 2: ", duo_start_two)
    print("duo boss: ", duo_boss_start)
    print("tri : ", tri_start)
    print("valks start: ", valks_start)
    print("tri boss: ", tri_boss_start)
    print("tet start: ", tet_start)
    print("tet_boss_start ", tet_boss_start)
    #exit(1)



    while not hitPen:
        #Sort stack list in descending order
        available_stack_list.sort(reverse=True)

        #If we have no stacks then add another 15 (base) stack 
        if not available_stack_list:
            print("adding 15 stack stack list")
            available_stack_list = [15]
            cost += base_stack_cost
        
        #If all availble stacks are too high to tap PRI reblath on add a base stack in case it is needed
        if available_stack_list[-1] > 21:
            available_stack_list.append(15)
            cost += base_stack_cost
            print("adding 15 stack #2")

        #Pick biggest stack that MAY be useable
        stack = available_stack_list[current_stack_index]

        #print("Max Stack: ", stack)
        #print(*reblath_array, sep = ", ")
        #print(*available_stack_list, sep = ", ")
        #if (succeed_duo + fail_duo) != 0:
        #    print("success: ", succeed_duo / (succeed_duo +fail_duo))

        #Tap Pri reblath
        if stack in(pri_start, pri_start + 1 * pri_gain, pri_start + 2 * pri_gain):
            #Assume inf supply of PRI reblath, aka we can always click it
            cost += enhance_pri(stack, reblath_array, available_stack_list)
            #Reset current stack index
            current_stack_index = 0
            

        #Tap Duo reblath
        elif stack in (duo_start, duo_start_two, duo_start_two + duo_gain):
            #Test if suitable gear to click on proposed stack exists
            if reblath_array[0] > 0:
                cost += enhance_duo(stack, reblath_array, available_stack_list)
                current_stack_index = 0
            else:
                #Click on this stack not possible, try next highest stack
                current_stack_index += 1
                continue
        
        #Tap Pri boss
        elif stack in (pri_boss_start, pri_boss_start + pri_boss_gain):
            #Assume inf pri boss supply
            cost += enhance_pri_boss(stack, boss_array, available_stack_list)
            current_stack_index = 0

        #Tap Duo boss
        elif stack in (duo_boss_start, duo_boss_start + duo_boss_gain):
            #Test if suitable gear to click on proposed stack exists
            if boss_array[0] > 0:
                cost += enhance_duo_boss(stack, boss_array, available_stack_list)
                current_stack_index = 0
            else:
                #Click on this stack not possible, try next highest stack
                current_stack_index += 1
                continue
        
        #Tap Tri reblath
        elif stack in (tri_start, tri_start + tri_gain, tri_start + 2*tri_gain, tri_start + 3*tri_gain):
            #Test if suitable gear to click on proposed stack exists
            if reblath_array[1] > 0:
                cost += enhance_tri(stack, reblath_array, available_stack_list)
                current_stack_index = 0
            else:
                #Click on this stack not possible, try next highest stack
                current_stack_index += 1
                continue

        #Valks +10
        elif stack == valks_start:
            available_stack_list.remove(stack)
            available_stack_list.append(stack + 10)
            cost += 30000000 #10 valks ~30 mil value based on costumes

        #Tap Tri boss
        elif stack in (tri_boss_start, tri_boss_start + 1 * tri_boss_gain, tri_boss_start + 2*tri_boss_gain):
            #Test if suitable gear to click on proposed stack exists
            if boss_array[1] > 0:
                cost += enhance_tri_boss(stack, boss_array, available_stack_list)
                current_stack_index = 0
            else:
                #Click on this stack not possible, try next highest stack
                current_stack_index += 1
                continue

        #Tap Tet reblath
        elif stack in (tet_start, tet_start + 1*tet_gain, tet_start + 2*tet_gain):
            #Test if suitable gear to click on proposed stack exists
            if reblath_array[2] > 0:
                cost += enhance_tet(stack, reblath_array, available_stack_list)
                current_stack_index = 0
            else:
                #Click on this stack not possible, try next highest stack
                current_stack_index += 1
                continue

        #Tap Tet boss
        elif stack >= tet_boss_start:
            #Test if suitable gear to click on proposed stack exists
            if boss_array[2] > 0:
                cost += enhance_tet_boss(stack, boss_array, available_stack_list)
                current_stack_index = 0
                if boss_array[3] > 0:
                    hitPen = True
            else:
                #Click on this stack not possible, try next highest stack
                current_stack_index += 1
                #Check to see if we hit a pen
                continue

        #Error condition
        else:
            print(stack)
            print("Error: Unhandled stack value")


        print("Cost: ", cost/1000000)

    #This code is reachable only after a PEN boss item is enhanced
    print("Stack: ", stack)
    print("Cost (Millions): ", cost/1000000)
    print("Stacks List: ")
    print(*available_stack_list, sep=", ")
    print("Reblath Gear: ")
    print(*reblath_array, sep=", ")
    print("Boss Gear: ")
    print(*boss_array, sep=", ")



def main():
    enhance_pen()

#RUN MAIN
main()