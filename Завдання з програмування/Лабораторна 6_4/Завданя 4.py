num = int(input())
p = 1
while num > 0:
    d = num % 10
    num = num // 10
    p *= d

print(p)
