my_dict = {'banana': 3, 'apple': 5, 'cherry': 1, 'date': 4}

# 🔹 Sort by KEY (Ascending)
sorted_by_key_asc = dict(sorted(my_dict.items()))
print("Sorted by key (ascending):", sorted_by_key_asc)

# 🔹 Sort by KEY (Descending)
sorted_by_key_desc = dict(sorted(my_dict.items(), reverse=True))
print("Sorted by key (descending):", sorted_by_key_desc)

# 🔹 Sort by VALUE (Ascending)
sorted_by_value_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted by value (ascending):", sorted_by_value_asc)

# 🔹 Sort by VALUE (Descending)
sorted_by_value_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Sorted by value (descending):", sorted_by_value_desc)
