from my_token import TOKEN
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update,  ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, Filters, MessageHandler, ContextTypes
import logging
from math_real import mult, div, sum, dif, int_div, int_mod, exponentiation, sqrt, factorial, log10, exp
from convert import str_to_int_real, str_to_complex
from exception import exception_number
from menu import menu1, menu2_complex, menu2_int, menu2_real

ONE, TWO, THREE, FOUR, FIVE , SIX, SEVEN, EIGHT, NINE = range(9)
operand = ''
str_num_1 = ''
str_num_2 = ''

op_str = {'mult':'*',  'div':'/', 'sum':'+', 'difference':'-', 'pov':'^',
            "int_div":'//', "int_mod":'int_mod',   'sqrt':"sqrt", "log10":"log10",
             "fact":'!',  'exp':'e^x'}
op_fun = {'mult':mult, 'div':div, 'sum':sum, 'difference':dif, 'pov':exponentiation, 
            "int_div":int_div, "int_mod":int_mod, 'sqrt':sqrt, "log10":log10, 
            "fact":factorial, 'exp':exp}

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s начал разговор", user.first_name)
    reply_markup=menu1()
    update.message.reply_text(
        text='Пожалуйста, выберите  с какими числами  будете работать:', reply_markup=reply_markup)
    return ONE

def start2(update, _):
    query = update.callback_query
    query.answer()
    variant = query.data
    query.edit_message_text(text=f"Выбранный вариант: {variant}")
    reply_markup = menu1()
    query.edit_message_text('Пожалуйста, выберите  с какими числами  будете работать2:', reply_markup=reply_markup)
    return ONE


def real_num(update, _):
    query = update.callback_query
    query.answer()
    reply_markup = menu2_real()
    query.edit_message_text(text=f'Выберете математическую операцию для работы\n с веществеными числами :', reply_markup=reply_markup)
    return TWO

def int_num(update, _):
    query = update.callback_query
    query.answer()
    reply_markup = menu2_int()
    query.edit_message_text(text=f'Выберете математическую операцию для работы с натуральными числами:', reply_markup=reply_markup)
    return THREE

def complex_num(update, _):
    query = update.callback_query
    query.answer()
    reply_markup = menu2_complex()
    query.edit_message_text(text=f'Выберете математическую операцию для работы с комплексными числами:', reply_markup=reply_markup)
    return SIX


def expression(update, _):
    query = update.callback_query
    query.answer()
    variant = query.data
    query.edit_message_text(text=f"Введите математическое выражение: ")
    return NINE


def expression2(update, _):
    user = update.message.from_user
    str_num_1 = update.message.text
    str_num=str_num_1.replace('^', '**').replace(' ', '').replace('=', '')
    if str_num.find("&")>-1 or str_num.find("$")>-1 or str_num.find("!")>-1:
        update.message.reply_text(text=f"Не распознано выражение, введите математическое выражение: или начните сначала /start ")
        return NINE
    logger.info("Пользователь %s ввел: %s", user.first_name, str_num_1)
    try:
        res= eval(str_num)
    except ZeroDivisionError:
        update.message.reply_text(text=f"ZeroDivisionError, введите математическое выражение: или начните сначала /start ")
        logger.info("Пользователь %s ввел ошибочное выражение : %s", user.first_name, str_num_1)
        return NINE
    except Exception:
        update.message.reply_text(text=f"Нераспознано выражение, введите математическое выражение: или начните сначала /start ")
        logger.info("Пользователь %s ввел ошибочное выражение : %s", user.first_name, str_num_1)
        return NINE
    update.message.reply_text(f"результат выражения {str_num_1} = {res} ")
    logger.info("Пользователь %s получил решение : %s", user.first_name, res)
    update.message.reply_text(text=f"Введите математическое выражение: или начните сначала /start ")
    return NINE


def digit_2(update, _):
    global operand 
    global str_num_1
    global str_num_2
    if operand in  list(op_str.keys())[0:7] and str_num_1=='':
        user = update.message.from_user
        str_num_1 = update.message.text
        if exception_number(str_num_1): 
            str_num_1=str_to_int_real(str_num_1)
        else:
            str_num_1=''
            update.message.reply_text(text=f'Введено неверное значение, посторите ввод.')
            return FOUR
        logger.info("Пользователь %s ввел: %s", user.first_name, str_num_1)
        update.message.reply_text(f"первое число {str_num_1}, введите второе число: ")
        return  FOUR
    else:
        user = update.message.from_user
        str_num_2 = update.message.text
        if exception_number(str_num_2): 
            str_num_2=str_to_int_real(str_num_2)
        else:
            update.message.reply_text(text=f'Введено неверное значение, посторите ввод.')
            return FOUR
        logger.info("Пользователь %s ввел: %s", user.first_name, str_num_1)
        try:
            res = f"{str_num_1} {op_str[operand]} {str_num_2} = {op_fun[operand](str_num_1,str_num_2)} "
        except ZeroDivisionError:
            update.message.reply_text(text=f"ZeroDivisionError, введите снова: или начните сначала /start ")
            logger.info("Пользователь %s ввел ошибочное выражение : %s", user.first_name, str_num_2)
            return FOUR
        except Exception:
            update.message.reply_text(text=f"Нераспознано выражение, введите снова: или начните сначала /start ")
            logger.info("Пользователь %s ввел ошибочное выражение : %s", user.first_name, str_num_2)
            return FOUR
        update.message.reply_text(res)
        logger.info("Пользователь %s получил решение : %s", user.first_name, res)
    str_num_1=''
    reply_markup = menu2_real()
    update.message.reply_text(text=f'Выберете математическую операцию для работы:', reply_markup=reply_markup)
    return TWO

def digit_1(update, _):
    user = update.message.from_user
    str_num_1 = update.message.text
    if exception_number(str_num_1): 
        str_num_1=str_to_int_real(str_num_1)
    else:
        str_num_1=''
        update.message.reply_text(text=f'Введено неверное значение, посторите ввод.')
        return FOUR
    logger.info("Пользователь %s ввел: %s", user.first_name, str_num_1)
    res=f"{op_str[operand]} {str_num_1}  = {op_fun[operand](str_num_1)}  "
    update.message.reply_text(res)
    logger.info("Пользователь %s получил решение: %s", user.first_name, res)
    str_num_1=''
    reply_markup = menu2_real()
    update.message.reply_text(text=f'Выберете математическую операцию для работы:', reply_markup=reply_markup)
    return TWO

def two_dig(update, _):
    query = update.callback_query
    query.answer()
    global operand 
    operand = query.data
    query.edit_message_text(text=f"Выбранный операнд: {op_str[operand]}, введите первое число: ")
    return  FOUR

def one_dig(update, _):
    query = update.callback_query
    query.answer()
    global operand 
    operand = query.data
    query.edit_message_text(text=f"Выбранный операнд: {op_str[operand]}, введите число: ")
    return FIVE


def digit_2_complex(update, _):
    global operand 
    global str_num_1
    global str_num_2
    if operand in  list(op_str.keys())[0:7] and str_num_1=='':
        user = update.message.from_user
        str_num_1 = update.message.text
        if exception_number(str_num_1): 
            str_num_1=str_to_complex(str_num_1)
        else:
            str_num_1=''
            update.message.reply_text(text=f'Введено неверное значение, посторите ввод.')
            return SEVEN
        logger.info("Пользователь %s ввел: %s", user.first_name, str_num_1)
        update.message.reply_text(f"первое комплексное число {str_num_1}, \n Введите действительную"
                                    " и мнимую части второго комплексного числа через пробел: ")
        return  SEVEN
    else:
        user = update.message.from_user
        str_num_2 = update.message.text
        if exception_number(str_num_2): 
            str_num_2=str_to_complex(str_num_2)
        else:
            update.message.reply_text(text=f'Введено неверное значение, посторите ввод.')
            return SEVEN
        try:
             res = f"{str_num_1} {op_str[operand]} {str_num_2} = {op_fun[operand](str_num_1,str_num_2)} "
        except ZeroDivisionError:     
                update.message.reply_text(text=f"ZeroDivisionError, введите снова: или начните сначала /start ")
                logger.info("Пользователь %s ввел ошибочное выражение : %s", user.first_name, str_num_2)
                return SEVEN
        except Exception:
            update.message.reply_text(text=f"Нераспознано выражение, введите снова: или начните сначала /start ")
            logger.info("Пользователь %s ввел ошибочное выражение : %s", user.first_name, str_num_2)
            return SEVEN
        logger.info("Пользователь %s ввел: %s", user.first_name, str_num_1)
        res = f"{str_num_1} {op_str[operand]} {str_num_2} = {op_fun[operand](str_num_1,str_num_2)} "
        update.message.reply_text(res)
        logger.info("Пользователь %s получил решение : %s", user.first_name, res)
    str_num_1=''
    reply_markup = menu2_complex()
    update.message.reply_text(text=f'Выберете математическую операцию для работы:', reply_markup=reply_markup)
    return SIX


def digit_1_complex(update, _):
    user = update.message.from_user
    str_num_1 = update.message.text
    if exception_number(str_num_1): 
        str_num_1=str_to_complex(str_num_1)
    else:
        str_num_1=''
        update.message.reply_text(text=f'Введено неверное значение, посторите ввод.')
        return EIGHT
    logger.info("Пользователь %s ввел: %s", user.first_name, str_num_1)
    res=f"{op_str[operand]} {str_num_1}  = {op_fun[operand](str_num_1)}  "
    update.message.reply_text(res)
    logger.info("Пользователь %s получил решение: %s", user.first_name, res)
    str_num_1=''
    reply_markup = menu2_complex()
    update.message.reply_text(text=f'Выберете математическую операцию для работы:', reply_markup=reply_markup)
    return SIX


def two_dig_complex(update, _):
    query = update.callback_query
    query.answer()
    global operand 
    operand = query.data
    query.edit_message_text(text=f"Выбранный операнд: {op_str[operand]}.  Введите действительную "
                                    " и мнимую части первого комплексного числа через пробел: ")
    return  SEVEN

def one_dig_complex(update, _):
    query = update.callback_query
    query.answer()
    global operand 
    operand = query.data
    query.edit_message_text(text=f"Выбранный операнд: {op_str[operand]}, Введите действительную "
                            " и мнимую части комплексного числа через пробел: ")
    return EIGHT


def help_command(update, _):
    query = update.callback_query
    query.answer()
    variant = query.data
    query.edit_message_text(text=f"Выбранный вариант: {variant} \n"
                           " Используйте `/start` что бы начать заново.")
    return ONE


def end(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s завершил разговор", user.first_name)
    update.message.reply_text(text="See you next time!")
    return ConversationHandler.END

if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={ 
            ONE: [
                CallbackQueryHandler(real_num, pattern='^real_num$'),
                CallbackQueryHandler(complex_num, pattern='^complex_num$'),
                CallbackQueryHandler(int_num, pattern='int_num'),
                CallbackQueryHandler(expression, pattern='^expression$'),
                CallbackQueryHandler(help_command, pattern='^help$'),
                CallbackQueryHandler(start2, pattern='^start$'),
                   ],      
            TWO:  # real  num
                 [
                CallbackQueryHandler(two_dig, pattern='^(mult|div|sum|difference|pov|int_div|int_mod)$'),
                CallbackQueryHandler(one_dig, pattern='^(sqrt|log10|exp)$'),
                CallbackQueryHandler(start2, pattern='^start$'),       
                ],
            THREE:   # int num
                 [ 
                CallbackQueryHandler(two_dig, pattern='^(mult|div|sum|difference|pov|int_div|int_mod)$'),
                CallbackQueryHandler(one_dig, pattern='^(sqrt|log10|fact|exp)$'),
                CallbackQueryHandler(start2, pattern='^start$'),       
                ],
            FOUR: [ # real digit  two number     
                    MessageHandler(Filters.regex('^(\d+|\d+.\d+|-\d+|-\d+.\d+)$'), digit_2)        
                  ],
            FIVE: [   # real digit  one number      
                   MessageHandler(Filters.regex('^(\d+|\d+.\d+|-\d+|-\d+.\d+)$'), digit_1)   
                  ],
            SIX:  [     # complex num
                    CallbackQueryHandler(two_dig_complex, pattern='^(mult|div|sum|difference|pov|int_div|int_mod)$'),
                    CallbackQueryHandler(one_dig_complex, pattern='^(sqrt|log10|exp)$'),
                    CallbackQueryHandler(start2, pattern='^start$'),      
                  ],
            SEVEN: [   # complex num  two number 
                   MessageHandler(Filters.text & ~Filters.command,digit_2_complex)       
                  ],
            EIGHT:
                  [   # complex num  one number 
                    MessageHandler(Filters.text & ~Filters.command,digit_1_complex)   
                  ],
            NINE:
                  [ # expression
                      MessageHandler(Filters.text & ~Filters.command,expression2) 
                  ]
        },
        fallbacks=[CommandHandler('start', start), CommandHandler('end', end)],
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()