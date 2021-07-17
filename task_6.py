user_dict = {'first_color': None, 'second_color': 'Green', 'third_color': None, "fourth color": "Blue"}
def value_for_dict(user_dict):
    empty = {k:v for k, v in user_dict.items() if v is not None}
    return empty
print(value_for_dict(user_dict))