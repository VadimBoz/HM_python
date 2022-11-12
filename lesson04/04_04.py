# 4.* Задана натуральная степень k. Сформировать случайным образом список
#  коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.

# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0


import random

k1 = int(input("Введите степень 1 многочлена: "))
k2 = int(input("Введите степень 2 многочлена: "))
k3 = int(input("Введите степень 3 многочлена: "))


if k1 < 0 or k2 < 0 or k3 < 0:
    exit("Error, введено некоректное значение")


def list_fill(count):  # Заполнение списка коэфициентов случайными значениями ------------------------------------
    array = [0]*(count+1)
    for i in range(count+1):
        array[i] = random.randint(-10, 10)
    return array
# end ------------------------------------------------------------------------------------------------


def polynom(k, array): # фомирование полинома--------------------------------------------------------
    res_str = ""
    for i in range(len(array)-1):
        temp = array[i]
        mlt = k-i
        
        if temp >= 0:
            sign = '+'
        else:
            sign = '-'
            temp = -temp
        if temp == 0:
            continue
        if temp==1:
            temp=''
        res_str += sign + str(temp) + "x^" + str(mlt)

    temp=array[k]
    if temp==0:
        return res_str
    if temp > 0:
         sign = '+'
    else:
        sign = '-'
        temp = -temp

    res_str +=sign+str(temp)
    return res_str+'=0'
# end ------------------------------------------------------------------------------------------------



def write_in_file(str,filename): # запись строки в файл --------------------------------------------------
    with open(filename, "a", encoding="utf-8") as my_f:
            my_f.write(f'{str}\n')
    print('данные записаны в файл',filename)
# end ------------------------------------------------------------------------------------------------


array1 = list_fill(k1)
print(array1)
str1 = polynom(k1, array1)
print(str1)


array2 = list_fill(k2)
print(array2)
str2 = polynom(k2, array2)
print(str2)

array3 = list_fill(k3)
print(array3)
str3 = polynom(k3, array3)
print(str3)


write_in_file(str1,"my_poly1.txt")
write_in_file(str2,"my_poly1.txt")
write_in_file(str3,"my_poly1.txt")

