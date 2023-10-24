import math as m
# A program that uses the same princple as trial division primality test to find the prime factors of a positive integer n
def tdFactorisation(n):
    factors = []
    for p in range(2,m.floor(m.sqrt(n))+1):
        e = 0
        if(n%p ==0):
            while(n%p == 0):
                e = e + 1
                n = n/p
            factors.append([p,e])
    return factors
print(tdFactorisation(169))

