# * 4. Напишите программу, которая принимает на вход 2 числа. 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях(не индексах).

# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15
Num=int(input("Введите число элементов: "))
num1=int(input("Первый индекс: "))
num2=int(input("Второй индекс: "))


def gen_list(Num):
    ar=list(range(-Num,Num+1))
    return ar

def multiplay_elenents(num1,num2,ar):
    multiplay=ar[num1-1]*ar[num2-1]
    return multiplay


ar=gen_list(Num)
print(ar)
len_ar=len(ar)
if num1==0 or num1>len_ar or num2==0 or num2> len_ar:
    print(f"Error! Индексы выходят за диапазон - [1, {len_ar}]")
elif num1==num2:
    print("Error! Введите отличающиеся индексы")
else:
    multiplay=multiplay_elenents(num1,num2,ar)
    print(f"Произведение элементов  - {multiplay}")

