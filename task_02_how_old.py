from datetime import datetime, date


class UserAge:
    def __init__(self, user_input, *args, **kwargs):
        self.birthday = self.check_date(user_input)
        self.age_attr = None
        self.now = date.today()
        self.age = self.birthday

    def check_date(self, checked_str):
        try:
            birthday = datetime.strptime(checked_str, "%d-%m-%Y").date()
        except ValueError:
            print('\033[91m--== ПППОЛЬЗОВАТЕЛЬ! Ты ввел неправильную дату! ==--\033[0m')
        assert birthday < self.now, "ты еще не родилься"
        return birthday

    @property
    def age(self):
        return self.age_attr

    @age.setter
    def age(self, birthday):
        now = self.now
        self.age_attr = self.now.year - birthday.year
        if birthday.month > now.month or birthday.month == now.month and birthday.day > now.day:
            self.age_attr -= 1


if __name__ == "__main__":
    print(f"Тебе {UserAge('02-12-1999').age} лет")
