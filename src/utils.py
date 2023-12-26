import json
import datetime


def get_all_operations(path):
    with open(path) as file:
        content = json.load(file)
        return content

operation_list = []
def get_executed_only():
    if {}.get('state') == 'EXECUTED':
        operation_list.append('state')
        return operation_list
def get_sort_operations():
    get_sort_operations = sorted(operation_list, key=lambda x: x['data'], reverse=True)
    return get_sort_operations

"""
    Функция преобразует дату 
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














