def validation(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b < c or b + c < a or a + c < b:
        return False
    return True

def equilateral(sides):
    a, b, c = sides
    if not validation(sides):
        return False
    if a == b and b == c:
        return True
    return False


def isosceles(sides):
    a, b, c = sides
    if not validation(sides):
        return False
    if a == b:
        return True
    if a == c:
        return True
    if c == b:
        return True
    return False
        

def scalene(sides):
    a, b, c = sides
    if not validation(sides):
        return False
    if a != b and b != c and c != a:
        return True
    return False
