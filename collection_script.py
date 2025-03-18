import random
import string

# random generated dictionary
dicts_number = random.randint(2, 10)
dicts_list = []
for _ in range(dicts_number):
    keys_num = random.randint(1, 5)
    random_dict = {
        # create a dict with random letter and random int from 0 to 100
        random.choice(string.ascii_lowercase): random.randint(1, 100)
        for _ in (range(keys_num))
    }
    dicts_list.append(random_dict)
# creating coomon dict to have the pair values for the same key
common_dict = {}
for index, sub in enumerate(dicts_list):
    # Each key and value in dictionary
    for key, value in sub.items():
        if key not in common_dict:
            common_dict[key] = []
        # returns the value and index and adds to my common dicts
        common_dict[key].append((value, index + 1))
# Creating the result dict, where max value
# is choosen and index for choosen value
result = {}
for key, values in common_dict.items():
    # run if there is 2 pairs to compare near one letter
    if len(values) > 1:
        # Find the dictionary index with the max value for this key
        max_value, max_index = max(values, key=lambda x: x[0])
        # get the max value and its index
        result[f"{key}_{max_index}"] = max_value
    else:
        result[key] = values[0][0]  # for single values, just add them as it is

print('Generated dictionary:', dicts_list)
print('Common dictionary:', result)
