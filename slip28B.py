# Accept input for two lists'

list1 = input("Enter elements of first list separated by space: ").split()
list2 = input("Enter elements of second list separated by space: ").split()
t=tuple(list1+list2)
print(t)
'''
# Convert elements to integers (optional, remove if you want strings)
list1 = [int(i) for i in list1]
list2 = [int(i) for i in list2]

# Merge into list of tuples
merged_list = list(zip(list1, list2))

# Display result
print("List of tuples:", merged_list)
'''
