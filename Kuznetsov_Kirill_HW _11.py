"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


import re


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def num_date(cls, date):
        splited_date = date.split('-')
        day = int(splited_date[0])
        month = int(splited_date[1])
        year = int(splited_date[2])
        return day, month, year

    @staticmethod
    def format_date(date):
        pattern_date = re.compile(r'\d\d-\d\d-\d\d\d\d')
        if not pattern_date.match(date):
            return f'Date {date} is not correct'
        return date


print(Date.num_date('08-07-2022'))
print(Date.format_date('08-07-2022'))
print(Date.format_date('435-65-4555'))


'2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на '
'данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать '
'эту ситуацию и не завершиться с ошибкой.'


class ZDE(Exception):

    @staticmethod
    def divide_nums():
        try:
            while True:
                try:
                    first_num = int(input('Enter first number: '))
                    second_num = int(input('Enter second number: '))
                    print(f'Result = {first_num / second_num}')
                except ZeroDivisionError:
                    print('cannot be divided by zero')
        except KeyboardInterrupt:
            print('The program is completed')

ZDE.divide_nums()



'''3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список 
необходимо только числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не 
остановит работу скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный 
список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода 
пользователем очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, 
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и 
отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться'''


class Only_Numbers_List(Exception):
    @staticmethod
    def make_only_num_lst():
        user_num_lst = []
        user_num = 0
        while user_num != 'stop':
            user_num = input('Введите число: ')
            if user_num.isdigit():
                user_num_lst.append(user_num)
            else:
                print(f'{user_num} не число')
        print(user_num_lst)

Only_Numbers_List.make_only_num_lst()


'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс 
«Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники 
(принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов. 
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники'''


class Warehouse:

    warehouse_lst = []

    def __init__(self, capacity, occupancy):
        self.capacity = capacity
        self.occupancy = occupancy

    def add_to_warehouse(self):
        print(f'Осталось {self.capacity - int(self.occupancy)} мест')


class Office_Equipment:

    def __init__(self, name):
        self.name = name


class Printer(Office_Equipment):

    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    def printer(self):
        print(self.name, self.model)


class Scanner(Office_Equipment):

    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    def scaner(self):
        print(self.name, self.model)



warehouse = Warehouse(50, 20)
warehouse.add_to_warehouse()



'''5. Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку
методов сложения и умножения комплексных чисел. Проверить работу проекта. Для этого создать экземпляры класса
(комплексные числа), выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного
результата.
'''

import math

class Complex_number(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = complex(a, b)
        print(self.x)

    def __add__(self, other):
        return f'sum {self.x} and {other.x}: {complex((self.a + other.a), (self.b + other.b))}'


first_num = Complex_number(3, 4)
second_num = Complex_number(5, 7)
print(first_num + second_num)