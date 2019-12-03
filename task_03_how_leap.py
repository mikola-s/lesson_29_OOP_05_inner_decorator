from task_02_how_old import UserAge


class UserLeap(UserAge):

    def __init__(self, user_input, *args, **kwargs):
        super().__init__(user_input)
        self.leap_years_count = 0
        self.leap_years = self.birthday

    @staticmethod
    def is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @property
    def leap_years(self):
        return self.leap_years_count

    @leap_years.setter
    def leap_years(self, birthday):
        for year in range(birthday.year, self.now.year + 1):
            self.leap_years_count += 1 if self.is_leap(year) else 0


if __name__ == "__main__":
    print(f"Високосных в твоей жизни -- {UserLeap('21-12-1999').leap_years} лет")
