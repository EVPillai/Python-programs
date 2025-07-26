# Sample list of tuples
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzip into individual lists
list1, list2 = zip(*list_of_tuples)

# Convert result to list (optional)
list1 = list(list1)
list2 = list(list2)

# Print results
print("Original list of tuples:", list_of_tuples)
print("First list:", list1)
print("Second list:", list2)
