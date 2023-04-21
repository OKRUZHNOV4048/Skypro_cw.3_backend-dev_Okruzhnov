from package_Skypro_cw3.function_dict_format_operations import dict_format_operations


def test_dict_format_operations():
    assert dict_format_operations(
        [{'id': 1, 'state': 'Исполнено'}, {'id': 1, 'state': 'Исполнено', 'from': 'Отправитель'}]) == [
               {'id': 1, 'state': 'Исполнено', 'from': ''}, {'id': 1, 'state': 'Исполнено', 'from': 'Отправитель'}]
