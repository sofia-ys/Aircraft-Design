import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Data
max_payload = np.array([25970, 41050, 18711, 23133, 18325, 22000, 62250, 23000, 16150, 40000, 33355])
MTOM = np.array([115680, 228000, 70896, 87997, 141521, 186880, 273310, 165000, 61500, 250000, 211374])
max_range = np.array([7222, 13530, 6300, 7408, 8112, 11305, 12270, 8000, 4815, 10000, 6862])
OEM = np.array([58390, 119950, 37080, 45450, 66670, 90770, 132800, 74000, 33300, 120400, 111795])

def linear_regression(p, y) :
    #convert p in appropriate form (sklearn = weird)
    X = p.reshape(-1, 1)
    # Train the model
    model = LinearRegression()
    model.fit(X, y)

    # Make predictions
    y_pred = model.predict(X)

    # Plotting the regression line
    plt.scatter(X, y, color='blue', label='Actual Data')
    plt.plot(X, y_pred, color='red', label='Regression Line')
    plt.xlabel('just type the name manually (x axis)')
    plt.ylabel('just type the name manually (y axis)')
    plt.legend()

    # Display the plot
    plt.show()

    # Get the regression coefficients
    b_1 = model.coef_[0]  # Slope (coefficient of X)
    b_0 = model.intercept_ # Intercept

    print(f"Estimated coefficients:\nb_0 (intercept) = {b_0}\nb_1 (slope) = {b_1}")

linear_regression(max_payload, MTOM)