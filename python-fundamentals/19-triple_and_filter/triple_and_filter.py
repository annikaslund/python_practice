def triple_and_filter(li):
    """ returns list of all numbers that are divisible by 4 tripled """
    
    return [num * 3 for num in li if num % 4 == 0]