from entity.edge import Edge
from entity.entity import Entity
from entity.face import Face
from entity.point3d import Point3D
from utils.color import Color


class Surface(Entity):

    def face(self):
        p0 = self.shift_point(0.0, 0.0, 0.0)
        p1 = self.shift_point(0.0, 1.0, 0.0)
        p2 = self.shift_point(1.0, 1.0, 0.0)
        p3 = self.shift_point(1.0, 0.0, 0.0)
        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def __init__(self, cords: Point3D, scale: float, color: Color):
        self.color = color
        super().__init__(cords, scale)

        self.set_faces([
            self.face()
        ])


