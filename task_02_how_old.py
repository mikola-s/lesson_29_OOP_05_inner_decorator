from datetime import datetime, date


class InvalidBirthday(Exception):
    pass


class UserAge:
    def __init__(self, user_input, *args, **kwargs):
        self.now = date.today()
        self.birthday = self.check_date(user_input)
        self.age = self.get_age(self.birthday)

    def check_date(self, checked_str):
        try:
            birthday = datetime.strptime(checked_str, "%d-%m-%Y").date()
        except ValueError:
            print('\033[91m--== ПППОЛЬЗОВАТЕЛЬ! Ты ввел неправильную дату! ==--\033[0m')
        if birthday > self.now:
            raise InvalidBirthday("ты еще не родилься")
        return birthday

    def get_age(self, birthday):
        now = self.now
        age = now.year - birthday.year
        if birthday.month > now.month or birthday.month == now.month and birthday.day > now.day:
            age -= 1
        return age


if __name__ == "__main__":
    print(f"Тебе {UserAge('02-12-1999').age} лет")
