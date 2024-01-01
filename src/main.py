import os.path
from src.utils import get_all_operations,get_executed_only,get_sort_operations,get_formated_operations
from config import ROOT_DIR
OPERATION_FAIL_PATH = os.path.join(ROOT_DIR, 'src', 'operations.json')


def main():
    all_operations = get_all_operations(OPERATION_FAIL_PATH)
    filtered_operations = get_executed_only(all_operations)
    sort_operations = get_sort_operations(filtered_operations)
    for operation in sort_operations[:5]:
        print(get_formated_operations(operation))

if __name__ == "__main__":
    main()