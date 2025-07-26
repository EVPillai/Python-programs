class StringRepeater:
    def __init__(self, text):
        self.text = text

    # Overload * operator
    def __mul__(self, n):
        return self.text * n

# Accept input from user
user_string = input("Enter a string: ")
n = int(input("Enter number of repetitions: "))

# Create object
obj = StringRepeater(user_string)

# Use overloaded * operator
result = obj * n

# Display result
print("Repeated string:", result)
