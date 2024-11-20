import csv
import file_obj


def main():
    file_location = "100_olympics.csv"
    header, datas = open_file(file_location)
    if not header:
        print("Files doesn't have any data.")
        return

    file = file_obj.FileMaintaining(header, datas)
    file.display()

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
                        section.append("None")
                    else:
                        section.append(data[field])
                datas.append(section)

            return header, datas
    except:
        return None, None


if __name__ == "__main__":
    main()