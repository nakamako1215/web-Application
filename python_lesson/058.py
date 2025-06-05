target_list = [1, 2, 3, None, 5, None, 7]
filtered_list = [str(item) for item in target_list if item is not None]
result = '&'.join(filtered_list)
print(result)