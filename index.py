import file_obj
import reading_data
from main_menu import menu


def main():
    file_location = input("File location: ")
    located = reading_data.open_file(file_location)[0]

    if located:
        headers, dict_datas, has_data = reading_data.open_file(file_location)[1:]
    else:
        print("File is not found!")
        return

    if not headers:
        print("File must have at least a header.")
        return
    
    file = file_obj.FileMaintaining(headers, dict_datas)

    menu()
    mode = ""
    while mode != "q":
        mode = input("mode (-h for help): ").lower()
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
        elif mode == "cls":
            file.clear_screen()
        elif mode == "q":
            return
        elif mode == "save":
            reading_data.saving_file(file.dict_datas, headers)      
        elif mode == "-h":
            menu()
    

if __name__ == "__main__":
    main()