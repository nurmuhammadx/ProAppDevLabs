class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Я кот. Меня зовут {self.name}. Мне {self.age} года.")

    def make_sound(self):
        print("Мяу!")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Я собака. Меня зовут {self.name}. Мне {self.age} года.")

    def make_sound(self):
        print("Гав!")


cat1 = Cat("Васька", 2.5)
dog1 = Dog("Рекс", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.print_info()
    animal.make_sound()
