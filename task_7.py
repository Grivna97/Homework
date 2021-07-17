from datetime import datetime
def is_date(day,month,year):
    try:
        is_date = datetime(year=year,month=month,day=day)
        print(True)
        print(is_date)
    except ValueError:
        print(False)
year = int(input("Введите год: "))
month = int(input("Введите месяц: "))
day = int(input("Введите день: "))
is_date(day,month,year)