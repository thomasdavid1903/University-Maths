import time
import random
import matplotlib.pyplot as plt
from sympy import factorint

def p_1_factorization(n, b):
    start_time = time.time()
    result = factorint(n, limit=b)
    end_time = time.time()
    return end_time - start_time

def plot_time_complexity(max_n, step, b):
    n_values = range(10, max_n, step)
    times = []

    for n in n_values:
        time_taken = p_1_factorization(n, b)
        times.append(time_taken)

    plt.scatter(n_values, times)
    plt.xlabel("Number to be factorized (N)")
    plt.ylabel("Time taken (seconds)")
    plt.title(f"P-1 Factorization Time Complexity (B={b})")
    plt.grid()
    plt.show()

max_n = 1000000  # Adjust the maximum N value as needed
step = 2     # Adjust the step size as needed
bound = 1   # Adjust the bound (B) as needed

plot_time_complexity(max_n, step, bound)
