def our_nums(number):
    if number ==1 and number ==0:
        return False
    elif number %2 ==0 and number!=2:
        return False
    for element in range(3,number):
        if number % element == 0:
            return False
    return True
element = int(input("Введите число от 1 до 1000: "))
print(our_nums(element))