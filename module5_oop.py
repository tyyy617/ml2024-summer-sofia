# Authoer   : Yuan Yu Yang
# Date      : 2024-08-04
# Assignment
# ---------------------------------------
# |The program asks the user for input N (positive integer) and reads it
# |Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
# |In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputted it before.
# |The basic functionality of data processing (data initialization, data insertion, data search) should be done via Object-Oriented Programming Paradigm (i.e. using Classes)
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
            return self.numbers.index(X) + 1
        else:
            return -1
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
