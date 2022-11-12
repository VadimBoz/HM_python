# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
#  значения которых больше предыдущего элемента. Use comprehension.

# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]


from random import randint


# Заполнение списка случайными значениями ----------------------------------------------
def list_fill(count: int):
    return [randint(0, 30) for i in range(count)]
# end -------------------------------------------------------------------------------------


def res_list(lst: list):
    return [lst[x] for x in range(1, len(lst)) if lst[x] > lst[x-1]]


lst = list_fill(int(input("Введите число элементов: ")))
print(lst)
lst2 = res_list(lst)
print(lst2)
