def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # strip() removes any leading/trailing whitespace or newline characters

# Usage example
file_path = input("Enter the file path: ")

# Using the generator to read the file
for line in read_file_line_by_line(file_path):
    print(line)
