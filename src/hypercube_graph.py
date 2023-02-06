"""
Rodney McCoy
rbmj2001@outlook.com
Created Thu Dec 29 16:08:51 2022
"""


import hypercube_class as sigma
import condition_testing as is_equal
import metrics

import matplotlib.pyplot as plt




# Takes a list of n_cube permutations and plots their 3 statistics 
def plot_d_i_ex(data1 : list, data2 : list):
    CountPoints = True
    
    ax = plt.axes(projection='3d')
    ax.set_xlabel("D_n")
    ax.set_ylabel("I_n/2")
    ax.set_zlabel("EX_n/2")
    
    x,y,z,ct = get_pts(data1)
    ax.scatter3D(x,y,z, color='Green')
    
    if CountPoints:        
        for i, txt in enumerate(ct):
            ax.text(x[i], y[i], z[i], txt)
    
    
    x,y,z,ct = get_pts(data2)
    ax.scatter3D(x,y,z, color='Red')

    if CountPoints:        
        for i, txt in enumerate(ct):
            ax.text(x[i], y[i], z[i], txt)

    return




# Takes a list of n_cube permutations and returns the 3 statistics as 3 lists
def get_pts(data : list):
    x_vals, y_vals, z_vals, vals_ct = [], [], [], []
    for c in data:
        d = c[1]
        i = c[2]
        ex = c[3]
        
        AddVal = True
        
        for j in range(len(x_vals)):
            if x_vals[j] == d and y_vals[j] == i and z_vals[j] == ex:
                vals_ct[j] += 1
                AddVal = False
                break
        
        if AddVal:
            x_vals.append(d)
            y_vals.append(i)
            z_vals.append(ex)
            vals_ct.append(1)
            
    return x_vals, y_vals, z_vals, vals_ct
    
    






# Graphs a single permutation, and its a_bar permutation
def plot(h : sigma.n_cube):
    figure, axs = plt.subplots(nrows = 1, ncols=2, figsize=(10, 10))

    
    x_h = [i for i in range(-len(h), len(h)+1)]
    x_h.remove(0)
    y_h = [h[i] for i in x_h]
    
    axs[0].scatter(x_h, y_h) 
    axs[0].set_title(str(h.window()) + "  " + str(metrics.K_n(h)) + " " + str(is_equal.test(h)) + " " +  str(metrics.D_n(h)))

    
    a = is_equal.a_bar(h)
    x_a = [i for i in range(-len(a), len(a)+1)]
    x_a.remove(0)
    y_a = [a[i] for i in x_a]
    

    axs[1].scatter(x_a, y_a, color="blue")
    
    x = h.max_ind()
    if x != len(h):
        axs[1].scatter(x, h[len(h)], color="green")
        axs[1].scatter(-x, -h[len(h)], color="red")

    axs[1].set_title(str(a.window()) + "  " + str(metrics.K_n(a)) + " " +  str(metrics.D_n(a)))

    axs[0].grid()
    axs[1].grid()

    for a in axs:
        a.set_aspect('equal', adjustable='box')
