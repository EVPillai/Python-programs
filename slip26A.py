# Lambda function to find area of square: side * side
square_area = lambda side: side * side

# Lambda function to find area of rectangle: length * breadth
rectangle_area = lambda length, breadth: length * breadth

# Get user input
side = int(input("Enter side of square: "))
length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))

# Calculate areas
print("Area of square:", square_area(side))
print("Area of rectangle:", rectangle_area(length, breadth))
