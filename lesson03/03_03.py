# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# Без использования встроенной функции преобразования, без строк.

# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

num = int(input("Введите число: "))


def decimal_to_binary(num):  
    if num<0:
        num=-num
        sign=-1
    else:
        sign=1

    binary_list = []
    while num:
        quotient = num % 2
        binary_list.append(quotient)
        num=num// 2
    binary_list = binary_list[::-1]
    binary=0
    for i in range(len(binary_list)):
        binary+=binary_list[-1-i]*10**i
    return binary*sign

print(decimal_to_binary(num))

