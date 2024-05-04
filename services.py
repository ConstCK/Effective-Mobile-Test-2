from typing import Generator, Literal, Any


class Validator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def validate_data(data: dict[str, Any]) -> bool:
        """Валидация вводимых данных о расходах/доходах"""
        return len(data["description"]) > 1 and data["price"] > 0

    @staticmethod
    def check_duplicates(data: dict, all_data: list[dict]) -> bool:
        """Проверка вводимых данных на повторение"""
        if all_data:
            result = any([True if data["id"] == x.get("id") else False for x in all_data])
            return result
        return False

    @staticmethod
    def validate_year(year: str) -> bool:
        """Валидация вводимых данных (года)"""
        return len(year) == 4 and 2100 > int(year) > 2000

    @staticmethod
    def validate_month(month: str) -> bool:
        """Валидация вводимых данных (месяца)"""
        return len(month) == 2 and 13 > int(month) > 0

    @staticmethod
    def validate_day(day: str) -> bool:
        """Валидация вводимых данных (дня)"""
        return len(day) == 2 and 32 > int(day) > 0

    @staticmethod
    def validate_sum(amount: int) -> bool:
        """Валидация вводимых данных (суммы)"""
        return amount > 0 and isinstance(amount, int)

    @staticmethod
    def validate_id(data_id: int) -> bool:
        """Валидация вводимых данных (id)"""
        return data_id > 0 and isinstance(data_id, int)

    @staticmethod
    def validate_description(description: str) -> bool:
        """Валидация вводимых данных (id)"""
        return 256 > len(description) > 0

    @staticmethod
    def validate_menu_choice(number) -> bool:
        """Валидация вводимых данных (номер операции меню)"""
        return 9 > number >= 0 and isinstance(number, int)


class Paginator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def paginate_data(data: list[dict], size: int = 5) -> Generator:
        """Пагинация выдаваемых данных по размеру (size)"""
        start: int = 0
        while start < len(data):
            yield data[start:size + start]
            start += size


class TerminalService:
    def __init__(self) -> None:
        self.validator = Validator()

    @staticmethod
    def page_input() -> bool:
        """Сервис продолжения/выхода из подменю"""
        while True:
            choice = input("Введите число (1 - для продолжения / 0 - для выхода): ")
            if choice == "1":
                return True
            elif choice == "0":
                return False
            else:
                print("Некорректный ввод (должно быть 1 или 0")

    def id_input(self) -> int:
        """Сервис ввода id"""
        while True:
            data_id = input("Введите id данных: ")
            try:
                data_id = int(data_id)
            except ValueError:
                print("Некорректный ввод id")
            else:
                if self.validator.validate_id(data_id):
                    return data_id
                else:
                    print("Некорректный ввод суммы")

    @staticmethod
    def category_input() -> Literal["Доходы", "Расходы"]:
        """Сервис ввода категории"""
        while True:
            choice = input("Выберите категорию (1 - для Расходов / 2 - для Доходов): ")
            if choice == "1":
                return "Расходы"
            elif choice == "2":
                return "Доходы"
            else:
                print("Некорректный ввод (должно быть 1 или 2")

    def date_input(self) -> dict[str, str]:
        """Сервис ввода даты"""
        while True:
            year = input("Введите год (в формате 2021): ")
            month = input("Введите месяц (в формате 05): ")
            day = input("Введите день (в формате 03): ")
            if self.validator.validate_year(year) and \
                    self.validator.validate_month(month) and \
                    self.validator.validate_day(day):
                return {"year": year, "month": month, "day": day}
            else:
                print("Некорректный ввод даты")

    def sum_input(self) -> int:
        """Сервис ввода суммы"""
        while True:
            amount = input("Введите сумму: ")
            try:
                amount = int(amount)
            except ValueError:
                print("Некорректный ввод суммы")
            else:
                if self.validator.validate_sum(amount):
                    return amount
                else:
                    print("Некорректный ввод суммы")

    def input_data(self, mode: str = None) -> dict[str, Any]:
        """Сервис ввода данных о расходах или доходах"""
        if mode == "Расходы":
            message = "Введите данные о расходах для добавления:"
        elif mode == "Доходы":
            message = "Введите данные о доходах для добавления:"
        else:
            message = "Введите данные для изменения:"
        print(message)
        while True:
            amount = input("Введите сумму: ")
            try:
                amount = int(amount)
            except ValueError:
                print("Некорректный ввод суммы")
            else:
                if self.validator.validate_sum(amount):
                    sum_data = amount
                    break
                else:
                    print("Некорректный ввод суммы")
        while True:
            description = input("Введите описание: ")
            if self.validator.validate_description(description):
                description = description
                break
            else:
                print("Некорректный ввод описания")
        return {"price": sum_data, "description": description}

    def menu_choice_input(self) -> int:
        """Сервис ввода номера операции меню терминала"""
        while True:
            try:
                choice = int(input("Введите номер операции: "))
                if self.validator.validate_menu_choice(choice):
                    return choice
                else:
                    print("Некорректный ввод номера операции (должно быть число от 0 до 8)")
            except ValueError:
                print("Ошибка ввода. Введите число (0-8)")
