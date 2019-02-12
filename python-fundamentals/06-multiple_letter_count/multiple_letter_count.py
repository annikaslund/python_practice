def multiple_letter_count(str):
    """ takes in a phrase and returns a dictionary 
    with the amount of times letters appear in the phrase""" 

    letter_count = {}

    for letter in str: 
        if letter in letter_count: 
            letter_count[letter] += 1
        else: 
            letter_count[letter] = 1
    
    return letter_count