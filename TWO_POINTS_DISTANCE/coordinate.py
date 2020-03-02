
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def find_distance(self, coordinate):
        dx = (self.x - coordinate.x)**2
        dy = (self.y - coordinate.y)**2

        return (dx+dy)**0.5




