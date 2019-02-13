def all_lists(li):
    for item in li:
        if not isinstance(item, li):
            return False 
    return True