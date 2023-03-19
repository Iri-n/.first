
print('Введите 2 числа: ')

summa = int(input())
proizv = int(input())

for i in range(1000):
    for j in range(1000):
        if (i + j == summa) and (i * j == proizv):
            print(i, j)
            
             