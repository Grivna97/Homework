num = int(input("Введите число"))
for num_2 in range(1, num+1):
    for num_3 in range(1,num_2+1):
        print(num_3, sep='', end='')
    print()