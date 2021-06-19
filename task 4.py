year = int(input('введите год:'))
if year % 400==0 and year% 100!=0 and year%4==0:
    print('Yes')
else:
    print('No')