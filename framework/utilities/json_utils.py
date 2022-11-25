import json
from typing import Union

import jsonschema
from jsonschema import validate


class JsonUtils:
    @staticmethod
    def is_valid_json_schema(schema: dict, instance: Union[dict, list], safe: bool = True) -> bool:
        """
        Check if json schema is valid or not
        :param schema (dict): Expected json schema
        :param instance (dict): json schema to be checked
        :param safe(optional, bool): return bool or raise exception flag
        :raises: AssertionError if instance hasn't expected json schema and safe is False
        :return: is instance has expected json schema or not
        :rtype: bool
        """
        try:
            validate(schema=schema, instance=instance)
        except jsonschema.exceptions.ValidationError as error:
            if safe:
                return False
            else:
                raise AssertionError(
                    f"Invalid Json schema. Actual: {instance}, Expected: {schema}. More info: {error.message}")
        return True

    @staticmethod
    def is_json(obj: str) -> bool:
        """
        Check if text is json or not
        :param obj (str): string to be checked
        :return: obj is json or not
        :rtype: bool
        """
        try:
            json.loads(obj)
        except ValueError:
            return False
        return True
