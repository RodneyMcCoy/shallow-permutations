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
import statistics





def calculate(p) -> dict:
    pi = sigma.n_cube(data=p)
    k = metrics.K_n(pi) 
    
    # Notify if conditions fail
    test = is_equal.test(pi)
    success = (test == (k==0))
    if not success:
        s = "Counter example found {} {} {}".format(pi, k, test)
        file.write(s + "\n")
        
        # graph.plot(pi)
    return int(success)
    
    




if(__name__ == "__main__"):
    # Write output to text file
    with open("results.txt", 'w+', encoding='utf-8') as file:
        low = 2
        upper = 7
        
        for n in range(low, upper+1):
            # Apply calculate to each n dimension hypercube
            accuracy = statistics.mean(map(calculate, search.n_cube_search(n)))
            
            # Print the accuracy of the test condition
            print(n, "- dim accuracy: ", accuracy)
    

    
    
    
