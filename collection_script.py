import random
import string

# random generated dictionary
number_dictionaries = random.randint(2, 10)
random_dictionary = []
for _ in range(number_dictionaries):
    keys_num = random.randint(1, 5)
    random_dict = {
        # create a dict with random letter and random int from 0 to 100
        random.choice(string.ascii_lowercase): random.randint(1, 100)
        for _ in (range(keys_num))
    }
    random_dictionary.append(random_dict)
# creating coomon dict to have the pair values for the same key
common_dictionary = {}
for index, sub in enumerate(random_dictionary):
    for key, value in sub.items():
        if key not in common_dictionary:
            common_dictionary[key] = []
        # returns the value and index and adds to my common dicts
        common_dictionary[key].append((value, index + 1))
# Creating the result dict, where max value
# is choosen and index for choosen value
result = {}
for key, values in common_dictionary.items():
    # run if there is 2 pairs to compare near one letter
    if len(values) > 1:
        # Find the dictionary index with the max value for this key
        max_value, max_index = max(values, key=lambda x: x[0])
        # get the max value and its index
        result[f"{key}_{max_index}"] = max_value
    else:
        result[key] = values[0][0]  # for single values, just add them as it is

print('Generated dictionary:', random_dictionary)
print('Common dictionary:', result)
