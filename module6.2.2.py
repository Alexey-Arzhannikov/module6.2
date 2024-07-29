class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner  # public
        self.__model = model   # protected
        self.__engine_power = engine_power
        self.__color = color

    # методы возвращающие характеристики транспорта
    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    # метод распечатывает результаты методов выше
    def print_info(self):
        print(f'Модель: {self.get_model()}\n'
              f'Мощность двигателя: {self.get_horsepower()}\n'
              f'Цвет: {self.get_color()}\n'
              f'Владелец: {self.owner}')

    # метод меняет цвет авто, если он есть в списке __COLOR_VARIANTS
    def set_color(self, chg_new_color: str):
        if chg_new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = chg_new_color
        else:
            print(f'Нельзя сменить цвет на {chg_new_color}')

# класс Sedan наследуется от класса Vehicle
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# создаем объект класса седан
vehicle1 = Sedan('Fedos', 'Toyota Mark ||', 500, 'blue')

# изначальные свойства
vehicle1.print_info()

# меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# проверяем что поменялось
vehicle1.print_info()



