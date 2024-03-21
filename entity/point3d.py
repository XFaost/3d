class Point3D:
    def __init__(self, x: float, y: float, z: float):
        self.x = round(x, 4)
        self.y = round(y, 4)
        self.z = round(z, 4)

    def __repr__(self):
        return f'{self.x}, {self.y}, {self.z}'

    def __eq__(self, other):
        if all([
            self.x == other.x,
            self.y == other.y,
            self.z == other.z,
        ]):
            return True
