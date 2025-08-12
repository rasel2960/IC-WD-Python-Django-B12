# Basic Dictionary Merging
dict1 = {'a': 1, 'b':2, 'c':3}
dict2 = {'d': 4, 'e': 5}
merged_dict = {**dict1, **dict2}
merged_dict2 = {**dict2, **dict1}
print(merged_dict)
print(merged_dict2)

