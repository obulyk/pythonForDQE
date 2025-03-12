from collections import defaultdict
import random
import string

# random number from 2 to 10
randomNumberOfList = random.randint(2, 10)
dict = []
my_list = []
# create a dict with random letter and random int from 0 to 100
for i in range(randomNumberOfList):
    dict = {random.choice(string.ascii_lowercase): random.randint(0, 100),
            random.choice(string.ascii_lowercase): random.randint(0, 100),
            random.choice(string.ascii_lowercase): random.randint(0, 100)}
    my_list.append(dict)
# I will need that dictionary in a future
commonDictionary = {}
# defaultdict used to make default empty list
res = defaultdict(list)
# each dictionary {} in List
for sub in my_list:
    # Each key in dictionary
    for key in sub:
        res[key].append(sub[key])
        # returns the value of the associated key
        res.get(key)
# printing result
for key, value in res.items():
    if len(value) > 1:
        commonDictionary.update({key + str('_') +
                                 str(value.index(max(value)) + 1): max(value)})
    else:
        commonDictionary.update({key: max(value)})

# common dict output
print('Common dictionary:', commonDictionary)
