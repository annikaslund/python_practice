def extract_full_name(li):
    """ returns list of full names of people in the argument list""" 
    
    names = []

    for person in li:
        f_name = person["first"]
        l_name = person["last"]
        names.append(f"{f_name} {l_name}")

    return names

    # return [f"{person['first']} {person['last']}" for person in li]