import math


def pollard_p_1(N, B):
    a = 2

    for j in range(2, B + 1):
        a = pow(a, j, N)  # Compute a^j modulo N

        p = math.gcd(a - 1, N)

        if p != 1 and p != N:
            return f"{p} is a factor of {N}"

    return "No result"


# Example usage:
N = 91
B = 10  # You can choose an appropriate value for B
result = pollard_p_1(N, B)
print(result)