x = int(input('введите номер месяца '))
if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
    print('в этом месяце 31 день')
elif x == 2:
    print('в этом месяце 28 дней или 29 дней раз в 4 года')
else:
    print('в этом месяце 30 дней')