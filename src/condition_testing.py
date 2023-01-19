"""
Rodney McCoy
rbmj2001@outlook.com
Created Thu Dec 29 21:04:36 2022
"""

import hypercube_class as sigma

import metrics
import copy




def a_bar(h : sigma.n_cube) -> sigma.n_cube:
    i = copy.copy(h)
    
    x = h.max_ind()

    i[x] = i[len(h)]
    del i[len(h)]
    return i




def a_bar_inv(h : sigma.n_cube) -> list:
    result = []
    H = h.window()
    
    for i in range(len(h)):
        H1 = copy.copy(H)
        H1.append(H[i])
        H1[i] = len(H)+1
        result.append(sigma.n_cube(H1))
        
        H1[i] = -H1[i]
        H1[len(h)] = - H1[len(h)]
        result.append(sigma.n_cube(H1))
        
    H.append(len(H)+1)
    result.append(sigma.n_cube(H))
    H[len(H)-1] = -H[len(H)-1]
    result.append(sigma.n_cube(H))
    return result   


def mu_lambda(h : sigma.n_cube):
    H = a_bar(h)
    i = h.max_ind()
    
    cond1 = True
    cond2 = True
    
    # if abs(i) == len(h):
        
    
    if i > 0:
        for ind in range(1, i):
            if H[ind] > H[i]:
                cond1 = False
                break
            
        for ind1 in range(i+1, len(H)+1):
            if H[ind1] < H[i]:
                cond2 = False
                break
    else:
        for ind in range(i, 0):
            if H[ind] > H[i]:
                cond1 = False
                break
            
        for ind1 in range(-len(H), i):
            if H[ind1] < H[i]:
                cond2 = False
                break
    
    return (cond1 or cond2)



def test(h : sigma.n_cube) -> bool:
    H = a_bar(h)
    i = h.max_ind()
    
    if len(h) <= 2:
        return True
    
    if metrics.K_n(H) != 0:
        return False
    
    if abs(i) == len(h):
        return metrics.K_n(H) == 0   
    
    if abs(i) != len(h):
        return mu_lambda(h)

    
    return -1
    