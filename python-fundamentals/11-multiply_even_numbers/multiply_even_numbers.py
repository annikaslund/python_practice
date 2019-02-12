def multiply_even_numbers(li):
""" takes in a list, multiples all even numbers, and returns 
product """

    total = 1

    for num in li:
        if num % 2 == 0:
            total *= num
    
    return total