
# Given tuples
t1 = (1, 2, 3, 4)
t2 = (3, 5, 2, 1)
t3 = (2, 2, 3, 1)

# Empty list to store result
result = []

# Loop through index positions
for i in range(len(t1)):
    sum_value = t1[i] + t2[i] + t3[i]
    result.append(sum_value)

# Convert list to tuple
result_tuple = tuple(result)

# Print result
print("Element-wise sum of the said tuples:", result_tuple)



# Use zip() to add corresponding elements
#result = tuple(a + b + c for a, b, c in zip(t1, t2, t3))
