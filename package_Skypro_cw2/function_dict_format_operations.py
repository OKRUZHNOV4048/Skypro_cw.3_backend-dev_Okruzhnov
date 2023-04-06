from package_Skypro_cw2.function_load_data import load_data

sorted_operations = load_data()


def dict_format_operations():
    """
    Для последующего создания экземпляров класса Operation, описывающих те переводы, которые не имеют отправителя:
    1. принимает list со вложенными dict, содержащий данные по последним пяти проведенным операциям;
    2. возвращает тот же лист list, но для операций, не имеющих отправителя,
      дополненный ключом ‘from’ и значением ‘’
      в каждом словаре, описывающем такую операцию.
    """
    sorted_operations_comprehensive_inf = []
    for operation in sorted_operations:
        if 'from' in operation:
            sorted_operations_comprehensive_inf.append(operation)
        else:
            operation['from'] = ''
            sorted_operations_comprehensive_inf.append(operation)

    return sorted_operations_comprehensive_inf
