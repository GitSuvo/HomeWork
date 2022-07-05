# 1. Создать класс TrafficLight (светофор).

import time


class TrafficLight:
    __color = ('Red', 'Yellow', 'Green')

    def __init__(self, *args):
        self.col = args

    def running(self):
        if TrafficLight.__color == self.col:
            while True:
                print(self.col[0])
                time.sleep(7)
                print(self.col[1])
                time.sleep(2)
                print(self.col[2])
                time.sleep(3)
        else:
            print('incorrect mode')


tra_lig = TrafficLight('Red', 'Yellow', 'Green')
tra_lig.running()


# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной
# в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:
    __weight = 25
    __number_layers = 5

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def total_weight(self):
        total_weight = self._lenght * self._width * Road.__weight * Road.__number_layers
        print(total_weight)


road = Road(20, 5000)
road.total_weight()


# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить
# значения атрибутов, вызвать методы экземпляров.


class Worker:
    income = {'wage': 42600, 'bonus%': 30}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        print(f'{self.surname} {self.name} {self.position}')

    def get_total_income(self):
        print(int(self.income['wage'] * (1 + (self.income['bonus%'] / 100))))

Vasia = Position('Vasia', 'Pupkin', 'Engineer')
Vasia.get_full_name()
Vasia.get_total_income()
print(Vasia.income['wage'])


# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self. name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        if direction == 'налево':
            print('Машина повернула налево')
        elif direction == 'направо':
            print('Машина повернула направо')

    def show_speed(self):
        print(f'{self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        print(f'{self.speed} км/ч')
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        print(f' {self.speed} км/ч')
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=True)

car = Car(60, 'Green', 'Lada', False)
print(car.color)
print(car.name)
print(car.is_police)
car.go()
car.stop()
car.turn('направо')
car.show_speed()


town_car = TownCar(80, 'Yellow', 'Moscvich', False)
print(town_car.color)
print(town_car.name)
print(town_car.is_police)
town_car.go()
town_car.stop()
town_car.turn('налево')
town_car.show_speed()


sport_car = SportCar(150, 'Red', 'Vesta', False)
print(sport_car.color)
print(sport_car.name)
print(sport_car.is_police)
town_car.go()
town_car.stop()
town_car.turn('направо')
town_car.show_speed()


police = PoliceCar(150, 'Blue', 'VAZ 2110', True)
print(police.color)
print(police.name)
print(police.is_police)
police.go()
police.stop()
police.turn('направо')
police.show_speed()

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Отрисовка ручкой')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Отрисовка карандашом')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Отрисовка маркером')


stationery = Stationery('Канцелярская пренадлежность')
stationery.draw()

pen = Pen('Пишущая ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()
