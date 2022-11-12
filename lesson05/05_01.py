# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
#  В тексте используется разделитель пробел.

# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

import random

print()
num = int(input("Введите число слов: "))
if num <= 0:
    exit("Ошибка ввода данных")


def list_gen(num):
    return " ".join(["".join(random.sample("абв", k=3)) for _ in range(num)])


def replaсe_world(stroke, world):
    # для наглядности удаленное заменяется на *
    return stroke.replace(world, '***')


stroke = list_gen(num)
print()
print("исходная строка")
print(stroke)
stroke2 = replaсe_world(stroke, "абв")
print()
print("в строке удалено 'абв'")
print(stroke2)
