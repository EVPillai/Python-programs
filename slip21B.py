# Original tuple
original_tuple = (('333', '33'), ('1416', '55'))

# Initialize empty list to store converted values
new_tuple = []

# Outer loop to go through each sub-tuple
for sub in original_tuple:
    inner_list = []
    # Inner loop to convert each string to int
    for item in sub:
        inner_list.append(int(item))
    # Convert inner list to tuple and append to result
    new_tuple.append(tuple(inner_list))

# Convert the outer list to tuple
converted_tuple = tuple(new_tuple)

# Print the result
print("Original tuple values:", original_tuple)
print("New tuple values:", converted_tuple)
