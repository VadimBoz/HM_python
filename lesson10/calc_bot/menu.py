from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def menu1():
    keyboard = [
                    [InlineKeyboardButton("Вещественные числа", callback_data='real_num'),
                        InlineKeyboardButton("Комплексные числа", callback_data='complex_num')],
                    [InlineKeyboardButton("Целые числа", callback_data='int_num'),
                        InlineKeyboardButton("Вычислить выражение", callback_data='expression')],
                    [InlineKeyboardButton("Помощь", callback_data="help")],
                    [InlineKeyboardButton("Начать заново", callback_data='start')],
                ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def menu2_real():
    keyboard = [
                  [
                  InlineKeyboardButton("*", callback_data='mult'),
                  InlineKeyboardButton(":", callback_data='div'),
                  InlineKeyboardButton("+", callback_data='sum'),
                  InlineKeyboardButton("-", callback_data='difference'),
                  InlineKeyboardButton("x^y", callback_data='pov'),
                  InlineKeyboardButton("div", callback_data="int_div"),
                  InlineKeyboardButton("mod", callback_data="int_mod"),
                  ],
                  [
                  InlineKeyboardButton("sqrt", callback_data="sqrt"),
                  InlineKeyboardButton("log10", callback_data="log10"),
                  InlineKeyboardButton("e^x", callback_data="exp"),
                  ],
                  [InlineKeyboardButton("Начать заново", callback_data='start')],
               ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def menu2_int():
    keyboard = [
                  [
                  InlineKeyboardButton("*", callback_data='mult'),
                  InlineKeyboardButton(":", callback_data='div'),
                  InlineKeyboardButton("+", callback_data='sum'),
                  InlineKeyboardButton("-", callback_data='difference'),
                  InlineKeyboardButton("x^y", callback_data='pov'),
                  InlineKeyboardButton("div", callback_data="int_div"),
                  InlineKeyboardButton("mod", callback_data="int_mod"),
                  ],
                  [
                  InlineKeyboardButton("sqrt", callback_data="sqrt"),
                  InlineKeyboardButton("log10", callback_data="log10"),
                  InlineKeyboardButton("x!", callback_data="fact"),
                  InlineKeyboardButton("e^x", callback_data="exp"),
                  ],
                  [InlineKeyboardButton("Начать заново", callback_data='start')],
               ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def menu2_complex():
    keyboard = [
                  [
                  InlineKeyboardButton("*", callback_data='mult'),
                  InlineKeyboardButton(":", callback_data='div'),
                  InlineKeyboardButton("+", callback_data='sum'),
                  InlineKeyboardButton("-", callback_data='difference'),
                  InlineKeyboardButton("x^y", callback_data='pov'),
                  ],
                  [
                  InlineKeyboardButton("sqrt", callback_data="sqrt"),
                  InlineKeyboardButton("e^x", callback_data="exp"),
                  ],
                  [InlineKeyboardButton("Начать заново", callback_data='start')],
               ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

