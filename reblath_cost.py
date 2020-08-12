#Computes average cost of stacking to X stack on +14 reblath

import random

# base_stack = 1
# desired_stack = 17
# trials = 100000

def stack_14(base_stack, desired_stack, trials):
    base_chance = 0.02 # 2%
    increase_per_stack = 0.002 #0.2%
    blackstones = 0
    reblath_repair = 0
    stack = 0

    for i in range(trials):
        stack = base_stack
        while stack < desired_stack:
            blackstones += 1
            if random.random() < (base_chance + stack * increase_per_stack):
                #This condition is when we make +15 reblath
                stack = base_stack
            else:
                stack += 1
                reblath_repair += 1
    avg_stack_cost = (blackstones/trials)*208000 + (reblath_repair/trials)*13000
    avg_stack_cost = avg_stack_cost/1000000
    return avg_stack_cost

# A 17 stack w/ +1 base enhance chance is 5.15 mil cost

#print(stack_14(base_stack=1, desired_stack=17, trials=100000)) #5.15 mil
stack_17_cost = 5.15

def stack_pri(base_stack, base_stack_cost, desired_stack, trials):
    base_chance = .0769
    increase_per_stack = 0.00770
    blackstones = 0
    reblath_repair = 0
    base_count = 0
    duos = 0
    for i in range(trials):
        stack = base_stack
        base_count += 1
        while stack < desired_stack:
            blackstones += 1
            if random.random() < (base_chance + stack * increase_per_stack):
                #This condition is when we make duo reblath
                stack = base_stack
                base_count += 1
                duos += 1
            else:
                stack += 3
                reblath_repair += 1
    
    cost = ((blackstones/trials)*2250000 + (reblath_repair/trials) * 13000)/1000000 + base_count/trials * base_stack_cost
    avg_cost = cost
    avg_duos = duos/trials

    return avg_cost, avg_duos

#print(stack_pri(base_stack=17, base_stack_cost=stack_17_cost, desired_stack=29, trials=100000))
stack_26_cost = 18.15
stack_26_duos = 1.2

def stack_duo(base_stack, base_stack_cost, base_duo_supply, desired_stack, trials):
    base_chance = 0.0625
    increase_per_stack = 0.00625
    blackstones = 0
    reblath_repair = 0
    base_stack_count = 0
    duos = base_duo_supply
    tris = 0

    for i in range(trials):
        stack = base_stack
        base_stack_count += 1
        while stack < desired_stack:
            blackstones += 1 #always use a blackstone
            duos -= 1 #always use a duo up (either downgrades to pri or upgrades to tri)
            if random.random() < (base_chance + stack * increase_per_stack):
                #This condition is when we succeed enhancement (tri reblath)
                stack = base_stack
                base_stack_count += 1
                duos += base_duo_supply #Every time we need a new "base" stack, we get the duos that makes too 
                tris += 1
            else:
                stack += 4
                reblath_repair += 1
    
    avg_cost = ((blackstones/trials)*2250000 + (reblath_repair/trials) * 13000)/1000000 + (base_stack_count/trials) * base_stack_cost
    avg_tris = tris/trials
    avg_duo_usage = duos/trials

    return avg_cost, avg_tris, avg_duo_usage

#print(stack_duo(base_stack=26, base_stack_cost=stack_26_cost, base_duo_supply=stack_26_duos, desired_stack=50, trials=1000000))
stack_50_cost = 179.1
stack_50_tris = 6.72
stack_50_duos = -17.2 #Making a 50 stack via this method results in a duo deficit

def stack_tri(base_stack, base_stack_cost, base_duo_supply, base_tri_supply, desired_stack, trials):
    base_chance = 0.02
    increase_per_stack = 0.002
    blackstones = 0
    reblath_repair = 0
    base_stack_count = 0
    tris = base_tri_supply
    duos = base_duo_supply
    tets = 0

    for i in range(trials):
        stack = base_stack
        base_stack_count += 1
        while stack < desired_stack:
            blackstones += 1 #always use a blackstone
            tris -= 1 #always use a tri up (either downgrades to duo or upgrades to tet)
            if random.random() < (base_chance + stack * increase_per_stack):
                #This condition is when we succeed enhancement (tet reblath)
                stack = base_stack
                base_stack_count += 1
                duos += base_duo_supply #Every time we need a new "base" stack, we get the duos that makes too
                tris += base_tri_supply #Every time we need a new "base" stack, we get the tris that makes too 
                tets += 1
            else:
                duos += 1
                stack += 5
                reblath_repair += 1
    
    avg_cost = ((blackstones/trials)*2250000 + (reblath_repair/trials) * 13000)/1000000 + base_stack_count/trials * base_stack_cost
    avg_tets = tets/trials
    avg_tri_usage = tris/trials
    avg_duo_usage = duos/trials

    return avg_cost, avg_tets, avg_tri_usage, avg_duo_usage

def stack_tet(base_stack, base_stack_cost, base_tri_supply, base_tet_supply, desired_stack, trials):
    base_chance = 0.003
    increase_per_stack = 0.0003
    blackstones = 0
    reblath_repair = 0
    base_stack_count = 0
    tris = base_tri_supply
    tets = base_tet_supply
    pens = 0

    for i in range(trials):
        stack = base_stack
        base_stack_count += 1
        while stack < desired_stack:
            blackstones += 1 #always use a blackstone
            tets -= 1 #always use a tri up (either downgrades to duo or upgrades to tet)
            if random.random() < (base_chance + stack * increase_per_stack):
                #This condition is when we succeed enhancement (tet reblath)
                stack = base_stack
                base_stack_count += 1
                tris += base_tri_supply #Every time we need a new "base" stack, we get the duos that makes too
                tets += base_tet_supply #Every time we need a new "base" stack, we get the tris that makes too 
                pens += 1
            else:
                tris += 1
                stack += 6
                reblath_repair += 1
    
    avg_cost = ((blackstones/trials)*2250000 + (reblath_repair/trials) * 13000)/1000000 + base_stack_count/trials * base_stack_cost
    avg_pens = pens/trials
    avg_tet_usage = tets/trials
    avg_tri_usage = tris/trials
    avg_base_stacks_used = base_stack_count/trials

    return avg_cost, avg_pens, avg_tet_usage, avg_tri_usage, avg_base_stacks_used
    
#print(stack_tri(base_stack=50, base_stack_cost=stack_50_cost, base_duo_supply=stack_50_duos, base_tri_supply=stack_50_tris, desired_stack=80, trials=1000000))


def stack_pri_boss(base_stack, base_stack_cost, desired_stack, trials):
    base_chance = .0769
    increase_per_stack = 0.00770
    blackstones = 0
    mem_frags = 0
    base_count = 0
    duos = 0
    for i in range(trials):
        stack = base_stack
        base_count += 1
        while stack < desired_stack:
            blackstones += 1
            if random.random() < (base_chance + stack * increase_per_stack):
                #This condition is when we make duo reblath
                stack = base_stack
                base_count += 1
                duos += 1
            else:
                stack += 3
                mem_frags += 10
    
    cost = ((blackstones/trials)*2250000 + (mem_frags/trials) * 1450000)/1000000 + base_count/trials * base_stack_cost
    avg_cost = cost
    avg_duos = duos/trials
    cost_duo_boss = avg_cost/avg_duos

    return avg_cost, avg_duos, cost_duo_boss

#print(stack_pri_boss(base_stack=29, base_stack_cost=30, desired_stack=38, trials=100000))

def stack_duo_boss(base_stack, base_stack_cost, base_duo_supply, desired_stack, trials):
    base_chance = 0.0625
    increase_per_stack = 0.00625
    blackstones = 0
    mem_frags = 0
    base_stack_count = 0
    duos = base_duo_supply
    tris = 0

    for i in range(trials):
        stack = base_stack
        base_stack_count += 1
        while stack < desired_stack:
            blackstones += 1 #always use a blackstone
            duos -= 1 #always use a duo up (either downgrades to pri or upgrades to tri)
            if random.random() < (base_chance + stack * increase_per_stack):
                #This condition is when we succeed enhancement (tri reblath)
                stack = base_stack
                base_stack_count += 1
                duos += base_duo_supply #Every time we need a new "base" stack, we get the duos that makes too 
                tris += 1
            else:
                stack += 4
                mem_frags += 10
    
    avg_cost = ((blackstones/trials)*2250000 + (mem_frags/trials) * 1450000)/1000000 + base_stack_count/trials * base_stack_cost
    avg_tris = tris/trials
    avg_duo_usage = duos/trials
    #cost_tri_boss = avg_cost/avg_tris

    return avg_cost, avg_tris, avg_duo_usage #, cost_tri_boss

def stack_tri_boss(base_stack, base_stack_cost, base_duo_supply, base_tri_supply, desired_stack, trials):
    base_chance = 0.02
    increase_per_stack = 0.002
    blackstones = 0
    reblath_repair = 0
    base_stack_count = 0
    tris = base_tri_supply
    duos = base_duo_supply
    tets = 0

    for i in range(trials):
        stack = base_stack
        base_stack_count += 1
        while stack < desired_stack:
            blackstones += 1 #always use a blackstone
            tris -= 1 #always use a tri up (either downgrades to duo or upgrades to tet)
            if random.random() < (base_chance + stack * increase_per_stack):
                #This condition is when we succeed enhancement (tet reblath)
                stack = base_stack
                base_stack_count += 1
                duos += base_duo_supply #Every time we need a new "base" stack, we get the duos that makes too
                tris += base_tri_supply #Every time we need a new "base" stack, we get the tris that makes too 
                tets += 1
            else:
                duos += 1
                stack += 5
                reblath_repair += 10
    
    avg_cost = ((blackstones/trials)*2250000 + (reblath_repair/trials) * 1450000)/1000000 + base_stack_count/trials * base_stack_cost
    avg_tets = tets/trials
    avg_tri_usage = tris/trials
    avg_duo_usage = duos/trials

    return avg_cost, avg_tets, avg_tri_usage, avg_duo_usage
#This will make x amount of Duos on avg, and need to account for that in 

#12, 13, 14, 15, 16, 17

def main():
    #print(stack_14(base_stack=1, desired_stack=15, trials=100000)) #5.15 mil
    stack_15_cost = 4.22

    #print(stack_pri(base_stack=15, base_stack_cost=stack_15_cost, desired_stack=24, trials=1000000))
    stack_24_cost = 20.15
    stack_24_duos = 1.07

    #print(stack_duo(base_stack=24, base_stack_cost=stack_24_cost, base_duo_supply=stack_24_duos, desired_stack=28, trials=100000))
    stack_28_cost = 28.5
    stack_28_tris = 0.27
    stack_28_duos = -0.98

    #print(stack_pri_boss(base_stack=28, base_stack_cost=stack_28_cost, desired_stack=31, trials=100000))
    stack_31_cost = 57.95
    stack_31_duos = 0.413

    [stack_39_cost, stack_39_tris, stack_39_duos] = stack_duo(base_stack=31, base_stack_cost=stack_31_cost, base_duo_supply=stack_28_duos, desired_stack=39, trials=100000)
    #print(stack_39_cost, stack_39_tris, stack_39_duos)

    #print(stack_duo_boss(base_stack=38, base_stack_cost=stack_38_cost, base_duo_supply=stack_38_duos, desired_stack=50, trials=100000))
    [stack_48_cost, stack_48_tris, stack_48_duos] = stack_duo_boss(base_stack=39, base_stack_cost=stack_39_cost, base_duo_supply=stack_31_duos, desired_stack=48, trials=100000)
    #print(stack_48_cost, stack_48_tris, stack_48_duos)

    [stack_68_cost, stack_68_tets, stack_68_tris, stack_68_duos] = stack_tri_boss(base_stack=48, base_stack_cost=stack_48_cost, base_duo_supply=stack_28_duos, base_tri_supply=stack_28_tris, desired_stack=68, trials=100000)
    print(stack_68_cost, stack_68_tets, stack_68_tris, stack_68_duos)

    stack_78_cost = stack_68_cost + 30 #3 mil cost per valk

    [stack_93_cost, stack_93_tets, stack_93_tris, stack_93_duos] = stack_tri(base_stack=78, base_stack_cost=stack_78_cost, base_duo_supply=stack_48_duos, base_tri_supply=stack_48_tris, desired_stack=93, trials=100000)
    print(stack_93_cost, stack_93_tets, stack_93_tris, stack_93_duos)

    [stack_111_cost, stack_111_tets, stack_111_tris, stack_111_duos, stack_111_avg_base_stacks_used] = stack_tet(base_stack=93, base_stack_cost=stack_93_cost, base_tri_supply=stack_93_tris, base_tet_supply=stack_93_tets, desired_stack=111, trials=100000)
    print(stack_111_cost, stack_111_tets, stack_111_tris, stack_111_duos, stack_111_avg_base_stacks_used)

    print(stack_93_tets * stack_111_avg_base_stacks_used) #Price of TET boss gear (can subtract from total stack value)
    stack_111_cost -= (stack_93_tets * stack_111_avg_base_stacks_used) #+ avg_pens




main()