import pytest
from framework.base_case import BaseCase
from framework.my_requests import MyRequests
from tests.assertions import Assertions
from tests.data_list_for_test import DataForDelete

id_req = '123-abc-321'
name = 'Jack'
surname = 'Lee'
age = 50
method = 'delete'


class TestDelete(BaseCase):
    def test_delete_user_success(self):
        response_create_user, phone = self.create_new_user(id_req=id_req, name=name, surname=surname, age=age)
        response_delete_user = MyRequests.delete(phone=phone)
        Assertions.checking_request_was_successful(id_req=id_req, method=method, response=response_delete_user)

    def test_delete_user_not_in_base(self):
        new_phone = self.generate_new_unique_phone()

        response = MyRequests.delete(phone=new_phone)
        Assertions.checking_request_failed(id_req=id_req, method=method, response=response)

    @pytest.mark.parametrize('data', DataForDelete.data_list_type_field_for_delete)
    def test_delete_check_type_field(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)

    @pytest.mark.parametrize('data', DataForDelete.data_list_without_one_field_for_delete)
    def test_delete_without_one_field(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)

    @pytest.mark.parametrize('data', DataForDelete.data_list_field_with_none_for_delete)
    def test_delete_field_none(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)
