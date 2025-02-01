from datetime import date, datetime


class Room:
    """
    Базовый класс для номеров в отеле
    """
    def __init__(self, room_number, price_per_night):
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.__is_booked = "не забронирована"

    def book(self):
        if self.__is_booked == "не забронирована":
            self.__is_booked = "забронирована"
            print(f"Комната {self.__room_number} забронирована.")
        else:
            raise ValueError(f"Комната {self.__room_number} уже забронирована.")

    def unbook(self):
        if self.__is_booked == "забронирована":
            self.__is_booked = "не забронирована"
            print(f"Комната {self.__room_number} освобождена.")

    def calculate_price(self, nights):
        return self.__price_per_night*nights

    def get_room_number(self):
        return self.__room_number

    def is_booked(self):
        return True if self.__is_booked == "забронирована" else False

    def __str__(self):
        return f"Комната {self.__room_number} {'Забронирована' if self.__is_booked == True else "Свободна"} цена {self.__price_per_night}"


class SingleRoom(Room):
    """
    Класс для одноместного номера
    """

    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)



class DoubleRoom(Room):
    """
    Класс для двухместного номера
    """

    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)


class Suite(Room):
    """
    Класс для люксового номера. Наценка 20%
    """
    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)

    def calculate_price(self, nights):
        return super().calculate_price(nights) * 1, 2


class Booking:
    """
    Класс для управления бронированием
    """
    def __init__(self, room: Room, check_in_date:date, check_out_date: date):
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.nights = (check_out_date - check_in_date).days
        self.total_price = room.calculate_price(self.nights)


    def confirm_booking(self):
        self.room.book()

    def cancel_booking(self):
        self.room.unbook()

    def __str__(self):
        return f"Бронирование: комната {self.room.get_room_number()} забронирована на {self.nights} ночей по цене {self.total_price}"



class Hotel:
    """
    Класс для управления отелем
    """
    def __init__(self, name: str, rooms: list[Room | SingleRoom | DoubleRoom | Suite] | None = None):
        self.name = name
        if rooms is None:
            self.rooms = []
        else:
            self.rooms = rooms

    def add_room(self, room):
        self.rooms.append(room)

    def find_available_room(self):
        for room in self.rooms:
            if not room.is_booked():
                return room
        raise ValueError("все номера забронированы")

    def __str__(self):
        return f"Отель {self.name} имеет {len(self.rooms)} номеров"


if __name__ == "__main__":
    # Создаем отель
    hotel = Hotel("Grand Hotel")

    # Добавляем номера
    hotel.add_room(SingleRoom(101, 100))
    hotel.add_room(DoubleRoom(102, 150))
    hotel.add_room(Suite(103, 300))

    print(hotel)

    # Находим свободный номер и бронируем его
    room_to_book = hotel.find_available_room()
    booking = Booking(room_to_book, date(2024, 9, 1), date(2024, 9, 5))
    print(booking)

    # Подтверждаем бронирование
    booking.confirm_booking()

    # Пробуем снова забронировать ту же комнату
    try:
        booking2 = Booking(room_to_book, date(2024, 9, 10), date(2024, 9, 15))
        booking2.confirm_booking()
    except ValueError as e:
        print(e)

    # Отмена бронирования
    booking.cancel_booking()