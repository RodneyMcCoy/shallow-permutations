"""
Rodney McCoy
Thu Oct 13 13:08:41 2022\
rbmj2001@outlook.com    

NOTE: Everything in this folder gives the permutation as a list in window notation.
As opposed to other files which deal with it directly as an instance of the n_cube class
"""

import itertools
import math





# Iterator class for searching through hypercube permutations of given dimension
# Ex: hypercube_search(2) gives,
# [1, 2] [1, -2], [-1, 2], [-1, -2] [2, 1] [2, -1] [-2, 1] [-2, -1]
class n_cube_search():
    
    def __init__(self, dimension : int):
        self.dim = abs(int(dimension))
        
    def __iter__(self):
        self.permutation = iter(itertools.permutations([i for i in range(1, self.dim+1)]))
        self.signs = 2**self.dim
        return self
        
    def __next__(self):
        if self.signs == 2**self.dim:
            self.signs = 0
            try:
                self.pi = list(next(self.permutation))
            except StopIteration:
                raise StopIteration
        bitmap = 1
        pi_temp = [i for i in self.pi]
        for i in range(self.dim):
            if (self.signs & bitmap) != 0:
                pi_temp[i] = -self.pi[i]
            bitmap = bitmap << 1
        self.signs += 1
        return pi_temp






# TODO Impliment this function

# Returns size amount of randomly sampled list of hypercube permutations.
# If non default dim (dimension) given, they will all be of dimension dim
def random_sample(size : int, dim : int = -1) -> list:
    if dim == -1:
        # Choose Random Dimension For Each
        return
    else:
        # Choose dim dimension for each
        return
    
    
    
    
# Counts total amount of hypercubes from dimension lower to dimension upper
def count_hypercubes(lower : int, upper : int) -> int:
    total = 0
    for i in range(lower, upper+1):
        total += 2**i * math.factorial(i)
    return total