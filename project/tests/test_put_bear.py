from http import HTTPStatus

import allure
import pytest

from framework.utilities import AssertUtils, RandomUtils
from project.models import Bear
from project.steps import CommonSteps
from project.utilities import BearUtils
from project.utilities.api_utilities import BearApiUtils
from project.utilities.api_utilities import constants


class TestPutBear:
    @allure.title("JIRA-23 Update single bear object by existing id")
    def test_put_single_bear_by_existing_id(self, default_bear):
        with allure.step("Update bear object by existing id"):
            bear_name = RandomUtils.get_random_string()
            response = BearApiUtils.update_bear(default_bear.bear_id, bear_name=bear_name)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.BODY_OK)
            default_bear.bear_name = bear_name.upper()

        CommonSteps.get_bear_and_assert_equal_to(default_bear.bear_id, default_bear)

    @allure.title("JIRA-24 Update single bear object by not existing id and invalid id")
    def test_put_single_bear_by_not_existing_id_and_invalid_id(self):
        CommonSteps.assert_empty_bear_list()

        with allure.step("Update bear object by not existing but valid id"):
            response = BearApiUtils.update_bear(RandomUtils.get_random_int())
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.NOT_FOUND,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.ERROR_NOT_FOUND)

        with allure.step("Update bear object by invalid id"):
            response = BearApiUtils.update_bear(RandomUtils.get_random_string())
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.ERROR_INVALID_ID)

    @allure.title("JIRA-25 Update bear_type of bear object with correct values")
    @pytest.mark.parametrize(Bear.FIELD_TYPE, BearUtils.get_valid_values(Bear.FIELD_TYPE))
    def test_put_bear_with_correct_bear_type(self, bear_type, default_bear):
        with allure.step("Update bear object with correct bear_type"):
            response = BearApiUtils.update_bear(default_bear.bear_id, bear_type=bear_type)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.BODY_OK)
            default_bear.bear_type = bear_type

        CommonSteps.get_bear_and_assert_equal_to(default_bear.bear_id, default_bear)

    @allure.title("JIRA-26 Update bear_type of bear object with incorrect values")
    @pytest.mark.parametrize(Bear.FIELD_TYPE, BearUtils.get_invalid_values(Bear.FIELD_TYPE))
    def test_put_bear_with_incorrect_bear_type(self, bear_type, default_bear):
        with allure.step("Update bear object with incorrect bear_type"):
            response = BearApiUtils.update_bear(default_bear.bear_id, bear_type=bear_type)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.ERROR_INVALID_VALUE_TMP.format(Bear.FIELD_TYPE))

        CommonSteps.get_bear_and_assert_equal_to(default_bear.bear_id, default_bear)

    @allure.title("JIRA-27 Update bear_type of bear object with incorrect value data types")
    @pytest.mark.parametrize(Bear.FIELD_TYPE, BearUtils.get_invalid_data_types(Bear.FIELD_TYPE))
    def test_put_bear_with_incorrect_bear_type_data_types(self, bear_type, default_bear):
        with allure.step("Update bear object with incorrect bear_type data types"):
            response = BearApiUtils.update_bear(default_bear.bear_id, bear_type=bear_type)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body,
                                             constants.ERROR_INVALID_DATA_TYPE_TMP.format(Bear.FIELD_TYPE))

        CommonSteps.get_bear_and_assert_equal_to(default_bear.bear_id, default_bear)

    @allure.title("JIRA-28 Update bear_name of bear object with correct values")
    @pytest.mark.parametrize(Bear.FIELD_NAME, BearUtils.get_valid_values(Bear.FIELD_NAME))
    def test_put_bear_with_correct_bear_name(self, bear_name, default_bear):
        with allure.step("Update bear object with correct bear_name"):
            response = BearApiUtils.update_bear(default_bear.bear_id, bear_name=bear_name)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.BODY_OK)
            default_bear.bear_name = bear_name.upper()

        CommonSteps.get_bear_and_assert_equal_to(default_bear.bear_id, default_bear)

    @allure.title("JIRA-29 Update bear_name of bear object with incorrect value data types")
    @pytest.mark.parametrize(Bear.FIELD_NAME, BearUtils.get_invalid_data_types(Bear.FIELD_NAME))
    def test_put_bear_with_incorrect_bear_name_data_types(self, bear_name, default_bear):
        with allure.step("Update bear object with incorrect bear_name data types"):
            response = BearApiUtils.update_bear(default_bear.bear_id, bear_name=bear_name)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body,
                                             constants.ERROR_INVALID_DATA_TYPE_TMP.format(Bear.FIELD_NAME))

        CommonSteps.get_bear_and_assert_equal_to(default_bear.bear_id, default_bear)

    @allure.title("JIRA-30 Update bear_age of bear object with correct values")
    @pytest.mark.parametrize(Bear.FIELD_AGE, BearUtils.get_valid_values(Bear.FIELD_AGE))
    def test_put_bear_with_correct_bear_age(self, bear_age, default_bear):
        with allure.step("Update bear object with correct bear_age"):
            response = BearApiUtils.update_bear(default_bear.bear_id, bear_age=bear_age)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.BODY_OK)
            default_bear.bear_age = bear_age

        CommonSteps.get_bear_and_assert_equal_to(default_bear.bear_id, default_bear)

    @allure.title("JIRA-31 Update bear_age of bear object with incorrect values")
    @pytest.mark.parametrize(Bear.FIELD_AGE, BearUtils.get_invalid_values(Bear.FIELD_AGE))
    def test_put_bear_with_incorrect_bear_age(self, bear_age, default_bear):
        with allure.step("Update bear object with incorrect bear_age"):
            response = BearApiUtils.update_bear(default_bear.bear_id, bear_age=bear_age)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body,
                                             constants.ERROR_VALUE_OUT_OF_RANGE_TMP.format(Bear.FIELD_AGE))

        CommonSteps.get_bear_and_assert_equal_to(default_bear.bear_id, default_bear)

    @allure.title("JIRA-32 Update bear_age of bear object with incorrect value data types")
    @pytest.mark.parametrize(Bear.FIELD_AGE, BearUtils.get_invalid_data_types(Bear.FIELD_AGE))
    def test_put_bear_with_incorrect_bear_age_data_types(self, bear_age, default_bear):
        with allure.step("Update bear object with incorrect bear_age data types"):
            response = BearApiUtils.update_bear(default_bear.bear_id, bear_age=bear_age)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body,
                                             constants.ERROR_INVALID_DATA_TYPE_TMP.format(Bear.FIELD_AGE))

        CommonSteps.get_bear_and_assert_equal_to(default_bear.bear_id, default_bear)

    @allure.title("JIRA-33 Update bear object with empty body")
    def test_put_bear_with_empty_body(self, default_bear):
        with allure.step("Update bear object with empty body"):
            response = BearApiUtils.update_bear(default_bear.bear_id)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.ERROR_PLS_FILL_AT_LEAST_ONE_PARAMETER)

        CommonSteps.get_bear_and_assert_equal_to(default_bear.bear_id, default_bear)

    @allure.title("JIRA-34 Update all fields of bear object with correct values")
    def test_put_all_bear_fields_with_correct_values(self, default_bear):
        with allure.step("Update bear object with all correct fields"):
            bear_type = RandomUtils.get_random_choice(
                BearUtils.get_valid_values(Bear.FIELD_TYPE), except_for=Bear.DEFAULT_BEAR_TYPE)
            bear_name = RandomUtils.get_random_choice(
                BearUtils.get_valid_values(Bear.FIELD_NAME), except_for=Bear.DEFAULT_BEAR_NAME)
            bear_age = RandomUtils.get_random_choice(
                BearUtils.get_valid_values(Bear.FIELD_AGE), except_for=Bear.DEFAULT_BEAR_AGE)
            response = BearApiUtils.update_bear(default_bear.bear_id, bear_type=bear_type, bear_name=bear_name,
                                                bear_age=bear_age)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.BODY_OK)
            default_bear.bear_type = bear_type
            default_bear.bear_name = bear_name.upper()
            default_bear.bear_age = bear_age

        CommonSteps.get_bear_and_assert_equal_to(default_bear.bear_id, default_bear)

    @allure.title("JIRA-35 Update all fields of bear object with incorrect values")
    def test_put_all_bear_field_with_incorrect_values(self, default_bear):
        with allure.step("Update bear object with all incorrect fields"):
            response = BearApiUtils.update_bear(default_bear.bear_id, bear_type=None, bear_name=None, bear_age=None)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            error_str = "\n".join(
                [constants.ERROR_INVALID_DATA_TYPE_TMP.format(field) for field in Bear.EDITABLE_FIELDS])
            AssertUtils.assert_objects_equal(response.body, error_str)

        CommonSteps.get_bear_and_assert_equal_to(default_bear.bear_id, default_bear)

    @allure.title("JIRA-36 Update bear object with not supported field")
    def test_put_bear_with_not_supported_field(self, default_bear):
        with allure.step("Update bear object with not supported field"):
            not_supported_field = RandomUtils.get_random_string()
            response = BearApiUtils.update_bear(default_bear.bear_id, not_supported_field=not_supported_field)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.BAD_REQUEST,
                                             AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(
                response.body, constants.ERROR_NOT_SUPPORTED_FIELD_TMP.format(not_supported_field))

        CommonSteps.get_bear_and_assert_equal_to(default_bear.bear_id, default_bear)

    @allure.title("JIRA-37 Update bear with data like another bear object")
    def test_put_bear_with_data_like_another_bear(self, default_bear):
        with allure.step("Create bear object #2 which is different from the default"):
            bear2_name = RandomUtils.get_random_choice(
                BearUtils.get_valid_values(Bear.FIELD_NAME), except_for=Bear.DEFAULT_BEAR_NAME)
            bear2_type = RandomUtils.get_random_choice(
                BearUtils.get_valid_values(Bear.FIELD_TYPE), except_for=Bear.DEFAULT_BEAR_TYPE)
            bear2_age = RandomUtils.get_random_choice(
                BearUtils.get_valid_values(Bear.FIELD_AGE), except_for=Bear.DEFAULT_BEAR_AGE)
            bear2 = Bear(bear_type=bear2_type, bear_name=bear2_name, bear_age=bear2_age)
            response = BearApiUtils.create_bear(bear2)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            bear2.bear_id = int(response.body)

        with allure.step("Update bear object #2 with default bear object data"):
            response = BearApiUtils.update_bear(
                bear2.bear_id, bear_type=Bear.DEFAULT_BEAR_TYPE,
                bear_name=Bear.DEFAULT_BEAR_NAME, bear_age=Bear.DEFAULT_BEAR_AGE)
            AssertUtils.assert_objects_equal(response.status_code, HTTPStatus.OK, AssertUtils.WRONG_STATUS_CODE_ERR_MSG)
            AssertUtils.assert_objects_equal(response.body, constants.BODY_OK)

        CommonSteps.get_bear_and_assert_equal_to(bear2.bear_id, default_bear, compare_id=False)
