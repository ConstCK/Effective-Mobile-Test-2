import jsonlines

from services import Validator


class DataBase:
    def __init__(self, name) -> None:
        self.name = name
        self.validator = Validator()

    def get_all_data(self) -> list[dict]:
        """Получение всей информации из базы данных"""
        with jsonlines.open(self.name, mode="r") as file:
            result = [item for item in file]
            return result

    def add_data(self, data):
        all_data = self.get_all_data()
        if self.validator.check_duplicates(data):
            return "Объект уже существует"

        with jsonlines.open(self.name, mode='a') as file:
            self.validator.validate_data(data)
            file.write(data)
        return "Успешное добавление данных"
