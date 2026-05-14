def is_armstrong_number(number):
    num = str(number)
    expo = len(num)

    counter = 0
    for digit in num:
        counter += (int(digit)**expo)

    if number == counter:
        return True
    return False
