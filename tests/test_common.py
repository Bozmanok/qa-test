import pytest
from framework.base_case import BaseCase
from framework.my_requests import MyRequests
from tests.assertions import Assertions
from tests.data_list_for_test import DataForCommon

id_req = '123-abc-321'
name = 'Jack'
surname = 'Lee'
age = 50
method = 'select'
filter_phone = '1234567890'


class TestCommon(BaseCase):
    def test_request_empty(self):
        response = MyRequests.any_method(data='{}')
        Assertions.check_failure_status_in_response(response=response)

    @pytest.mark.parametrize('data', DataForCommon.data_list_type_method)
    def test_check_type_methods(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)

    @pytest.mark.parametrize('data', DataForCommon.data_list_without_field_method)
    def test_without_field_method(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)

    @pytest.mark.parametrize('data', DataForCommon.data_list_method_is_none)
    def test_field_method_none(self, data):
        response = MyRequests.any_method(data=data)
        Assertions.check_failure_status_in_response(response=response)
