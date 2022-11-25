from typing import Any, Iterable


class AssertUtils:
    """
    Class with useful asserts methods
    """
    WRONG_STATUS_CODE_ERR_MSG = "Wrong status code. Actual: {}, expected: {}"
    WRONG_LIST_LENGTH = "Wrong list length. Actual: {}, expected: {}"

    @staticmethod
    def soft_assert(received_data: dict, expected_data: dict, assert_message: str = None) -> None:
        """
        Do soft assert. Compare all values and raise AssertionError if exists
        :param received_data(dict): dict with received data like {"key1": "value1", "key2", "value2"}
        :param expected_data(dict): dict with expected data like {"key1": "value1", "key2": "value2"}
        :param assert_message(optional, [None, str]): None means use default assert message,
                                                        str - string with 3 placeholders for value, recieved_value,
                                                                                                    expected_value
        :raises: AssertionError if dicts received_data and expected_data are different
        :return: None
        """
        if not assert_message:
            assert_message = "Wrong {} value. Received={}, expected={}"

        assert_messages = []
        for key in received_data:
            if received_data[key] != expected_data[key]:
                assert_messages.append(assert_message.format(key, received_data[key], expected_data[key]))
        if assert_messages:
            raise AssertionError("\n".join(assert_messages))

    @staticmethod
    def assert_objects_equal(received_data: Any, expected_data: Any, assert_message: str = None) -> None:
        """
        Assert objects equal
        :param received_data(any): Received data
        :param expected_data(any): Expected data same type as received data
        :param assert_message(optional, [None, str]): None means use default assert message,
                                                        str - string with 2 placeholders for received_data,
                                                                                             expected_data
        :raises: AssertionError if received_data != expected_data
        :return: None
        """
        if not assert_message:
            assert_message = "Error. Received data = {}, but {} expected"

        assert received_data == expected_data, assert_message.format(received_data, expected_data)

    @staticmethod
    def assert_objects_not_equal(object1: Any, object2: Any, assert_message: str = None) -> None:
        """
        Assert objects not equal
        :param object1(any): Received data
        :param object2(any): Expected data same type as object1
        :param assert_message(optional, [None, str]): None means use default assert message,
                                                        str - string with 2 placeholders for object1 value,
                                                                                             object2 value
        :raises: AssertionError if received_data == expected_data
        :return: None
        """
        if not assert_message:
            assert_message = "Error. object1 [{}] == object2 [{}], but not expected"

        assert object1 != object2, assert_message.format(object1, object2)

    @staticmethod
    def assert_object_in_list(obj: Any, objects_list: Iterable, assert_message: str = None) -> None:
        """
        Assert object in Iterable
        :param obj (any): Expected object in the objects_list collection
        :param objects_list (iterable): collection
        :param assert_message(optional, [None, str]): None means use default assert message,
                                                        str - string with 2 placeholders for obj and objects_list
        :raises: AssertionError if obj not in objects_list
        :return: None
        """
        if not assert_message:
            assert_message = "Error. {} isn't in collection {}, but expected"

        assert obj in objects_list, assert_message.format(obj, objects_list)

    @staticmethod
    def assert_object_not_in_list(obj: Any, objects_list: Iterable, assert_message: str = None) -> None:
        """
        Assert object not in Iterable
        :param obj (any): Not an expected object in the objects_list collection
        :param objects_list (iterable): collection
        :param assert_message(optional, [None, str]): None means use default assert message,
                                                        str - string with 2 placeholders for obj and objects_list
        :raises: AssertionError if obj in objects_list
        :return: None
        """
        if not assert_message:
            assert_message = "Error. {} is in collection {}, but wasn't expected"

        assert obj not in objects_list, assert_message.format(obj, objects_list)
