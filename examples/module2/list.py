my_list = [1, 2, 3, 4, 5]
print(my_list) # Output: [1, 2, 3, 4, 5]

##########

my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list) # Output: [1, 2, 3, 4, 5, 6]

###########

my_list = [1, 2, 3, 5]
my_list.insert(3, 4) # Insert number 4 at position 3
print(my_list) # Output: [1, 2, 3, 4, 5]

##############

my_list = [1, 2, 3, 4, 5]
my_list.remove(3) # Removes number 3 from the list
print(my_list) # Output: [1, 2, 4, 5]

##########

my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()
print(my_list) # Output: [1, 1, 2, 3, 4, 5, 9]