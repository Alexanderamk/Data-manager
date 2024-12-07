def menu():
    messages = [
        ["'dp' to display the data    "],
        ["'s' to search data          "],
        ["'a' to add new data         "],
        ["'del' to delete the data    "],
        ["'up' to update/edit the data"],
        ["'cls' to clear the screen"   ],
        ["'q' to quit the program     "],
        ["'save' to save the file     "]
    ]

    for message in messages:
        print(*message)
