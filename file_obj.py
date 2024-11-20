from tabulate import tabulate  # Correct import


class FileMaintaining:
    def __init__(self, header, datas):
        self.header = header
        self.datas = datas

    def display(self):
            print(tabulate(self.datas, self.header))
