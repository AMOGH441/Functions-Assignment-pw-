class Fibonacci:
    def __init__(self, num_terms):
        self.num_terms = num_terms  # Number of terms to generate
        self.count = 0  # Counter to keep track of iterations
        self.a, self.b = 0, 1  # Initial values for Fibonacci sequence (F(0) = 0, F(1) = 1)

    def __iter__(self):
        return self  # Return the iterator object itself

    def __next__(self):
        if self.count >= self.num_terms:
            raise StopIteration  # Stop the iteration when the number of terms is reached
        
        # Generate the next Fibonacci number
        if self.count == 0:
            self.count += 1
            return self.a  # Return the first Fibonacci number (0)
        elif self.count == 1:
            self.count += 1
            return self.b  # Return the second Fibonacci number (1)
        else:
            self.a, self.b = self.b, self.a + self.b  # Update values for Fibonacci sequence
            self.count += 1
            return self.b

# Usage example:
num = int(input("Enter the number of Fibonacci terms: "))
fib = Fibonacci(num)

# Iterating through Fibonacci numbers
for fib_num in fib:
    print(fib_num, end=" ")
