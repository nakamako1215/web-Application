target_text = "hello"
count_dict = {}
for char in target_text:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1
        
print(count_dict)