tuples_list = [(1, 3), (4, 1), (5, 2), (2, 4)]

# Sort the list using a lambda function, which accesses the second element (index 1)
sorted_list = sorted(tuples_list, key=lambda x: x[1])

print("Sorted list based on the second element:", sorted_list)