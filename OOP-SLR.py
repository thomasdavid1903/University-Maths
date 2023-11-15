import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

x = [3.4, 2, 5, 2.3, 3.1, 5.5, 1, 2.8, 2.4, 4.3, 2.1, 1.1, 6.1, 4.8, 3.8]
y = [26.2, 17.8, 31.3, 23.1, 27.5, 36.0, 14.1, 22.3, 19.6, 31.3, 24.0, 17.3, 43.2, 36.4, 26.1]


class slr():
    def __init__(slr, y, x):
        slr.y = y
        slr.x = x

    def Sxx(slr):
        slr.x = x
        S = sum([x[i] * x[i] for i in range(0, len(x))])
        return S - np.mean(x) * np.mean(x) * len(x)

    def Sxy(slr):
        slr.x = x
        slr.y = y
        S = sum([x[i] * y[i] for i in range(0, len(x))])
        return S - np.mean(x) * np.mean(y) * len(x)

    def bhat(slr):
        slr.y = y
        slr.x = x
        return slr.Sxy() / slr.Sxx()

    def ahat(slr):
        slr.y = y
        slr.x = x
        ybar = np.mean(y)
        xbar = np.mean(x)
        return ybar - slr.bhat() * xbar

    def f(slr, x):
        a = slr.ahat()
        b = slr.bhat()
        return a + b * x

    def sse(slr):
        a = slr.ahat()
        b = slr.bhat()
        return sum([(y[i] - (a + b * x[i])) ** 2 for i in range(0, len(y))])

    def sst(slr):
        return sum([(y[i] - np.mean(y)) ** 2 for i in range(0, len(y))])

    def ssr(slr, a, b):
        a = slr.ahat()
        b = slr.bhat()
        return slr.sst() - slr.sse()

    def RSquared(slr):
        a = slr.ahat()
        b = slr.bhat()
        return (slr.sst(y, x, a, b) - slr.sse()) / slr.sst()

    def Ssquared(slr):
        a = slr.ahat()
        b = slr.bhat()
        return slr.sse() / (len(y) - 2)

    def ei(slr):
        a = slr.ahat()
        b = slr.bhat()
        return [y[i] - slr.f(x[i]) for i in range(0, len(x))]

    def plot(slr):
        a = slr.ahat()
        b = slr.bhat()
        plt.scatter(x, y, label="Data", color="purple")
        plt.xlabel("$x_i$")
        plt.ylabel("$y_i$")
        plt.title("Scatter Plot")
        plt.legend()
        plt.show()

    def plotFitted(slr):
        a = slr.ahat()
        b = slr.bhat()
        plt.scatter(x, y, label="Data", color="purple")
        predicted = [slr.f(x[i]) for i in range(0, len(x))]
        plt.plot(x, predicted, label="Predicted", color="pink")
        plt.xlabel("$x_i$")
        plt.ylabel("$y_i$")
        plt.title("Scatter Plot")
        plt.legend()
        plt.show()

    def plotResiduals(slr):
        a = slr.ahat()
        b = slr.bhat()
        plt.scatter(x, y, label="Data", color="purple")
        predicted = [slr.f(x[i]) for i in range(0, len(x))]
        plt.plot(x, predicted, label="Predicted", color="pink")
        plt.xlabel("$x_i$")
        plt.ylabel("$y_i$")
        plt.title("Scatter Plot")
        plt.legend()
        for i in range(0, len(x)):
            plt.plot([x[i], x[i]], [y[i], slr.f(x[i])], color="orange", linestyle="-.")
        plt.show()

    def t(slr):
        a = slr.ahat()
        b = slr.bhat()
        return b / (np.sqrt(slr.Ssquared() / slr.Sxx()))

    def pvalue(slr, n, val):
        # val needs to be t obs
        p = 2 * (1 - stats.t.cdf(val, n))
        if (p > 0.05):
            print(f"We accept the null hypothesis as {round(p, 10)}>0.05")
        if (p <= 0.05):
            print(f"We reject the null hypothesis as {round(p, 10)}<=0.05")
        return p

    def plotAll(slr):
        plt.subplot(1, 3, 1)
        slr.plot()
        plt.subplot(1, 3, 2)
        slr.plotFitted()
        plt.subplot(1, 3, 3)
        slr.plotResiduals()
        plt.show()

graph1 = slr(y, x)
print("The slope of the graph ", graph1.bhat())
print("The intercept of the graph ", graph1.ahat())
print("f(1) =", graph1.f(1))
print("The p value of the hypothesis test : ", graph1.pvalue(len(x), graph1.t()))
print("The residuals of the graph is, ", np.round(graph1.ei(), decimals=3))
# graph1.plotResiduals()
graph1.plotAll()
