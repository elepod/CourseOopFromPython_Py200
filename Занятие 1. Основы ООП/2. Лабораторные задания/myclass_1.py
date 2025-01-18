import doctest


class Task:
    def __init__(self, name: str, description: str, status: bool=False):
        """

        :param name: Название задания
        :param description: Описание задания
        :param status: Статус выполнения задания

        >>> task = Task('Лабораторная №1', 'Задание по курсу ООП, лабораторная №1', True)
        >>> task1 = Task('Лабораторная №1', 'Задание по курсу ООП, лабораторная №1', 'blabla')
        Traceback (most recent call last):
        TypeError: Статус задания должен быть типа bool
        """
        self.name = name
        self.description = description
        if not isinstance(status, bool):
            raise TypeError("Статус задания должен быть типа bool")
        self.status = status

    def display(self) -> None:
        """
        Отображение статуса задачи

        >>> task = Task('Лабораторная №1', 'Задание по курсу ООП, лабораторная №1', True)
        >>> task.display()
        Лабораторная №1 выполнена
        """
        if self.status:
            print(f"{self.name} выполнена")
        else:
            print(f"{self.name} не выполнена")

    def set_status(self, status: bool) -> bool:
        """

        :param status: Статус выполнения задания
        :return: Новый статус выполнения задания
        >>> task = Task('Лабораторная №1', 'Задание по курсу ООП, лабораторная №1', True)
        >>> task.set_status(True)
        True
        """
        if not isinstance(status, bool):
            raise TypeError("Статус задания должен быть типа bool")
        self.status = status
        return self.status


if __name__ == "__main__":
    doctest.testmod()