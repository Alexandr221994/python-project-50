import argparse
import json


def generate_diff(file_path1, file_path2):
    json_1 = load_file(file_path1)
    json_2 = load_file(file_path2)
    return calculate_diff(json_1, json_2)


def load_file(file_path):
    _json = json.load(open(file_path))
    return _json


def calculate_diff(json1, json2):
    all_keys = sorted(json1.keys() | json2.keys())
    final_string = ''

    for key in all_keys:
        value_1 = json1.get(key)
        value_2 = json2.get(key)
        if value_2 is None:
            final_string += f'  - {key}: {value_1}\n'
        elif value_1 is None:
            final_string += f'  + {key}: {value_2}\n'
        elif value_1 == value_2:
            final_string += f'    {key}: {value_1}\n'
        else:
            final_string += f'  - {key}: {value_1}\n'
            final_string += f'  + {key}: {value_2}\n'
    return '{\n' + final_string + '}'


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
        )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        '-f', '--format', dest='FORMAT', help='set format of output'
        )

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    import sys
    if "-h" in sys.argv or "--help" in sys.argv:
        main()
    main()
