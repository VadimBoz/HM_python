# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

import random


count= int(input("Введите количество элементов массива: "))
if count<0:
    exit("Error, введено некоректное значение")


def list_fill(count):  # Заполнение списка случайными значениями ------------------------------------
    array=[0]*count
    for i in range(count):
        array[i]=random.randrange(1,11) 
    return array
#end ------------------------------------------------------------------------------------------------


def multiplay_elements(array): # Произведение пар элементов массива -----------------------------------
    m_array=[]
    len_ar=len(array)
    for i in range(len_ar//2):
        res=array[i]*array[-1-i]
        m_array.append(res)
    if len_ar%2!=0:
        m_array.append(array[len_ar//2])
    return m_array
#end ------------------------------------------------------------------------------------------------


array=list_fill(count)
print(array)
print(multiplay_elements(array))