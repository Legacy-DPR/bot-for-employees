from telebot import types

buttons_employee = {
    'back'          : '⬅ Назад в меню работника.',
    'get_ticket'    : '🗒 Обработать текущий билет.',
    'take_ticket'   : '🗯 Взять билет из очереди.',
    'get_stats'     : '📊 Получить статистику за смену.',
    'end_shift'     : '🚪 Закончить смену оператора.',
    'start_shift'   : '💼 Начать смену оператора.',

    'accept_ticket' : '🟢 Обработать талон',
    'deny_ticket'   : '🔴 Отказать в обработке талона'
}

def employee_back_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(buttons_employee['back']))
    return markup

def employee_main_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(types.KeyboardButton(buttons_employee['get_ticket']))
    markup.add(types.KeyboardButton(buttons_employee['take_ticket']))
    markup.add(types.KeyboardButton(buttons_employee['get_stats']))
    markup.add(types.KeyboardButton(buttons_employee['end_shift']))
    return markup

def employee_start_shift_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(buttons_employee['start_shift']))
    return markup

def employee_process_ticket_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(types.KeyboardButton(buttons_employee['accept_ticket']))
    markup.add(types.KeyboardButton(buttons_employee['deny_ticket']))
    markup.add(types.KeyboardButton(buttons_employee['back']))
    return markup