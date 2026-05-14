def is_valid(isbn):
    counter = 0
    new_isbn = isbn.replace("-","")

    if len(new_isbn) != 10:
        return False

    for index in range(10):
        digit = new_isbn[index]

        if not digit.isnumeric() and (digit != 'X' or index != 9):
            return False
        
        if digit == 'X' and index == 9:
            digit = "10"

        counter = counter + (int(digit) * (10 - index))

    if counter % 11 == 0:
        return True

    return False
