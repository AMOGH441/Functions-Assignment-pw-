def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    # Use filter() with a lambda function to remove vowels
    no_vowels = filter(lambda char: char not in vowels, input_string)
    
    # Convert the filter object to a string
    return ''.join(no_vowels)

# Input from the user
user_input = input("Enter a string: ")

# Call the function to remove vowels and print the result
result = remove_vowels(user_input)
print("String after removing vowels:", result)
