class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    def __str__(self):
        return super().__str__() + f'  Количество страниц: {self._pages}'

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError('Некорректный тип данных')
        if pages < 0:
            raise ValueError('Некорректное значение')
        self._pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        if not isinstance(duration, int):
            raise TypeError('Некорректный тип данных')
        if duration < 0:
            raise ValueError('Некорректное значение')
        self._duration = duration

    def __str__(self):
        return super().__str__() + f'  Продолжительность {self._duration} часов'


if __name__ == "__main__":
    pbook = PaperBook(name='Война и мир', author="Л.Н. Толстой", pages=1000)
    print(pbook.pages)
    pbook.pages = 1500
    print(pbook.pages)
    print(pbook)

    abook = AudioBook(name='Война и мир', author="Л.Н. Толстой", duration=1000)
    print(abook)
