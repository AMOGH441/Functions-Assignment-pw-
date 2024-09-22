def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Prompt user for a number between 1 and 200
while True:
    number = int(input("Enter a number between 1 and 200: "))
    if 1 <= number <= 200:
        break  # Exit the loop if the number is within the valid range
    print("Invalid number! Please enter a number between 1 and 200.")

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
