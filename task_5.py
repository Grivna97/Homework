def square(a):
    p = 4 * a
    s = a * a
    d = (a ** 2) / 2
    d = d ** 0.5
    k = tuple(("Периметр квадрата равен ",p,"Площадь квадрата равна " , s , "Диагональ квадрата равна" ,d))
    return k
print(square(8))