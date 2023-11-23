import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

def bhat(X,y):
    return np.linalg.inv( (np.transpose(X)@X))@(np.transpose(X))@y

def s2(X,y):
    return sse(X,y) / (len(y) - len(bhat(X,y)) )

def sse(X,y):
    return sum( [ (y[i]-f(X,y,X[i,:]))**2 for i in range(0,len(y))  ] )

def sst(X,y):
    return sum( [ (y[i]-np.mean(y))**2 for i in range(0,len(y))  ] )

def ssr(X,y):
    return sum( [ (np.mean(y)-f(X,y,X[i,:]))**2 for i in range(0,len(y))  ] )

def r2(X,y):
    return ssr(X,y)/sst(X,y)

init_seed= 42
np.random.seed(init_seed)
n = 10

x=[]

err=np.random.normal(0,5,n)
x1=np.random.uniform(0,10,n)
x2=np.random.uniform(0,5,n)
x3=np.random.uniform(0,2,n)
y=3*x1 -2*x2 + 5*x3 +err


x = np.column_stack((x1, x2, x3))
X = np.column_stack((np.ones([n,1]),x1, x2, x3))
print(x)
print(" ")
bhat = bhat(X,y)
print("My code : ",bhat)

print(" ")

Model = LinearRegression()
Model.fit(x, y)
print("Sklearn : ",Model.intercept_, Model.coef_[0], Model.coef_[1],Model.coef_[2] )
y_pr= Model.predict(x)
mse = mean_squared_error(y, y_pr)
print("Sklearn : Mean Squared Error : ", mse)
#R-squared, coeff. of determination
r2 = r2_score(y, y_pr)
print("Sklearn : Coefficient of Determinition : ", r2)