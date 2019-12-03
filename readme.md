## Lesson 29 OOP 5 встроенные декораторы

#### 1. Переделать домашенне задание урока 28 используя полученную информацию


<details>
    <summary> результат (спойлер) </summary>
    
```python



```
</details>

[ccылка на файл](task_01_redo_lsn28_hw.py)

-------

#### 2. Дописать класс начатый на уроке

<details>
    <summary> результат (спойлер) </summary>
    
```python

from datetime import datetime, date


class UserAge:
    def __init__(self, user_input, *args, **kwargs):
        self.birthday = self.check_date(user_input)
        self.age_attr = None
        self.age = self.birthday

    @staticmethod
    def check_date(checked_str):
        try:
            birthday = datetime.strptime(checked_str, "%d-%m-%Y").date()
        except ValueError:
            print('\033[91m--== ПППОЛЬЗОВАТЕЛЬ! Ты ввел неправильную дату! ==--\033[0m')
        assert birthday < date.today(), "ты еще не родилься"
        return birthday

    @property
    def age(self):
        return self.age_attr

    @age.setter
    def age(self, birthday):
        today = date.today()
        self.age_attr = today.year - birthday.year
        if today.month < birthday.month:
            self.age_attr -= 1
        elif today.month == birthday.month and today.day < birthday.day:
            self.age_attr -= 1


if __name__ == "__main__":
    user = UserAge('12-12-2000')
    print(f"Тебе {user.age} лет")


```
</details>


[ccылка на файл](task_02_how_old.py)

-------

#### 3. Дописать класс из второго задания так чтобы он считал количество прожитых високосных лет

<details>
    <summary> результат (спойлер) </summary>
    
```python



```
</details>


[ccылка на файл](task_03_how_leap.py)

-------  
