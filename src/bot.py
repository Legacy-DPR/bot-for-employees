import telebot
from telebot import types
from markups_employee import *
from markups_admin import *
from config import *
from users import *
from admin_control import *

bot = telebot.TeleBot(bot_token)
global current_user_is_admin

"""
General handlers
"""

@bot.message_handler(commands=["start"])
def start(message):
    user_id : str = message.from_user.id
    is_valid = check_if_user_in_db(user_id)

    if not is_valid:
        print("К боту пытался подключиться неизвестный пользователь!")
        bot.send_message(message.chat.id, "Отказано в доступе. Ваш ID не найден в базе данных.")
    else:
        current_user = get_user(user_id)
        current_user_is_admin = check_if_user_is_admin(current_user)
        print(f"Текущий пользователь: {current_user}")
        print(f"Является ли текущий пользователь {current_user} администратором: {current_user_is_admin}")

        if not current_user_is_admin:
            bot.send_message(message.chat.id,
                            f"Добро пожаловать, {current_user["name"]}!\nДля продолжения нажмите {buttons_employee["start_shift"]}",
                            reply_markup=employee_start_shift_markup()
            )
        else:
            bot.send_message(message.chat.id,
                            f"Добро пожаловать, {current_user["name"]}!\nВыберите один из пунктов меню.",
                            reply_markup=admin_start_shift_markup()
            )

@bot.message_handler(func=lambda message: message.text not in buttons_employee.values() and message.text not in buttons_admin.values())
def unknown_message(message):
    bot.send_message(message.chat.id, "Неизвестная команда. Пожалуйста, выберите действие из меню.")

"""
Handlers to standard employee user
"""
@bot.message_handler(func=lambda message: message.text == buttons_employee["start_shift"])
def employee_begin_shift(message):
    current_user = get_user(message.from_user.id)
    set_user_on_duty(current_user)
    bot.send_message(message.chat.id, "Смена начата! Выберите действие:", reply_markup=employee_main_menu_markup())

@bot.message_handler(func=lambda message: message.text == buttons_employee["take_ticket"])
def employee_take_ticket_menu(message):
    bot.send_message(message.chat.id, "Вы находитесь в меню выбора талона.", reply_markup=employee_back_markup())

@bot.message_handler(func=lambda message: message.text == buttons_employee["get_ticket"])
def employee_process_ticket_menu(message):
    bot.send_message(message.chat.id, "Вы находитесь в меню обработки билетов.", reply_markup=employee_process_ticket_markup())

@bot.message_handler(func=lambda message: message.text == buttons_employee["get_stats"])
def employee_generate_report_menu(message):
    bot.send_message(message.chat.id, "Вы находитесь в меню составления статистики за вашу смену.", reply_markup=employee_back_markup())

@bot.message_handler(func=lambda message: message.text == buttons_employee["end_shift"])
def employee_end_shift(message):
    current_user = get_user(message.from_user.id)
    set_user_not_on_duty(current_user)
    bot.send_message(message.chat.id,
                     f"Смена завершена. Для начала новой смены нажмите {buttons_employee["start_shift"]}.", 
                     reply_markup=employee_start_shift_markup()
    )

@bot.message_handler(func=lambda message: message.text == buttons_employee["back"])
def selected_back(message):
    bot.send_message(message.chat.id, buttons_employee["back"], reply_markup=employee_main_menu_markup())

"""
Handlers to admin user
"""
@bot.message_handler(func=lambda message: message.text == buttons_admin["start_shift"])
def ticket_begin_shift(message):
    current_user = get_user(message.from_user.id)
    set_user_on_duty(current_user)
    bot.send_message(message.chat.id, "Смена начата! Выберите действие:", reply_markup=admin_main_menu_markup())

@bot.message_handler(func=lambda message: message.text == buttons_admin["get_operators"])
def selected_get_operators(message):
    bot.send_message(message.chat.id, "Список всех операторов текущего отделения:", reply_markup=admin_main_menu_markup())

@bot.message_handler(func=lambda message: message.text == buttons_admin["back"])
def selected_back(message):
    bot.send_message(message.chat.id, buttons_admin["back"], reply_markup=admin_back_markup())

@bot.message_handler(func=lambda message: message.text == buttons_admin["change_duties"])
def selected_change_duties(message):
    bot.send_message(message.chat.id,
                     "Введите имя работника, у которого вы ходите изменить список операций:",
                     reply_markup=admin_main_menu_markup()
    )

@bot.message_handler(func=lambda message: message.text == buttons_admin["add_operator"])
def selected_add_operator(message):
    bot.send_message(message.chat.id,
                     "Введите имя работника, которого вы желаете добавить:",
                     reply_markup=admin_main_menu_markup()
    )

@bot.message_handler(func=lambda message: message.text == buttons_admin["end_shift"])
def selected_admin_end_shift(message):
    current_user = get_user(message.from_user.id)
    set_user_not_on_duty(current_user)
    bot.send_message(message.chat.id,
                     f"Смена завершена. Для начала новой смены нажмите {buttons_employee["start_shift"]}.", 
                     reply_markup=employee_start_shift_markup()
    )
