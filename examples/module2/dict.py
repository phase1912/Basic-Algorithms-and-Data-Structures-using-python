my_dict = {'name': 'John', 'age': 25}
print(my_dict) # Output: {'name': 'John', 'age': 25}

############

my_dict = {'name': 'John', 'age': 25}
print(my_dict['name']) # Output: John

##############

my_dict = {'name': 'John', 'age': 25}
my_dict['age'] = 26
print(my_dict) # Output: {'name': 'John', 'age': 26}

############

my_dict = {'name': 'John', 'age': 25}
my_dict['city'] = 'New York'
print(my_dict) # Output: {'name': 'John', 'age': 25, 'city': 'New York'}

########

my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
del my_dict['city']
print(my_dict) # Output: {'name': 'John', 'age': 25}