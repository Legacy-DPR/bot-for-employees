from telebot import types

buttons_admin = {
    'back'             : '⬅ Назад.',
    'get_operators'    : '🗂️ Просмотреть список операторов в отделении и их статистику.',
    'change_duties'    : '📘 Изменить список операций для конкретного оператора.',
    'add_operator'     : '📨 Добавить оператора.',
    'end_shift'        : '🚪 Закончить смену администратора.',
    'start_shift'      : '💼 Начать смену администратора.'
}

def admin_back_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(buttons_admin['back']))
    return markup

def admin_main_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(types.KeyboardButton(buttons_admin['get_operators']))
    markup.add(types.KeyboardButton(buttons_admin['change_duties']))
    markup.add(types.KeyboardButton(buttons_admin['add_operator']))
    markup.add(types.KeyboardButton(buttons_admin['end_shift']))
    return markup

def admin_list_operators_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(buttons_admin['back']))
    return markup

def admin_start_shift_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(buttons_admin['start_shift']))
    return markup