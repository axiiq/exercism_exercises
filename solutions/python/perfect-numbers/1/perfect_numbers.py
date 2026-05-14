def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    counter = 0

    for num in range(1, number):
        if number % num == 0:
            counter += num

    if counter == number:
        return "perfect"

    if counter > number:
        return "abundant"

    return "deficient"