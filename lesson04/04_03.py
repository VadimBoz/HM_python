# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1
# out
# Negative value of the number of numbers!
# []

# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


lst=[4, 4, 5, 5, 6, 2, 3, 0, 9, 4]

import random

count= int(input("Введите количество элементов массива: "))
if count<0:
    exit("Error, введено некоректное значение")



def list_fill(count):  # Заполнение списка случайными значениями ------------------------------------
    array=[0]*count
    for i in range(count):
        array[i]=random.randint(0,10)
    return array
#end ------------------------------------------------------------------------------------------------


def del_dubl(lst): # удаление дублей в списке ----------------------------------------------------------

    lst_temp=[]
    for i in range(0, len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i]==lst[j]:
                lst_temp.append(lst[i]) # создаем список дублей

    for i in range(len(lst_temp)):             
        while lst_temp[i] in lst:
            lst.remove(lst_temp[i])
    return lst
#end ------------------------------------------------------------------------------------------------


lst= list_fill(count)
print(lst)

lst = del_dubl(lst)
print(lst)