import requests
from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())
    print('Текущая дата', datetime.now())
    print(requests.get('https://vk.com'))
