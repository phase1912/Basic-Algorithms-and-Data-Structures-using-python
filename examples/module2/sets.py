﻿my_set = set([1, 2, 3, 4, 5])
print(my_set) # Output: {1, 2, 3, 4, 5}

#############

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set) # Output: {1, 2, 3, 4, 5, 6}

#########

my_set = {1, 2, 3, 4, 5}
my_set.remove(1)
print(my_set) # Output: {2, 3, 4, 5}

###########

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # Output: {4, 5}
print(set1.difference(set2)) # Output: {1, 2, 3}
print(set1.symmetric_difference(set2)) # Output: {1, 2, 3, 6, 7, 8}