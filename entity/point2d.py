class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    def __round(self, value):
        return round(value, 4)

    def __repr__(self):
        return f'({self.__round(self.x)}, {self.__round(self.y)})'
