import pytest
from framework.base_case import BaseCase
from framework.my_requests import MyRequests
from tests.assertions import Assertions
from tests.data_list_for_test import DataForUpdate

id_req = '123-abc-321'
name = 'Jack'
surname = 'Lee'
age = 50
method = 'update'

id_req_upd = '123-abc-321-upd'
name_upd = 'Jack-upd'
surname_upd = 'Lee-upd'
age_upd = 75


class TestUpdate(BaseCase):
    def test_update_user_success(self):
        response_create_user, phone = self.create_new_user(id_req=id_req, name=name, surname=surname, age=age)
        response_update_user = MyRequests.update(
            id_req=id_req_upd,
            name=name_upd,
            surname=surname_upd,
            phone=phone,
            age=age_upd
        )
        Assertions.checking_request_was_successful(id_req=id_req_upd, method=method, response=response_update_user)

        response_select_user = MyRequests.select(phone=phone)
        Assertions.compare_field_updated_values_from_select_by_phone(
            name=name_upd,
            surname=surname_upd,
            phone=phone,
            age=age_upd,
            response=response_select_user
        )

        MyRequests.delete(phone=phone)

    def test_update_user_with_the_same_data(self):
        response_create_user, phone = self.create_new_user(id_req=id_req, name=name, surname=surname, age=age)
        response_update_user = MyRequests.update(id_req=id_req, name=name, surname=surname, phone=phone, age=age)
        Assertions.checking_request_was_successful(id_req=id_req_upd, method=method, response=response_update_user)

        response_select_user = MyRequests.select(phone=phone)
        Assertions.compare_field_updated_values_from_select_by_phone(
            name=name,
            surname=surname,
            phone=phone,
            age=age,
            response=response_select_user
        )

        MyRequests.delete(phone=phone)

    def test_update_user_with_age_less_than_zero(self):
        response_create_user, phone = self.create_new_user(id_req=id_req, name=name, surname=surname, age=age)
        response_update_user = MyRequests.update(id_req=id_req, name=name, surname=surname, phone=phone, age=-50)
        Assertions.checking_request_failed(id_req=id_req_upd, method=method, response=response_update_user)

        response_select_user = MyRequests.select(phone=phone)
        Assertions.compare_field_updated_values_from_select_by_phone(
            name=name,
            surname=surname,
            phone=phone,
            age=age,
            response=response_select_user
        )

        MyRequests.delete(phone=phone)

    @pytest.mark.parametrize('data', DataForUpdate.data_list_type_field_for_update)
    def test_update_check_type_field(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)

    @pytest.mark.parametrize('data', DataForUpdate.data_list_without_one_field_for_update)
    def test_update_without_one_field(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)

    @pytest.mark.parametrize('data', DataForUpdate.data_list_field_with_none_for_update)
    def test_update_field_none(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)
