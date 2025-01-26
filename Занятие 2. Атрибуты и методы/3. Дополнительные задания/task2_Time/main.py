class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"Time(hour={self.hour}, minute{self.minute})"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __lt__(self, other):
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False

    def __le__(self, other):
        if self.hour <= other.hour:
            return True
        elif self.hour == other.hour and self.minute <= other.minute:
            return True
        else:
            return False


if __name__ == "__main__":
    time1 = Time(14, 30)
    time2 = Time(16, 45)
    time3 = Time(14, 30)

    print(time1 == time2)  # False
    print(time1 < time2)  # True
    print(time1 <= time3)  # True
