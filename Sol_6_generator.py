def powers_of_two(max_exponent):
    for exponent in range(max_exponent + 1):
        yield 2 ** exponent

# Usage example
max_exp = int(input("Enter the maximum exponent: "))

# Using the generator
for power in powers_of_two(max_exp):
    print(power)
