import numpy as np
import matplotlib.pyplot as plt
import pylatex


def count_decimal_places(number):
    if isinstance(number, (int, float)):
        number_str = str(number)
        if '.' in number_str:
            return len(number_str.split('.')[1])
        else:
            return 0


class continuous:
    def __init__(continuous, x_n, a_n):
        x_n.insert(0, x_n[0] - 10)
        x_n.append(x_n[-1] + 10)
        continuous.x_n = x_n
        continuous.a_n = a_n
        correctFormat = False
        if (len(a_n) - 1 == len(x_n)):
            correctFormat = True
            print("Correct Format")
        continuous.correctFormat = correctFormat

    def plot(continuous):
        a_n = continuous.a_n
        x_n = continuous.x_n

        color = ["red", "blue", "orange", "purple", "green"]

        for i in range(len(a_n)):
            gap = x_n[i + 1] - x_n[i]
            precision = count_decimal_places(gap)
            x = np.arange(x_n[i], x_n[i + 1], 10 ** (precision - 1))
            y = [a_n[i]] * len(x)

            if (i > 0):
                plt.scatter(x_n[i], a_n[i], color=color[i])
            if (i == 0):
                plt.scatter(x_n[i + 1], a_n[i], s=80, facecolors='none', edgecolors=color[i])

            if (i > 0 and i < len(a_n)):
                labels = "f(x)=" + str(a_n[i]) + " : " + str(x_n[i]) + "<x<" + str(x_n[i + 1])
            if (i == 0):
                labels = "f(x)=" + str(a_n[i]) + " : " "x<" + str(x_n[i + 1])
            if (i == len(a_n) - 1):
                labels = "f(x)=" + str(a_n[i]) + " : " "x>" + str(x_n[i])

            plt.plot(x, y, label=labels, color=color[i])
            plt.legend()

        plt.xlim(x_n[0], x_n[-1])
        plt.title("f(x)")
        plt.show()

    def value(continuous, x):
        a_n = continuous.a_n
        x_n = continuous.x_n
        current_a = a_n[0]
        for i in range(len(a_n)):

            if (i == 0 and x_n[i] <= x and x <= x_n[i]):
                current_a = a_n[i]

            if (x_n[i] < x and x <= x_n[i + 1]):
                current_a = a_n[i]
            if (x_n[i] < x):
                current_a = a_n[i]
        return (current_a)

    def integral(continuous, a, b):
        a_n = continuous.a_n
        x_n = continuous.x_n
        area = 0
        if (a <= b):
            for i in range(len(a_n)):
                print("Section : ", i)
                if (x_n[i] < a and b < x_n[i + 1]):
                    area += (b - a) * a_n[i]
                    print("1 : ", (b - a) * a_n[i])

                if (a <= x_n[i] and x_n[i + 1] <= b):
                    area += (x_n[i + 1] - x_n[i]) * a_n[i]
                    print("2 : ", (x_n[i + 1] - x_n[i]) * a_n[i])

                if (a < x_n[i] and b < x_n[i + 1] and x_n[i] < b):
                    area += (b - x_n[i]) * a_n[i]
                    print("3 : ", (b - x_n[i]) * a_n[i])

                if (x_n[i] < a and x_n[i + 1] < b and a < x_n[i + 1]):
                    area += (x_n[i + 1] - a) * a_n[i]
                    print("4 : ", (x_n[i + 1] - a) * a_n[i])
        return area


graph1 = continuous([10, 21, 33, 40], [7, 2, 4, 2.5, 5])

graph1.plot()
print(graph1.value(51))
print(graph1.integral(0, 40))