import math as m
import numpy as np
import matplotlib.pyplot as plt
import random

##a simulation study that concerns the problem of approximating a continuous function by polynomials

n = 200
x = 0.5
estimate = []
random_list = sorted([random.uniform(0, 1) for _ in range(random.randint(1, 10))])


def f(x):
    return m.tan(x)


def chose(n, k):
    return m.factorial(n) / (m.factorial(n - k) * m.factorial(k))


def summation(x, n):
    if (abs(x) < 1):
        summation = 0
        for k in range(n):
            summation += f(k / n) * chose(n, k) * (x) ** k * (1 - x) ** (n - k)
    else:
        raise Exception("|x|<1 needs to be satisfied")
    return summation


def maxFind(random_list, n):
    maximum = random_list[0]
    for point in random_list:
        if (summation(point, n) > summation(maximum, n)):
            maximum = point
    print("Maximum :" + str(maximum) + " from " + str(random_list))


def graphPlot(n, x):
    for i in range(n):
        estimateN = summation(x, i)
        difference = abs(f(x) - summation(x, i))
        estimate.append(difference)

    xaxis = np.arange(0, len(estimate), 1)
    plt.scatter(xaxis, estimate, label="$|f(x)-\sum_{i=1}^{n} f(in^{-1})B_{x,k}(x)|$", s=40, facecolors='none',
                edgecolors="r")
    plt.axhline(y=0, color="black", label="X-axis (n)")
    plt.axvline(x=0, color="black", label="Y-axis ")
    plt.title("$|{(P_n(x_i)-f(x)}|$")
    plt.legend()
    graphText1 = "$f(x) = $" + str(f(x))
    graphText2 = "$f_n(x) = $" + str(estimateN) + " when $n=$" + str(n)
    graphText3 = "Simulations confirm the theoretical result about the convergence"
    plt.text(n // 2, estimate[2], graphText1)
    plt.text(n // 2, estimate[3], graphText2)
    plt.text(n // 2, estimate[4], graphText3)
    plt.show()

graphPlot(n, x)
maxFind(random_list, n)
