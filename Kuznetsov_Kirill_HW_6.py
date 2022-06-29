# 1.1 Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
# кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

# [
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ]


import requests

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = str(requests.get(URL).text)

with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.write(response)


def file_log(some_file):
    lst_part_log = [(line.split()[0], line.split()[5].replace('"', ''), line.split()[6]) for line in some_file]
    some_file.close()
    return lst_part_log

#1.1*


def file_log_ip(some_file):
    ip_lst = [line.split()[0] for line in some_file]
    unique_ip = set(ip_lst)
    count_ip = {}
    for ip in unique_ip:
        n = ip_lst.count(ip)
        count_ip[ip] = n
        some_file.close()
    return count_ip


# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при
# хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о
# хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
# чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи
# считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):


import csv
from itertools import zip_longest

users = [['Иванов, Иван, Иванович'],
         ['Петров, Петр, Петрович'],
         ['Кузнецов, Кирилл, Александрович'],
         ['Путин Владимир Владимирович'],
         ['Панин Алексей Вячеславович']]

hobbies = [['скалолазание'], ['охота'], ['горные лыжи'], ['дзюдо']]

with open('user.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(users)

with open('hobbies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(hobbies)

FILE1 = 'user.csv'
with open(FILE1, 'r',) as f:
    reader = csv.reader(f)
    lst_users = [(','.join(row)).replace(',', '') for row in reader]
    print(lst_users)

FILE2 = 'hobbies.csv'
with open(FILE2, 'r',) as f:
    reader = csv.reader(f)
    lst_hobbies = [(','.join(row)) for row in reader]
    print(lst_hobbies)

dict_user_hobby = dict(zip_longest(lst_users, lst_hobbies))


with open('dict.txt', 'w', encoding='utf-8') as f:
    f.write(str(dict_user_hobby))

# Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом командной
# строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки значение
# суммы продаж. Для чтения данных реализовать в командной строке следующую логику:


import sys
with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(f'{sys.argv[1:]}\n')


with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(sys.argv) == 1:
        print(f.read())
    if len(sys.argv) == 2:
        for line in f.readlines()[int(sys.argv[1]) - 1:]:
            print(line.strip())
    if len(sys.argv) == 3:
        for line in f.readlines()[int(sys.argv[1]) - 1:int(sys.argv[2]) + 1]:
            print(line.strip())




