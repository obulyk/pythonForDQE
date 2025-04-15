import random
import string


def generate_random_dict():
    keys_num = random.randint(1, 5)
    return {
        random.choice(string.ascii_lowercase): random.randint(1, 100)
        for _ in range(keys_num)
    }


def generate_list_of_dicts():
    number_dictionaries = random.randint(2, 10)
    return [generate_random_dict() for _ in range(number_dictionaries)]


def group_values_by_keys(dict_list):
    grouped = {}
    for index, d in enumerate(dict_list):
        for key, value in d.items():
            if key not in grouped:
                grouped[key] = []
            grouped[key].append((value, index + 1))
    return grouped


def create_result_dict(grouped):
    result = {}
    for key, values in grouped.items():
        if len(values) > 1:
            max_value, max_index = max(values, key=lambda x: x[0])
            result[f"{key}_{max_index}"] = max_value
        else:
            result[key] = values[0][0]
    return result


def main():
    random_dicts = generate_list_of_dicts()
    print("Generated Dictionaries:")
    for i, d in enumerate(random_dicts, 1):
        print(f"{i}: {d}")

    grouped = group_values_by_keys(random_dicts)
    result = create_result_dict(grouped)

    print("\nUnified dictionaries:", result)


if __name__ == "__main__":
    main()
