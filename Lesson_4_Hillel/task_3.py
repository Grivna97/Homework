num_1 = (int(input("Введите цифру A: ")))
num_2 = (int(input("Введите цифру В: ")))

if num_1 < num_2:
    print(list(range(num_1,num_2+1)))
elif num_1 > num_2:
    print(list(range(num_1,num_2-1, -1)))
else:
    print(0)