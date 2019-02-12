def multiply_even_numbers(li):
    total = 1

    for num in li:
        if num % 2 == 0:
            total *= num
    
    return total