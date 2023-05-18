a = int(input("Введіть занчення a: "))
b = int(input("Введіть занчення b: "))
c = int(input("Введіть занчення c: "))
if a>b:
    a, b=b, a
if b>c:
    b, c=c, b
if a>b:
    a, b=b, a
print("числа в порядку за незменшенням:", a, b, c)
