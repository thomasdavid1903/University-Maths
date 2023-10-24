def facotorisation(n):
    factors = []
    # Check for divisibility by 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # Check for divisibility by odd numbers starting from 3
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    # If n is still greater than 1, it is a prime number
    if n > 1:
        factors.append(n)

    return factors

number = 56
result = facotorisation(number)
print(f"The prime factors of {number} are: {result}")
