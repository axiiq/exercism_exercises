def ordinal(number):
    ending = ""

    number = str(number)


    if number[-2::] == "11" or number[-2::] == "12" or number[-2::] == "13":
        ending = "th"
    
    elif number[-1] == "1":
        ending = "st"

    elif number[-1] == "2":
        ending = "nd"

    elif number[-1] == "3":
        ending = "rd"

    else:
        ending = "th"
    
    return f"{number}{ending}"
    
def line_up(name, number):
    return f"{name}, you are the {ordinal(number)} customer we serve today. Thank you!"
