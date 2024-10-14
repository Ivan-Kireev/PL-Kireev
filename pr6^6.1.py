a = [4, 7, 12, 43, 863, 234, 11, 425, 21, 10]
max_elements = max(a)
m = 0
b = 0
for x in a:
    if x < max_elements:
        m += 1
for x in a:
    if x > max_elements:
        b += 1
print('максимальный элемент', max_elements)
print('колличество меньших элементов', m)
print('колличество больших элементов', b)