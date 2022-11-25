import random
import string
from typing import Any, Sequence


class RandomUtils:
    """
    Class with basic random utilities
    """

    @staticmethod
    def get_random_string(length: int = 10) -> str:
        """
        Get random string.
        :param length (optional, int): random string length
        :return: random string
        :rtype: str
        """
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def get_random_int(minimum: int = 0, maximum: int = 100) -> int:
        """
        Get random integer.
        :param minimum (optional, int): left bound of a range of random numbers
        :param maximum (optional, int): right bound of a range of random numbers
        :return: random integer from interval [minimum, maximum]
        :rtype: int
        """
        return random.randint(minimum, maximum)

    @staticmethod
    def get_random_number(minimum: int = 0, maximum: int = 100, accuracy: int = 3) -> float:
        """
        Get random number.
        :param minimum (optional, int): left bound of a range of random numbers
        :param maximum (optional, int): right bound of a range of random numbers
        :param accuracy (optional, int): returned number accuracy
        :return: random number from interval [minimum, maximum]
        :rtype: float
        """
        return round(random.uniform(minimum, maximum), accuracy)

    @staticmethod
    def get_random_choice(seq: Sequence, except_for: Any = None) -> Any:
        """
        Get random obj from collection
        :param seq (sequence): collection
        :param except_for (optional, any): Object to be excluded from the collection
        :return: random object from seq
        :rtype: any
        """
        if except_for:
            return random.choice([item for item in seq if item != except_for])
        return random.choice(seq)
