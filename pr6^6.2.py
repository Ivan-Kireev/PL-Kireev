a = []
for i in range(11):
    print('введите', i, 'элемент:')
    a.append(int(input()))
k = 0
for x in a:
    if x > 5:
        k += x
print('сумма чисел, которые больше 5: ', k)