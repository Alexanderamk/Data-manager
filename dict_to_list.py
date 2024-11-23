def dict_to_list(dict, header):
    
    list = []
    for data in dict:
        section = []
        for field in header:
            if data[field] == "":
                section.append("-")
            else:
                section.append(data[field])
        list.append(section)
    
    return list