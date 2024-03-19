from typing import Optional

from entity.edge import Edge
from entity.entity import Entity
from entity.face import Face
from entity.point3d import Point3D
from utils.color import Color


class Cube(Entity):
    def front_face(self):
        p0 = self.shift_point(0.0, 0.0, 0.0)
        p1 = self.shift_point(0.0, 1.0, 0.0)
        p2 = self.shift_point(1.0, 1.0, 0.0)
        p3 = self.shift_point(1.0, 0.0, 0.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0)
        ])

    def back_face(self):
        p0 = self.shift_point(1.0, 0.0, 1.0)
        p1 = self.shift_point(1.0, 1.0, 1.0)
        p2 = self.shift_point(0.0, 1.0, 1.0)
        p3 = self.shift_point(0.0, 0.0, 1.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0)
        ])

    def left_face(self):
        p0 = self.shift_point(0.0, 0.0, 1.0)
        p1 = self.shift_point(0.0, 1.0, 1.0)
        p2 = self.shift_point(0.0, 1.0, 0.0)
        p3 = self.shift_point(0.0, 0.0, 0.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def right_face(self):
        p0 = self.shift_point(1.0, 0.0, 0.0)
        p1 = self.shift_point(1.0, 1.0, 0.0)
        p2 = self.shift_point(1.0, 1.0, 1.0)
        p3 = self.shift_point(1.0, 0.0, 1.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def top_face(self):
        p0 = self.shift_point(0.0, 1.0, 0.0)
        p1 = self.shift_point(0.0, 1.0, 1.0)
        p2 = self.shift_point(1.0, 1.0, 1.0)
        p3 = self.shift_point(1.0, 1.0, 0.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def bottom_face(self):
        p0 = self.shift_point(1.0, 0.0, 0.0)
        p1 = self.shift_point(1.0, 0.0, 1.0)
        p2 = self.shift_point(0.0, 0.0, 1.0)
        p3 = self.shift_point(0.0, 0.0, 0.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def __init__(
            self,
            cords: Point3D,
            scale: float,
            visible_lines_color: Optional[Color] = None,
            invisible_lines_color: Optional[Color] = None
    ):
        super().__init__(
            cords,
            scale,
            visible_lines_color,
            invisible_lines_color
        )

        self.set_faces([
            self.top_face(),
            self.bottom_face(),
            self.back_face(),
            self.front_face(),
            self.left_face(),
            self.right_face()
        ])
