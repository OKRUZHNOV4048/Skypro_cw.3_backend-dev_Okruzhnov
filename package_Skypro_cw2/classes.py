class Operation:

    def __init__(self, id_operation, state, date, amount, name, code, description, to_account, from_account):
        self.id_operation = id_operation
        self.state = state
        self.date = date
        self.amount = amount
        self.name = name
        self.code = code
        self.description = description
        self.to_account = to_account
        self.from_account = from_account

    def observe(self):
        return f"""
Операция id {self.id_operation}, имеющая статус {self.state}, была  инициирована {self.date}.
Сумма операции: {self.amount} {self.name} ({self.code}). Назначение перевода: {self.to_account}.
Перевод отправлен от: {self.from_account}.
Дополнительная информация: {self.description}."""
