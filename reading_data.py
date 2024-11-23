import csv
from dict_to_list import dict_to_list


def open_file(file_dir):
    try:
        with open(file_dir, "r") as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames
            dict_datas = list(reader)
            datas = dict_to_list(dict_datas, header)

            return header, datas, dict_datas
    except:
        raise ValueError("File is not found.")