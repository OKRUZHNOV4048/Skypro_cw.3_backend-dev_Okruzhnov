class Operation:

    def __init__(self, id, state, date, amount, currency, name, code, description, from_account, to):
        self.id = id
        self.state = state
        self.date = date
        self.amount = amount
        self.currency = currency
        self.name = name
        self.code = code
        self.description = description
        self.from_account = from_account
        self.to = to

    def observe(self):
        return f"Опреация с {id}, имеющая статус {state}, была  инициирована {date}." \
               f"Сумма операции {amount}{name} ({code})." \
               f"Перевод инициирован со счета {from_account} на счет {to}" \
               f"Дополнительная информация: {description}"

