def mode(li):
    """ takes in list, returns most frequent number in the list """

    num_counts = {}
    most_frequent = None

    for num in li: 
        num_counts[num] = num_counts.get(num, 0) + 1
    
    for (num, freq) in num_counts.items(): 
        if most_frequent is None or freq > most_frequent:
            most_frequent = num

    return most_frequent

    
