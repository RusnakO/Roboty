num_A = float(input("Введіть число A:"))
num_N = int(input("Введіть число N:"))
P= 1
for i in range(1,num_N+1):
    P=P*num_A**i
    print("Число %s в степіні %s довівнює %s" % (num_A, i, P))
print("Всі цілі степіні числа %s від 1 да %s: %s"%(num_A, num_N, P))
                    
