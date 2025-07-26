def is_prime(num):
    for i in range(2, int(num)):
        if num % i == 0:
            return False
    return True

# Function to find factorial
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Get input from user
number = int(input("Enter a number: "))

# Prime check
if is_prime(number):
    print(f"{number} is a Prime Number.")
else:
    print(f"{number} is NOT a Prime Number.")

# Factorial calculation
fact = factorial(number)
print(f"Factorial of {number} is: {fact}")
