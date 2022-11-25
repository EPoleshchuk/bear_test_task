from typing import List, Union

from framework.constants import DataTypes
from framework.utilities import RandomUtils


class TestDataUtils:
    @staticmethod
    def get_wrong_data_types(wrong_for: str) -> List:
        """
        Get wrong data type objects for specified data type.
        :param wrong_for (str): object data type for which wrong type objects will be generated
        :return: list with wrong data types for wrong_for type
        :rtype: list
        """
        all_data_types = {DataTypes.INTEGER: RandomUtils.get_random_int(),
                          DataTypes.NUMBER: RandomUtils.get_random_number(),
                          DataTypes.STRING: RandomUtils.get_random_string(),
                          DataTypes.NULL: None,
                          DataTypes.ARRAY: [],
                          DataTypes.OBJECT: {}}
        all_data_types.pop(wrong_for)
        if wrong_for == DataTypes.NUMBER:
            all_data_types.pop(DataTypes.INTEGER)
        return list(all_data_types.values())

    @staticmethod
    def get_boundary_values(limits: List[int], step: Union[int, float], valid: bool = True) -> List:
        """
        Get boundary valid or invalid values.
        :param limits (list): list with two boundaries
        :param step (int, float): step of deflection
        :param valid(bool, optional): generate valid values or not
        :return: list with boundary values
        :rtype: list
        """
        if valid:
            values = [limits[0], limits[0] + step, limits[1] - step, limits[1]]
        else:
            values = [limits[0] - step, limits[1] + step]
        return list(set(values))
