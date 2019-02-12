def flip_case(str, letter):
    swapped = ""

    for let in str:
        if let.lower() == letter.lower():
            let = let.swapcase()
        swapped += let 
    
    return swapped