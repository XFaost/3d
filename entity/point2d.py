
class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    def __repr__(self):
        return f'{self.x}, {self.y}'

    def __eq__(self, other):
        if all([
            self.x == other.x,
            self.x == other.y
        ]):
            return True

