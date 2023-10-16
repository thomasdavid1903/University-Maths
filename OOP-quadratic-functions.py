import numpy as np
import matplotlib.pyplot as plt

# A program that can be used to create quadratics using OOP then apply methods to perform tasks, like solve, plot and find the global max/mini

class quadratic():
    def __init__(quadratic, a, b, c):
        quadratic.a = a
        quadratic.b = b
        quadratic.c = c

    def value(quadratic, x):
        return quadratic.a * (x ** 2) + quadratic.b * x + quadratic.c

    def solve(quadratic):
        a = quadratic.a
        b = quadratic.b
        c = quadratic.c
        x1 = 0
        x2 = 0

        if (a != 0):
            x1 = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
            x2 = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
        if (a == 0 and b != 0):
            x1 = -c / b

        if (b ** 2 - 4 * a * c > 0 and a != 0):
            statement_solve = "There are only real roots : " + str(x1) + " and " + str(x2)
        if (b ** 2 - 4 * a * c < 0):
            statement_solve = "There are only complex roots : " + str(x1) + " and " + str(x2)
        if (b ** 2 - 4 * a * c == 0):
            statement_solve = "There are only one root : " + str(x1)
        if (a == 0):
            statement_solve = "There is only one real root : " + str(x1)
        if (a == 0 and b == 0):
            statement_solve = "The graph is constant and f(x) = " + str(c) + " so no solutions to f(x) = 0"
        if (a == 0 and b == 0 and c == 0):
            statement_solve = "The graph is constant and f(x) = 0 so there is infinite solutions"

        return x1, x2, statement_solve

    def globalM(quadratic):
        a = quadratic.a
        b = quadratic.b
        c = quadratic.c
        m = 0
        if (a > 0):
            m = -b / (2 * a)
            statement_global = "Global minimum is at ( " + str(m) + " , " + str(quadratic.value(m)) + " )"
        if (a < 0):
            m = -b / (2 * a)
            statement_global = "Global maximum is at ( " + str(m) + " , " + str(quadratic.value(m)) + " )"
        if (a == 0):
            statement_global = "No global maximum or minimum as the graph is linear"
        return m, statement_global

    def plot(quadratic, x1, x2):

        title = ""

        a = quadratic.a
        b = quadratic.b
        c = quadratic.c

        if ((a != 1 or a != -1) and a != 0):
            title = str(a) + "x$^2$"
        if (a == 1):
            title = "x$^2$"
        if (a == -1):
            title = "-x$^2$"
        if (b > 0 and a != 0):
            title = title + "+" + str(b) + "x"
        if (b < 0 and a != 0):
            title = title + str(b) + "x"
        if (a == 0):
            if (b == 1):
                title = "x"
            if (b == -1):
                title = "-x"
            if (b != 1 and b != -1):
                title = str(b) + "x"
        if (c > 0):
            title = title + "+" + str(c)
        if (c < 0):
            title = title + str(c)

        if (a == 0 and b == 0):
            x1 = -5
            x2 = 5

        x = np.arange(x1, x2, .1)
        plt.plot(x, quadratic.value(x), linestyle="-.", label=title)
        plt.title(title)
        # plt.xlabel("x values")
        # plt.ylabel(quadratic.a,"x^2",quadratic.b,"x +",quadratic.c)

    def localM(quadratic, x1, x2):
        m, statementGlobal = quadratic.globalM()
        a = quadratic.a
        b = quadratic.b
        c = quadratic.c

        maximum = ""
        minimum = ""

        if (a > 0):
            if (x1 < m and m < x2):
                minimum = "Local minimum is ( " + str(m) + " , " + str(quadratic.value(m)) + " )"
                mini_p = m
                if (m - x1 < x2 - m):
                    maximum = "Local maximum is ( " + str(x2) + " , " + str(quadratic.value(x2)) + " )"
                    max_p = x2
                if (m - x1 > x2 - m):
                    maximum = "Local maximum is ( " + str(x1) + " , " + str(quadratic.value(x1)) + " )"
                    max_p = x1
                if (m - x1 == x2 - m):
                    maximum = "Local maximum is ( " + str(x1) + " , " + str(
                        quadratic.value(x1)) + " )" + " and " + + str(x2) + " , " + str(quadratic.value(x2)) + " )"
                    max_p = x1
            if (x2 < m):
                minimum = "Local minimum is ( " + str(x2) + " , " + str(quadratic.value(x2)) + " )"
                maximum = "Local maximum is ( " + str(x1) + " , " + str(quadratic.value(x1)) + " )"
                max_p = x1
                mini_p = x2
            if (m < x1):
                minimum = "Local minimum is ( " + str(x1) + " , " + str(quadratic.value(x1)) + " )"
                maximum = "Local maximum is ( " + str(x2) + " , " + str(quadratic.value(x2)) + " )"
                max_p = x2
                mini_p = x1

        if (a < 0):
            if (x1 < m and m < x2):
                maximum = "Local maximum is ( " + str(m) + " , " + str(quadratic.value(m)) + " )"
                max_p = m
                if (m - x1 < x2 - m):
                    minimum = "Local minimum is ( " + str(x2) + " , " + str(quadratic.value(x2)) + " )"
                    mini_p = x2
                if (m - x1 > x2 - m):
                    minimum = "Local miniimum is ( " + str(x1) + " , " + str(quadratic.value(x1)) + " )"
                    mini_p = x1
                if (m - x1 == x2 - m):
                    minimum = "Local miniimum is ( " + str(x1) + " , " + str(
                        quadratic.value(x1)) + " )" + " and ( " + str(x2) + " , " + str(quadratic.value(x2)) + " )"
                    mini_p = x1
            if (x2 < m):
                minimum = "Local minimum is ( " + str(x1) + " , " + str(quadratic.value(x1)) + " )"
                maximum = "Local maximum is ( " + str(x2) + " , " + str(quadratic.value(x2)) + " )"
                max_p = x2
                mini_p = x1
            if (m < x1):
                minimum = "Local minimum is ( " + str(x2) + " , " + str(quadratic.value(x2)) + " )"
                maximum = "Local maximum is ( " + str(x1) + " , " + str(quadratic.value(x1)) + " )"
                max_p = x1
                mini_p = x2
        if (a == 0):
            if (b > 0):
                max_p = x2
                mini_p = x1
            if (b < 0):
                max_p = x1
                mini_p = x2
            if (b == 0):
                max_p = x2
                mini_p = x1
        minimum += " in the domain [" + str(x1) + " , " + str(x2) + "]"
        maximum += " in the domain [" + str(x1) + " , " + str(x2) + "]"
        return minimum, maximum, mini_p, max_p

    def everything(quadratic, low, high):
        a = quadratic.a
        b = quadratic.b
        c = quadratic.c

        x1, x2, statement_solve = quadratic.solve()
        quadratic.plot(low - 5, high + 5, )
        if (a != 0 and b != 0):

            m, statement_global = quadratic.globalM()

            minimum, maximum, mini_p, max_p = quadratic.localM(low, high)
            if (a > 0):
                gap = -20
                global_m = "Global Minimum"
            if (a < 0):
                gap = +20
                global_m = "Global Maximum"
            if (a == 0):
                gap = +20
                global_m = "Not a quadratic function"

            plt.scatter(m, quadratic.value(m), color="red", label=global_m)
            if (b ** 2 - 4 * a * c >= 0):
                plt.scatter(x1, quadratic.value(x1), color="green")
                plt.text(x1, quadratic.value(x1) + 15, "(" + str(x1) + "," + str(quadratic.value(x1)) + ")",
                         horizontalalignment='center')
                plt.scatter(x2, quadratic.value(x2), color="green", label='Roots')
                plt.text(x2, quadratic.value(x2) + 15, "(" + str(x2) + "," + str(quadratic.value(x2)) + ")",
                         horizontalalignment='center')

            plt.text(m, quadratic.value(m) + gap, "(" + str(m) + "," + str(quadratic.value(m)) + ")",
                     horizontalalignment='center')
            plt.axvline(x=low, color='purple', label='Lower Bound of Interval', linestyle="dotted")
            plt.axvline(x=high, color='purple', label='Upper Bound of Interval', linestyle="dotted")
        if (a == 0 and b != 0):
            plt.scatter(x1, quadratic.value(x1), color="green", label="Roots")
            plt.text(x1, quadratic.value(x1) + 2, "(" + str(x1) + "," + str(quadratic.value(x1)) + ")",
                     horizontalalignment='center')
        plt.axhline(y=0, color="black")
        plt.axvline(x=0, color="black")
        plt.legend()

        if (a != 0 or (a != 0 and b != 0)):
            print(statement_global)
            print(maximum)
            print(minimum)
            print(statement_solve)


graph1 = quadratic(1, 11, 18)
graph2 = quadratic(1, 2, 1)

print(graph1.solve()[2])
minimum, maximum, max_p, mini_p = graph1.localM(0, 2)
print(minimum)
print(maximum)
global_m = graph1.globalM()
print(global_m[1])

print(" ")

graph2.everything(-10, 10)

# graph3.everything(-10,10)

plt.show()