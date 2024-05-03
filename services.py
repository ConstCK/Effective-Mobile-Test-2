class Validator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def validate_data(data) -> bool:
        return len(data["description"]) > 1 and data["price"] > 0

    @staticmethod
    def check_duplicates(data: dict, all_data: list[dict]) -> bool:
        if all_data:
            result = any([True if data["id"] == x.get("id") else False for x in all_data])
            return result
        return False
