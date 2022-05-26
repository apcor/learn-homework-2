"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

name_dict = [
        {'name': 'Marie', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Elon', 'age': 39, 'job': 'Programmer'}, 
        {'name': 'Tim', 'age': 48, 'job': 'Big boss'},
        {'name': 'George', 'age': 34, 'job': 'Engineer'},
        {'name': 'Kate', 'age': 27, 'job': 'HR manager'}
    ]

def main():
    with open('employees.csv', 'w', encoding='utf-8', newline='') as f:
        col_names = ['name', 'job', 'age']
        writer = csv.DictWriter(f, col_names, delimiter=';')
        writer.writeheader()
        for person in name_dict:
            writer.writerow(person)


if __name__ == "__main__":
    main()
