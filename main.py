from budget import Budget

a = Budget(name="John", db_name="db.json")
a.add_data(mode="income", data={"price": 10000, "description": "Salary"})
a.add_data(mode="spending", data={"price": 2000, "description": "Pizza buying"})
a.add_data(mode="spending", data={"price": 1000, "description": "Beer buying"})
a.add_data(mode="income", data={"price": 5000, "description": "Bonus"})
a.add_data(mode="spending", data={"price": 3000, "description": "Snacks buying"})
a.add_data(mode="spending", data={"price": 4000, "description": "Whores buying"})
a.change_data(data_id=1, new_data={"price": 5999, "description": "Salary!"})
# print(a.get_meta())
# print(a.get_data_by_category('Доходы'))
# print(a.get_data_by_category('Расходы'))
# print(a.get_data_by_date(year='2024', month='05', day='03'))
print(a.get_data_by_price(3000, "greater"))

