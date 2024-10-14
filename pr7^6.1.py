a = int(input())
b = int(input())
def nod(a, b):
    while b:
        a, b = b, a % b
    return a
s = nod(a,b)
def nok(a,b):
    return (a*b)//s
d = nok(a,b)
s = nod(a,b)
print(s, d)