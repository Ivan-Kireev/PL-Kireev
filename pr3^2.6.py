a= int(input('введите а'))
b = int(input('введите b'))
x = 0
if a<b and b>4:
    x = a+b
elif a>b:
    x = a-b
else:
    x = a**2
print(x)