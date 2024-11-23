import file_obj
from main_menu import menu
from reading_data import open_file


def main():
    file_location = "blank.csv"
    header, datas, dict_datas = open_file(file_location)
    if not header:
        print("File must have at least a header.")
        return
    file = file_obj.FileMaintaining(header, datas, dict_datas)

    menu()
    mode = ""
    while mode != "q":
        mode = input("mode: ").lower()
        if mode == "dp":
            file.display()
        elif mode == "a":
            file.add(int(input("Number of new rows: ")))
        elif mode == "s":
            if datas:
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