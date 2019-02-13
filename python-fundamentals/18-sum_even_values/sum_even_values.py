def sum_even_values(li):
    """ sums even values in list and returns sum """
    total = 0

    for num in li:
        if num % 2 == 0:
            total += num 

    return total

    # return sum([num for num in li if num % 2 == 0])