class Vehicle(object):  # Родительский класс Vehicle(Транспортное средство)
    def __init__(self, speed, max_speed):
        self.speed = speed
        self.max_speed = max_speed

    def accelerate(self, x):  # метод для установки скорости
        self.speed = self.speed + x
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def brake(self, x):  #
        self.speed = self.speed - x
        if self.speed < 0:
            self.speed = 0

    def print_status(self):  #
        print('Скорость транспортного средства равна {0} км/ч'.format(
            self.speed))


class Motorcycle(Vehicle):  # Дочерний класс мотоцикл
    def __init__(self, speed, max_speed):
        super(Motorcycle, self).__init__(speed, max_speed)  # вызов супер класса
        # Дополнительные поля
        self._front_tire_width = 95
        self._rear_tire_width = 95
        print('Был создан мотоцикл!')

    def set_tires_width(self, front, rear):  # метод для установки новых шин
        self._front_tire_width = front
        self._rear_tire_width = rear
        print('На мотоцикл были установлены новые шины')

    def print_tire_info(self):
        print('Ширина передней шины {0} мм'.format(self._front_tire_width))
        print('Ширина задней шины {0} мм'.format(self._rear_tire_width))


class Automobile(Vehicle):  # Дочерний класс автомобиль
    def __init__(self, speed, max_speed):
        super(Automobile, self).__init__(speed, max_speed)  # вызов супер класса
        # Дополнительные поля
        self._gear = 0
        self._color = 'синий'
        print('Был создан автомобиль!')

    def set_gear(self, gear):  # метод для установки скорости
        self._gear = gear

    def print_status(self):
        super(Automobile, self).print_status()
        print('Автомобиль переключен на скорость № {0}'.format(self._gear))
        print('Автомобиль покрашен в {0} цвет'.format(self._color))

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color


m = Motorcycle(60, 120)
m.print_status()
m.set_tires_width(90, 100)
m.print_tire_info()

print('\n\n')

a = Automobile(0, 150)
a.accelerate(40)
a.set_gear(2)
a.print_status()
a.set_color('красный')
color = a.get_color()
print(color)
