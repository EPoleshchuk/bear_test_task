import json
from typing import Union, List

import requests
from requests import Response

from framework.logger import Logger
from framework.utilities.json_utils import JsonUtils


def log_response(func):
    def _log_response(*args, **kwargs) -> Response:
        """
        Log response data and other information
        """
        response = func(*args, **kwargs)
        body = json.dumps(response.json(), indent=2) if JsonUtils.is_json(response.text) else response.text
        Logger.info(f"Response status code={response.status_code}, elapsed time = {response.elapsed}\n\n{body}\n")
        return response

    return _log_response


class ApiUtils:
    """
    Class with basic API utilities
    """

    @staticmethod
    @log_response
    def get(url: str, params: Union[dict, List[tuple]] = None, **kwargs) -> Response:
        """
        Send a GET request.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary, list of tuples or bytes to send
            in the query string for the :class:`Request`.
        :param kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        """
        Logger.info(f"Send 'GET' request to {url} with params={params}, kwargs={kwargs}")
        return requests.get(url, params=params, **kwargs)

    @staticmethod
    @log_response
    def post(url: str, data: Union[dict, List[tuple]] = None, json: dict = None, **kwargs) -> Response:
        """
        Send a POST request.
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        """
        Logger.info(f"Send 'POST' request to {url} with data={data}, json={json}, kwargs={kwargs}")
        return requests.post(url, data=data, json=json, **kwargs)

    @staticmethod
    @log_response
    def put(url: str, data: Union[dict, List[tuple]] = None, **kwargs) -> Response:
        """
        Send a PUT request.
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        """
        Logger.info(f"Send 'PUT' request to {url} with data={data}, kwargs={kwargs}")
        return requests.put(url, data=data, **kwargs)

    @staticmethod
    @log_response
    def patch(url: str, data: Union[dict, List[tuple]] = None, **kwargs) -> Response:
        """
        Send a PATCH request.
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        """
        Logger.info(f"Send 'PATCH' request to {url} with data={data}, kwargs={kwargs}")
        return requests.patch(url, data=data, **kwargs)

    @staticmethod
    @log_response
    def delete(url: str, **kwargs) -> Response:
        """
        Send a DELETE request.
        :param url: URL for the new :class:`Request` object.
        :param kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        """
        Logger.info(f"Send 'DELETE' request to {url} with kwargs={kwargs}")
        return requests.delete(url, **kwargs)
