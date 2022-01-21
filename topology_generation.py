# this program aims to calculate all the possible permutations of a
# linkage mechanism with one degree of freedom composed of N rigid bodies.
import itertools

f = open("cadeiasImpostas.txt", "w")

for n_bars in range(6,26 + 1, 2):
    N = n_bars; # number of rigid bodies. must be even and greater than 6 (max 26)
    f.write('____________________________________________N = ')
    f.write(str(N))
    f.write(' bars____________________________________________')
    f.write('\n')
    k_max = round(N/2); # the maximum number of edges that a bar can have to be a viable linkage system with one degree of freedom

    max_bars= [0*a for a in range(1,k_max)] # this list is used to store the maximum amount of bars of the same type that could still form a viable linkage mechanism with one degree of freedom
    for bar in range(4,k_max + 1): # starting with n4 until the nk_max
        count = 0
        # this while loop verifies , given that there is only one type of a bar, whats the maximum amount of the same bar can exist before making n3 be negative
        while ((N - 4) - (bar - 2)*count) >= 0: 
            count += 1
        max_bars[bar - 2] = count - 1 # the nbar ocuppies the [bar - 2] index in the array, since it is: [n2, n3, n4, ..., nkmax]
    f.write("   ")
    f.write('[')
    f.write(','.join(['n' + str(value) for value in range(2,k_max + 1)])) # prints out on the console the order in which the amount of each bar will appear in the lists
    f.write(']')
    possible_permut = []
    # opens the amount of bars to all possibilities, ranging from 0 to the maximum that was previously calculated
    for index in range(4, k_max + 1):
        all_permut = [n for n in range(0,max_bars[index - 2] + 1)]
        possible_permut.append(all_permut)
    # the line bellow makes use of a function from itertools to permutate all possible scenarious that arrise from combining their individual possibilities
    permuts = list(itertools.product(*possible_permut)) 

    linkage_mech = []
    count = 0
    for permut in permuts:
        possible_mech = [4, (N - 4)] # ititial values for n2 and n3, independent of the amout of other kinds of bars
        for j in range(0,len(permut)):
            possible_mech.append(permut[j])
        
        for bar in range(4,k_max + 1):
            possible_mech[0] += (bar - 3)*possible_mech[bar - 2] # calculates the number of n2 bars based on the number of n4, n5, n6, ...
            possible_mech[1] += -(bar - 2)*possible_mech[bar - 2] # calculates the number of n3 bars based on the number of n4, n5, n6, ...
        
        if sum(possible_mech) == N and (possible_mech[1] >= 0): # verifies if the permutation is valid for the desired conditions
            linkage_mech.append(possible_mech)
            count += 1
            possible_mech = [str(possible_mech[a]) for a in range(0,len(possible_mech))]
            f.write('\n')
            f.write(str(count))
            f.write('->')
            f.write('[')
            f.write(', '.join(possible_mech))
            f.write(']')

    f.write('\n')
    text = 'There are a total of ', str(len(linkage_mech)), ' possible configurations for a linkage mechanism with one degree of freedom composed of ', str(N), ' rigid bodies.'
    f.write(str("".join(text)))
    f.write('\n')
    f.write('___________________________________________________________________________________________________')
    f.write('\n')
    f.write('\n')
   

print("DONE!")