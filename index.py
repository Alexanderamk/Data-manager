import file_obj
from main_menu import menu
from reading_data import open_file


def main():
    file_location = "files/olympics.csv"
    headers, dict_datas, has_data = open_file(file_location)
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
            file.add(int(input("Number of new rows: ")))
        elif mode == "s":
            if has_data:
                file.search()
            else:
                print("Files doesn't have any data to search!")
        elif mode == "del":
            file.delete()
        elif mode == "up":
            ...
        elif mode == "q":
            return
        else:
            menu()
    

if __name__ == "__main__":
    main()