import json


""""
    Функция берет данные из json
"""
def get_all_operations(path):
    with open(path, "r", encoding="UTF-8") as file:
        content = json.load(file)
        return content
"""
    Создаем новый список, убираем все лишнее
"""
operation_list = []
def get_executed_only(operation:list):
    if {}.get('state') == 'EXECUTED':
        operation_list.append('state')
        return operation_list

"""
    Сортируем список по датам
"""
sort_operation_list =[]
def get_sort_operations(operation:list):
    get_sort_operations = operation_list.sort(key=lambda x: x.get["date"], reverse=True)
    sort_operation_list.append('date')
    return sort_operation_list

"""
    Функция преобразует дату в нужный формат
"""
def get_from_date (operation:list):
    form_date = int()
    for date in sort_operation_list:
        date_1 = date.split('T')
        date_2 = date_1[0].split('-')
        form_date = '.'.join(reversed(date_2))
    return form_date

"""
   Функция кодирует карту и счет
"""
def hide_requisites(requistes:str):
    parts = requistes.split()
    number = parts[-1]
    if parts.lower().statwith('счет'):
        hided_number = f"**{number[-4:]}"
    else:
        hided_number = f"{number[:4]} {number[4:6]} ** **** {number[-4:]}"
        parts[-1] = hided_number
    return ' '.join(parts)

"""
    Функция возвращает всю информацию по операции
"""
def get_formated_operations(operation):
    from_date = get_from_date(operation)
    type_operation = operation['description']
    line_one_output = f"{from_date} {type_operation}"
    if operation.get('from'):
        hided_from = hide_requisites(operation.get('from'))
    else:
        hided_from = 'Нет данных'
    hided_to = hide_requisites(operation.get('to'))
    line_two_output = f"{hided_from} -->  {hided_to}"

    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    line_three_output = f"{amount} {currency}"
    return (f"{line_one_output}"
            f"{line_two_output}"
            f"{line_three_output}")

















