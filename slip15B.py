# User-defined function to remove characters at odd indexes
def remove(str):
    result = ""
    for i in range(len(str)):
        if not (i % 2 == 0):  # Keep only even index characters
            result += str[i]
    return result

# Take input from the user
user_input = input("Enter a string: ")

# Call the function
output = remove(user_input)

# Display result
print("String after removing odd index characters:", output)
