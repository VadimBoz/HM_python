# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.

# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

import random
count = int(input("Введите количество элементов массива: "))
if count < 2:
    exit("Error, введено некоректное значение")


def list_fill(count):  # Заполнение списка случайными значениями ------------------------------------
    array = [0]*count
    for i in range(count):
        array[i] = round(random.uniform(0, 10), 2)
    return array
# end ------------------------------------------------------------------------------------------------


# нахождение максимальной разницы дробных частей элементов массива --------
def max_differense(array):
    list_fraction = list(map(lambda num: round(num-int(num), 2), array))
    max, min = 0, 1
    for i in range(len(list_fraction)):
        if list_fraction[i] > max:
            max = list_fraction[i]
        if list_fraction[i] < min:
            min = list_fraction[i]
    res = round(max-min, 2)
    return res
# end ------------------------------------------------------------------------------------------------


array = list_fill(count)
print(array)
print(max_differense(array))
