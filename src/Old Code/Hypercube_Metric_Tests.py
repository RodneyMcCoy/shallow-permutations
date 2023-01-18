"""
Rodney McCoy
Thu Oct 13 13:08:41 2022\
rbmj2001@outlook.com    
"""



import itertools           # For Basic Permutation Operations
import copy



#%% ----- Basic Permutation Methods, Conversion and Format Checking ----- 



# In: Signed Permutation in 1 line notation
# Out: Permutation in cycle notation (as disjoint cycles, not necessarily
#       transpositions) also 1 cycles are left in
def to_cycle(pi : list) -> list:
    cycles = []
    # For each possible value of permutation
    for i in pi.keys():
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
        if(pi[i] == i):
            cycles.append([i])
        else:
            j = i
            c = []
            while(True):
                if j in c:
                    break
                c.append(j)
                j = pi[j]        
            cycles.append(c)
    return cycles



# In: A Signed Permutation in 1 Line Notation
# Out: The Permutation Decomposed into 2 Cycles
def to_2_cycle(pi : list) -> list:
    # Change 1 line to disjoint cycles
    cycles = to_cycle(pi)
    
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
                # (possible bug) should i go to 1+1 rather than 1 since it zero indexes
                two_cycles.append([c[0], c[i-1]])
    return two_cycles



# Out: True if input is in 1 line format, false else
def check_1_line(pi : dict):
    if (not isinstance(pi, dict) or max(pi.keys()) != max(pi.values()) or 
        min(pi.keys()) != min(pi.values()) or max(pi.keys()) != -min(pi.keys())):
        raise Exception("Inputed permutation is not in 1 line")
    if 0 in pi.keys() or 0 in pi.values():
        raise Exception("Inputed permutation is not in 1 line")



# Out: True if input in disjoint cycles format, false else
def check_cycles(pi : list) -> bool:
    if not isinstance(pi, list):
        raise Exception("Inputed permutation is not in cycle")
    for j in pi:
        if not isinstance(j, list):
            raise Exception("Inputed permutation is not in cycle")



# Out: True if input in 2 cycles format, false else
def check_2_cycles(pi : list) -> bool:
    if not isinstance(pi, list):
        raise Exception("Inputed permutation is not in 2 cycle")
    for j in pi:
        if not isinstance(j, list) or len(j) != 2:
            raise Exception("Inputed permutation is not in 2 cycle")



# In: A Signed Permutation Decomposed into 1 line notation, and 2 * dim. of the
#       hypercube
# Out: True if Permutation is Isomorphic to a Hypercube, False else
def is_hyper_cube(pi : list) -> bool:    
    # Ensure its actually a signed permutation 
    check_1_line(pi)
    
    # Ensure permutation maps opposite faces to opposite faces
    for i in range (1, max(pi.values()) + 1):
        if pi[i] != - pi[-i]:
            return False
    return True









#%% ----- Metrics and "Recursive Characterization" Test Conditions -----



# In: A Signed Permutation in 1 line notation, a 1 indexed integer i
# Out: The permutation a|_i, created by me
def a_bar(a : dict, dim : int, i : int) -> list:
    # do work
    # if dim 
    
    return []
    raise Exception("Unable to calculate a_bar / a|_i with permutation", a)



# In: A Signed Permutation in 1 line notation, and integer representing S_n,
#       the permutation group we are in
# Out: True if permutation satisfies recursive characterization for hypercubes, else false
def is_equal(pi : dict, dim : int) -> bool:
    if dim <= 2:
        return True
    return False


 
# In: A Signed Permutation in 1 line notation
# Out: Length of the permutation. Total Amount of hypercube inversions over 
#       the Permutation
def I_n(pi : dict) -> int:
    count = 0
    
    for i in pi.keys():
        for j in range(i+1, max(pi.keys()) + 1):
            if j == 0:
                continue
            if pi[i] > pi[j]:
                count += 1   

    
    count = count/2
    
    for i in range(1, max(pi)+1):
        if(pi[i] < pi[-i]):
            count += 1/2  
    
    return int(count)
    



# In: A Signed Permutation in 1 line notation
# Out: The reflection length of the permutation. Or, n - all cycles of the 
#       form (i j k ) (-i -j -k). NOTE: not necessarily length three, (i j)
#       (-i -j) also counts
def EX_n(pi : dict) -> int:
    c_pi = to_cycle(pi)
    
    val = 0
    for i in range(len(c_pi)):
        for j in range(i+1, len(c_pi)):
            if len(c_pi[i]) != len(c_pi[j]):
                continue
            is_valid = True
            for k in c_pi[i]:
                if not -k in c_pi[j]:
                    is_valid = 0
                    break
            if is_valid:
                val += 1
                    
    return int(len(pi)/2) - val



# In: A Signed Permutation in 1 line notation
# Out: Depth of permutation, as shown in "depth in classic coxeter groups"
def D_n(pi : dict) -> int:
    val = 0
    n = max(pi.keys())
    
    
    # calculate everything except b oddness
    for i in range(1, n +1):
        if pi[i] > i:
            val += pi[i] - i
        if pi[i] < 0:
            val += abs(pi[i]) - 1/2
        
    # calculate b oddness
    decomposition = []
    temp_1 = [0]
    while max(temp_1) < n:
        i = max(temp_1)+1
        temp_1 = []
        
        '''
        while not i in temp_1:
            temp_1.append(i)
            i = abs(pi[i])
        '''
        
        not_finished = False
        while not_finished == False:
            while not i in temp_1:
                temp_1.append(i)
                i = abs(pi[i])
            temp_1.sort()
            not_finished = True
            for j in range(len(temp_1)-1):
                if temp_1[j+1] - temp_1[j] != 1:
                    not_finished = False
                    i = temp_1[j] + 1
                    break
                
                
        
        decomposition.append( [i for i in range(min(temp_1), max(temp_1)+1)] )
    
    
    # count sections with odd negative entries
    for d in decomposition:
        count = 0
        for i in d:
            if pi[i] < 0:
                count += 1
        if count % 2 == 1:
            val += 1/2
        
    return val



# In: A Signed Permutation in 1 line notation
# Out: D_n - I_n - EX_n using hypercube metrics
def K_n(h : dict) -> int:
    return D_n(h) - (I_n(h) + EX_n(h))/2









#%% ----- Main Function -----


results1 = []


def main():
    max_dimension = 5
    
    for n in range(1, max_dimension+1):
        r = []
        id_n = [i for i in range(-n, n+1)]
        id_n.remove(0)
        pi = {i : 0 for i in id_n}
        print(n)
        for pi_tuple in itertools.permutations(id_n):
            for unsigned_id, signed_id  in enumerate(id_n):
                pi[signed_id] = pi_tuple[unsigned_id]
            if not is_hyper_cube(pi):
                continue
            if K_n(pi) != 0 or K_n(pi) == 0:
                r.append( ( [pi[i] for i in range (1, n+1)], 
                            D_n(pi), I_n(pi)/2, EX_n(pi)/2, K_n(pi), 
                            is_equal(pi, int(len(pi)/2)))
                          )
                # copy.copy(pi),
        results1.append(n)
        results1.append(r)
        
    #pi ={-3:3, -2:2, -1:1, 1:-1, 2:-2, 3:-3}
    #print((pi, D_n(pi), I_n(pi), EX_n(pi), K_n(pi) ))


if(__name__ == "__main__"):
    main()  