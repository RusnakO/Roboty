t = float(input("Введіть масу тіла: "))
tr = float(input("Введіть початкову температуру тіла: "))
t2 = float(input("Введіть кінцеву температуру тіла: "))
c = float(input("Введіть питому теплоємність речовини: "))
Q = c * t * (tr - t2)
print("Кількість теплоти, яка потрібна для нагрівання тіла: ", Q)
