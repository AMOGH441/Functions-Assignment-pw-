tuples_list = [(10, 5), (3, 2), (7, 8), (6, 1)]

# Sort the list using a lambda function, which accesses the second element (index 1)
sorted_list = sorted(tuples_list, key=lambda x: x[1])

print("Sorted list based on the second element:", sorted_list)