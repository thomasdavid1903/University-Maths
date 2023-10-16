import numpy as np
import time
import matplotlib.pyplot as plt
from retriever import retrieve

## This program is designed to determine if a given number is prime or composite


n = 4952019383323
p = int((np.floor(np.sqrt(n))))
i = 2
factor = False

primes = np.array(retrieve())


times = [0]*len(primes)


start = time.time()
print("Start : ", start)
for x in range(len(primes)):
    time.sleep(0.1)
    while (p > i and factor == False):

        if (n % i == 0):
            factor = True
            print("Factor Found : ", i)
        i += 1
    if(factor == False):
        print("Prime")
    else:
        print("Composite : ", n, " = ", i - 1, " * ", n / (i - 1))
        factor = True
    end = time.time()
    print(end)
    times[x] = end - start -0.1*x
print(times)
plt.scatter(primes,times)
print(primes)
plt.show()
