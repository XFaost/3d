
class Point3D:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __round(self, value):
        return round(value, 4)

    def __repr__(self):
        return f'({self.__round(self.x)}, {self.__round(self.y)}, {self.__round(self.z)})'
