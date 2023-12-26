import json
import datetime

""""
    Функция берет данные из json
"""
def get_all_operations(path):
    with open(path) as file:
        content = json.load(file)
        return content
"""
    Создаем новый список, убираем все лишнее
"""
operation_list = []
def get_executed_only():
    if {}.get('state') == 'EXECUTED':
        operation_list.append('state')
        return operation_list
"""
    Сортируем список по датам
"""
def get_sort_operations():
    get_sort_operations = sorted(operation_list, key=lambda x: x['data'], reverse=True)
    return get_sort_operations

"""
    Функция преобразует дату в нужный формат
"""
def get_from_date ():
    form_date = datetime.datetime.fromisoformat(operation_list['date']).strftime('%d%m%y')
    return form_date

"""
   Функция кодирует карту и счет
"""
def hide_requisites(requistes:str):
	parts = requistes.split()
	namber = parts[-1]
	if reguistes.lower().statwith('счет'):
		hided_namber = f"**{number[-4:]}"
	else:
		hided_namber = f"{number[:4]} {number[4:6]} ** **** {number[-4:]}"
	return ' '.join(parts)

"""
    Функция возвращает всю информацию по операции
"""
def get_formated_operations(operations_list):
    formated_date = formate_data(operation_list['date'])
    type_operation = operation_list['description']
    line_one_output = f"{formated_date} {type_operation}"
    if operations_list.get('from'):
        hided_from = hide_requisites(operations_list.get('from'))
    else:
        hided_from = 'Нет данных'
    hided_to = hide_requisites(operations_list.get('to'))
    line_two_output = f"{hided_from} -->  {hided_to}"
    amount = operations_list['operationAmount']['amount']
    currency = operations_list['operationAmount']['currency']['name']
    line_three_output = f"{amount} {currency}"
    return (f"{line_one_output}"
            f"{line_two_output}"
            f"{line_three_output}")

















