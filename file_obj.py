from tabulate import tabulate  # Correct import


class FileMaintaining:
    def __init__(self, header, datas):
        self.header = header
        self.datas = datas

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