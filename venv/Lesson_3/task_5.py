import random
print("Попытка №1")
chance_1 = int(input("введите число от 0 до 10: "))
chance_2 = random.randint(0,10)
print(chance_1)
print(chance_2)
if chance_1 == chance_2:
    print("You won!")
else:
    print("You lose!")

print("Попытка №2")
chance_3 = int(input("введите число от 0 до 10: "))
chance_4 = random.randint(0,10)
print(chance_3)
print(chance_4)
if chance_3 == chance_4:
    print("You won!")
else:
    print("You lose!")
print("Попытка №3")
chance_5 = int(input("введите число от 0 до 10: "))
chance_6 = random.randint(0,10)
print(chance_5)
print(chance_6)
if chance_5 == chance_6:
    print("You won!")
else:
    print("You lose!")