from datetime import datetime
from package_Skypro_cw2.function_dict_format_operations import dict_format_operations
from package_Skypro_cw2.classes import Operation

sorted_operations = dict_format_operations()
result_report = []


def result_output():
    """
    Принимает упорядоченный список со вложенными словарями, в том числе, включающих параметры операций,
    для которых не оказан источник перевода. Возвращает список строк, отформатированных под условия задания.
    """
    for i in range(len(sorted_operations)):
        # На каждой итерации создается экземпляр класса Operation, которому поедаются соответствующие значения полей,
        # в зависимости от данных списка sorted_operations, вернувшегося после вызова функции dict_format_operations().
        operation = Operation(sorted_operations[i]['id'], sorted_operations[i]['state'], sorted_operations[i]['date'],
                              sorted_operations[i]['operationAmount']['amount'],
                              sorted_operations[i]['operationAmount']['currency']['name'],
                              sorted_operations[i]['operationAmount']['currency']['code'],
                              sorted_operations[i]['description'], sorted_operations[i]['to'],
                              sorted_operations[i]['from'])

        date_operation = operation.date.partition('T')[0]
        format_data = "%Y-%m-%d"
        date_operation = datetime.strptime(date_operation, format_data)

        # В зависимости от вида отправителя и получателя (а. счет, б. карта, в. для отправителя возможно значение
        # в виде пустой str ‘’) переменным экземпляра класса присваиваются строковые значения с разным типом маскировки.

        if operation.from_account:
            if 'Счет' in operation.from_account:
                operation.from_account = operation.from_account[:4] + ' **' + operation.from_account[-4:]
            else:
                operation.from_account = operation.from_account[:-12] + ' ' + operation.from_account[-12:-10] + \
                                         '** **** ' + operation.from_account[-4:]

        if operation.to_account:
            if 'Счет' in operation.to_account:
                operation.to_account = operation.to_account[:4] + ' **' + operation.to_account[-4:]
            else:
                operation.to_account = operation.to_account[:-12] + ' ' + operation.to_account[-12:-10] + \
                                       '** **** ' + operation.to_account[-4:]

        result_report.append(f"{date_operation.strftime('%d.%m.%Y')} {operation.description} \n"
                             f"{operation.from_account} -> {operation.to_account} \n"
                             f"{operation.amount} {operation.name} \n")

    return result_report
