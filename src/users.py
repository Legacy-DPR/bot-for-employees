import requests
from config import database_url, request_header

def check_if_user_in_db(tg_id: int):
    tg_id_str: str = str(tg_id)
    response = requests.get(f"{database_url}employees/{tg_id_str}", headers=request_header) 

    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        raise Exception("[ОШИБКА] НЕИЗВЕСТНЫЙ КОД ОТВЕТА!")

def get_user(tg_id: int):
    tg_id_str: str = str(tg_id)
    response = requests.get(f"{database_url}employees/{tg_id_str}", headers=request_header) 

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return "ПОЛЬЗОВАТЕЛЬ НЕ ОПРЕДЕЛЁН"
    else:
        raise Exception("НЕИЗВЕСТНЫЙ КОД ОТВЕТА")

def set_user_on_duty(current_user):
    tg_id = current_user["telegramId"]
    try:
        response = requests.patch(f"{database_url}employees/{tg_id}/set-duty", json={'onDuty' : True}, headers=request_header)
        if response.status_code == 200:
            print(f"Пользователь {response.text} зашёл на смену.")
        else:
            print(f"[ОШИБКА] {response.status_code}")
            print("[ОТВЕТ]", response.text)
    except requests.exceptions.RequestException as e:
        print(f"[ОШИБКА] {e}")

def set_user_not_on_duty(current_user):
    tg_id = current_user["telegramId"]
    try:
        response = requests.patch(f"{database_url}employees/{tg_id}/set-duty", json={'onDuty' : False}, headers=request_header)
        if response.status_code == 200:
            print(f"Пользователь {response.text} вышел со смены:")
        else:
            print(f"[ОШИБКА] {response.status_code}")
            print("[ОТВЕТ]", response.text)
    except requests.exceptions.RequestException as e:
        print(f"[ОШИБКА] {e}")

def check_if_user_is_admin(current_user):
    return current_user["admin"] == True

def add_new_employee(employee):
    response = requests.post(f"{database_url}employees", json=data, headers=request_header)
    if response.status_code == 200:
        print("Успешно добавлен пользователь в БД")
        return True
    else:
        print(f"[ОШИБКА]: {response.status_code}")
        print("[ОШИБКА]: ПОЛЬЗОВАТЕЛЬ НЕ ДОБАВЛЕН")
        return False
