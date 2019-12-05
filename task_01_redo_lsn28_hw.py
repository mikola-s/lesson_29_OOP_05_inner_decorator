from bcrypt import gensalt, hashpw, checkpw


class CustomException(Exception):
    pass


class AccessDeniedException(Exception):
    pass


class Users:
    def __init__(self, first_name: str, last_name: str, password: str, addresses: list, phones: list):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.password = password
        self.addresses = self._check_addresses(addresses)
        self.phones = self._check_phones(phones)

    def get_full_name(self) -> str:
        """ возврацает полное имя"""
        return f"{self.first_name} {self.last_name}"

    @property
    def password(self) -> None:
        raise AccessDeniedException('в доступе отказано')

    @password.setter
    def password(self, pwd: str) -> None:
        self.__password = self.hash_password(pwd)

    @staticmethod
    def hash_password(pwd: str) -> bool:
        return hashpw(pwd.encode(), gensalt())

    def check_password(self, input_str: str) -> bool:
        """ проверяет строку на совпадение с паролем """
        return checkpw(input_str.encode(), self.__password)

    def _check_phones(self, phones_list: list) -> list:
        """ проверяет количество телефонов (< 4) и количество символов ( < 16) """
        if self._check_phones_count(phones_list):
            if self._check_phones_length(phones_list):
                return phones_list
            raise CustomException("неправильный телефон")
        raise CustomException("много телефонов")

    @staticmethod
    def _check_phones_count(phones_list: list) -> bool:
        """ проверяет количество телефонов """
        return len(phones_list) < 4

    @staticmethod
    def _check_phones_length(phones_list: list) -> bool:
        """ проверяет длинну телефонов """
        return all(len(phone) < 16 for phone in phones_list)

    @staticmethod
    def _check_addresses(addresses: list) -> list:
        """ проверяет соответствие адреса шаблону """
        check_list = ["country", "city", "billing_address", "index"]
        for address in addresses:
            if not all([item in address for item in check_list]):
                raise CustomException("неправильный адрес")
        return addresses


arrival_addresses = [{"country": "Ukraine",
                      "city": "Kharkov",
                      "billing_address": "111 Shevchenko street",
                      "index": "111-111"},
                     {"country": "USA",
                      "city": "New York",
                      "billing_address": "111 Shevchenko street",
                      "index": "111-111"},
                     ]

arrival_phones = ["+380501111121",
                  "+380501111111",
                  "+380501111111",
                  # "+380501111111+380501111111", # для проверуи длинны
                  # "+380501111222", # для проверки количества
                  ]

user = Users(
    first_name='Petrenko',
    last_name='Petro',
    password='1234',
    addresses=arrival_addresses,
    phones=arrival_phones,
)

print(f"Check password '1234' -- {user.check_password('1234')}")


# print(user.password)

