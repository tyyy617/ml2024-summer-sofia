# Assignment #8.2: (Optional) Scikit-learn intro (a bit deeper)
# Yuan Yu Yang

#The program asks the user for input N (positive integer) and reads it.
#Then the program asks the user to provide N (x, y) points (one by one) 
# and reads all of them: first: x value, then: y value for every point one by one. 
# X is treated as the ground truth (correct) class label and Y is treated as the predicted class. 
# Both X and Y are either 0 or 1.
#In the end, the program outputs: the Precision and Recall based on the inputs.
#The basic functionality of data processing (data initialization, data insertion), 
# should be done using Numpy library 
# while the computation (ML) part should be done using Scikit-learn library 
# as much as possible (note: you can combine with what you've done from the previous tasks).


import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Read the number of data points
    N = int(input("Enter the number of points (N): "))

    # Initialize numpy arrays to store ground truth and predicted labels
    y_true = np.zeros(N, dtype=int)  # Ground truth labels
    y_pred = np.zeros(N, dtype=int)  # Predicted labels

    for i in range(N):
        x = int(input(f"Enter ground truth label (0 or 1) for point {i + 1}: "))
        if x != 0 and x != 1:
            print("Error: x can only be 0 or 1.")
            return
        y = int(input(f"Enter predicted label (0 or 1) for point {i + 1}: "))
        if y != 0 and x != 1:
            print("Error: y can only be 0 or 1.")
            return
        y_true[i] = x
        y_pred[i] = y

    # Compute Precision and Recall
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)

    # Output results
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")

if __name__ == "__main__":
    main()