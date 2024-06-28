class Vehicl:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'BLACK', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__color = str(__color)
        self.__engine_power = str(__engine_power)

    def get_model(self):
        if self.__model:
            return f'Модель: {self.__model}'

    def get_horspower(self):
        if self.__engine_power:
            return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        if self.__color:
            return f'Цвет: {self.__color}'

    def print_info(self):
        print('', self.get_model(), '\n',
              self.get_horspower(), '\n',
              self.get_color(), '\n',
              f'Владелец:{self.owner}')

    def set_color(self, new_color):
        new_color = str(new_color)
        d = []
        for i in self.__COLOR_VARIANTS:
            d.append(i.upper())
        if new_color.upper() in d:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicl):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('PINK')
vehicle1.set_color('GREEN')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
