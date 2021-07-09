user_dict = {'first_color': None, 'second_color': 'Green', 'third_color': None, "fourth color": "Blue"}
empty = [k for k, v in user_dict.items() if not v]
for k in empty:
    del user_dict[k]
print(user_dict)