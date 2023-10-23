

def fermatTest(a,p):
    probablyPrime = True
    if(a**(p-1) % p != 1):
        probablyPrime = False
    return probablyPrime

fermatTest(2,9)