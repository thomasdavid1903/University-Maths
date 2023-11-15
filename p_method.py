import math
import time
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches
import os, psutil
import numpy as np

def pollard_p_1(N, B):
    a = 2
    for p in range(2, B + 1):
        a = pow(a, p, N) # Compute a^p modulo N
        d = math.gcd(a - 1, N) # Calculate the GCD of (a^p - 1) and N
        if 1 < d < N: # Check if d is a non-trivial factor
            return d # If a non-trivial factor is found, return it
    return None # If no non-trivial factor is found, return None

def plotter_TC():
    times = []
    ##primes = np.array(retrieve())
    ##primes = primes[100:400]
    ##primes = np.array(primes)
    colors = []
    primes = list(range(1, 100000, 1))

    for i in primes:
        start = time.time_ns()
        prime = pollard_p_1(i, i-1)
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
    plt.scatter(primes,times,color=colors,s=0.5)
    plt.title("Time taken for $p-1$ method on n")
    plt.xlabel("$n$")
    plt.ylabel("Time (ns seconds)")
    plt.xlim(primes[0], primes[-1])







def pollard_p_1_SC(N, B):
    a = 2
    for p in range(2, B + 1):
        a = pow(a, p, N) # Compute a^p modulo N
        d = math.gcd(a - 1, N) # Calculate the GCD of (a^p - 1) and N
        if 1 < d < N: # Check if d is a non-trivial factor
            print(d) # If a non-trivial factor is found, return it
    return psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)

def plotter_SC(n):
    times = []
    colors = ["pink"]
    space = []
    primes = list(range(3, n, 2))

    for i in primes:
        space.append(pollard_p_1_SC(i, i-1))


    print(times)
    print(len(times))
    plt.scatter(primes,space,color=colors,s=0.5)
    plt.title("Memory Used for $p-1$ method on n in MB")
    plt.xlabel("$n$")
    plt.ylabel("Memory (MB)")
    plt.xlim(primes[0], primes[-1])


def plotter_SC2(n):
    storage = []
    primes = list(range(3, n, 2))
    for i in primes:
        s  = pollard_p_1_SC(i,i-1)
        storage.append(s)
    return storage