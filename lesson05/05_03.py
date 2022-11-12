# Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.

from random import choice

print("\n" * 100)

print("Игра в крестики нолики")
print()
name1 = input("Введите имя первого игрока: ")
if name1 == "":
    exit("неверное имя")
name2 = input("Введите имя второго игрока: ")
if name2 == "":
    exit("неверное имя")


# игровое поле -----------------------------
def print_squre(items=[str(i)+'.' for i in range(1, 10)]):

    print("-"*33)
    print("|", "  ", items[0], "  ", "|", "  ",
          items[1], "  ", "|", "  ", items[2], "  ", "|")
    print("-"*33)
    print("|", "  ", items[3], "  ", "|", "  ",
          items[4], "  ", "|", "  ", items[5], "  ", "|")
    print("-"*33)
    print("|", "  ", items[6], "  ", "|", "  ",
          items[7], "  ", "|", "  ", items[8], "  ", "|")
    print("-"*33)
# end -----------------------------------------------------------------------------------------------


def check_win(items):  # проверка есть ли победитель  -------------------------------------------------
    for i in range(3):
        if items[i*3] == items[i*3+1] == items[i*3+2]:
            return True
        if items[i] == items[i+3] == items[i+6]:
            return True
    if items[0] == items[4] == items[8]:
        return True
    if items[2] == items[4] == items[6]:
        return True
    return False
# end -----------------------------------------------------------------------------------------------


# проверка на ничью -----------------------------------------------
def check_no_win(items, n1, n2):
    count = 0
    for i in range(9):
        if items[i] == n1 or items[i] == n2:
            count += 1
    return count
 # end -----------------------------------------------------------------------------------------------


gamers = [name1, name2]
first_gamer = choice(gamers)
print("право первого хода выпадает игроку:", first_gamer)
second_gamer = name1 if first_gamer == name2 else name2

n1 = '\U0001F353'
n2 = '\U0001F352'

items = [str(i)+'.' for i in range(1, 10)]
print_squre(items)
while True:
    st1 = int(input(f"{first_gamer} \U0001F353 введите число: "))
    while items[st1-1] == n1 or items[st1-1] == n2:
        st1 = int(input("Поле занято, введте другой номер: "))
    items[st1-1] = n1
    print()
    print_squre(items)
    if check_win(items):
        exit(f"Победил {first_gamer} \U0001F353")
    if check_no_win(items, n1, n2) == 9:
        exit("!!!!!!!!!!!!!НИЧЬЯ !!!!!!!!!!!!")

    st2 = int(input(f"{second_gamer}  \U0001F352 введите число: "))
    while items[st2-1] == n1 or items[st2-1] == n2:
        st2 = int(input("Поле занято, введте другой номер: "))
    items[st2-1] = n2
    print()
    print_squre(items)
    if check_win(items):
        exit(f"Победил {second_gamer} \U0001F352")
    if check_no_win(items, n1, n2) == 9:
        exit("!!!!!!!!!!!НИЧЬЯ !!!!!!!!!!!!")
