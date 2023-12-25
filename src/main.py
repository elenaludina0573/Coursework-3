import os.path
from src.utils import get_all_operations
from config import DATA-DIR


def main():
    all_operations = get_all_operations(DATA-DIR)
    filtered_operations = get_executed_only(all_operations)
    sorted_operations = get_sort_operations(filtered_operations)
    for operation in sorted_operations[:5]:
        print(get_formated_operations(operation))