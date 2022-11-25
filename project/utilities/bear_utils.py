from typing import List

from framework.constants import DataTypes
from framework.utilities import RandomUtils, TestDataUtils
from project.models import Bear


class BearUtils:
    """
    Class with Bear object utilities
    """
    BEAR_AGE_LIMITS = [0, 100]
    CORRECT_BEAR_TYPES = ["POLAR", "BROWN", "BLACK", "GUMMY"]

    DATA_TYPES = {Bear.FIELD_ID: DataTypes.INTEGER,
                  Bear.FIELD_TYPE: DataTypes.STRING,
                  Bear.FIELD_NAME: DataTypes.STRING,
                  Bear.FIELD_AGE: DataTypes.NUMBER}

    @staticmethod
    def get_valid_values(field_name: str) -> List:
        """
        Get valid values for bear field field_name
        :param field_name (str): bear field name
        :return: list with valid values
        :rtype: list
        """
        valid_values = {
            Bear.FIELD_TYPE: BearUtils.CORRECT_BEAR_TYPES,
            Bear.FIELD_NAME: ["", RandomUtils.get_random_string()],
            Bear.FIELD_AGE: TestDataUtils.get_boundary_values(BearUtils.BEAR_AGE_LIMITS, step=0.01, valid=True)}

        if field_name not in valid_values:
            raise NotImplementedError(f"Valid values for {field_name} field not implemented!")
        return valid_values[field_name]

    @staticmethod
    def get_invalid_values(field_name: str) -> List:
        """
        Get invalid values for bear field field_name
        :param field_name (str): bear field name
        :return: list with invalid values
        :rtype: list
        """
        invalid_values = {
            Bear.FIELD_TYPE: [value.lower() for value in BearUtils.CORRECT_BEAR_TYPES] +
                             ["", RandomUtils.get_random_string()],
            Bear.FIELD_AGE: TestDataUtils.get_boundary_values(BearUtils.BEAR_AGE_LIMITS, step=0.01, valid=False)}

        if field_name not in invalid_values:
            raise NotImplementedError(f"Invalid values for {field_name} field not implemented!")
        return invalid_values[field_name]

    @staticmethod
    def get_invalid_data_types(field_name: str) -> List:
        """
        Get invalid data types for bear field field_name
        :param field_name (str): bear field name
        :return: list with invalid data types
        :rtype: list
        """
        invalid_data_types = {
            Bear.FIELD_TYPE: TestDataUtils.get_wrong_data_types(BearUtils.DATA_TYPES[Bear.FIELD_TYPE]),
            Bear.FIELD_NAME: TestDataUtils.get_wrong_data_types(BearUtils.DATA_TYPES[Bear.FIELD_NAME]),
            Bear.FIELD_AGE: TestDataUtils.get_wrong_data_types(BearUtils.DATA_TYPES[Bear.FIELD_AGE])
        }

        if field_name not in invalid_data_types:
            raise NotImplementedError(f"Invalid data types for {field_name} field not implemented!")
        return invalid_data_types[field_name]
