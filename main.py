from package_Skypro_cw2.function_dict_format_operations import dict_format_operations
from package_Skypro_cw2.function_load_data import load_data
from package_Skypro_cw2.function_result_output import result_output

input_data = "operations.json"
sorted_operations = dict_format_operations(load_data(input_data))


def main():
    result = result_output(sorted_operations)
    for i in range(len(result)):
        print(result[i])


main()
