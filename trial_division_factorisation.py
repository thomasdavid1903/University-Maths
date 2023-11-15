import math as m
import os, psutil
from retriever import retrieve
import numpy as np
import matplotlib.pyplot as plt

def get_memory_usage():
    return psutil.Process().memory_info().rss / (1024 * 1024)
initial_memory = get_memory_usage()
# A program that uses the same princple as trial division primality test to find the prime factors of a positive integer n
def tdFactorisation(n):
    num = n
    factors = []
    for p in range(2,m.floor(m.sqrt(n))+1):
        e = 0
        #print
        # prints how many Mib are being used
        if(n%p == 0):
            while(n%p == 0):
                e = e + 1
                n = n/p
            print(psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2))
            factors.append([p,e])
    print("The factors of {}".format(num), "and their powers")
    print(factors)
    return factors

def plotter_SC(N):
    storage = []
    #primes = np.array(retrieve())
    #primes = np.array(primes)
    #primes = primes[70:500]
    primes = np.arange(3,N,2)

    for i in primes:
        s  = tdFactorisationP(i)
        storage.append(s)

    plt.plot(primes,storage)
    plt.title("Storage used for trial division n")
    plt.xlabel("$n$")
    plt.ylabel("Storage used (MB)")
    plt.xlim(0, primes[-1])


def tdFactorisationP(n):
    num = n
    factors = []
    for p in range(2, m.floor(m.sqrt(n)) + 1):
        e = 0
        if (n % p == 0):
            while (n % p == 0):
                e = e + 1
                n = n / p
            factors.append([p, e])
    print("Memory " , get_memory_usage())
    return psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)

def plotter_SC2(n):
    storage = []
    primes = np.arange(3,n,2)
    for i in primes:
        s  = tdFactorisationP(i)
        storage.append(s)
    return storage






