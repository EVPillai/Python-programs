
my_dict = {'a': 1, 'b': 2, 'c': 3}

key = input("Enter key to check: ")

if key in my_dict:

    print(key, "exists with value", my_dict[key])

    new_key = input("Enter new key to replace it with: ")
    new_value = input("Enter value for new key: ")

    my_dict.pop(key)

    # Add new key-value pair
    my_dict[new_key] = new_value

else:
    print(key," does not exist in the dictionary.")

# Display updated dictionary
print("Updated dictionary:", my_dict)
