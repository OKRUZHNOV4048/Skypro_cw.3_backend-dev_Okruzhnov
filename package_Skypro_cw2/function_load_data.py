import json


def load_data():
    """
    Загружает данные по операциям клиента из файла operations.json в формате JSON, распаковывает из JSON и преобразует
    в объект Python. Возвращает list со вложенными dict, содержащий данные по последним пяти проведенным операциям.
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        operations_data = json.load(file)

    # Неупорядоченный по датам список выполненных операций, т.е. имеющих статус 'EXECUTED'.
    completed_operations_with_id = []
    # Упорядоченный реверсированный список дат последних пяти операций.
    sorted_operations_date = []
    # Упорядоченный по датам список последни пяти выполненных операций, начиная с самой последней.
    sorted_completed_operations_with_id = []

    # Создание неупорядоченного по датам списка выполненных операций, т.е. имеющих статус 'EXECUTED'.
    # Цикл формирует указанный список, игнорируя вложенные словари, не содержащие ключ 'id'. В данном случае
    # логика следующая: любому корректно выполненному запросу на операцию присваивается 'id'.
    # Если 'id' не присвоен, значит вложенный словарь не включает в себя параметры
    # операции, имеющей определенный статус (исполненной, неисполненной или отклоненной).
    # Также цикл включает в новый список, только те словари, описывающие параметры операций,
    # которые имеют статус 'ИСПОЛНЕННАЯ' (это по условию задания).
    for operation in operations_data:
        if 'id' in operation and operation['state'] == 'EXECUTED':
            completed_operations_with_id.append(operation)

    # Создание упорядоченного списка дат последних пяти операций.
    for operation in completed_operations_with_id:
        sorted_operations_date.append(operation['date'])
    # Сортировка по возрастанию дат из проитериррованного списка выполненных операций.
    sorted_operations_date.sort()
    sorted_operations_date = sorted_operations_date[:-6:-1]

    # Создание упорядоченного по датам списка последни пяти выполненных операций.
    # Так как у нас уже есть упорядоченный реверсированный список дат последних пяти операций
    # (sorted_operations_date) мы можем использовать свойство цикла for in, в соответствии с которым
    # перебор списка осуществляется слева направо.
    operation_counter = 0
    for operation_date in sorted_operations_date:
        for operation in completed_operations_with_id:
            if operation_date == operation['date']:
                sorted_completed_operations_with_id.append(operation)
            else:
                operation_counter += 1

    return sorted_completed_operations_with_id
