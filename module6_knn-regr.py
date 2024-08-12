# Assignment #6.2: (Optional) Numpy
# Yuan Yu Yang
# Create a Python program:
# The program asks the user for input N (positive integer) and reads it.
# Then the program asks the user for input k (positive integer) and reads it.
# Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, 
#   then: y value for every point one by one. X and Y are the real numbers.
# In the end, the program asks the user for input X and outputs: 
#   the result (Y) of k-NN Regression if k <= N, or any error message otherwise.
# The basic functionality of data processing (data initialization, data insertion, 
#   data calculation) should be done using Numpy library as much as possible (note: you can combine with OOP from the previous task).


import numpy as np

class KNNRegressor:
    def __init__(self, points, k):
        self.points = np.array(points)
        self.k = k

    def predict(self, x):
        # Calculate distances between x and all points
        distances = np.abs(self.points[:, 0] - x)
        # Get indices of the k nearest neighbors
        k_nearest_indices = np.argsort(distances)[:self.k]
        # Get the y values of the k nearest neighbors
        k_nearest_y = self.points[k_nearest_indices, 1]
        # Return the mean of the y values of the k nearest neighbors
        return np.mean(k_nearest_y)

def main():
    # Read input values
    N = int(input("Enter the number of points (N): "))
    k = int(input("Enter the value of k: "))

    if k > N:
        print("Error: k cannot be greater than N.")
        return

    points = []
    for i in range(N):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y = float(input(f"Enter y value for point {i + 1}: "))
        points.append((x, y))

    X = float(input("Enter the value of X to predict Y: "))

    # Initialize the KNN Regressor
    knn = KNNRegressor(points, k)
    result = knn.predict(X)

    print(f"The predicted value of Y for X = {X} is: {result}")

if __name__ == "__main__":
    main()