import random
# comprehension for list generation
random_numb_list = [random.randint(0, 1000) for _ in range(100)]

# Cvycle for sorting. I've used Insertion algorithm for sorting from min to max
for i in range(1, len(random_numb_list)):  # Start from the second element
    key = random_numb_list[i]  # The current element to be inserted
    last_elem = i - 1  # The index of the last element
    # of the sorted part is i-1

    # Move elements of random_numb_list[0..i-1],
    # that are greater than key, to one position ahead
    while last_elem >= 0 and random_numb_list[last_elem] > key:
        # Shift element to the right
        random_numb_list[last_elem + 1] = random_numb_list[last_elem]
        last_elem = last_elem - 1
    random_numb_list[last_elem + 1] = key
# comprehension in creating a list even numbers
even_numbers = [num for num in random_numb_list if num % 2 == 0]
odd_numbers = [num for num in random_numb_list if num % 2 != 0]

print("Average result for even numbers: ", sum(even_numbers)/len(even_numbers))
print("Average result for odd numbers: ", sum(odd_numbers)/len(odd_numbers))
