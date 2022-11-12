
from random import choice



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


def bot_game(items): # ход тупого бота -----------------------------------------------------------------
    while True:
        num = choice(range(9))
        if items[num].isdigit():
            return num
# end -----------------------------------------------------------------------------------------------


# проверка на ничью -----------------------------------------------
def check_no_win(items, n1, n2):
    count = 0
    for i in range(9):
        if items[i] == n1 or items[i] == n2:
            count += 1
    return count
 # end -----------------------------------------------------------------------------------------------



def check_exist(items:list, i:int, str1:str, str2:str):
    if items[i] == str1 or items[i] == str2:
          return True  
    return False

