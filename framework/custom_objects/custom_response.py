from typing import Any


class CustomResponse:
    """
    Custom response class with extra fields
    """

    def __init__(self, status_code: int, body: Any, headers: dict = None):
        """
        Initializer of CustomResponseObject class
        :param status_code(int): response status_code
        :param body (any): response content
        :param headers (dict): dictionary with response headers
        """
        self.status_code = status_code
        self.body = body
        self.headers = headers
