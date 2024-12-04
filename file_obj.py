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
            mode = {"align": "pretty", "grid": "outline"}
            keys = list(mode.keys())
            print(f"Grid Type: {', '.join(keys)} or enter for default.")
            grid_fmt = input("> ")

            if grid_fmt:
                self.grid_fmt = mode[grid_fmt]     
            datas = self.dict_datas[:50]
        elif dis_mode == "add":
            datas = self.dict_datas[-10:]            

        if self.__more_than_100(self.dict_datas) and (dis_mode == "df" or dis_mode == "add"):
            print(tabulate(datas, headers="keys", tablefmt=self.grid_fmt))
            print(f"Total rows: {len(self.dict_datas)}")
        else:
            if dis_mode == "df" or dis_mode == "add":
                print(tabulate(self.dict_datas, headers="keys", tablefmt=self.grid_fmt))
            else:
                print(tabulate(datas, headers="keys", tablefmt=self.grid_fmt))
            if dis_mode == "search" or dis_mode == "delete" or dis_mode == "update":
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
        keyword, value = self.searching_data("search")
        
        dict_find = []
        for data in self.dict_datas:
            if data[keyword] == value:
                dict_find.append(data)

        if dict_find:
            self.display("search", dict_find)
        else:
            print(f"Data with {keyword} = {value} was not found")
        
    def delete(self):
        keywords_dict = self.searching_data("delete")
        if keywords_dict is None:
            print("Delete operation canceled.")
            return

        dict_delete = []
        for data in self.dict_datas:
            match = all(data.get(k) == v for k, v in keywords_dict.items())
            if match:
                dict_delete.append(data)

        if dict_delete:
            for entry in dict_delete:
                self.dict_datas.remove(entry)
            self.display("delete", dict_delete)
        else:
            print(f"No data found matching to delete.")
        
    def searching_data(self, mode):
        print(f"Keywords to {mode} by> {', '.join(self.headers)}")
        keyword = input("Keyword: ")
        while keyword not in self.headers:
            keyword = input("Make sure your keyword matches a header in the file: ")

        value = input(f"{mode.capitalize()} by {keyword}: ")

        if mode == "delete" or mode == "update":
            print(f"Do you want to {mode} all the data where {keyword} is {value}?")
            specific = input("y (to agree), sp(to specify more), or q (to cancel): ")
            if specific.lower() == "y":
                return {keyword: value}
            elif specific.lower() == "q":
                return None
            elif specific.lower() == "sp":
                num_keys = int(input("Num of keywords to specify (no more than 3): "))
                while num_keys > 3:
                    num_keys = int(input("Num of keywords must be <= 3: "))
                
                additional_keys = {keyword: value}
                for _ in range(num_keys):
                    available_headers = [head for head in self.headers if head not in additional_keys]
                    extra_key = input(f"Additional keyword {', '.join(available_headers)}: ")
                    while extra_key not in available_headers:
                        extra_key = input("Make sure the additional keyword matches a header in the file and is different from the others: ")
                    extra_value = input(f"{mode.capitalize()} by {extra_key}: ")
                    additional_keys[extra_key] = extra_value

                return additional_keys
        else:
            return keyword, value

    def update(self):
        # Use the searching_data function in "update" mode
        criteria = self.searching_data("update")
        if criteria is None:
            print("Update canceled.")
            return

        # Find matching data
        matching_records = []
        for record in self.dict_datas:
            if all(record.get(key) == value for key, value in criteria.items()):
                matching_records.append(record)

        if not matching_records:
            print("No matching records found.")
            return

        # Display the matching records
        print("Matching records:")
        self.display("update", matching_records)
            
        # Prompt the user to update specific fields
        for record in matching_records:
            for key in self.headers:
                if key in record:  # Only allow updating existing fields
                    new_value = input(f"Enter new value for '{key}' (leave blank to keep '{record[key]}'): ")
                    if new_value:
                        record[key] = new_value # update the self.dict_datas directly due to the reference-based nature of Python's mutable objects
            print() # for new line
    