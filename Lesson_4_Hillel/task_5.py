def my_function(join_for_task):
    return "".join([str(i) for i in join_for_task])
my_string = ['ABCDEFGHIJKLMN']
result = my_function(my_string)
print("a:",result[2])  # Вывести третий символ строки
print("b:",result[-2:-1]) # Вывести предпоследний список строки
print("c:",result[:5]) # Вывести первых 5 элементов строки
print("d:",result[:-2]) # Вывести все элементы строки, кроме последних 2-х
print("e:", result[0::2]) # Вывести все символы с чётными индексами
print("f:", result[1::2]) # Вывести все символы с нечётными индексами
print("g:",result[::-1]) # Вывести элементы строки реверсивно
print("h:", result[-1::-2]) # Вывести элементы строки реверсивно через одну
print("i:", len(result)) # Вывести длину строки