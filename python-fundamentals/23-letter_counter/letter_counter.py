def letter_counter(string):
""" returns number of times letter occurs in string """

    def inner_count(letter):
        return string.lower().count(letter.lower())
    
    return inner_count
