def intersection(li1, li2):
    """ finds items that exist in both list one and list two, 
    returns in a new list """
    
    return list(set(li1) & set(li2))