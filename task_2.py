temp = float(input("Введите температуру: "))
scale = str(input("Введите шкалу температуры, Цельсий, Фаренгейт, или Кельвин: "))


def temp_calculator(number, string):
    if string == "Цельсий":
        fahrenheit = number * 9 / 5 + 32
        kelvin = number + 273.15
        return (f"температура в Цельсиях {number} градусов, в Фаренгейтах {fahrenheit} градусов, в Кельвинах {kelvin} "
        f"градусов")
    elif string == "Фаренгейт":
        celsius = (string - 32) * 5/ 9
        kelvin = (number - 32) * 5/9 + 273.15
        return (f"температура в Фаренгейтах {number} градусов, в Цельсиях {celsius} градусов, в Кельвинах {kelvin} "
        f"градусов")
    elif string == "Кельвин":
        celsius = number - 273.15
        fahrenheit = number * 9/5 + 32
        return (f"температура в Кельвинах {number} градусов, в Цельсиях {celsius} градусов, в Фаренгейтах {fahrenheit} "
        f"градусов")
    else:
        return "Вы ввели неверные данные"


print(temp_calculator(temp, scale))