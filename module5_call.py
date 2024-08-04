# Authoer   : Yuan Yu Yang
# Date      : 2024-08-04
# Assignment
# ---------------------------------------
# |Call class from module5_mod.py
# ---------------------------------------

from module5_mod import *

def main():
    processor = NumberProcessor()
    processor.read_N()
    processor.read_numbers()

    
    while True: # Use while true loop to ensure user input the valid positive integer
        try:
            X = int(input("Enter the number to search from the list: "))
            break
        except ValueError:
            print("invlid input. Please enter an integer")
    
    result = processor.search_number(X)
    print(result)


if __name__ == "__main__":
    main()