A = []
i=0
while i<10:
    x = float(input("x = "))
    A = A+[x]
    i=i+1
print("Вихідний список")
print("A = ",A)

print("Зманшення списку А на 3 елемента")
i=0
while i<3:
    n = len(A)
    del A[n-1]
    i=i+1
print("A = ",A)
print("Зменшення списку ще на 3 останны елементи")
del A[n-3:n-1]
print("A = ",A)
