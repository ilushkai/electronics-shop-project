import csv

from src.exceptions import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if not issubclass(other.__class__, self.__class__):
            raise ValueError('Экземпляр должен быть класса: Phone или Item')
        return self.quantity + other.quantity

    def __radd__(self, other):
        if not issubclass(other.__class__, self.__class__):
            raise ValueError('Экземпляр должен быть класса: Phone или Item')
        return other.quantity + self.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """Срезает строку, если больше 10 символов"""
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, file='../src/items.csv'):
        """Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv"""
        cls.all.clear()

        try:
            with open(file, encoding='windows-1251') as f:
                reader = csv.DictReader(f)

                # Вызов исключения, если файл поврежден
                if len(reader.fieldnames) != 3:
                    raise InstantiateCSVError
                [cls((row['name']), row['price'], row['quantity']) for row in reader]

        except InstantiateCSVError:
            print('InstantiateCSVError: Файл items.csv поврежден')

        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл items.csv')

    @staticmethod
    def string_to_number(number: str) -> float:
        """Статический метод, возвращающий число из числа-строки"""
        return round(int(float(number)))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """

        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price
