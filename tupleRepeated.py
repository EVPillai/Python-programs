my_tuple = (1, 2, 2, 4, 2, 3, 5, 6, 3, 1)

# Empty dictionary to count items
count_dict = {}

# Count each item
for item in sample_tuple:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

# Print only repeated items
print("Repeated items:")
for key, value in count_dict.items():
    if value > 1:
        print(key," appears",value," times")

