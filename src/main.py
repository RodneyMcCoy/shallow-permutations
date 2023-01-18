"""
Rodney McCoy
Thu Oct 13 13:08:41 2022\
rbmj2001@outlook.com    
"""

import hypercube_search as search
import hypercube_class as sigma
import hypercube_graph as graph
import condition_testing as is_equal
import metrics

   




def calculate(lower : int, upper : int = -1) -> dict:
    # Note: Searching gets slow above max_dimension = 5
    accuracy = 0
    
    if upper == -1:
        upper = lower
        
    print("Search Started")
    
    Equal, NotEqual = [], []
        
    # Search through hypercube dimensions 1 to max_dimension
    for n in range(lower, upper+1):
                
        # Search through all possible hypercubes
        for p in search.n_cube_search(n):
            
            # Calculate and Save Various Statistics
            pi = sigma.n_cube(data=p)
            d = metrics.D_n(pi)
            i = metrics.I_n(pi)/2
            ex = metrics.EX_n(pi)/2
            k = d-i-ex      

            temp = [pi, is_equal.a_bar(pi), k]

            if k == 0:
                Equal.append(temp)      
            else:
                NotEqual.append(temp)      

            # Test Conditions
            is_true = is_equal.true(pi)
            is_false = is_equal.false(pi)
            
            # Count Successful condition usage
            if is_true == True and k == 0:
                accuracy += 1
            if is_false == False and k != 0:
                accuracy += 1
            
            # Notify if conditions fail
            if is_true == True and k != 0:
                print("Counter example found true()", pi)
            if is_false == False and k == 0:
                print("Counter example found to false()", pi)
            
                
        print(n, "- dim search finished")
    
    print("Accuracy of Conditions: ", accuracy / search.count_hypercubes(lower, upper))
    
    return Equal, NotEqual     






def output(data : list, equality : bool):
    if equality == True:
        name = "Equal"
    else:
        name = "Not Equal"
    
    with open(name + str(".txt"), 'w+', encoding='utf-8') as file:
        file.read()
        file.write(name + "\n")
        for i in data:
            s = str(i[0]) + "  " + str(i[2])  + "\n"
            
            write = True
            for ind, j in enumerate(is_equal.a_bar_inv(i[0])):
                k = metrics.K_n(j)
                
                s += str(j) + " " + str(k)
                
                if ind % 2 == 0:
                    s += "  "
                else:
                    s += "\n"
                
                if k != 0:
                    write = False
            
            write = True
            if write or equality == False:
                file.write(s + "\n")
    print("Wrote some data to: " + name + str(".txt"))






def a_bar_test(c : sigma.n_cube):
    for i in is_equal.a_bar_inv(c):
        print(i, metrics.K_n(i))
        a = is_equal.a_bar(i)
        if a != c:
            raise Exception("Inverse doesnt work", a, c)






if(__name__ == "__main__"):
    equal, not_equal = calculate(4)  
    

    
    # Output Results
    Equal = [(str(i[0]), i[2], str(i[1]), metrics.K_n(i[1])) for i in equal]
    NotEqual = [(str(i[0]), i[2], str(i[1]), metrics.K_n(i[1])) for i in not_equal]
    
    
    output(equal, True)
    output(not_equal, False)
    

    del equal, not_equal