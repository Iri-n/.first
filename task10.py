print('Ведедите число монет: ')
n = int(input())
orel = 0
reshka = 0
print('Введите номинал в виде 0 - орел и 1 - решка', n, 'монет')
mon = [0] * n
# mon = [] 

for i in range(n):
    mon[i] = int(input())
    if mon[i] == 1:
        orel +=1
    else:
        reshka +=1

print('Минимальное число монет, которые нужно перевернуть: ')        
if orel < reshka:
    print(orel)
else:
    print(reshka)

    
