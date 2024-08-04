# Authoer   : Yuan Yu Yang
# Date      : 2024-08-04
# Assignment
# ---------------------------------------
# |Functionality outside of the main running code as module5_mod.py
# ---------------------------------------

class NumberProcessor:
    def __init__(self):
        self.numbers = []
        self.N = 0
        
    def read_N(self):    
        while True:
            try:
                self.N = int(input("Enter a positive integer N: "))
                if self.N > 0:
                    break
                else:
                    print("N must be a positive integer. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

    def read_numbers(self):
        for i in range(self.N):
            while True:
                try:
                    number = int(input(f"Please input {self.N} number to the list NO.{i+1}: "))
                    self.numbers.append(number)
                    break
                except ValueError:
                    print("Invlid input. Please enter an integer")

    def search_number(self, X):
        if X in self.numbers:
            return f'The index of the input {X} in the list is: {self.numbers.index(X) + 1}'
        else:
            return -1


