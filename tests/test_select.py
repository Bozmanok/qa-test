import pytest
from framework.base_case import BaseCase
from framework.my_requests import MyRequests
from tests.assertions import Assertions
from tests.data_list_for_test import DataForSelect

id_req = '123-abc-321'
name = 'Jack'
surname = 'Lee'
age = 50
method = 'select'
filter_phone = '1234567890'


class TestSelect(BaseCase):
    def test_select_user_success_by_name(self):
        response_create_user, phone = self.create_new_user(id_req=id_req, name=name, surname=surname, age=age)

        response_select_user = MyRequests.select(name=name)
        Assertions.compare_field_values_from_select_by_name(name=name, response=response_select_user)

        MyRequests.delete(phone=phone)

    def test_select_multiple_users_success_by_surname(self):
        response_first_user, first_phone = self.create_new_user(id_req=id_req, name=name, surname=surname, age=age)
        response_second_user, second_phone = self.create_new_user(id_req='32-dfg', name='John', surname=surname, age=32)

        response_select_user = MyRequests.select(surname=surname)
        Assertions.compare_field_values_from_select_by_surname(
            surname=surname,
            response=response_select_user
        )

        MyRequests.delete(phone=first_phone)
        MyRequests.delete(phone=second_phone)

    def test_select_user_success_by_phone(self):
        response_user, phone = self.create_new_user(id_req=id_req, name=name, surname=surname, age=age)

        response_select_user = MyRequests.select(phone=phone)
        Assertions.compare_field_values_from_select_by_phone(
            phone=phone,
            response=response_select_user
        )

        MyRequests.delete(phone=phone)

    def test_select_user_not_in_base_by_phone(self):
        phone = self.generate_new_unique_phone()

        response_select_user = MyRequests.select(phone=phone)
        Assertions.check_empty_list_users_from_select(response=response_select_user)

    def test_select_user_not_in_base_by_name(self):
        phone = self.generate_new_unique_phone()

        response_select_user = MyRequests.select(name=phone)
        Assertions.check_empty_list_users_from_select(response=response_select_user)

    def test_select_user_not_in_base_by_surname(self):
        phone = self.generate_new_unique_phone()

        response_select_user = MyRequests.select(surname=phone)
        Assertions.check_empty_list_users_from_select(response=response_select_user)

    def test_select_by_name_and_surname(self):
        response_select_user = self.select_by_multiple_criteria(id_req=id_req, name=name, surname=surname)
        Assertions.checking_request_select_failed(id_req=id_req, response=response_select_user)

    def test_select_by_name_and_phone(self):
        response_select_user = self.select_by_multiple_criteria(id_req=id_req, name=name, phone=filter_phone)
        Assertions.checking_request_select_failed(id_req=id_req, response=response_select_user)

    def test_select_by_surname_and_phone(self):
        response_select_user = self.select_by_multiple_criteria(id_req=id_req, surname=surname, phone=filter_phone)
        Assertions.checking_request_select_failed(id_req=id_req, response=response_select_user)

    def test_select_without_criteria(self):
        response_select_user = self.select_by_multiple_criteria(id_req=id_req)
        Assertions.checking_request_select_failed(id_req=id_req, response=response_select_user)

    def test_select_by_age(self):
        response_select_user = self.select_by_age_criteria(id_req=id_req, age=50)
        Assertions.checking_request_select_failed(id_req=id_req, response=response_select_user)

    @pytest.mark.parametrize('data', DataForSelect.data_list_type_field_for_select)
    def test_select_check_type_field(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)

    @pytest.mark.parametrize('data', DataForSelect.data_list_without_one_field_for_select)
    def test_select_without_one_field(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)

    @pytest.mark.parametrize('data', DataForSelect.data_list_field_with_none_for_select)
    def test_select_field_none(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)
