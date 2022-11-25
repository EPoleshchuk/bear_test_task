from http import HTTPStatus

import allure

from framework.utilities import AssertUtils, RandomUtils
from project.steps import CommonSteps
from project.utilities.api_utilities import BearApiUtils
from project.utilities.api_utilities import constants


class TestDeleteBear:
    @allure.title("JIRA-4 Delete all bear objects list")
    def test_delete_all_bears(self):
        for _ in range(3):
            CommonSteps.create_default_bear()

        with allure.step("Delete bear objects list"):
            response = BearApiUtils.delete_bears()
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.BODY_OK)

        CommonSteps.assert_empty_bear_list()

        with allure.step("Delete bear objects list again"):
            response = BearApiUtils.delete_bears()
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.BODY_OK)

    @allure.title("JIRA-5 Delete single bear object by existing id")
    def test_delete_single_bear_by_existing_id(self, default_bear):
        with allure.step("Delete bear object by existing id, check data and validate json schema"):
            response = BearApiUtils.delete_bears(default_bear.bear_id)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.BODY_OK)

        with allure.step("Get deleted bear object by id"):
            response = BearApiUtils.get_bears(default_bear.bear_id)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.NOT_FOUND,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.ERROR_NOT_FOUND)

    @allure.step("JIRA-6 Delete single bear object by not existing id and invalid id")
    def test_delete_single_bear_by_not_existing_id_and_invalid_id(self):
        CommonSteps.assert_empty_bear_list()

        with allure.step("Delete single bear object by not existing id but valid"):
            response = BearApiUtils.delete_bears(RandomUtils.get_random_int())
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.NOT_FOUND,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.ERROR_NOT_FOUND)

        with allure.step("Delete single bear object by invalid id"):
            response = BearApiUtils.delete_bears(RandomUtils.get_random_string())
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.ERROR_INVALID_ID)

    @allure.step("JIRA-7 Delete single bear object by id twice")
    def test_delete_single_bear_by_id_twice(self, default_bear):
        with allure.step("Delete single bear object by id for first time"):
            response = BearApiUtils.delete_bears(default_bear.bear_id)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.BODY_OK)

        with allure.step("Delete single bear object by id for second time"):
            response = BearApiUtils.delete_bears(default_bear.bear_id)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.NOT_FOUND,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.ERROR_NOT_FOUND)
