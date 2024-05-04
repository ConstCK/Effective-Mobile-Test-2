import time

from budget import Budget
from services import Validator, Paginator, TerminalService


class Terminal:
    def __init__(self, name: str, db_name: str, new: bool):
        self.validator = Validator()
        self.paginator = Paginator()
        self.conn = Budget(name, db_name, new)
        self.service = TerminalService()

    def greetings(self) -> None:
        """Приветствие в терминале"""
        print(f"Добро пожаловать в {self.conn}")
        print(f"Используйте ввод чисел (1-7) для навигации по меню")

    @staticmethod
    def show_menu() -> None:
        """Вывод всех команд меню в терминале"""
        print("1 - Вывод баланса, суммы доходов и расходов")
        print("2 - Получение всех данных кошелька")
        print("3 - Получение данных кошелька по категории")
        print("4 - Получение данных кошелька по дате")
        print("5 - Получение данных кошелька по сумме")
        print("6 - Добавление данных о расходах")
        print("7 - Добавление данных о доходах")
        print("8 - Изменение существующих данных")
        print("0 - Завершение работы терминала")

    def get_meta_data(self):
        """Вывод баланса, суммы доходов и расходов"""
        return self.conn.get_meta()

    def get_all_data(self):
        """Получение всех данных кошелька"""
        data = self.conn.get_all_data()
        result = self.paginator.paginate_data(data)
        go_ahead = True
        print("Получение всех данных кошелька:")
        while go_ahead:
            try:
                for item in next(result):
                    print(item)
                print("*"*100)
            except StopIteration:
                print("Данных больше нет...")
                break
            go_ahead = self.service.page_input()

    def get_categorized_data(self):
        """Получение данных по выбранной категории"""
        mode = self.service.category_input()
        data = self.conn.get_data_by_category(mode=mode)
        result = self.paginator.paginate_data(data)
        go_ahead = True
        print("Получение данных по указанной категории:")
        while go_ahead:
            try:
                for item in next(result):
                    print(item)
                print("*"*100)
            except StopIteration:
                print("Данных больше нет...")
                break
            go_ahead = self.service.page_input()

    def get_dated_data(self):
        """Получение данных по указанной дате"""
        date = self.service.date_input()
        data = self.conn.get_data_by_date(year=date.get("year"),
                                          month=date.get("month"),
                                          day=date.get("day"))
        result = self.paginator.paginate_data(data)
        go_ahead = True
        print("Получение данных по указанной дате:")
        while go_ahead:
            try:
                for item in next(result):
                    print(item)
                print("*"*100)
            except StopIteration:
                print("Данных больше нет...")
                break
            go_ahead = self.service.page_input()

    def get_priced_data(self):
        """Получение данных по указанной сумме"""
        amount = self.service.sum_input()
        data = self.conn.get_data_by_sum(amount=amount)
        result = self.paginator.paginate_data(data)
        go_ahead = True
        print("Получение данных по указанной сумме:")
        while go_ahead:
            try:
                for item in next(result):
                    print(item)
                print("*"*100)
            except StopIteration:
                print("Данных больше нет...")
                break
            go_ahead = self.service.page_input()

    def add_spending_data(self) -> None:
        """Добавление данных о расходах"""
        data = self.service.input_data(mode="Расходы")
        print(self.conn.add_data(data=data,
                                 mode="Расходы"))

    def add_income_data(self) -> None:
        """Добавление данных о доходах"""
        data = self.service.input_data(mode="Доходы")
        print(self.conn.add_data(data=data,
                                 mode="Доходы"))

    def change_data(self) -> None:
        """Изменение существующих данных"""
        while True:
            try:
                data_id = self.service.id_input()
                break
            except:
                print('sadfsadfsafsafsa')
                continue
        data = self.service.input_data()
        print(self.conn.change_data(data_id=data_id, new_data=data))

    def run_program(self) -> None:
        """Ввод команд меню для управления справочником"""
        while True:
            self.show_menu()
            choice = self.service.menu_choice_input()

            match choice:
                case 0:
                    print("Завершение программы...")
                    time.sleep(3)
                    break
                case 1:
                    print(self.get_meta_data())
                    print("*"*100)
                    time.sleep(3)
                case 2:
                    self.get_all_data()
                case 3:
                    self.get_categorized_data()
                case 4:
                    self.get_dated_data()
                case 5:
                    self.get_priced_data()
                case 6:
                    self.add_spending_data()
                case 7:
                    self.add_income_data()
                case 8:
                    self.change_data()

        print("Программа завершена!")
