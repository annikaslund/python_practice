def number_compare(num1, num2):
    """ takes in two numbers and returns a string 
    indicating how the numbers compare to each other. """ 

    if num1 > num2: 
        return "First is greater"
    elif num2 > num1: 
        return "Second is greater"
    else: 
        return "Numbers are equal"