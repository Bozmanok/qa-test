import random
from framework.my_requests import MyRequests


class BaseCase:
    @staticmethod
    def generate_phone():
        return str(random.randint(0, 999999999)).zfill(9)

    @staticmethod
    def check_user_in_base(phone: str):
        response = MyRequests.select(phone=phone)
        users = list(response['users'])
        if len(users) > 0:
            return True
        elif len(users) == 0:
            return False
        else:
            raise Exception(f'Не удалось выполнить операцию поиска пользователя по номеру {phone}')

    @staticmethod
    def generate_new_unique_phone():
        phone = ''
        result = False
        while not result:
            phone = BaseCase.generate_phone()
            check_user = BaseCase.check_user_in_base(phone)
            if not check_user:
                result = True
        return phone

    def create_new_user(self, name: str, surname: str, age: int, id_req: str = '321-hvhgg-24523'):
        phone = self.generate_new_unique_phone()
        return MyRequests.add(id_req=id_req, name=name, surname=surname, phone=phone, age=age), phone

    @staticmethod
    def select_by_multiple_criteria(name: str = None, surname: str = None, phone: str = None, id_req: str = '123412'):
        if name is not None and surname is not None and phone is not None:
            data = '{' \
                   f'"id": "{id_req}",' \
                   '"method": "select",' \
                   f'"name": "{name}",' \
                   f'"surname": "{surname}",'\
                   f'"phone": "{phone}"' \
                   '}'
        elif name is not None and surname is not None:
            data = '{' \
                   f'"id": "{id_req}",' \
                   '"method": "select",' \
                   f'"name": "{name}",' \
                   f'"surname": "{surname}"' \
                   '}'
        elif surname is not None and phone is not None:
            data = '{' \
                   f'"id": "{id_req}",' \
                   '"method": "select",' \
                   f'"surname": "{surname}",' \
                   f'"phone": "{phone}"' \
                   '}'
        elif name is not None and phone is not None:
            data = '{' \
                   f'"id": "{id_req}",' \
                   '"method": "select",' \
                   f'"name": "{name}",' \
                   f'"phone": "{phone}"' \
                   '}'
        else:
            data = '{' \
                   f'"id": "{id_req}",' \
                   '"method": "select"' \
                   '}'

        return MyRequests.any_method(data)

    @staticmethod
    def select_by_age_criteria(age: int, id_req: str = '123412'):
        data = '{' \
               f'"id": "{id_req}",' \
               '"method": "select",' \
               f'"age": {age}' \
               '}'
        return MyRequests.any_method(data)
