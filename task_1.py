def user_string(func):
    def user_string_1(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.split()
    return user_string_1


@user_string
def user_input():
    user_input_1 = input("Пожалуйста, введите строку :")
    return user_input_1
print(user_input())