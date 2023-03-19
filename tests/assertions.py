from typing import Any


class Assertions:
    @staticmethod
    def compare_field_id_from_request_and_response(id_req: str, response: Any):
        assert id_req == str(response['id']), 'Идентификаторы запроса не совпадают'

    @staticmethod
    def compare_field_method_from_request_and_response(method: str, response: Any):
        assert method == str(response['method']), 'Методы не совпадают'

    @staticmethod
    def check_success_status_in_response(response: Any):
        assert 'success' == str(response['status']), 'Статус ответа не равен success'

    @staticmethod
    def check_failure_status_in_response(response: Any):
        assert 'failure' == str(response['status']), 'Статус ответа не равен failure'

    @staticmethod
    def checking_request_was_successful(id_req: str, method: str, response: Any):
        Assertions.compare_field_id_from_request_and_response(id_req, response)
        Assertions.compare_field_method_from_request_and_response(method, response)
        Assertions.check_success_status_in_response(response)

    @staticmethod
    def checking_request_failed(id_req: str, method: str, response: Any):
        Assertions.compare_field_id_from_request_and_response(id_req, response)
        Assertions.compare_field_method_from_request_and_response(method, response)
        Assertions.check_failure_status_in_response(response)

    @staticmethod
    def check_field_users_in_response(response: Any):
        assert 'users' in str(response), 'В ответе отсутствует поле users'

    @staticmethod
    def checking_request_select_was_successful(id_req: str, response: Any):
        Assertions.compare_field_id_from_request_and_response(id_req, response)
        Assertions.compare_field_method_from_request_and_response('select', response)
        Assertions.check_success_status_in_response(response)
        Assertions.check_field_users_in_response(response)

    @staticmethod
    def compare_field_updated_values_from_select_by_phone(name: str, surname: str, age: int, phone: str, response: Any):
        users = str(response['users'])
        assert name in users, f'Значение поля name не соответсвует значению {name}'
        assert surname in users, f'Значение поля surname не соответсвует значению {surname}'
        assert str(age) in users, f'Значение поля age не соответсвует значению {age}'
        assert phone in users, f'Значение поля phone не соответсвует значению {phone}'

    @staticmethod
    def compare_field_values_from_select_by_name(name: str, response: Any):
        users = list(response['users'])
        count_users = len(users)
        assert count_users >= 1, 'В списке users нет пользователей'
        for i in range(count_users):
            assert name == str(users[i]['name']), f'Значение в поле name не соответствует значению {name}'

    @staticmethod
    def compare_field_values_from_select_by_surname(surname: str, response: Any):
        users = list(response['users'])
        count_users = len(users)
        assert count_users >= 1, 'В списке users нет пользователей'
        for i in range(count_users):
            assert surname == str(users[i]['surname']), f'Значение в поле surname не соответствует значению {surname}'

    @staticmethod
    def compare_field_values_from_select_by_phone(phone: str, response: Any):
        users = list(response['users'])
        count_users = len(users)
        assert count_users == 1, 'В списке users пользователей больше одного или нет совсем'
        for i in range(count_users):
            assert phone == str(users[i]['phone']), f'Значение в поле phone не соответствует значению {phone}'

    @staticmethod
    def check_empty_list_users_from_select(response: Any):
        users = list(response['users'])
        assert len(users) == 0, 'Cписок users не пустой'

    @staticmethod
    def checking_request_select_failed(id_req: str, response: Any):
        Assertions.compare_field_id_from_request_and_response(id_req, response)
        Assertions.check_failure_status_in_response(response)
        assert 'reason' in response, 'Нет поля reason с описанием ошибки'
        assert 'method' not in response, 'В ответе указано поле method'
        assert 'users' not in response, 'В ответе указано поле users'
