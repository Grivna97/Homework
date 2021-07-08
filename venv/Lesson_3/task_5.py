import random
n = random.randint(0,10)
chance = 1
print("Отгадайте число")
while chance <= 3:
    u = int(input(str(chance) + '-я попытка: '))
    if u > n or u<n:
        print('You lose!')
    else:
        print('You won!')
        break
    chance += 1
else:
    print('Вы исчерпали 3 попытки')
