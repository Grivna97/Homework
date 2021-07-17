def function_for_enumerate(x):
    user_list = enumerate(x)
    user_value = dict((key, value) for key, value in user_list)
    return user_value
list_index = ['a', 'b', 'c', 'd', 'e']
print(function_for_enumerate(list_index))