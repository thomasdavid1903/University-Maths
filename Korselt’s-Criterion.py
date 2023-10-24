from improve_trial_divison import trial_division
#if this criterion is satisfied by an odd integer n then n is a Carmichael number, which is a pseudoprime for every base of fermats primality test

def korseltsCriterion(x):
    #need to check if x is a odd number
    statement =""
    if(x%2 == 0):
        statement = "Not a carmichael number as its even"
    else:
        if(trial_division(x) == True):
            statement = "Not a carmichael number as its prime"
        else:
            factors = prime_factors(x)
            squareFree = True
            for num in factors:
                count = factors.count(num)
                if(count!=1):
                    statement = "Not a carmichael number as its not square-free"
                    squareFree = False
            if(squareFree == True):
                divisibility  = True
                for p in factors:
                    if( (x-1)%(p-1) != 0):
                        divisibility = False
                        statement = "Not a carmichael number as n-1|p-1 where p is a prime factor of n"
                if(divisibility == True):
                    print("Factors are " , str(factors]) )
                    statement = str(x) + " is carmichael number"

    return statement

def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

print(korseltsCriterion(561))
