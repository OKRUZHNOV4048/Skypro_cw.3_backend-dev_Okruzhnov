import json


def load_data():
    """
    Загружает данные по операциям клиента из файла operations.json в формате JSON,
    распаковывает из JSON и преобразует в объект Python.
    Возвращает list со вложенными dict.
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data
