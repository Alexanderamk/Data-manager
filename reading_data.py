import csv


def open_file(file_dir):
    try:
        with open(file_dir, "r") as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames
            dict_datas = list(reader)
            datas = []

            for data in dict_datas:
                section = []
                for field in header:
                    if data[field] == "":
                        section.append("-")
                    else:
                        section.append(data[field])
                datas.append(section)

            return header, datas
    except:
        raise ValueError("File is not found.")