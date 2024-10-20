import requests
from config import database_url, request_header

def get_all_employees():
    response = requests.get(f"http://localhost:8080/departments/dep1/employees", headers=request_header)
    print(response.status_code)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("[ОШИБКА] НЕПРАВИЛЬНЫЙ КОД ОТВЕТА!")