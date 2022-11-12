# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#  https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/

# in
# - 3
# - 6
# - 2
# - 1

# out
# 5.099

x1 = float(input("введите координату 'х' первой точки: "))
y1 = float(input("введите координату 'y' первой точки: "))
x2 = float(input("введите координату 'х' второй точки: "))
y2 = float(input("введите координату 'y' второй точки: "))

def distanse(x1, y1, x2, y2):
    dist = ((x2-x1)**2+(y2-y1)**2)**0.5
    return dist

dist = round(distanse(x1, y1, x2, y2), 3)
print(f"Растояние между точками ({x1}, {y1})  ({x2}, {y2}) -  {dist}")
