n = int(input("Enter a number: "))

# Create dictionary
d = {}
for x in range(1, n + 1):
    d[x] = x * x

# Print the dictionary
print("Generated Dictionary:", d)
