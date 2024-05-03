from services import Validator


class Budget:
    def __init__(self, name: str, db_name: str) -> None:
        self.validator = Validator()
        self.name = name
        self.db = db_name
        self.id = 0

    def __str__(self) -> str:
        return f"Личный финансовый кошелек: {self.name}"

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
