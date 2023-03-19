print("Введите число N: ")
N = int(input())
stepen = 1
number = 0

while number <= N:
    number = 2**stepen

    print(2**(stepen-1))
    stepen +=1

