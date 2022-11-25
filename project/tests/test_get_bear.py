from http import HTTPStatus

import allure

from framework.utilities import AssertUtils, RandomUtils
from project.steps import CommonSteps
from project.utilities.api_utilities import BearApiUtils
from project.utilities.api_utilities import constants


class TestGetBear:
    @allure.title("JIRA-1 Get all bear objects list")
    def test_get_all_bears(self):
        CommonSteps.assert_empty_bear_list()

        bear = CommonSteps.create_default_bear()

        with allure.step("Get bear objects list, check element inside and validate json schema"):
            response = BearApiUtils.get_bears(validate_json=True)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_object_in_list(bear, response.body)

    @allure.title("JIRA-2 Get single bear object by existing id")
    def test_get_single_bear_by_existing_id(self, default_bear):
        with allure.step("Get bear object by existing id, check data and validate json schema"):
            response = BearApiUtils.get_bears(bear_id=default_bear.bear_id, validate_json=True)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, default_bear)

    @allure.title("JIRA-3 Get single bear object by not existing id and invalid id")
    def test_get_single_bear_by_not_existing_id_and_invalid_id(self):
        CommonSteps.assert_empty_bear_list()

        with allure.step("Get bear object by not existing id but valid"):
            response = BearApiUtils.get_bears(bear_id=RandomUtils.get_random_int())
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.NOT_FOUND,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.ERROR_NOT_FOUND)

        with allure.step("Get bear object by invalid id"):
            response = BearApiUtils.get_bears(bear_id=RandomUtils.get_random_string())
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST)
            AssertUtils.assert_objects_equal(response.body, constants.ERROR_INVALID_ID)
