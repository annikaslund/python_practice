def partition(li, cb):
    """ checks each item in the list, evaulates truthiness, 
    if true sorted into true_items list, if false sorts into false_items list.
    returns both lists in a new list """

    true_items = []
    false_items = []

    for item in li: 
        if cb(item):
            true_items.append(item)
        else: 
            false_items.append(item)
    
    return [true_items, false_items]