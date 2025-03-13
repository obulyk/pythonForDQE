# import bibliothek random
import random
# create empty List
rand_list_100 = []
# cycle for that creates 0 to 100 cells
for i in range(0, 100):
    # numb assign random numb in diapason from0 to 1000
    numb = random.randint(0, 1000)
    # append function adds created random numb to our list
    rand_list_100.append(numb)

srt_min_2_max = []
while rand_list_100:
    # first numb is lowest
    min = rand_list_100[0]
    # cycle for x=1 to rand_list_1000
    for x in rand_list_100:
        # if x=1 is lower than the first numb of random numb
        if x < min:
            # min is set to X
            min = x
    # add that lower numb as first numb to new List
    srt_min_2_max.append(min)
    # remove that numb from list
    rand_list_100.remove(min)
# empty list for even numbs
e_numb = []
# empty list for odd numbs
o_numb = []
for e in srt_min_2_max:
    # if a numb is divided on 2 without any decimal numbs
    if (e % 2) == 0:
        # Add to empty list with that even numbs
        e_numb.append(e)
    # another case: not even
    else:
        # add that numb to odd list
        o_numb.append(e)
print("Average sequence fer even numbs: "
      + str(sum(e_numb) / len(e_numb)))
print("Average sequence fer not even numbs: "
      + str(sum(o_numb) / len(o_numb)))
