from package_Skypro_cw3.function_result_output import result_output


def test_result_output():
    assert result_output([{'id': 801684332, 'state': 'EXECUTED',
                           'date': '2019-11-05T12:04:13.781725',
                           'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                           'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381',
                           'from': ''}]) == ['05.11.2019 Открытие вклада \n -> Счет **8381 \n21344.35 руб. \n']
