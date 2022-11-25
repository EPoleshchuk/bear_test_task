from http import HTTPStatus

import allure
import pytest

from framework.utilities import AssertUtils
from project.models import Bear
from project.steps import CommonSteps
from project.utilities import BearUtils
from project.utilities.api_utilities import BearApiUtils
from project.utilities.api_utilities import constants


class TestPostBear:
    @allure.title("JIRA-8 Create bear object with correct data")
    def test_post_bear_with_correct_data(self):
        bear = CommonSteps.create_default_bear()

        CommonSteps.get_bear_and_assert_equal_to(bear.bear_id, bear)

    @allure.title("JIRA-9 Create bear object with different correct bear_type key values")
    @pytest.mark.parametrize(Bear.FIELD_TYPE, BearUtils.get_valid_values(Bear.FIELD_TYPE))
    def test_post_bear_with_correct_bear_type(self, bear_type):
        with allure.step("Create bear object with correct data and correct bear_type"):
            bear = Bear(bear_type=bear_type)
            response = BearApiUtils.create_bear(bear)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            bear.bear_name = bear.bear_name.upper()
            bear.bear_id = int(response.body)

        CommonSteps.get_bear_and_assert_equal_to(bear.bear_id, bear)

    @allure.title("JIRA-11 Create bear object with different incorrect bear_type key values")
    @pytest.mark.parametrize(Bear.FIELD_TYPE, BearUtils.get_invalid_values(Bear.FIELD_TYPE))
    def test_post_bear_with_incorrect_bear_type(self, bear_type):
        with allure.step("Create bear object with correct data and incorrect bear_type"):
            bear = Bear(bear_type=bear_type)
            response = BearApiUtils.create_bear(bear)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.ERROR_INVALID_VALUE_TMP.format(Bear.FIELD_TYPE))

        CommonSteps.assert_empty_bear_list()

    @allure.title("JIRA-10 Create bear object with different incorrect bear_type key value data types")
    @pytest.mark.parametrize(Bear.FIELD_TYPE, BearUtils.get_invalid_data_types(Bear.FIELD_TYPE))
    def test_post_bear_with_incorrect_bear_type_data_types(self, bear_type):
        with allure.step("Create bear object with correct data and invalid bear_type data types"):
            bear = Bear(bear_type=bear_type)
            response = BearApiUtils.create_bear(bear)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body,
                                             constants.ERROR_INVALID_DATA_TYPE_TMP.format(Bear.FIELD_TYPE))

        CommonSteps.assert_empty_bear_list()

    @allure.title("JIRA-12 Create bear object with different correct bear_age key values")
    @pytest.mark.parametrize(Bear.FIELD_AGE, BearUtils.get_valid_values(Bear.FIELD_AGE))
    def test_post_bear_with_correct_bear_age(self, bear_age):
        with allure.step("Create bear object with correct data and valid bear_age"):
            bear = Bear(bear_age=bear_age)
            response = BearApiUtils.create_bear(bear)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            bear.bear_name = bear.bear_name.upper()
            bear.bear_id = int(response.body)

        CommonSteps.get_bear_and_assert_equal_to(bear.bear_id, bear)

    @allure.title("JIRA-13 Create bear object with different incorrect bear_age key values")
    @pytest.mark.parametrize(Bear.FIELD_AGE, BearUtils.get_invalid_values(Bear.FIELD_AGE))
    def test_post_bear_with_incorrect_bear_age(self, bear_age):
        with allure.step("Create bear object with correct data and incorrect bear_age"):
            bear = Bear(bear_age=bear_age)
            response = BearApiUtils.create_bear(bear)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body,
                                             constants.ERROR_VALUE_OUT_OF_RANGE_TMP.format(Bear.FIELD_AGE))

        CommonSteps.assert_empty_bear_list()

    @allure.title("JIRA-14 Create bear object with different correct bear_age key value data type")
    @pytest.mark.parametrize(Bear.FIELD_AGE, BearUtils.get_invalid_data_types(Bear.FIELD_AGE))
    def test_post_bear_with_incorrect_bear_age_data_types(self, bear_age):
        with allure.step("Create bear object with correct data and incorrect bear_age data types"):
            bear = Bear(bear_age=bear_age)
            response = BearApiUtils.create_bear(bear)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body,
                                             constants.ERROR_INVALID_DATA_TYPE_TMP.format(Bear.FIELD_AGE))

        CommonSteps.assert_empty_bear_list()

    @allure.title("JIRA-15 Create bear object with different correct bear_name key values")
    @pytest.mark.parametrize(Bear.FIELD_NAME, BearUtils.get_valid_values(Bear.FIELD_NAME))
    def test_post_bear_with_correct_bear_name(self, bear_name):
        with allure.step("Create bear object with correct data and correct bear_name"):
            bear = Bear(bear_name=bear_name)
            response = BearApiUtils.create_bear(bear)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            bear.bear_name = bear.bear_name.upper()
            bear.bear_id = int(response.body)

        CommonSteps.get_bear_and_assert_equal_to(bear.bear_id, bear)

    @allure.title("JIRA-16 Create bear object with different incorrect bear_name key value data types")
    @pytest.mark.parametrize(Bear.FIELD_NAME, BearUtils.get_invalid_data_types(Bear.FIELD_NAME))
    def test_post_bear_with_incorrect_bear_name_data_types(self, bear_name):
        with allure.step("Create bear object with correct data and incorrect bear_name data types"):
            bear = Bear(bear_name=bear_name)
            response = BearApiUtils.create_bear(bear)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body,
                                             constants.ERROR_INVALID_DATA_TYPE_TMP.format(Bear.FIELD_NAME))

        CommonSteps.assert_empty_bear_list()

    @allure.title("JIRA-18 Create bear object with all incorrect values")
    def test_post_bear_with_all_incorrect_values(self):
        with allure.step("Create bear object with all incorrect values"):
            bear = Bear(bear_type=None, bear_name=None, bear_age=None)
            response = BearApiUtils.create_bear(bear)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            error_str = "\n".join(
                [constants.ERROR_INVALID_DATA_TYPE_TMP.format(field) for field in Bear.EDITABLE_FIELDS])
            AssertUtils.assert_objects_equal(response.body, error_str)

        CommonSteps.assert_empty_bear_list()

    @allure.title("JIRA-21 Check autoincrement bear_id key value after deleting")
    def test_autoincrement_bear_id_after_deleting(self, default_bear):
        with allure.step("Delete bear object by id"):
            response = BearApiUtils.delete_bears(default_bear.bear_id)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.BODY_OK)

        with allure.step("Create new bear object and, compare data and bear_id fields"):
            new_bear = CommonSteps.create_default_bear()
            AssertUtils.assert_objects_equal(new_bear.bear_id, default_bear.bear_id + 1)

            CommonSteps.get_bear_and_assert_equal_to(new_bear.bear_id, new_bear)

    @allure.title("JIRA-22 Create two bear objects with the same values")
    def test_post_two_bears_with_same_values(self):
        bear1 = CommonSteps.create_default_bear()

        bear2 = CommonSteps.create_default_bear()

        with allure.step("Compare two bear objects data and bear_id fields"):
            AssertUtils.assert_objects_equal(bear2.bear_id, bear1.bear_id + 1)

            bears = [BearApiUtils.get_bears(bear.bear_id).body for bear in (bear1, bear2)]
            AssertUtils.soft_assert(bears[0].to_dict(), bears[1].to_dict())
            AssertUtils.assert_objects_equal(bears[1].bear_id, bears[0].bear_id + 1,
                                             "Bear1 id [{}] should differ from Bear2 id [{}] by one")
