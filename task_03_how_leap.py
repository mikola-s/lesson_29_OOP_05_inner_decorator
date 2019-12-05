from task_02_how_old import UserAge


class UserLeap(UserAge):

    def __init__(self, user_input, *args, **kwargs):
        super().__init__(user_input)
        self.leap_years = self.get_leap_years()

    @staticmethod
    def is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def get_leap_years(self):
        life_period = range(self.birthday.year, self.now.year + 1)
        return sum([self.is_leap(year) for year in life_period])


if __name__ == "__main__":
    print(f"Високосных в твоей жизни -- {UserLeap('21-12-1999').leap_years} лет")
