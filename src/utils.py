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
def get_sort_operations(operation_list):
    get_sort_operations = sorted(operation_list, key=lambda x: x['data'], reverse=True)
    return get_sort_operations












