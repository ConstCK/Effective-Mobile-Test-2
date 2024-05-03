from typing import Any

import jsonlines


class Validator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def validate_data(data) -> bool:
        return len(data["description"]) > 1 and data["price"] > 0

    @staticmethod
    def check_duplicates(data: dict, all_data: list[dict]) -> bool:
        result = any([True if data["id"] == x["id"] else False for x in all_data])
        print(result)
        return result
