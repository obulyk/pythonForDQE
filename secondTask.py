from collections import defaultdict
import random
import string
# empty list
# random number from 2 to 10
randomNumberOfList = random.randint(2, 10)
#cycle from 0 to random number
dictionary = []
my_list = []
for i in range(randomNumberOfList):
# crate a dictionary with random letter and random int from 0 to 100
    dictionary = {random.choice(string.ascii_lowercase): random.randint(0, 100),
                  random.choice(string.ascii_lowercase): random.randint(0, 100),
                  random.choice(string.ascii_lowercase): random.randint(0, 100)}
    my_list.append(dictionary)
# maybe I will need that list in a future
commonDictionary = {}
# defaultdict used to make default empty list
res = defaultdict(list)
#each dictionary {} in List
for sub in my_list:
# Each key in dictionary
    for key in sub:
# result with key(for ex: q) add key from dictionary {'l': 50, 'e': 84, 'y': 98}
        res[key].append(sub[key])
#returns the value of the associated key
        res.get(key)
# printing result
for key, value in res.items():
    if len(value) > 1:
        commonDictionary.update({key + str('_') + str(value.index(max(value)) + 1): max(value)})
    else:
        commonDictionary.update({key: max(value)})

# common dict output
print('Common dictionary:', commonDictionary)