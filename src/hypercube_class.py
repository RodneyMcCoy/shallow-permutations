"""
Rodney McCoy
Thu Oct 13 13:08:41 2022\
rbmj2001@outlook.com    
"""


import copy



# Impliments a data structure to store a signed permutation which represents a
# hyper cube.
class n_cube():
    
    
    # Data should be in window notation. i.e. [+-1, +-2, ... , +- dim]
    def __init__(self, data=[]):
        self.data = copy.copy(data)
        if not self.formatted_properly():
            raise Exception("n_cube permutation class was given bad input data", data)

    
    
    # To get the dimension of the hypercube stored in this class
    def __len__(self):
        return len(self.data)
    
    # Simple copy method
    def __copy__(self):
        return n_cube(self.window())
    
    
    def __eq__(self, other):
        return self.data == other.data
    
    
    def __neq__(self, other):
        return self.data != other.data
    
    
    # 1 Index array indexing operator
    def __getitem__(self, x):
        if x < 0:
            return -self.data[abs(x+1)]
        elif x > 0:
            return self.data[x-1]
        else:
            raise Exception("A zero was given to a subscript of a n_cube class. This shouldnt happen.")
    
    
    # 1 Index array indexing operator
    def __setitem__(self, x, new_val):
        if x < 0:
            self.data[abs(x+1)] = -new_val
        elif x > 0:
            self.data[x-1] = new_val
        else:
            raise Exception("A zero was given to a subscript of a n_cube class. This shouldnt happen.")
            
            
    # 1 Index array element deletion operator
    def __delitem__(self, x):
        if x < 0:
            del self.data[abs(x+1)]
        elif x > 0:
            del self.data[x-1]
        else:
            raise Exception("A zero was given to a delete subscript of a n_cube class. This shouldnt happen.")
        if self.data == []:
            raise Exception("Permutation class has had all elements removed")
            
            
    # Return string for nice printing
    def __str__(self):
        spacing = len(str(len(self)))
        str_format = '{x: >' + str(spacing+1) + '}'
        string = "" 
        
        for i in range(len(self)):
            # string += str(self.data[i])
            string += str_format.format(x=str(self.data[i])) 
            
            if i != len(self)-1:
                string += ", "
            
        return "[" + string + "]"
    
    def __repr__(self):
        return str(self)
    
    
    



    
    def fancy_str(self):
        string = ""
        for i in range(len(self)):
            
            if self.data[i] > 0:
                string += str(self.data[i])
            else:
                # FANCY TEXT OUTPUT OCCURS HERE
                string += "\033[4m\033[1;34m"
                string += str(abs(self.data[i]))
                string += "\033[0m"
                        
            if i != len(self)-1:
                string += ", "
        
        return "[" + string + "]"
    
    

    def formatted_properly(self):
        if self.data == []:
            return False
        if not isinstance(self.data, list):
            return False
        for i in self.data:
            if not isinstance(i, int) or i < -len(self) or i > len(self) or i == 0:
                return False
        for i in range(1, len(self)+1):
            if i not in self.data and -i not in self.data:
                return False
        return True
        
    
    # 1 indexed max index
    
    def max_ind(self):
        x = 0
        n = len(self)
        for x in range(1, n+1):
            if self.data[x-1] == n:
                return x
            if self.data[x-1] == -n:
                return -x
        raise Exception("Expected max element not found in n_cube permutation", self.data)
    
    
    
    
    
    
    # ACCESSORS TO DATA. CONVERTS IT TO VARIOUS PERMUTATION REPRESENTATION TYPES    
    
    # Returns data in window / 1 line notation, as a list
    def window(self) -> list:
        return [i for i in self.data]
    
    
    
    # Returns data as a normal 1 line permutation, as a dictionary
    def normal(self) -> list:
        result = {}
        for i in range(len(self)):
            result[-(i+1)] = -self.data [i]
            result[i+1] = self.data[i]
        return  dict(sorted(result.items()))



    # In: Signed Permutation in 1 line notation
    # Out: Permutation in cycle notation (as disjoint cycles, not necessarily
    #       transpositions) also 1 cycles are left in
    def cycle(self) -> list:
        pi = self.normal()
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
    def two_cycle(self) -> list:
        # Change 1 line to disjoint cycles
        cycles = self.cycle()
        
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
    
    


