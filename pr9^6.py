#простое число
import math
n = int(input())
def f(n, x=2):
    if n % x == 0:
        return "NO"
    if x > math.sqrt(n) :
        return "YES"
    return f(n, x+1)
print(f(n))
