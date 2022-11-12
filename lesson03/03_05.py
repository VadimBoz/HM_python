# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

num = int(input("Введите число членов ряда Фибоначчи: "))
if num<1:
    exit("Некоректное число")

def fibonachi(num):
    res1 = [0, 1]
    res2 = [0, 1]
    for i in range(2, num+1):
        res1.append(res1[-2]+res1[-1])
        res2.append(res2[i-2]-res2[i-1])
    res = res2[:1:-1]+[1]+res1
    return res

print(fibonachi(num))

