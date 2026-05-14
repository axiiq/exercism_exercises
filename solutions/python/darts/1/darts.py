"""Module for darts with a scoring function."""
def score(x, y):
    """Function for calculating score based on the coordinates of the dart."""
    val = (x**2+y**2)**(1/2)
    # inner - 1 unit radius
    if val <= 1:
        return 10

    # middle - 5 unit radius
    if val <= 5:
        return 5
    
    # outer - 10 unit radius
    if val <= 10:
        return 1

    return 0
    
