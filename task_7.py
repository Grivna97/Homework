from datetime import datetime
try:
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    day = int(input("Введите день: "))
    is_date = datetime(year=year,month=month,day=day)
    print(True)
    print(is_date)
except ValueError:
    print(False)