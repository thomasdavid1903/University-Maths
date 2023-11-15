import time
import math as m
import matplotlib.pyplot as plt
import numpy as np
from retriever import retrieve

start = time.time()

def trial_division(x):
    isPrime = True
    for i in range(2,m.floor(m.sqrt(x))):
        if(x%i==0):
            isPrime = False
    return isPrime

def trial_division_factor(x):
    isPrime = True
    factors = []
    for i in range(2,m.floor(m.sqrt(x))):
        if(x%i==0):
            factors.append(i)
            isPrime = False
    return factors



def plotter_SC(n):
    primes = list(range(3, n, 2))
    times = []


    for i in primes:
        start = time.time()
        trial_division(i)
        times.append(time.time() - start)

    plt.scatter(primes,times)
    plt.title("Time taken for trial division n")
    plt.xlabel("n $(1 = 1e13)$")
    plt.ylabel("Time (seconds)")
    plt.xlim(0, primes[-1])





