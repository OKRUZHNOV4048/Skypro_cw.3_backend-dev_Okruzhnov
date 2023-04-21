def dict_format_operations(sorted_operations):
    """
    Для последующего создания экземпляров класса Operation, описывающих те переводы, которые не имеют отправителя:
    1. Принимает list со вложенными dict, содержащий данные по последним пяти проведенным операциям;
    2. Возвращает тот же лист list, но для словарей, описывающих операций без номерного источника перевода
       (например, для операций по открытию вклада), вводится дополненный ключ ‘from’ со значением в виде пустой str ‘’.
    """
    sorted_operations_comprehensive_inf = []
    for operation in sorted_operations:
        if 'from' in operation:
            sorted_operations_comprehensive_inf.append(operation)
        else:
            operation['from'] = ''
            sorted_operations_comprehensive_inf.append(operation)

    return sorted_operations_comprehensive_inf
