# Assignment #9.2: (Optional) Scikit-learn
# Yuan Yu Yang
#The program asks the user for input N (positive integer) and reads it.
#Then the program asks the user to provide N (x, y) pairs (one by one) and reads all of them: 
# first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. 
# X is a real number, Y is a non-negative integer.
#This set of pairs constitutes the training set TrainS = {(x, y)_i}, i = 1..N.
#Then the program asks the user for input M (positive integer) and reads it.
#Then the program asks the user to provide M (x, y) pairs (one by one) and reads all of them: first: 
# x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. 
# X is a real number, Y is a non-negative integer.
#This set of pairs constitutes the test set TestS = {(x, y)_i}, i = 1..M.
#In the end, the program outputs: the best k for the kNN Classification method and the corresponding test accuracy. 
# kNN Classifier should be trained on pairs from TrainS, tested on x values from TestS and compared with y values from TestS.
#The basic functionality of data processing (data initialization, data insertion), 
# should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library 
# as much as possible (note: you can combine with what you've done from the previous tasks). 
#Note: you can try the following range of k: 1 <= k <= 10.


import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    # Read the number of data points
    N = int(input("Enter the number of training points (N): "))

    # get X and Y
    X_train = np.zeros(N)
    y_train = np.zeros(N, dtype=int)

    for i in range(N):
        x = float(input(f"Enter x value for training point {i + 1}: "))
        y = int(input(f"Enter y value (non-negative integer) for training point {i + 1}: "))
        X_train[i] = x
        y_train[i] = y

    # Read the number of test points
    M = int(input("Enter the number of test points (M): "))

    # Initialize numpy arrays to store test data
    X_test = np.zeros(M)
    y_test = np.zeros(M, dtype=int)

    for i in range(M):
        x = float(input(f"Enter x value for test point {i + 1}: "))
        y = int(input(f"Enter y value (non-negative integer) for test point {i + 1}: "))
        X_test[i] = x
        y_test[i] = y

    # Reshape the training and test data to fit scikit-learn's expectations
    X_train = X_train.reshape(-1, 1)
    X_test = X_test.reshape(-1, 1)

    best_k = 1
    best_accuracy = 0

    # Try k values from 1 to min(10, N)
    for k in range(1, min(11, N+1)):
        # Initialize and train the kNN classifier
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)

        # Predict on the test set
        y_pred = knn.predict(X_test)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)

        print(f"Accuracy for k = {k}: {accuracy}")

        # Update best k if the current k gives a better accuracy
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k

    # Output the best k and corresponding accuracy
    print(f"The best k is {best_k} with an accuracy of {best_accuracy}")

if __name__ == "__main__":
    main()
