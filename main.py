from package_Skypro_cw2.function_load_data import load_data
from package_Skypro_cw2.function_dict_format_operations import dict_format_operations
from package_Skypro_cw2.classes import Operation

sorted_operations = dict_format_operations()

i = 4
operation = Operation(sorted_operations[i]['id'], sorted_operations[i]['state'], sorted_operations[i]['date'],
                      sorted_operations[i]['operationAmount']['amount'],
                      sorted_operations[i]['operationAmount']['currency']['name'],
                      sorted_operations[i]['operationAmount']['currency']['code'],
                      sorted_operations[i]['description'], sorted_operations[i]['to'], sorted_operations[i]['from'])

print(operation.observe())