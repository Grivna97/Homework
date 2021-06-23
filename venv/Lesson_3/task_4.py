list_of_six = []
for elements in range(100, 200, 6):
    list_of_six.append(elements)
print("list_of_six = ",list_of_six)
for elements_2 in list_of_six:
    if elements_2 % 5 ==0 and elements_2 < 150:
        print(elements_2)