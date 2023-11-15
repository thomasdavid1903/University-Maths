import math
import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches
import os, psutil

def rho(n): ## pollards rho algorithm
    x = 2
    y = x
    d = 1

    while d==1:
        x = (x**2+1)%n ##  x = g(x)
        y = (((y**2+1)%n)**2+1)%n ##  x = g(g(y))
        if(x-y>0):
            diff = x-y ## used to find |x-y|
        else:
            diff = y-x ## used to find |x-y|
        d = math.gcd(diff,n) ## gcd(|x - y|, n)
    if d == n:
        return  None
    else:
        return d # returns the non-trivial factor of n

def plotter_TC(): ## shows the time complexity of pollards rho
    times = []
    colors = []
    primes = list(range(3, 10000000, 200))

    for i in primes:
        start = time.time_ns()
        prime = rho(i)
        print(f"{i} has a factor {prime}")
        times.append(time.time_ns() - start)
        if(prime == None):
            colors.append("pink")
        else:
            colors.append("purple")

    # access legend objects automatically created from data
    handles, labels = plt.gca().get_legend_handles_labels()

    # create manual symbols for legend
    patch1 = mpatches.Patch(color='pink', label="Primes")
    patch2 = mpatches.Patch(color='purple', label="Composite")

    # add manual symbols to auto legend
    handles.extend([patch1, patch2])

    plt.legend(handles=handles)

    print(times)
    print(len(times))
    plt.scatter(primes,times,color=colors,s=0.75)
    plt.title("Time taken for Pollards Rho on n")
    plt.xlabel("$n$")
    plt.ylabel("Time (ns seconds)")
    plt.xlim(primes[0], primes[-1])


def rho_sc(n): ## pollards rho algorithm
    x = 2
    y = x
    d = 1

    while d==1:
        x = (x**2+1)%n ##  x = g(x)
        y = (((y**2+1)%n)**2+1)%n ##  x = g(g(y))
        if(x-y>0):
            diff = x-y ## used to find |x-y|
        else:
            diff = y-x ## used to find |x-y|
        d = math.gcd(diff,n) ## gcd(|x - y|, n)
        return psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2) ##return memory usage for function


def plotter_SC(n):## shows the space complexity of pollard rho
    colors = ["pink"]
    space = []

    primes = list(range(3, n, 2))

    for i in primes:
        space.append(rho_sc(i))
        print(i)

    plt.scatter(primes,space,color=colors,s=0.5)
    plt.title("Memory Used for Pollards Rho on n in MB")
    plt.xlabel("$n$")
    plt.ylabel("Memory (MB)")
    plt.xlim(primes[0], primes[-1])

def plotter_SC2(n):
    storage = []
    primes = list(range(3, n, 2))
    for i in primes:
        s  = rho_sc(i)
        storage.append(s)
    return storage



