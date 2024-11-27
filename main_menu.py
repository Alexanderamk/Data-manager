def menu():
    messages = [
        ["'dp' to display the data    "],
        ["'a' to add new data         "],
        ["'s' to search data          "],
        ["'del' to delete the data    "],
        ["'up' to update/edit the data"],
        ["'q' to quit the program     "],
        ["'-h' to see main menu       "],
    ]

    for message in messages:
        print(*message)
