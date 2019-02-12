def return_day(num):
    """ takes in a number representing a day of the week, returns 
    a string of that day of the week """

    day_pair = {1: "Sunday", 2: "Monday", 3: "Tuesday", 
    4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}

    if num > 0 and num < 8:
        return day_pair[num]