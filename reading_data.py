import csv


def open_file(file_dir):
    try:
        with open(file_dir, "r", encoding='utf-8') as file:
            dict_datas = list()
            reader = csv.DictReader(file)
            headers = reader.fieldnames
            
            for read in reader:
                dict_row = {}
                for head in headers:
                    if read[head] == "":
                        dict_row[head] = "-"
                    else:
                        dict_row[head] = read[head]
                dict_datas.append(dict_row)

            return headers, dict_datas, len(dict_datas) >= 1
    except Exception as e:
        raise ValueError(e)