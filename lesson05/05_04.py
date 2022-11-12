# 4. ** Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?


#     Добавьте игру против бота
#     Подумайте как наделить бота "интеллектом"

from random import choice
from time import sleep

print("\n" * 100)

print("Игра в конфеты")


# проверяем выигрышь ---------------------------------------------
def check_win(count_candy, next_gamer):
    if count_candy <= 28:
        exit(f"выиграл игрок!!!!!!       {next_gamer}")
 # end --------------------------------------------------------------------------------------


def game_2x2(name1, name2, start_count_candy):  # игра человека с человеком

    gamers = [name1, name2]
    first_gamer = choice(gamers)
    print()
    print("определяем первого игрока.......")
    sleep(2)
    print("Право первого хода выпадает игроку:", first_gamer)
    second_gamer = name1 if first_gamer == name2 else name2
    count_candy = start_count_candy
    while True:
        print()
        print("Колличество конфет на кону: ", count_candy)

        while True:
            st1 = int(
                input(f"{first_gamer}, введите количество конфет (не более 28): "))
            if st1 <= 28 and st1 > 0:
                count_candy -= st1
                break
            else:
                print("введите число более 0 и менее 29")
        check_win(count_candy, second_gamer)
        print()
        print("Колличество конфет на кону: ", count_candy)

        while True:
            st1 = int(
                input(f"{second_gamer}, введите количество конфет (не более 28): "))
            if st1 <= 28 and st1 > 0:
                count_candy -= st1
                break
            else:
                print("введите число более 0 и менее 29 ")
        check_win(count_candy, first_gamer)
 # end --------------------------------------------------------------------------------------


def bot(count_candy):  # волво конфет забираемое ботом---------------------------------------
    res = count_candy % 29
    return res
 # end --------------------------------------------------------------------------------------


# игра с ботом -------------------------
def game_bot_vs_human(name1, name2, start_count_candy=100):
    gamers = [name1, name2]
    active_gamer = choice(gamers)
    print()
    print("определяем первого игрока.......")
    sleep(2)
    print("Право первого хода выпадает игроку:", active_gamer)
    count_candy = start_count_candy
    st1 = 0
    while True:

        if active_gamer == name2:
            print()
            print("Колличество конфет на кону: ", count_candy)
            st2 = bot(count_candy)
            print(name2, ",  забирает конфет :",  end=' ')
            sleep(3)
            print(st2)
            sleep(2)
            count_candy = count_candy-st2
            active_gamer = name1
            check_win(count_candy, active_gamer)

        else:
            print()
            print("Колличество конфет на кону: ", count_candy)

            while True:
                st2 = int(
                    input(f"{active_gamer}, введите количество конфет (не более 28): "))
                if st2 <= 28 and st2 > 0:
                    break
                else:
                    print("введите число более 0 и менее 29 ")
            count_candy = count_candy-st2
            active_gamer = name2
            check_win(count_candy, active_gamer)


# end --------------------------------------------------------------------------------------


flag = int(input("Введите 1 для игры с ботом или 2 для игры 2х человек: "))
if flag == 2:
    name1 = input("Введите имя первого игрока: ")
    if name1 == "":
        exit("неверное имя")
    name2 = input("Введите имя второго игрока: ")
    if name2 == "":
        exit("неверное имя")
elif flag == 1:
    name1 = input("Введите имя игрока: ")
    if name1 == "":
        exit("неверное имя")
    else:
        name1 = "\U0001F466" + " " + name1
        name2 = "\U0001F4BB Bot"
else:
    exit("введено неверное число")


if flag == 2:
    game_2x2(name1, name2, start_count_candy=100)
else:
    game_bot_vs_human(name1, name2, start_count_candy=100)
