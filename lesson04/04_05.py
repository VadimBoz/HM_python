# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
#  Задача - сформировать файл, содержащий сумму многочленов.

# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"

# out
# The contents of the files do not match!

def read_file(filename): # чтение строк из файл --------------------------------------------------
    data1=''
    with open(filename, "r", encoding="utf-8") as my_f:
        data=my_f.readlines()
    return data
# end ------------------------------------------------------------------------------------------------


def write_in_file(str1,str2,filename): # запись строки в файл --------------------------------------------------
    with open(filename, "a", encoding="utf-8") as my_f:
        my_f.write(str1[:-3]+str2)
    print('данные записаны в файл',filename)
# end ------------------------------------------------------------------------------------------------



data1=read_file('my_poly1.txt')
data2=read_file('my_poly2.txt')

if len(data1)!=len(data1):
    print('The contents of the files do not match!')

for i in range(len(data1)):
    write_in_file(data1[i],data2[i],'my_poly1-2.txt')

