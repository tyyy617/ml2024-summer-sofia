# Assignment #7.2: (Optional) Scikit-learn intro
# Yuan Yu Yang

#The program asks the user for input N (positive integer) and reads it.
#Then the program asks the user for input k (positive integer) and reads it.
#Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: 
# first: x value, then: y value for every point one by one. X and Y are the real numbers.
#In the end, the program asks the user for input X and outputs: 
# the result (Y) of k-NN Regression if k <= N, or any error message otherwise.
#Additionally, provide the variance of labels in the training dataset.
#The basic functionality of data processing (data initialization, data insertion), 
# should be done using Numpy library while the computation (ML) part should be done 
# using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous task).

import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    # Read input values
    N = int(input("Enter the number of points (N): "))
    k = int(input("Enter the value of k: "))

    if k > N:
        print("Error: k cannot be greater than N.")
        return

    # Initialize a numpy array to store the points
    points = np.zeros((N, 2))  # Two columns: x and y
    labels = np.zeros(N)  # Array to store y values

    for i in range(N):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y = float(input(f"Enter y value for point {i + 1}: "))
        points[i] = [x, y]
        labels[i] = y

    X = float(input("Enter the value of X to predict Y: "))

    # Compute the variance of the labels
    variance = np.var(labels)
    print(f"The variance of the labels in the training dataset is: {variance}")

    # Prepare data for KNeighborsRegressor
    X_train = points[:, 0].reshape(-1, 1)  # Feature matrix
    y_train = points[:, 1]  # Target values

    # Initialize and fit the KNeighborsRegressor
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)

    # Predict the value for the given X
    X_test = np.array([[X]])
    result = model.predict(X_test)[0]

    print(f"The predicted value of Y for X = {X} is: {result}")

if __name__ == "__main__":
    main()
