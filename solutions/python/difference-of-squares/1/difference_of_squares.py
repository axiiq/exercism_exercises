def square_of_sum(number):
    added = sum([num for num in range(number+1)])
    return added**2

def sum_of_squares(number):
    added = sum([num**2 for num in range(number+1)])
    return added

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
