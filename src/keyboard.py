from src.item import Item


class MixinLang:
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Возвращает новое множество, содержащее только тот языковой код,
           который отсутствует в переменной self.__language"""

        self.__language = ({"RU", "EN"} - {self.__language}).pop()
        return self



class Keyboard(MixinLang, Item):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
