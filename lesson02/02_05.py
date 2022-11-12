# 5. ** Реализуйте алгоритм перемешивания списка. 
# Без функции shuffle из модуля random.

# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random
num=int(input("Введите число элементов массива: "))


def rnd_array(array): # ----------------------------------------------------------------------------
    length_ar=len(array)
    for i in range(length_ar-1):
        j=random.randint(i+1,length_ar-1)
        array[i], array[j] = array[j], array[i]
# end -----------------------------------------------------------------------------------------------

array=list(range(num))
print(f"Исходный массив \n {array} \n")
rnd_array(array)
print(f"Массив со сучайными элементами \n {array}")