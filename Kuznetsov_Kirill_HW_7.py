# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp


import os
import yaml
from pathlib import Path as P


def start_project(*args):
    if not os.path.exists(args[0]):
        os.mkdir(args[0])
        os.chdir(args[0])
    for i in (args[1:]):
        os.mkdir(i)


# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
#|--my_project
   # |--settings
   # |  |--__init__.py
   # |  |--dev.py
   # |  |--prod.py
   # |--mainapp
   # |  |--__init__.py
   # |  |--models.py
   # |  |--views.py
   # |  |--templates
   # |     |--mainapp
   # |        |--base.html
   # |        |--index.html
   # |--authapp
   # |  |--__init__.py
   # |  |--models.py
   # |  |--views.py
   # |  |--templates
   # |     |--authapp
   # |        |--base.html
   # |        |--index.html



config_dict = {'my_project': {'settings': ['__init__.py', 'dev.py', 'prod.py'],
               'mainapp': ['__init__.py', 'models.py', 'views.py', 'templates', 'mainapp', 'base.html', 'index.html'],
               'auth-app': ['__init__.py', 'models.py', 'views.py', 'templates', 'auth-app', 'base.html', 'index.html']}}


with open('config.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(config_dict, f, default_flow_style=False, sort_keys=False)

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def create_project():
    for key in data:
        if not os.path.exists(key):
            os.mkdir(key)
            os.chdir(key)
            pth = os.getcwd()
            for k in data[key]:
                if not os.path.exists(k):
                    os.mkdir(k)
                    print(os.getcwd())
                    for file in data[key][k]:
                        if file.endswith('y'):
                            os.chdir(k)
                            with open(f'{file}', 'a', encoding='utf-8') as f:
                                f.writelines('made file')
                            os.chdir(pth)
                        else:
                            if file.startswith('temp'):
                                os.chdir(k)
                                os.mkdir(file)
                                os.chdir(file)
                            else:
                                if file.endswith('app'):
                                    os.mkdir(file)
                                    os.chdir(file)
                                else:
                                    with open(f'{file}', 'a', encoding='utf-8') as p:
                                        p.writelines('made file')
                                        os.chdir(pth)


# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
# ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
# количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0), например:
# {
# 100: 15,
# 1000: 3,
# 10000: 7,
# 100000: 2
# }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.


def make_stat(any_directory):
    stat_of_folder = {
        100: 0,
        1000: 0,
        10000: 0,
        100000: 0
    }
    any_pth = P.cwd()

    for file in os.listdir(fr'{any_pth}\{any_directory}'):
        if os.stat(fr'{any_pth}\{any_directory}\{file}').st_size <= 100:
            stat_of_folder[100] += 1
        elif os.stat(fr'{any_pth}\{any_directory}\{file}').st_size <= 1000:
            stat_of_folder[1000] += 1
        elif os.stat(fr'{any_pth}\{any_directory}\{file}').st_size <= 10000:
            stat_of_folder[10000] += 1
        else:
            stat_of_folder[100000] += 1

    return stat_of_folder


































