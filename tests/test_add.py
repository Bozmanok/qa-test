import pytest
from framework.base_case import BaseCase
from framework.my_requests import MyRequests
from tests.assertions import Assertions
from tests.data_list_for_test import DataForAdd

id_req = '123-abc-321'
name = 'Jack'
surname = 'Lee'
age = 50
method = 'add'


class TestAdd(BaseCase):
    def test_create_user_success(self):
        response, phone = self.create_new_user(id_req=id_req, name=name, surname=surname, age=age)
        Assertions.checking_request_was_successful(id_req=id_req, method=method, response=response)

        MyRequests.delete(phone=phone)

    def test_repeat_create_user_with_new_phone(self):
        response_first_user, phone = self.create_new_user(id_req=id_req, name=name, surname=surname, age=age)
        new_phone = self.generate_new_unique_phone()
        response = MyRequests.add(id_req=id_req, name=name, surname=surname, phone=new_phone, age=age)
        Assertions.checking_request_was_successful(id_req=id_req, method=method, response=response)

        MyRequests.delete(phone=phone)
        MyRequests.delete(phone=new_phone)

    def test_repeat_create_user(self):
        response_first_user, phone = self.create_new_user(id_req=id_req, name=name, surname=surname, age=age)
        response = MyRequests.add(id_req=id_req, name=name, surname=surname, phone=phone, age=age)
        Assertions.checking_request_failed(id_req=id_req, method=method, response=response)

    def test_create_user_with_age_is_zero(self):
        response, phone = self.create_new_user(id_req=id_req, name=name, surname=surname, age=0)
        Assertions.checking_request_was_successful(id_req=id_req, method=method, response=response)

        MyRequests.delete(phone=phone)

    def test_create_user_with_age_less_than_zero(self):
        response, phone = self.create_new_user(id_req=id_req, name=name, surname=surname, age=-50)
        Assertions.checking_request_failed(id_req=id_req, method=method, response=response)

    @pytest.mark.parametrize('data', DataForAdd.data_list_type_field_for_add)
    def test_add_check_type_field(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)

    @pytest.mark.parametrize('data', DataForAdd.data_list_without_one_field_for_add)
    def test_add_without_one_field(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)

    @pytest.mark.parametrize('data', DataForAdd.data_list_field_with_none_for_add)
    def test_add_field_none(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)
