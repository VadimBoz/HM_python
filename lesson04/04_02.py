# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# Простые делители числа

# in 54
# out
# [2, 3, 3, 3]

# in  9990
# out
# [2, 3, 3, 3, 5, 37]

# in  650
# out
# [2, 5, 5, 13]

num = int(input("введите натуральное число: "))


def factor(n):
    res = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            res.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        res.append(n)
    return res

print(factor(num))
