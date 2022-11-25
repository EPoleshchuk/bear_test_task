from http import HTTPStatus
from typing import Union

import allure

from framework.utilities import AssertUtils
from project.models import Bear
from project.utilities.api_utilities import BearApiUtils


class CommonSteps:
    @staticmethod
    @allure.step("Create default bear object")
    def create_default_bear() -> Bear:
        """
        Create default bear, edit it to server repr, check status_code and return created bear object
        :return: created default bear object
        :rtype: Bear
        """
        bear = Bear()
        response = BearApiUtils.create_bear(bear)
        bear.bear_name = bear.bear_name.upper()
        bear.bear_id = int(response.body)

        AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
        return bear

    @staticmethod
    @allure.step("Get bear objects list and assert bear objects list is empty")
    def assert_empty_bear_list() -> None:
        """
        Get all bear objects, check status_code and assert len(bear objects) is equals to zero
        :return: None
        """
        response = BearApiUtils.get_bears()
        AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
        AssertUtils.assert_objects_equal(len(response.body), 0, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)

    @staticmethod
    @allure.step("Get bear object by id and compare with other bear object")
    def get_bear_and_assert_equal_to(bear_id: Union[str, int], bear_object: Bear, compare_id=False) -> None:
        """
        Get bear object by bear_id and assert response body is equal to bear_object
        :param bear_id (str, int): object id to be receive
        :param bear_object (Bear): object to be compared with
        :return: None
        """
        response = BearApiUtils.get_bears(bear_id)
        AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)

        received_data = response.body.to_dict() if compare_id else response.body
        expected_data = bear_object.to_dict() if compare_id else bear_object
        AssertUtils.assert_objects_equal(received_data, expected_data)
