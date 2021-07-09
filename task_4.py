my_list = [1,4,6,8,6,47,17,89,56,33,56,35,36,58,13]
new_list = []
for element in my_list:
    if element % 2 == 0:
        new_list.append(element)
    else:
        new_list.append(0)
print(new_list)