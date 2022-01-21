import itertools
from file_handling import *

def generate_topologies(max_bars):
    """
    Calculate all the possible permutations of a linkage mechanism with one 
    degree of freedom from a given kinematic chain composed of N rigid bodies.
    """
    filename = "topologies.txt"
    write_in_file(filename, "Possible Topologies: \n")

    for n_bars in range(6, max_bars + 1, 2):
        N = n_bars; # number of rigid bodies in the kinematic chain.
        message = ('____________________________________________N = ' + str(N) + 
                    ' bars____________________________________________' + '\n')
        append_to_file(filename, message)

        # k_max is the maximum number of joints that a bar can have so that the
        # kinematic chain can sitll be a viable linkage system with one DoF.
        k_max = round(N/2);

        max_bars= [0*a for a in range(1,k_max)] # maximum amount of bars of the same type
        for bar in range(4, k_max + 1): # starting with n4 until the nk_max
            count = 0
            
            
            while ((N - 4) - (bar - 2)*count) >= 0: 
                # counts the theoretic maximum amount of rigid bodies of the same type.
                count += 1
            max_bars[bar - 2] = count - 1 # the n_th bar ocuppies the [bar - 2] index
                                        
        
        message = ("   " + '[' + 
                ','.join(['n' + str(value) for value in range(2,k_max + 1)]) + ']')
        append_to_file(filename, message)

        possible_permut = []
        for index in range(4, k_max + 1):
            all_permut = [n for n in range(0,max_bars[index - 2] + 1)]
            possible_permut.append(all_permut)
        # Permutate all possible topologies
        permuts = list(itertools.product(*possible_permut)) 

        linkage_mech = []
        count = 0
        for permut in permuts:
            possible_mech = [4, (N - 4)] # ititial values for n2 and n3.
            for j in range(0,len(permut)):
                possible_mech.append(permut[j])
            
            for bar in range(4,k_max + 1):
                # Number of n2 bars based on the number of n4, n5, n6, ...
                possible_mech[0] += (bar - 3)*possible_mech[bar - 2]
                # Number of n3 bars based on the number of n4, n5, n6, ...
                possible_mech[1] += -(bar - 2)*possible_mech[bar - 2]
            
            if sum(possible_mech) == N and (possible_mech[1] >= 0):
                # verifies if the permutation is valid for the desired conditions.
                linkage_mech.append(possible_mech)
                count += 1
                possible_mech = [str(possible_mech[a]) for a in range(0,len(possible_mech))]
                message = ('\n' + str(count) + '->' + 
                        '[' + ', '.join(possible_mech) + ']')
                append_to_file(filename, message)

        message = ('\n' + 'There are a total of ' + str(len(linkage_mech)) + 
        ' possible configurations for a linkage mechanism composed of ' + str(N) + 
        ' rigid bodies.' + '\n' + '_______________________________________'
        + '____________________________________________________________' + '\n\n')
        append_to_file(filename, message)

    print(f"A file named '{filename}' was created with the desired topologies.")