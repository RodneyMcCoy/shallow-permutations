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
    # Calculate Statistics
    pi = sigma.n_cube(data=p)
    rho = is_equal.a_bar(pi)

    d_pi = metrics.signed_decomposition(pi)
    d_rho = metrics.signed_decomposition(rho)

    k = metrics.K_n(pi)
    # i = metrics.I_n(pi)
    # d = metrics.D_n(pi)
    # ex = metrics.EX_n(pi)

    diff = metrics.b_oddness(rho) - metrics.b_oddness(pi)
    #k_rho = metrics.K_n(rho)

    

    # Test Condition, output to file
    test = is_equal.test(pi)
    success = (test == (k==0))
    
        
    if not success:
        s = "{} {} {} {} {}".format(diff, pi, d_pi, rho, d_rho)

        file.write(s + "\n")
        # graph.plot(pi)
        # if diff != 2:
            # print(s)

    return int(success)
    
    




if(__name__ == "__main__"):
    # Write output to text file
    with open("results.txt", 'w+', encoding='utf-8') as file:
        low = up = 5 # no CE up to 9
        
        for n in range(low, up+1):
            # Apply calculate to each n dimension hypercube
            accuracy = statistics.mean(map(calculate, search.n_cube_search(n)))
            
            # Print the accuracy of the test condition
            print(n, "- dim accuracy: ", accuracy)
    del file, low, up, n, accuracy
    

    
    
    
