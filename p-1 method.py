import math


def pollard_p_1(N, B):
    a = 2  # Start with a base value of 2

    for j in range(2, B + 1):
        a = pow(a, j, N)  # Compute a^j modulo N

        p = math.gcd(a - 1, N)  # Calculate the GCD of (a^j - 1) and N

        if p != 1 and p != N:  # Check if p is a non-trivial factor
            return f"{p} is a factor of {N}"

    return "No result"  # If no factor found within the specified range


# Example usage:
N = 91
B = 10  # You can choose an appropriate value for B
result = pollard_p_1(N, B)
print(result)