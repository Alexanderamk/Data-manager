from tabulate import tabulate  # Correct import


class FileMaintaining:
    def __init__(self, headers, dict_datas):
        self.headers = headers
        self.dict_datas = dict_datas
        self.grid_fmt = ""

    def __more_than_100(self, datas):
        tot_num_row = len(datas)
        if tot_num_row > 100:
            return True
        return False 

    def display(self, dis_mode="df", dict_find=None):
        datas = dict_find

        if dis_mode == "df":
            mode = {"align": "pretty", "grid_1": "outline", "grid_2": "presto"}
            keys = list(mode.keys())
            print(f"Grid Type: {', '.join(keys)}")
            grid_fmt = input("> ")

            while grid_fmt not in keys:
                print(f"Grid Type: {', '.join(keys)}")
                grid_fmt = input(f"Only choose from the provide list: ")

            self.grid_fmt = mode[grid_fmt]     
            datas = self.dict_datas[:50]
        elif dis_mode == "add":
            datas = self.dict_datas[-10:]

        if self.__more_than_100(self.dict_datas) and (dis_mode == "df" or dis_mode == "add"):
            print(tabulate(datas, headers="keys", tablefmt=self.grid_fmt))
            print(f"Total rows: {len(self.dict_datas)}")
        else:
            print(tabulate(datas, headers="keys", tablefmt=self.grid_fmt))
            if dis_mode == "search":
                print(f"Total rows: {len(datas)}")
            else:
                print(f"Total rows: {len(self.dict_datas)}")  
        datas = [] # Freeing memory

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
        self.display("add")
    
    def search(self):
        keyword, search = self.searching_data("search")
        
        dict_find = []
        for data in self.dict_datas:
            if data[keyword] == search:
                dict_find.append(data)

        if dict_find:
            self.display("search", dict_find)
        else:
            print(f"datas with {keyword} is {search} are not found")
    
    def delete(self):
        keywords_dict = self.searching_data("delete")

        if keywords_dict:
            keywords = keywords_dict.keys()
            for data in self.dict_datas:
                for key in keywords:
                    if data[key] == keywords_dict[key]:
                        self.dict_datas.remove(data)
        else:
            print("Deletion has quit.")

    def searching_data(self, mode):
        print(f"Keywords to {mode} by> {', '.join([head for head in self.headers])}")
        keyword = input("keyword: ")
        while keyword not in self.headers:
            keyword = input("Make sure your keyword is same with the header in the file: ")
            
        value = input(f"{mode} by {keyword}: ")

        if mode == "delete":
            keywords = {}
            print(f"Do you want to delete all the data with {keyword} is {value}?")
            specific = input("y(to agree) or n(to specific more) or q(for cancle): ")
            if specific.lower() == "y":
                keywords[keyword] = value
                return keywords
            elif specific.lower() == "q":
                return None
            elif specific.lower() == "n":
                

                times = input("Num keywords to specify (no more than 3): ")
                while times > 3:
                    times = input("Num of keywords must be <= 3: ")


        else:
            return keyword, value
