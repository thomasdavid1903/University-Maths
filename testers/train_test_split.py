import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

size = 50

# Function to generate synthetic data
np.random.seed(42)
X_2 = 2 * np.random.rand(size, 1)
y_2 = 4 + 3 * X_2 + np.random.randn(size, 1)



# Function to fit a polynomial regression model and evaluate it
def fit_and_evaluate(X_train, y_train, X_test, y_test, degree):
    X_train_poly = PolynomialFeatures(degree=degree).fit_transform(X_train)
    model = LinearRegression().fit(X_train_poly, y_train)

    X_test_poly = PolynomialFeatures(degree=degree).fit_transform(X_test)
    y_pred = model.predict(X_test_poly)

    r2 = r2_score(y_test, y_pred)
    return model, r2


# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_2, y_2, test_size=0.2, random_state=42)

# Fit and evaluate models with different degrees
degree_high = 15
degree_low =  2
model_high, r2_high = fit_and_evaluate(X_train, y_train, X_test, y_test, degree_high)
model_low, r2_low = fit_and_evaluate(X_train, y_train, X_test, y_test, degree_low)

# Plot the models
plt.scatter(X_test,y_test,label="Test Data",color="red")
plt.scatter(X_train, y_train, label="Training Data")
X_plot = np.linspace(0, 2, 100).reshape(-1, 1)
print(X_plot)
plt.plot(X_plot, model_high.predict(PolynomialFeatures(degree=degree_high).fit_transform(X_plot)), label="train")
plt.plot(X_plot, model_low.predict(PolynomialFeatures(degree=degree_low).fit_transform(X_plot)), label="test", color="red")
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

X_test_poly_low = PolynomialFeatures(degree=degree_low).fit_transform(X_test)
y_pred_low = model_low.predict(X_test_poly_low)
r2_low = r2_score(y_test, y_pred_low)
print(f'R² Score (Test): {r2_low}')
print(f'R² Score (Train): {r2_high}')