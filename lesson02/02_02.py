# 2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

num=int(input("Введите целое число: "))

array=[]
multilpay=1
i=1
if num>0:
    while i != num+1:
        multilpay*=i
        array.append(multilpay)
        i+=1
elif num<0:
   
    while i != num-1:
        multilpay*=i
        array.append(multilpay)
        i-=1
        i=-1 if i==0 else i
else:
    exit("число должно быть отлично от нуля")
print(array)
