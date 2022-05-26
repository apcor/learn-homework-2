"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime as dt

def print_days():
    yest_date = dt.date.today() - dt.timedelta(days=1)
    tod_date = dt.date.today()
    d30_date = dt.date.today() - dt.timedelta(days=30)
    print(f'Yesterday was {yest_date}')
    print(f'Today is {tod_date}')
    print(f'30 days ago was {d30_date}')


def str_2_datetime(date_string):
    return dt.datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
