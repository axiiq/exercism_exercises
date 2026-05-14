"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int):  Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int):  Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """
    total_aliens_created = 0
    
    def __init__(self, x_coord, y_coord):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, other):
        pass

#TODO (Student):  Create the new_aliens_collection() function below to call your Alien class with a list of coordinates
def new_aliens_collection(positions):
    aliens = []
    for pos in positions:
        aliens.append(Alien(pos[0],pos[1]))
    return aliens
    
