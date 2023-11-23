import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

steam = pd.read_excel("SteamData.xlsx")


#print(steam)
#print(steam.head())

YX1X2=np.array(steam)
#print(y)

y=YX1X2[:,0]
x=YX1X2[:,1:3]

#let's see the type of y and its parameters


B=np.ones([25,1])

X=np.c_[B, x]
#np.transpose(X)
def bhat(X,y):
    return np.linalg.inv( (np.transpose(X)@X))@(np.transpose(X))@y

def f(X, y, predictor):
    np.insert(predictor,0,1)
    predictor = np.array(predictor)
    return predictor @ bhat(X, y)

def sse(X,y):
    return sum( [ (y[i]-f(X,y,X[i,:]))**2 for i in range(0,len(y))  ] )

def sst(X,y):
    return sum( [ (y[i]-np.mean(y))**2 for i in range(0,len(y))  ] )

def ssr(X,y):
    return sum( [ (np.mean(y)-f(X,y,X[i,:]))**2 for i in range(0,len(y))  ] )

def r2(X,y):
    return ssr(X,y)/sst(X,y)

def s2(X,y):
    return sse(X,y) / (len(y) - len(bhat(X,y)) )
print(bhat(X,y))
print(sse(X,y))
print(sst(X,y))
print(ssr(X,y))
print(s2(X,y))