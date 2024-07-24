# Authoer   : Yuan Yu Yang
# Date      : 2024-07-23

if __name__ == "__main__":
    # Ask the user for the input N (positive integer)
    n = int(input("Please enter a positive integer N: "))

    # Asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
    numberList = []
    for i in range(n):
        num = int(input(f"Please input {n} number to the list NO.{i+1}: "))
        numberList.append(num)

    # The program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, 
    # or the index (from 1 to N) of this X if the user inputed it before.
    x = int(input("Enter integer number x to search from the list: "))

    if x in numberList:
        index = numberList.index(x) + 1 # Get 1-based index
        print(f'The index of the input x in the list is: {index}')
    else:
        print(-1)