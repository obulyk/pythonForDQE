import random
import string
from typing import Dict


def get_random_size(min_val: int, max_val: int) -> int:
    return random.randint(min_val, max_val)


def generate_random_dict(min_keys: int, max_keys: int) -> Dict[str, int]:
    if not (1 <= min_keys <= max_keys <= 26):
        raise ValueError("min_keys and max_keys must be between 1 and 26 inclusive.")

    keys_num = get_random_size(min_keys, max_keys)
    keys = random.sample(string.ascii_lowercase, keys_num)
    random_dict = {key: get_random_size(1, 100) for key in keys}

    return random_dict

def generate_list_of_dicts(min_dicts: int, max_dicts: int, min_keys: int, max_keys: int):
    if not (1 <= min_dicts <= max_dicts <= 100):
        raise ValueError("min_dicts and max_dicts must be between 1 and 100 inclusive.")

    if not (1 <= min_keys <= max_keys <= 26):
        raise ValueError("min_keys and max_keys must be between 1 and 26 inclusive.")

    number_dictionaries = get_random_size(min_dicts, max_dicts)

    result = [generate_random_dict(min_keys, max_keys) for _ in range(number_dictionaries)]

    if not isinstance(result, list):
        raise TypeError("Output must be a list.")
    if not all(isinstance(d, dict) for d in result):
        raise TypeError("All elements in the output list must be dictionaries.")

    return result


def group_values_by_keys(dict_list):
    if not isinstance(dict_list, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(d, dict) for d in dict_list):
        raise ValueError("All elements in the list must be dictionaries.")

    grouped = {}
    for index, d in enumerate(dict_list):
        for key, value in d.items():
            if key not in grouped:
                grouped[key] = []
            grouped[key].append((value, index + 1))

    if not isinstance(grouped, dict):
        raise TypeError("Output must be a dictionary.")
    if not all(isinstance(v, list) for v in grouped.values()):
        raise ValueError("All values in output dictionary must be lists.")

    return grouped


def create_result_dict(grouped):
    if not isinstance(grouped, dict):
        raise TypeError("Input must be a dictionary.")
    if not all(isinstance(v, list) for v in grouped.values()):
        raise ValueError("All values must be lists.")
    if not all(isinstance(item, tuple) and len(item) == 2 for sublist in grouped.values() for item in sublist):
        raise ValueError("Each list must contain tuples of the form (value, index).")

    result = {}
    for key, values in grouped.items():
        if len(values) > 1:
            max_value, max_index = max(values, key=lambda x: x[0])
            result[f"{key}_{max_index}"] = max_value
        else:
            result[key] = values[0][0]
    return result


def main():
    min_dicts = int(input('Enter minimum number of dictionaries: '))
    max_dicts = int(input('Enter maximum number of dictionaries: '))

    min_keys = int(input('Enter minimum number of keys in dict: '))
    max_keys = int(input('Enter maximum number of keys in dict: '))

    random_dicts = generate_list_of_dicts(min_dicts, max_dicts, min_keys, max_keys)
    print("Generated Dictionaries:")
    for i, d in enumerate(random_dicts, 1):
        print(f"{i}: {d}")

    grouped = group_values_by_keys(random_dicts)
    result = create_result_dict(grouped)

    print("\nUnified dictionaries:", result)


if __name__ == "__main__":
    main()
