import math
def figure(tip):
    if tip == "треугольник":
        a = float(input("Введите сторону а: "))
        b = float(input("Введите сторону b: "))
        c   = float(input("Введите сторону c: "))
        p=(a+b+c)/2
        s = math.sqrt((p*(p-a)*(p-b)*(p-c)))
        print("Площадь треугольника равна: ",s)
    elif tip == "квадрат":
        a = int(input("Введите сторону квадрата: "))
        s = a**2
        print("Площадь квадрата равна: ",s)
    else:
        print("Программа рассчитывает только площадь квадрата, либо треугольника")
tip = str(input("Введите название фигуры: "))
figure(tip)