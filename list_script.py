# import bibliothek random
import random

# create empty List
randomList100 = []
# cycle for that creates 0 to 100 cells
for i in range(0, 100):
    # number assign random number in diapason from0 to 1000
    number = random.randint(0, 1000)
    # append function adds created random number to our list
    randomList100.append(number)

sortedListMinToMax = []
while randomList100:
    # first number is lowest
    minimum = randomList100[0]
    # cycle for x=1 to randomList1000
    for x in randomList100:
        # if x=1 is lower than the first number of random number
        if x < minimum:
            # minimum is set to X
            minimum = x
    # add that lower number as first number to new List
    sortedListMinToMax.append(minimum)
    # remove that number from list
    randomList100.remove(minimum)
# empty list for even Numbers
evenNumbers = []
# empty list for odd Numbers
oddNumbers = []
# Cycle for
for e in sortedListMinToMax:
    # if a number is divided on 2 without any decimal numbers
    if (e % 2) == 0:
        # Add to empty list with that even Numbers
        evenNumbers.append(e)
    # another case: not even
    else:
        # add that number to odd list
        oddNumbers.append(e)
    # case when we have 0, which is not even and not add
sumaEvenNumbers = sum(evenNumbers)
countEvenNumbers = len(evenNumbers)
print("Average sequence fer even numbers: "
      + str(sumaEvenNumbers / countEvenNumbers))
sumaOddNumber = sum(oddNumbers)
countOddNumbers = len(oddNumbers)
# print the result
print("Average sequence fer not even numbers: "
      + str(sumaOddNumber / countOddNumbers))
