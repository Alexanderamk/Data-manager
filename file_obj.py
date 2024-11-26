from tabulate import tabulate  # Correct import


class FileMaintaining:
    def __init__(self, headers, dict_datas):
        self.headers = headers
        self.dict_datas = dict_datas
        self.tot_num_row = len(dict_datas)

        if self.tot_num_row > 100:
            row_100 = dict_datas[:50]        
        
        self.rows_100 = row_100


    def searching_data(self, mode):
        print(f"Keywords to {mode} by> {', '.join([head for head in self.headers])}")
        keyword = input("keyword: ")
        while keyword not in self.headers:
            keyword = input("Make sure your keyword is \nthe same with the header in the file: ")
        
        search = input(f"{mode} by {keyword}: ")
        return keyword, search

    def display(self):
            grid_fmt = "pretty"
            if self.rows_100:
                print(tabulate(self.rows_100, headers="keys", tablefmt=grid_fmt))
                print(f"Total rows: {len(self.dict_datas)}")
            else:
                print(tabulate(self.dict_datas, headers="keys", tablefmt=grid_fmt))
                print(f"Total rows: {len(self.dict_datas)}")       
    
    def add(self, times):
        for _ in range(times):
            new_row = {}
            for field in self.headers:
                new = input(f"Enter the new '{field}': ")
                if new == "":
                    new_row[field] = "-"
                else:
                    new_row[field] = new
            self.dict_datas.append(new_row)
            print() # For space
        self.display()
    
    def search(self):
        keyword, search = self.searching_data("search")
        
        dict_find = []
        for data in self.dict_datas:
            if data[keyword] == search:
                dict_find.append(data)

        if dict_find:
            print(tabulate(dict_find, headers="keys"))
            print(f"Total rows: {len(dict_find)}")
        else:
            print(f"data with {keyword} = {search} is not found")
    
    def delete(self):
        keyword, search = self.searching_data("delete")

        for data in self.datas:
            if data[keyword] == search:
                ...