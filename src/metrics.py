"""
Rodney McCoy
rbmj2001@outlook.com
Created Sun Dec 25 11:44:07 2022
"""

import hypercube_class as sigma





 
# In: A Signed Permutation in 1 line notation
# Out: Length of the permutation. Total Amount of hypercube inversions over 
#       the Permutation
def I_n(x : sigma.n_cube) -> float:
    pi = x.normal()
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
def EX_n(pi : sigma.n_cube) -> float:
    c_pi = pi.cycle()
    
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
                    
    return int(len(pi)) - val



# In: A Signed Permutation in 1 line notation
# Out: Depth of permutation, as shown in "depth in classic coxeter groups"
def D_n(x : sigma.n_cube) -> float:
    pi = x.normal()
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






def K_n(h : sigma.n_cube) -> float:
    return D_n(h) - (I_n(h) + EX_n(h))/2