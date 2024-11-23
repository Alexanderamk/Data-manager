from tabulate import tabulate  # Correct import
from dict_to_list import dict_to_list


class FileMaintaining:
    def __init__(self, header, datas, dict_datas):
        self.header = header
        self.datas = datas
        self.dict_datas = dict_datas

    def display(self):
            print(tabulate(self.datas, self.header))
            print(f"Total rows: {len(self.datas)} \n")
    
    def add(self, times):
        for _ in range(times):
            new_row = []
            for field in self.header:
                new = input(f"Enter the new '{field}': ")
                if new == "":
                    new_row.append("-")
                else:
                    new_row.append(new)
            self.datas.append(new_row)
            print() # For space
        self.display()
    
    def search(self):
        print(f"Keywords to search by> {', '.join([head for head in self.header])}")
        keyword = input("keyword: ")
        while keyword not in self.header:
            keyword = input("Make sure your keyword is \nthe same with the header in the file: ")
        
        search = input(f"Search by {keyword}: ")
        dict_find = []
        for data in self.dict_datas:
            if data[keyword] == search:
                dict_find.append(data)

        if dict_find:
            list_find = dict_to_list(dict_find, self.header)
            print(tabulate(list_find, self.header))
            print(f"Total rows: {len(list_find)}")
        else:
            print(f"data with {keyword} = {search} is not found")