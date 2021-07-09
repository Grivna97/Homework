user_input = str(input("Напишите любые слова: "))
symbol = len(user_input)
symbol_2 = (len(user_input) - user_input.count(' '))
words = (user_input.count(' ') + 1)

print("Колличество символов: ", symbol_2)
print("Колличество слов: ", words)