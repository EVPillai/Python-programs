# Sample string
text = 'tybba(ca) from B G college'

# Dictionary to count characters
d= {}

# Count each character
for char in text:
    d[char] = d.get(char, 0) + 1
print (d)
# Print only repeated characters
print("Repeated characters:")
for char, count in d.items():
    if count > 1:
        print(char,"-",count, end=', ')
