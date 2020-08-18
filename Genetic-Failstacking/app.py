# STEP 1: Be able to simulate enhancing to x stack given some preprogrammed method
# STEP 2: Paramaterize fs method so it can be used as "DNA"
# STEP 3: Implement genetic algorthim to optimize fs method solution space

import random

#----- GLOBAL CONSTANTS -----
base_grunil_price = 0.343 #Pull from API later
concentrated_price = 2.25 #Pull from API later
starting_fs = 21 #Base failstack you begin enhancing on
cost_of_base_fs = 10
num_pri_grunil = 250 #number of grunil pieces you have to enhance with
cost_per_click_fail = base_grunil_price + concentrated_price
cost_per_click_success = concentrated_price + cost_of_base_fs
fs_per_click = [2, 3, 4, 5] #Failstacks for FAILING TO TAP: duo, tri, tet, pen

# Create success chance 2D array:
pri_to_duo = [0.0769, 0.0077, 82, 0.00155] #base chance, increase per stack (before softcap), softcap stack, increase per stack (after softcap)
duo_to_tri = [0.0625, 0.00625, 102, 0.00125] 
tri_to_tet = [0.02, 0.002, 340, 0]
tet_to_pen = [0.003, 0.0003, 2324, 0]

success_chances = [pri_to_duo, duo_to_tri, tri_to_tet, tet_to_pen]



# Create clicking method 2D array [Will optimize over this array later]
# These numbers are INCLUSIVE, any number in range, including endpoints, we will tap on
pri_to_duo_click_range = [starting_fs, 29]
duo_to_tri_click_range = [30, 49]
tri_to_tet_click_range = [50, 99]
tet_to_pen_click_range = [100, 200]

click_method = [pri_to_duo_click_range, duo_to_tri_click_range, tri_to_tet_click_range, tet_to_pen_click_range]

# -----------------------------------------------------------------------------------------------

def sustainably_build_fs(num_pri_grunils, target_stack):
    #This function will return the average cost of a failstack built using a SUSTAINABLE method. In this context sustainable means
    #that there is no influx of new armor pieces to failstack on as the stack is built, what you start with is what you end with.
    #This means that the function is (like in real life) occasionally forced to make less than optimal taps if the optimal enhance
    #level is not available within the existing supply. This results in a much more accurate avg failstack cost.
    #INPUTS:
    #num_pri_grunils: Your supply of failstacking armor pieces
    #target_stack: The failstack number you would like to build
    #iterations: The amount of times to run the simulation

    # count_pri = num_pri_grunils
    # count_duo = 0
    # count_tri = 0
    # count_tet = 0
    # count_pen = 0

    armor_level_counts = [num_pri_grunils, 0, 0, 0, 0] #pri count, duo count, tri count, tet count, pen count
    saved_stacks = []
    stack = starting_fs # fuck with this later, need to account for cost of 20 stacks
    cost = 10
    number_of_taps = 0
    while stack < target_stack:
        if (stack <= pri_to_duo_click_range[1]) and (armor_level_counts[0] != 0):
            print("Clicking PRI")
            [stack, cost, armor_level_counts] = click(0, armor_level_counts, pri_to_duo, stack, cost)
        elif (stack <= duo_to_tri_click_range[1]) and (armor_level_counts[1] != 0):
            print("Clicking DUO")
            [stack, cost, armor_level_counts] = click(1, armor_level_counts, duo_to_tri, stack, cost)
        elif (stack <= tri_to_tet_click_range[1]) and (armor_level_counts[2] != 0):
            print("Clicking TRI")
            [stack, cost, armor_level_counts] = click(2, armor_level_counts, tri_to_tet, stack, cost)
        elif (stack <= tet_to_pen_click_range[1]) and (armor_level_counts[3] != 0):
            print("Clicking TET")
            [stack, cost, armor_level_counts] = click(3, armor_level_counts, tet_to_pen, stack, cost)
        else:
            saved_stacks.append(stack)
            stack = starting_fs 
        #     print("EVERYTHING IS PEN?!?!?!?")
        #     print("Pens made: " + str(armor_level_counts[4]))
        #     print("Num PRIs: " + str(armor_level_counts[0]))
        #     print("Num DUOs: " + str(armor_level_counts[1]))
        #     print("Num TRIs: " + str(armor_level_counts[2]))
        #     print("Num TETs: " + str(armor_level_counts[3]))
        #     return

        number_of_taps += 1
        
        
        print("Num Taps: " + str(number_of_taps))
        print("Cost: " + str(cost))
        print("Current Stack: " + str(stack))

    print("Pens made: " + str(armor_level_counts[4]))
    print("Num PRIs: " + str(armor_level_counts[0]))
    print("Num DUOs: " + str(armor_level_counts[1]))
    print("Num TRIs: " + str(armor_level_counts[2]))
    print("Num TETs: " + str(armor_level_counts[3]))
    print(saved_stacks)

    #Determine what taps we can make
    #if stack in range but cannot make tap, go to next best range

    # if stack in range(pri_to_duo_click_range[0], pri_to_duo_click_range[1] + 1): # and available
    #     print("lol")
    # elif stack in range(duo_to_tri_click_range[0], duo_to_tri_click_range[1] + 1): # if stack in range pri OR duo (and duo available)
    #     print("ranges get fucked lol")
    # elif stack in range(tri_to_tet_click_range[0], tri_to_tet_click_range[1] + 1):
    #     print("todo")
    # elif stack in range (tet_to_pen_click_range[0], tet_to_pen_click_range[1] + 1):
    #     print("todo")
    # else:
    #     print("Something went wrong fam")

# def test():
#     if stack >= pri_to_duo_click_range[0] and stack <= pri_to_duo_click_range[1] and isAvailble:
#         do x
#     elif stack >= pri_to_duo_click_range[0] and stack <= duo_to_tri_click_range[1] and isAvailble:
#         do x
#     elif stack >= pri_to_duo_click_range[0] and stack <= tri_to_tet_click_range[1] and isAvailable:
#         do x
#     elif stack >= pri_to_duo_click_range[0] and stack <= tet_to_pen_click_range[1] and isAvailable:
#         do x
    

#PYTHON IS PASS BY REFERENCE!!!

def click(armor_level, armor_level_counts, click_type, stack, cost):
    #Preform 1 Click
    #INPUTS:
    #click_type array of [base chance, increase per stack (pre-softcap), softcap stack, increase per stack (after softcap)] 
    base_chance = click_type[0]
    increase_per_stack_pre_softcap = click_type[1]
    softcap = click_type[2]
    increase_per_stack_post_softcap = click_type[3]

    if stack <= softcap:
        chance = base_chance + stack * increase_per_stack_pre_softcap
    elif stack > softcap:
        chance = base_chance + softcap * increase_per_stack_pre_softcap + (stack - softcap) * increase_per_stack_post_softcap
    else:
        print("If you're reading this the program's wrong")

    if random.random() < chance:
        #Enhancement success
        print("Enhancement success!!")
        stack = starting_fs
        cost += cost_per_click_success

        armor_level_counts[armor_level] -= 1
        armor_level_counts[armor_level + 1] += 1
    else:
        #Enhancement failure
        print("Enhancement failure!!")
        stack += fs_per_click[armor_level]
        cost += cost_per_click_fail

        if armor_level != 0:
            armor_level_counts[armor_level] -= 1
            armor_level_counts[armor_level - 1] += 1
        #else: armor level is 0, so we do not need to update armor counts on failure
    return stack, cost, armor_level_counts

# def build_base_stack():
#     armor_stone_price = 0
#     reblath_price = 0

#How to seperate random chance from a good enchancing method? Save random seed between trials?
#How to seperate method of tapping from sustainable tapping i.e no influx of new pris

#ATTEMPT 1: Generate a "Sustainable tapping method" tap x, if x is not available tap next best thing, repeat

# Provide some failstacking "method"

#Sustainable tapping follows failstacking method unless it is no longer possible to do so, taps next best thing
#Add in stack slots that can be "rotated in and out for free" (new enhance slots) - this allows for more chances at optimal stacking

#Stacking method could be defined like [pri to duo range, duo to tri range, tri to tet range, tet to pen range]

sustainably_build_fs(250, 100)
#click(duo_to_tri, 120)

#Compute at what stack each boss gear piece would become profitable, tap that when out of stacks to build instead of
#doing a non optimal grunil stack

#At what chance is pri boss gear money, duo, tri, tet etc.
#Make function do 100 trials of enhancing X stack to see avg cost
#Implement functionality for stack saving/swapping on the fly

#Best way to increase stacks from like 90 to 110
