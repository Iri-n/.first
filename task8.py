
print("Введите размер шоколада и количество кусочков: ")
m = int(input())
n = int(input())
k = int(input())

if (k % m == 0) or (k % n == 0):
    print("Yes")
else:
    print("No") 
