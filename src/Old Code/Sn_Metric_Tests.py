"""
Rodney McCoy
Thu Oct 13 13:08:41 2022\
rbmj2001@outlook.com
"""

import itertools           # For Basic Permutation Operations
import colorama as color   # For fancy colored text






# ----- Basic Permutation Methods ----- 


    
# In: Permutation in 1 line notation (a list of integers 1 through length of
#       permutation)
# Out: Permutation in cycle notation (as disjoint cycles, not necessarily
#       transpositions) also 1 cycles are left in
def to_cycle(a : list) -> list:
    cycles = []
    
    # For each possible value of permutation
    for i in range(1, len(a) + 1):
        skip = False
        
        # Skip if i has already been placed in cycle
        if len(cycles) != 0:
            for x in cycles:
                if i in x:
                    skip = True
        if(skip):
            continue
        
        # If i is not swapped, add it alone to cycles, 
        # Else produce the cycle that swaps i and add it to cycles
        if(a[i-1] == i):
            cycles.append([i])
        else:
            j = i
            c = []
            while(True):
                if j in c:
                    break
                c.append(j)
                j = a[j-1]        
            cycles.append(c)
    
    return cycles



# In: A Permutation in Cycle Notation
# Out: The Permutation Decomposed into 2 Cycles (Not necessarily minimal by 
#       amount of 2 cycles)
def to_2_cycle(a : list) -> list:
    # Change 1 line to disjoint cycles
    cycles = to_cycle(a)
    
    two_cycles = []
    
    # For each disjoint cycle
    for c in cycles:
        # If it is already a 2 cycle, add it
        # Else decompose into 2 cycles, and add each Its decomposed in the form
        # (a_1, ..., a_n) = (a_1 a_n) (a_1 a_{n-1}) ... (a_2 a_1)
        if (len(c) == 2):
            two_cycles.append(c)
        else:
            for i in range(len(c), 1, -1):
                two_cycles.append([c[0], c[i-1]])
    return two_cycles



# In: A Permutation Decomposed into Two Cycles, and the dim. of the hypercube
# Out: True if Permutation is Isomorphic to a Hypercube, False else
def is_hyper_cube(a : list, n : int) -> bool:    
    # Permutation representation of hypercube must be 2 * dimension of hypercube
    if (n % 2 == 1):
        return False
    dim = int(n/2)

    for i in range(0, dim):
        print(i, a[i], a[n-1-i])
        if a[i] + a[n-1-i] != n+1:
            return False
        
    return True


    # Copy array and shift [1, 2n] to [-n, -1] and [1, n]
    a_1 = [ [i[0]-dim if i[0] > dim else i[0] - (dim+1),
             i[1]-dim if i[1] > dim else i[1] - (dim+1) ] for i in a ]
    
    # Remove from a_1 transpositions of the form [-i, i]
    a_2 = [ i for i in a_1 if i[0] + i[1] != 0]
    if(len(a_2) == 0):
        return True
    
    # if we have an odd amount of 2 cycles left, there will be atleast one left
    # not in the form [i,j] [-i,-j]
    if len(a_2) % 2 == 1:
        return False
    
    # Remove from a_2 transpositions of the form [i, j] [-i, -j]
    while(True):
        if (len(a_2) == 0):
            return True
        
        l = len(a_2)-1
        i, j = a_2[l][0], a_2[l][1]
        
        # For the 1st to len - 1 cycle of the permutation
        for k in range (l-1, 1, -1):
            # If of the form [i, j][-i, -j], we are done
            if (a_2[k][0] == -i and a_2[k][1] == -j) or (a_2[k][0] == -j and a_2[k][1] == -i):
                del a_2[k]
                a_2.pop()
                break
        
            # If we cant make it in the form [i, j][-i, -j] by commuting it
            # since we run into a +-i or +-j, return false
            if abs(a_2[k][0]) == i or abs(a_2[k][0]) == j or abs(a_2[k][1]) == i or abs(a_2[k][1]) == j:                
                return False
            
        # If we can commute to the end without decomposing it, return false
        return False
        
    print("We definitely shouldnt be here")


# p[i] + p[n-1-i] = n+1 
# over all reasonable i


# In: A Permutation in 1 line notation, a 1 indexed integer i
# Out: The permutation a|_i, as defined in Section 4
def a_bar(a : list, i : int) -> list:
    n = len(a)
    a_1 = [i for i in a]
    if (n >= 2 and i==1):
        a_1[0] = a_1[n-1]
        a_1.pop()
        return a_1
    elif (n >= 2 and i == n):
        a_1.pop()
        a_1[n-3], a_1[n-2] = a_1[n-2], a_1[n-3]
        return a_1
    elif (n >= 3 and n >= i and i >= 1):
        a_1[i-1] = a[n-1]
        a_1.pop()
        return a_1
        
    raise Exception("Unable to calculate a_bar / a|_i with permutation", a)



# In: A Permutation in 1 line notation, and integer representing S_n,
#       the permutation group we are in
# Out: True if permutation satisfies recursive characterization, else false
def is_equal(a : list, n : int) -> bool:
    # Find i such tha a_i = n
    n = len(a)
    for i, a_i in enumerate(a):
        if a_i == n:
            break
    i += 1
    print(i)
    
    # if in S_1 return True
    if n == 1:
        return True
    
    # if i == n then check if permutation is in M_2, else check if permutation in M_1
    if i == n:
        return is_equal(a_bar(a, n), n-1)
    else:
        lambda_i = 0
        mu_i = 0
        
        # Calculate lambda_i
        for j in range(0, i):
            if(a[i] < a[j]):
                lambda_i += 1  
                
        # Calculate mu_i
        for j in range(i, n):
            if(a[j] < a[i]):
                mu_i += 1  
        
        if lambda_i != 0 and mu_i != 0:
            return False
        
        return is_equal(a_bar(a, i), n-1)






# ----- Metrics Referenced in "A re-examination of the Diaconis-Graham Ineuality" -----


 
# In: A Permutation in 1 line notation
# Out: Total Amount of inversions over the Permutation
def I_n(a : list) -> int:
    count = 0
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if(a[i] > a[j]):
                count += 1      
    return count



# In: A Permutation in 1 line notation
# Out: n - # of disjoint cycles in permutation (including 1 cycles)
def EX_n(a : list) -> int:
    a_1 = to_cycle(a)
    '''
    print(color.Fore.CYAN + "1 Line " + color.Fore.RESET + str(a)
         + color.Fore.CYAN + "\t\tCycle " + color.Fore.RESET + str(a_1)
         + color.Fore.CYAN + "\t2 Cycles " + color.Fore.RESET + str(to_2_cycle(a)))
    '''
    return len(a) - len(a_1)



# In: A Permutation in 1 line notation
# Out: sum over |a_i - i|
def D_n(a : list) -> int:
    the_sum = 0
    for i in range(1, len(a)+1):
        the_sum += abs(a[i-1] - i)
    return the_sum



# In: A Permutation in 1 line notation
# Out: D_n - I_n - EX_n
def K_n(h : list) -> int:
    return D_n(h) - I_n(h) - EX_n(h)






# ----- Main Function -----



results = []

def main():
    for n in range(4, 8+1, 2):
        r = []
        for pi in itertools.permutations([i for i in range(1, n + 1)]):
            if not is_hyper_cube(pi,n):
                continue
            r.append( (pi,K_n(pi),is_equal(pi, n) ) )
        results.append(n)
        results.append(r)


if(__name__ == "__main__"):
    main()  