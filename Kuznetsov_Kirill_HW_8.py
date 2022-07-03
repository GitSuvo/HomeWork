# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного
# выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
# виде словаря. Если адрес не валиден, выбросить исключение ValueError.
# Пример:
# --- email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# --- email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ...
# raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
# выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
# """


import re
import sys
VALID_EMAIL = re.compile(r'\w*@\w*\.ru')


def email_parse(email):
    res_dict = {}
    try:
        if VALID_EMAIL.search(email):
            res = re.split(r'@', email)
            res_dict['username'] = res[0]
            res_dict['domain'] = res[1]
        else:
            raise ValueError
    except ValueError:
        return print('Wrong email')

    return res_dict


# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
# функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)


def type_logger(funс):
    def wrapper(*args):
        res = {i: type(i) for i in args}
        return res
    return wrapper


@type_logger
def calc_cube(*args):
    res = [arg**3 for arg in args]
    return res


a = calc_cube(5)
print(a)
b = calc_cube(5, 6)
print(b)

# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и
# выбрасывать исключение ValueError, если что-то не так, например:
#
# ef val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5


def val_checker(fun):
    def _val_checker(func):
        def wrapper(*args):
            try:
                for num in args:
                    if num < 1:
                        raise ValueError
            except ValueError:
                return print(f'wrong value {num}')
            return func(num)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(5)
print(a)
b = calc_cube(-5)
print(b)


