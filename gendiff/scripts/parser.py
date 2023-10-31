import json
import yaml


def parser(file_data, extension):
    if extension == 'json':
        return json.load(file_data)
    if extension == 'yaml':
        return yaml.load(file_data,  Loader=yaml.FullLoader)
