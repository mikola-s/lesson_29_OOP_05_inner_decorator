import bcrypt


class CustomException(Exception):
    def __init__(self, text, *args, **kwargs):
        print(text)


class AccessDeniedException(Exception):
    def __init__(self, text, *args, **kwargs):
        print(text)


class Users:
    def __init__(self, first_name=None,
                 last_name=None,
                 password=None,
                 addresses=None,
                 phones=None):
        self.__salt = None
        self.first_name = first_name
        self.last_name = last_name
        self._password = self._set_password(password)
        self.addresses = self._check_addresses(addresses)
        self.phones = self._check_phones(phones)

    def __getattribute__(self, name):
        if name == "_password":
            raise (AccessDeniedException("в доступе отказано"))
        return super(Users, self).__getattribute__(name)

    def _set_password(self, passwd):
        """создает хешированный пароль"""
        self.__salt = bcrypt.gensalt()
        return bcrypt.hashpw(passwd.encode(), self.__salt)

    def check_password(self, input_str: str) -> bool:
        """ проверяет строку на совпадение с паролем """
        check_str = bcrypt.hashpw(input_str.encode(), self.__salt)
        return check_str == self.__dict__["_password"] if True else False

    # """ короткий вариант проверки телефонов """
    # def __check_phones(self, phones_list) -> list:
    #     if len(phones_list) < 4:
    #         if all([(True if len(phone) < 16 else False) for phone in phones_list]):
    #             return phones_list
    #         raise CustomException("неправильный телефон")
    #     raise CustomException("много телефонов")

    def _check_phones(self, phones_list) -> list:
        """ проверяет количество телефонов (< 4) и количество символов ( < 16) """
        if self._check_phones_count(phones_list):
            if self._check_phones_length(phones_list):
                return phones_list
            raise CustomException("неправильный телефон")
        raise CustomException("много телефонов")

    def _check_phones_count(self, phones_list):
        """ проверяет количество телефонов """
        return True if len(phones_list) < 4 else False

    def _check_phones_length(self, phones_list):
        """ проверяет длинну телефонов """
        for phone in phones_list:
            if len(phone) > 15:
                raise CustomException("Неправильный телефон")
        return True

    def _check_addresses(self, addresses) -> dict:
        """ проверяет соответствие адреса шаблону """
        check_list = ["country", "city", "billing_address", "index"]
        for address in addresses:
            for item in address:
                if item not in check_list:
                    raise CustomException("неправильный адрес")
        return addresses

        # то же в 4 строки
        # check_list = ["country", "city", "billing_address", "index"]
        # if all([True if item in check_list else False for item in list(address.keys())]):
        #     raise CustomException("неправильный адрес")
        # return addresses


arrival_addresses = [{"country": "Ukraine",
                      "city": "Kharkov",
                      "billing_address": "111 Shevchenko street",
                      "index": "111-111"},
                     {"country": "USA",
                      "city": "New York",
                      "billing_address": "111 Shevchenko street",
                      "index": "111-111"},
                     ]

arrival_phones = ["+380501111111",
                  "+380501111111",
                  "+380501111222",
                  ]

user = Users(
    first_name='Petrenko',
    last_name='Petro',
    password='1234',
    addresses=arrival_addresses,
    phones=arrival_phones,
)

print(f"Check password '1234' -- {user.check_password('1234')}")

# print(user.__dict__)

# print(dir(user))
