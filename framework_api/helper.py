import json
import allure
from jsonschema import validate


def validate_json_schema(schema_path, response_json):

    with allure.step('Валидация схемы json'):
        with open(schema_path) as file:
            schema = json.loads(file.read())
            validate(response_json, schema=schema)