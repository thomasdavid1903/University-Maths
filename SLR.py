import matplotlib.pyplot as plt
import numpy as np

#Functions for Simple Linear Regression

# Given data
x = [3.4, 1.8, 4.6, 2.3, 3.1, 5.5, 0.7, 3.0, 2.6, 4.3, 2.1, 1.1, 6.1, 4.8, 3.8]
y = [26.2, 17.8, 31.3, 23.1, 27.5, 36.0, 14.1, 22.3, 19.6, 31.3, 24.0, 17.3, 43.2, 36.4, 26.1]

# Function to calculate the sum of cross-products
def S(xs, ys):
    S = sum([xs[i] * ys[i] for i in range(0, len(xs))])
    return S - np.mean(xs) * np.mean(ys) * len(xs)

# Function to calculate the slope of the regression line (b)
def bhat(y, x):
    return S(x, y) / S(x, x)

# Function to calculate the intercept of the regression line (a)
def ahat(y, x):
    ybar = np.mean(y)
    xbar = np.mean(x)
    return ybar - bhat(y, x) * xbar

# Function for the regression line equation
def f(x, a, b):
    return a + b * x

# Function to calculate the sum of squared errors
def sse(y, x, a, b):
    return sum([(y[i] - (a + b * x[i]))**2 for i in range(0, len(y))])

# Function to calculate the total sum of squares
def sst(y, x):
    return sum([(y[i] - np.mean(y))**2 for i in range(0, len(y))])

# Function to calculate the sum of squares due to regression
def ssr(y, x, a, b):
    return sst(y, x) - sse(y, x, a, b)

# Function to calculate the coefficient of determination (R-squared)
def RSquared(y, x, a, b):
    return (sst(y, x, a, b) - sse(y, x, a, b)) / sst(y, x, a, b)

# Function to calculate the estimated variance of the residuals
def Ssquared(y, x, a, b):
    return sse(y, x, a, b) / (len(y) - 2)

# Function to calculate the residuals
def ei(y, x, a, b):
    return [y[i] - f(x[i], a, b) for i in range(0, len(x))]

# Function to plot the scatter plot
def plot(y, x, a, b):
    plt.scatter(x, y, label="Data", color="purple")
    plt.xlabel("$x_i$")
    plt.ylabel("$y_i$")
    plt.title("Scatter Plot")
    plt.legend()

# Function to plot the scatter plot with the fitted line
def plotFitted(y, x, a, b):
    plt.scatter(x, y, label="Data", color="purple")
    predicted = [f(x[i], a, b) for i in range(0, len(x))]
    plt.plot(x, predicted, label="Predicted", color="pink")
    plt.xlabel("$x_i$")
    plt.ylabel("$y_i$")
    plt.title("Scatter Plot")
    plt.legend()

# Function to plot the scatter plot with the residuals
def plotResiduals(y, x, a, b):
    plt.scatter(x, y, label="Data", color="purple")
    predicted = [f(x[i], a, b) for i in range(0, len(x))]
    plt.plot(x, predicted, label="Predicted", color="pink")
    plt.xlabel("$x_i$")
    plt.ylabel("$y_i$")
    plt.title("Scatter Plot")
    plt.legend()
    for i in range(0, len(x)):
        plt.plot([x[i], x[i]], [y[i], f(x[i], a, b)])

# Plot the residuals
plotResiduals(y, x, ahat(y, x), bhat(y, x))

# Print the intercept (ahat)
print("Intercept (ahat):", ahat(y, x))

# Calculate and print the total sum of squares (sst)
print("Total Sum of Squares (sst):", sst(y, x))
