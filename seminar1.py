# n = 700
# m = 750
# s = 0



# if m > n: s = 1
# s = m//n + s

# k = (n + m/2)/m


# print(s)
# print(int(k))



# a, b, c = int(input()), int(input()), int(input())
# result = (a + a % 2 + b + b % 2 + c + c % 2) // 2
# print(result)

year = int(input('Введите пожалуйста год:'))

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('yes')
else:
    print('no')    
    