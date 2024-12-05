#второй по величине
def f(max1=0, max2=0):
    n = int(input("Введите число по одному (0 для окончания): "))
    if n == 0:
        return max2
    if n > max1:
        return f(n, max1)
    elif n > max2:
        return f(max1, n)
    else:
        return f(max1, max2)
print(f())
