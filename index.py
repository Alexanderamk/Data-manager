import file_obj
import reading_data
from main_menu import menu


def main():
    file_location = "files/blank.csv"
    headers, dict_datas, has_data = reading_data.open_file(file_location)
    if not headers:
        print("File must have at least a header.")
        return
    file = file_obj.FileMaintaining(headers, dict_datas)

    menu()
    mode = ""
    while mode != "q":
        mode = input("mode: ").lower()
        if mode == "dp":
            if has_data:
                file.display()
            else:
                print("Files doesn't have any data to display!")
        elif mode == "a":
            num_row = input("Number of new rows: ")
            while not num_row.isnumeric():
                num_row = input("Only numbers: ")
            file.add(int(num_row))
        elif mode == "s":
            if has_data:
                file.search()
            else:
                print("Files doesn't have any data to search!")
        elif mode == "del":
            file.delete()
        elif mode == "up":
            file.update()
        elif mode == "q":
            return
        elif mode == "save":
            reading_data.saving_file(file.dict_datas, headers)
        else:
            menu()


if __name__ == "__main__":
    main()