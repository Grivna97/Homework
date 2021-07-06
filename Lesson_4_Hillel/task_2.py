def _input_():
    my_list = []
    while True:
        _input_ = int(input("Введите число: "))
        if _input_ == 0:
            break
        my_list.append(_input_)
    return my_list
def amount_of_numbers(my_list: list) -> int:
    return len(my_list)
def sum_of_numbers(my_list):
    _sum_ = 0
    for num in my_list:
        _sum_ += num
    return _sum_
def derivative(my_list: list) -> int:
    number_ = 1
    for x in my_list:
        number_ = number_ * x
    return number_
def average(my_list) -> int:
    s = 0
    for i in my_list:
        s+=i
    return s / i
def max_number(my_list: list) -> int:
    return  max(my_list),  my_list.index(max(my_list))+1
def second_max_value(my_list: list) -> int:
    my_list_1 = my_list.copy()
    max_value = max(my_list_1)
    my_list_1.pop(my_list_1.index(max_value))
    return max(set(my_list_1))
def even_number(my_list: list) -> int:
    index = 0
    for my_list_2 in my_list:
        if my_list_2 % 2 == 0:
            index +=1
    return index, len(my_list) - index
def number_of_coincidences(my_list: list) -> int:
    my_number = 0
    for maximum in my_list:
        if maximum == max(my_list):
            my_number+=1
    return my_number
def main():
    my_list = _input_()
    function_to_call = {"Количетсво чисел: " : amount_of_numbers,
                        "Сумма чисел: ": sum_of_numbers,
                        "Среднее арифметическое чисел: ": average,
                        "Производная: ": derivative,
                        "Максимальное число и его порядковый номер соответственно: ": max_number,
                        "Второе по величине число": second_max_value,
                        "Количество чётных и нечётных чисел соответственно: ": even_number,
                        "Количество максимальных чисел: ": number_of_coincidences}
    for key, func in function_to_call.items():
        print(key, func(my_list))
main()