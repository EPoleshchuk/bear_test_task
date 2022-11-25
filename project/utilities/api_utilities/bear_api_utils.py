from typing import Union

from framework.custom_objects import CustomResponse
from framework.utilities import ApiUtils
from framework.utilities.json_utils import JsonUtils
from project import config
from project.models import Bear
from project.models import BearsCollection


class BearApiUtils(ApiUtils):
    """
    Class with API utilities for bear objects
    """
    BEAR_JSON_SCHEMA = \
        {"type": "object",
         "properties": {"bear_id": {"type": "integer"},
                        "bear_name": {"type": "string"},
                        "bear_type": {"enum": ["POLAR", "BROWN", "BLACK", "GUMMY"]},
                        "bear_age": {"type": "number", "minimum": 0, "maximum": 100}}}

    BEARS_JSON_SCHEMA = \
        {"type": "array",
         "items": BEAR_JSON_SCHEMA}

    @classmethod
    def get_bears(cls, bear_id: Union[int, str] = None, validate_json: bool = False) -> CustomResponse:
        """
        Get single bear object or list of bear objects or response text/json in all other cases
        :param bear_id (optional, [int, str]): get list of bear object if None and single bear object otherwise
        :param validate_json (optional, bool): validate json schema or not
        :return: response object with status_code, body
        :rtype: CustomResponse
        """
        response = cls.get(config.BEAR_ENDPOINT_URL + (f"/{bear_id}" if bear_id else ""))
        if JsonUtils.is_json(response.text):
            json_resp = response.json()
            if isinstance(json_resp, list):
                if validate_json:
                    JsonUtils.is_valid_json_schema(cls.BEARS_JSON_SCHEMA, json_resp, safe=False)
                body = BearsCollection(json_resp)
            elif isinstance(json_resp, dict):
                if validate_json:
                    JsonUtils.is_valid_json_schema(cls.BEAR_JSON_SCHEMA, json_resp, safe=False)
                body = Bear(**json_resp)
            else:
                body = json_resp
        else:
            body = response.text

        return CustomResponse(response.status_code, body)

    @classmethod
    def delete_bears(cls, bear_id: Union[int, str] = None) -> CustomResponse:
        """
        Delete single bear object or list of bear objects
        :param bear_id (optional, [int, str]): delete list of bear object if None and single bear object otherwise
        :return: response object with status_code, body
        :rtype: CustomResponse
        """
        response = cls.delete(config.BEAR_ENDPOINT_URL + (f"/{bear_id}" if bear_id else ""))
        return CustomResponse(response.status_code, response.text)

    @classmethod
    def create_bear(cls, bear_object: Bear) -> CustomResponse:
        """
        Create bear object
        :param bear_object (Bear): create bear object with bear_object data
        :return: response object with status_code, body
        :rtype: CustomResponse
        """
        response = cls.post(config.BEAR_ENDPOINT_URL, json=bear_object.to_dict())
        return CustomResponse(response.status_code, response.text)

    @classmethod
    def update_bear(cls, bear_id: Union[str, int], **new_data) -> CustomResponse:
        """
        Update bear object
        :param bear_id (str, int): bear_id of bear object to be updated
        :param new_data (dict): fields to be updated
        :return: response object with status_code, body
        :rtype: CustomResponse
        """
        response = cls.put(config.BEAR_ENDPOINT_URL + f"/{bear_id}", json=new_data)
        return CustomResponse(response.status_code, response.text)
