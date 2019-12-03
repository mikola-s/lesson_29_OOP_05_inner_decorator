from datetime import datetime
from datetime import timedelta
from datetime import date


class UserAge:
    def __init__(self, str, *args, **kwargs):
        self.birthday = self.check_date(str)

    @staticmethod
    def check_date(check_str):
        try:
            birthday = datetime.strptime(check_str, "%d-%m-%Y").date()
        except ValueError():
            print('пользователь, ты ввел неправильную дату')
        else:
            assert birthday < date.today(), "ты еще не родилься"
            return birthday

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birthday.year
        if today.month < self.birthday.month:
            age -= 1
        elif today.month == self.birthday.month and today.day < self.birthday.day:
            age -= 1
        return age


if __name__ == "__main__":

    date_ch = '44-12-1999'

    user = UserAge(date_ch)

    print(f"Тебе {user.age} лет")
