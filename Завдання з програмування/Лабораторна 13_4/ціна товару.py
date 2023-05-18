def cost(x, y):
    return x * 100 + y

a = int(input("Введіть ціну першого товару (грн.): "))
b = int(input("Введіть ціну першого товару (коп.): "))
c = int(input("Введіть ціну другого товару (грн.): "))
d = int(input("Введіть ціну другого товару (коп.): "))

grn1 = cost(a, b)
grn2 = cost(c, d)

total_cost = grn1 + grn2

print(f"Ціна двох товарів: {total_cost // 100} грн. {total_cost % 100} коп")
