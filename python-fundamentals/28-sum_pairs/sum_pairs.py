def sum_pairs(li, num):
    for num1 in li:
        for num2 in li:
            if num1 + num2 == num:
                return (num1, num2)
    
    return ()