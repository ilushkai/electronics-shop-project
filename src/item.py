import csv


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
    def instantiate_from_csv(cls):
        """Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv"""
        cls.all.clear()
        items = []
        with open('../src/items.csv', newline='', encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                _ = cls(row['name'], row['price'], row['quantity'])
                items.append(_)

        return items

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


Item.instantiate_from_csv()
