"""
Given two lists, use the standard deviation function from numpy to determine
which language has the largest standard deviation. Usage will be np.std()
https://numpy.org/doc/stable/reference/generated/numpy.std.html
"""

"""
Dr. Forsyth's Code. Do Not Modify.
"""
# bring in randomness because we need it in our lives
import random
import numpy as np

# randomly sample a distribution between 20 and 100
random_length = int(random.uniform(20, 100))

# generate a random list of random length containing values up to 100
random_list_A = random.sample(range(100), random_length)

# generate a random list of random length containing values up to 100
random_list_B = random.sample(range(100), random_length)

# use the std() method from numpy to determine which list has the largest standard deviation

### YOUR CODE HERE

# set this variable equal to the list with the largest standard deviation

L1 = np.std(random_list_A)

L2 = np.std(random_list_B)


if L1 > L2 :
    print("List A has the highest standard Deviationt")
    highest_stedv = L1
elif L1 == L2:
    print("Both lists have the same standard deviation")
else:
    print("List B has the highest standard Deviation")
    highest_stdev = L2


# do not modify this variable's name, you can/should adjust the contents ;)
# e.g. longest_list_is = myList
if len(random_list_A) > len(random_list_B):
    longest_length = L1
elif len(random_list_A) < len(random_list_B):
    longest_length = L2
else:
    longest_length = 0

longest_list_is = longest_length
print(longest_list_is)

### YOUR CODE HERE
