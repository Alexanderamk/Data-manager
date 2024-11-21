import csv
import file_obj


def main():
    file_location = "blank.csv"
    header, datas = open_file(file_location)
    if not header:
        print("Files doesn't have any data.")
        return

    file = file_obj.FileMaintaining(header, datas)
    file.display()
    num_new_rows = 2
    file.add(num_new_rows)

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
        raise ValueError("File is not found.")
    

if __name__ == "__main__":
    main()