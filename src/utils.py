import datetime
import json


""""
    Функция берет данные из json
"""
def get_all_operations(OPERATION_FAIL_PATH):
    """
        Функция берет данные из json
    """
    with open(OPERATION_FAIL_PATH, "r", encoding="UTF-8") as file:
        operation = json.load(file)
        return operation
def get_executed_only(operation:list)->list:
    """
        Создаем новый список, убираем все лишнее
    """
    operation_list = [opr for opr in operation if opr != {} and opr["state"] == "EXECUTED"]
    return operation_list
def get_sort_operations(operation_list:list)->list:
    """
        Сортируем список по датам
    """
    sorted_items = sorted(operation_list,reverse=True, key=lambda x: x["date"])
    return sorted_items
def hide_requisites(requistes:str)->str:
    """
       Функция кодирует карту и счет
    """
    parts = requistes.split()
    number = parts[-1]
    check = parts[0]
    if check.lower() == 'счет':
        hided_number = f"**{number[-4:]}"
    else:
        hided_number = f"{number[:4]} {number[4:6]} ** **** {number[-4:]}"
    parts[-1] = hided_number
    return ' '.join(parts)
def get_formated_operations(operation_list)->str:
    """
        Функция возвращает всю информацию по операции
    """
    from_date = datetime.datetime.fromisoformat(operation_list['date']).strftime('%d.%m.%y')
    type_operation = operation_list['description']
    line_one_output = f"{from_date} {type_operation}"
    if from_pay:=operation_list.get('from'):
        hided_from = hide_requisites(from_pay)
    else:
        hided_from = 'Нет данных'
    hided_to = hide_requisites(operation_list.get('to'))
    line_two_output = f"{hided_from} -->  {hided_to}"

    amount = operation_list['operationAmount']['amount']
    currency = operation_list['operationAmount']['currency']['name']
    line_three_output = f"{amount} {currency}"
    return (f"{line_one_output}\n"
            f"{line_two_output}\n"
            f"{line_three_output}\n")

















