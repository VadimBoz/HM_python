from my_token import TOKEN
from game import *
import logging
from random import choice
from time import sleep

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

n_1 = '\U0001F353' #бот
n_2 = '\U0001F352' # user
GAME1, GAME2  = range(2)



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)



# игровое поле -----------------------------
def playing_field(update, items, _):
    update.message.reply_text(f"|  {items[0]}  |  {items[1]}  |   {items[2]}  |")
    update.message.reply_text(f"|  {items[3]}  |  {items[4]}  |   {items[5]}  |")
    update.message.reply_text(f"|  {items[6]}  |  {items[7]}  |   {items[8]}  |")
# end -----------------------------------------------------------------------------------------------


def start(update, _):
    update.message.reply_text("Давай поиграем в крестики \U0001F353 - нолики \U0001F352" )
    update.message.reply_text(
        'Меня зовут профессор Бот. Я буду с вами играть. \n '
        '/game - начать игру \n'
        '/cancel  прекратить игру\n',
        )
    return GAME1

def game1(update, _):
    global name1, name2, first_gamer1,  lst_g
    global markup_key
    lst_g=['1', '2', '3', '4', '5', '6', '7', '8', '9']
    user = update.message.from_user
    logger.info("User %s start game", user.first_name)
    name1= 'Бот'
    name2 = user.first_name
    first_gamer1 = choice([name1, name2 ])
    update.message.reply_text('Определяем первого игрока ....')
    sleep(2)
    update.message.reply_text(f'Первый ход выпадает {first_gamer1}')
    if first_gamer1 == 'Бот':
        num=bot_game(lst_g)
        lst_g[num] = '\U0001F353'
        update.message.reply_text(f'Бот делает ход на поле {num+1}')
        sleep(2)
        playing_field(update, lst_g, _)
    else:
        playing_field(update, lst_g, _)

    reply_keyboard = [[lst_g[0], lst_g[1], lst_g[2] ], [lst_g[3], lst_g[4], lst_g[5] ],
                          [lst_g[6], lst_g[7], lst_g[8] ]]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(f"{user.first_name} \U0001F352 ваш ход",reply_markup=markup_key)
    return GAME2    
   

def game2(update, _):
    global  lst_g
    global markup_key
    user = update.message.from_user
    update.message.reply_text(f"{user.first_name} ход сделан ", reply_markup=markup_key)
    str_num = update.message.text
    if str_num.isdigit():
        num=int(str_num)-1
    else:
        update.message.reply_text(f"{str_num} поле уже занято повторите ввод")
        return GAME2
    logger.info(f"Пользователь %s сделал ход {num}", user.first_name)
    lst_g[num] = '\U0001F352'
    playing_field(update, lst_g, _)
    if check_win(lst_g):
        update.message.reply_text(f"{user.first_name} \U0001F352 выиграл, игра закончена", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    if check_no_win(lst_g, '\U0001F352', '\U0001F353') == 9:
        update.message.reply_text("!!!!!!!!!!!!!НИЧЬЯ !!!!!!!!!!!!", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END

    num=bot_game(lst_g)
    lst_g[num] = '\U0001F353'
    update.message.reply_text(f'Бот делает ход на поле {num+1}')
    sleep(2)
    playing_field(update, lst_g, _)
    reply_keyboard = [[lst_g[0], lst_g[1], lst_g[2] ], [lst_g[3], lst_g[4], lst_g[5] ],
                          [lst_g[6], lst_g[7], lst_g[8] ]]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(f"обновляем кнопки",reply_markup=markup_key)
    if check_win(lst_g):
        update.message.reply_text(f'Бот \U0001F353 выиграл, игра закончена', reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    if check_no_win(lst_g, '\U0001F352', '\U0001F353') == 9:
        update.message.reply_text("!!!!!!!!!!!!!НИЧЬЯ !!!!!!!!!!!!", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END

    reply_keyboard = [[lst_g[0], lst_g[1], lst_g[2] ], [lst_g[3], lst_g[4], lst_g[5] ],
                          [lst_g[6], lst_g[7], lst_g[8] ]]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(f"{user.first_name} \U0001F352 ваш ход", reply_markup=markup_key)

    return GAME2


def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил игру.", user.first_name)
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            GAME1: [MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9|\U0001F352|\U0001F353)$'), game1), CommandHandler('game', game1)],
            GAME2: [MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9|\U0001F352|\U0001F353)$'), game2)]
         },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()