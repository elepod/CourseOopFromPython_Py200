from datetime import datetime
import doctest


class Student:
    def __init__(self, name: str, birthday: str, group: [int, None] = None):
        """

        :param name: ФИО студента
        :param description: Дата рождение студента
        :param status: Номер группы

        >>> st1 = Student('Иванов Иван', '11.11.2006', 123)
        >>> st2 = Student('Петров Олег', '12-12-2005', 245)
        Формат даты дожен быть день.месяц.год
        """
        self.name = name
        try:
            bool(datetime.strptime(birthday, "%d.%m.%Y"))
        except ValueError:
            print("Формат даты дожен быть день.месяц.год")
        self.birthday = birthday
        if not isinstance(group, (int, None)):
            raise TypeError("Группа должна быть типа int ли не задана")
        self.group = group

    def display(self) -> None:
        """
        Отображение статуса задачи

        >>> st1 = Student('Иванов Иван', '11.11.2006', 123)
        >>> st1.display()
        Студент: Иванов Иван 11.11.2006 123
        """
        print(f"Студент: {self.name} {self.birthday} {self.group}")

    def set_group(self, group: int) -> int:
        """

        :param group: Группа студента
        :return: Группа студента
        >>> st1 = Student('Иванов Иван', '11.11.2006', 123)
        >>> st1.set_group(456)
        456
        """
        if not isinstance(group, int):
            raise TypeError("Группа должна быть типа int")
        self.group = group
        return self.group


if __name__ == "__main__":
    doctest.testmod()