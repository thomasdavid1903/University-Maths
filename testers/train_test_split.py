from sklearn.model_selection import train_test_split
import numpy as np

X= list(range(1,10))
Y= list(range(11,20))

X_train, X_test,Y_train, Y_test, = train_test_split(X,Y, train_size=2, test_size=2, random_state=42)


print(X_train)
print(X_test)

print(" ")

print(Y_train)
print(Y_test)