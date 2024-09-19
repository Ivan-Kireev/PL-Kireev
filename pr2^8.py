import math
x = -2.235*10**-2
y = 2.23
z = 15.221
#s = math.sqrt(10*(math.pow(x, (1/3)) + x**(y+2))) * ((math.asin(z))**2 - abs(x-y))
s = ((math.exp(abs(x-y)) * ((abs(x-y))**(x+y)))/(math.atan(x) + math.atan(z))) + math.pow((x**6 + (math.log10(y))**2), (1/3))
print(s)
