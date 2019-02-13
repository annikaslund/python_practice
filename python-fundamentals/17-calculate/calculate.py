def calculate(op, first, second, make_int=False, msg="Success!"):
    if op == "add":
        addition = first + second
        string_sum = f" {addition}"
        return msg + string_sum
    if op == "subtract":
        subtraction = first - second
        string_diff = f" {subtraction}"
        return msg + string_diff
    if op == "multiply":
        product = first * second
        string_prod = f" {product}"
        return msg + string_prod
