# Python3 code to demonstrate working of
# Vertical Concatenation in Matrix
# Using join() + list comprehension + zip_longest()
from itertools import zip_longest

# initializing lists
test_list = [["Gfg", "good"], ["is", "for"], ["Best"]]

# printing original list
print("The original list : " + str(test_list))

# using join to concaternate, zip_longest filling values using
# "fill"
res = ["".join(ele) for ele in zip_longest(*test_list, fillvalue ="")]

# printing result
print("List after column Concatenation : " + str(res))
