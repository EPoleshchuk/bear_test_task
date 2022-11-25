from copy import deepcopy
from typing import Any


class Bear:
    """
    Bear object model class
    """
    FIELD_ID = "bear_id"
    FIELD_TYPE = "bear_type"
    FIELD_NAME = "bear_name"
    FIELD_AGE = "bear_age"
    EDITABLE_FIELDS = [FIELD_TYPE, FIELD_NAME, FIELD_AGE]

    DEFAULT_BEAR_TYPE = "BLACK"
    DEFAULT_BEAR_NAME = "mikhail"
    DEFAULT_BEAR_AGE = 17.5

    def __init__(self,
                 bear_id: Any = None,
                 bear_type: Any = DEFAULT_BEAR_TYPE,
                 bear_name: Any = DEFAULT_BEAR_NAME,
                 bear_age: Any = DEFAULT_BEAR_AGE):
        """
        Bear model initializer
        :param bear_id (optional, any): Id of bear object
        :param bear_type (optional, any): type of bear object
        :param bear_name (optional, any): name of bear object
        :param bear_age (optional, any): age of bear object
        """
        self.bear_id = bear_id
        self.bear_type = bear_type
        self.bear_name = bear_name
        self.bear_age = bear_age

    def to_dict(self) -> dict:
        """
        Get dict representation of bear object (except field id)
        :return: dict with bear object data
        :rtype: dict
        """
        dict_repr = deepcopy(self.__dict__)
        dict_repr.pop(self.FIELD_ID, None)
        return dict_repr

    def __str__(self) -> str:
        """
        Get str representation of bear object
        :return: string representation
        :rtype: str
        """
        fields = ", ".join([f"{key}={value}" for key, value in self.to_dict().items()])
        return f"{self.__class__.__name__}[id={self.bear_id}]({fields})"

    def __eq__(self, other: Any) -> bool:
        """
        Compare bear object with other objects
        :param other (any): object to compare
        :return: equal or not
        :rtype: bool
        """
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__
