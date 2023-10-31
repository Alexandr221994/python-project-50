import argparse
from gendiff.scripts.formatter import stringify
from gendiff.scripts.parser import parser


def generate_diff(file_path1, file_path2):
    data_first_file = get_data_file(file_path1)
    data_second_file = get_data_file(file_path2)
    return calculate_diff(parser(*data_first_file), parser(*data_second_file))


def get_data_file(file_path):
    file_data = open(file_path)
    extension = file_path.split('.')[-1]
    return file_data, extension


def calculate_diff(json1, json2, indentation=" "):
    all_keys = sorted(json1.keys() | json2.keys())
    indentation *= 2

    final_string = ''

    for key in all_keys:
        value_1 = stringify(json1.get(key))
        value_2 = stringify(json2.get(key))
        if value_2 is None:
            final_string += f'{indentation}- {key}: {value_1}\n'
        elif value_1 is None:
            final_string += f'{indentation}+ {key}: {value_2}\n'
        elif value_1 == value_2:
            final_string += f'{indentation}{key}: {value_1}\n'
        elif isinstance(value_1, dict) and isinstance(value_2, dict):
            final_string += f'{indentation}{key}: {calculate_diff(value_1, value_2, indentation)}'
        else:
            final_string += f'{indentation}- {key}: {value_1}\n'
            final_string += f'{indentation}+ {key}: {value_2}\n'
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
