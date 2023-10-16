
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

size = 10000

x = np.arange(0,size,1)
y = np.array( [0]*size)
counter = 0
for num in x:
    if(isprime(num) == True):
        counter+=1
        y[num] = counter
    if (isprime(num) == False):
        y[num] = counter

plt.scatter(x,y,label = "π(x) - Distribution of Primes",color = "purple",s=1)
plt.scatter(x,x/np.log(x), label=r'$\frac{x}{log(x)}$',color ="pink",s=1)
plt.xlabel(r'$x$', size = 20)
plt.ylabel( r'$\frac{x}{log(x)}$' ,size = 20)
plt.title("Distribution of primes vs "+ r'$\frac{x}{log(x)}$',size=30)

plt.legend(prop={'size': 20})
plt.grid()
plt.grid(color='grey', linestyle='-.', linewidth=0.5)
plt.xlim(0,size)
plt.ylim(0,size/10)
plt.xticks(size=15)
plt.yticks(size=15)
plt.show()

