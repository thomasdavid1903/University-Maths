import numpy as np
import p_method  as p_1
import trial_division_factorisation as td
import PollardRho as pr
import matplotlib.pyplot as plt

def sc(n):
    a = pr.plotter_SC2(n)

    b = td.plotter_SC2(n)

    c = p_1.plotter_SC2(n)

    plt.scatter(list(range(3, n, 2)), a, label='TD', color='red')
    plt.scatter(list(range(3, n, 2)), b, label='P-1', color='blue')
    plt.scatter(list(range(3, n, 2)), c, label='Rho', color='orange')
    plt.show()


sc(100000)

