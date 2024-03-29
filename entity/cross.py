from typing import Optional

from entity.edge import Edge
from entity.entity import Entity
from entity.face import Face
from entity.point3d import Point3D
from utils.color import Color, random_color


class Cross(Entity):
    def front_face(self):
        p0 = self.shift_point(1.0, 0.0, 0.0)
        p1 = self.shift_point(1.0, 1.0, 0.0)
        p2 = self.shift_point(0.0, 1.0, 0.0)
        p3 = self.shift_point(0.0, 2.0, 0.0)
        p4 = self.shift_point(1.0, 2.0, 0.0)
        p5 = self.shift_point(1.0, 4.0, 0.0)
        p6 = self.shift_point(2.0, 4.0, 0.0)
        p7 = self.shift_point(2.0, 2.0, 0.0)
        p8 = self.shift_point(3.0, 2.0, 0.0)
        p9 = self.shift_point(3.0, 1.0, 0.0)
        p10 = self.shift_point(2.0, 1.0, 0.0)
        p11 = self.shift_point(2.0, 0.0, 0.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p4),
            Edge(p4, p5),
            Edge(p5, p6),
            Edge(p6, p7),
            Edge(p7, p8),
            Edge(p8, p9),
            Edge(p9, p10),
            Edge(p10, p11),
            Edge(p11, p0),
        ])

    def back_face(self):
        p0 = self.shift_point(2.0, 0.0, 1.0)
        p1 = self.shift_point(2.0, 1.0, 1.0)
        p2 = self.shift_point(3.0, 1.0, 1.0)
        p3 = self.shift_point(3.0, 2.0, 1.0)
        p4 = self.shift_point(2.0, 2.0, 1.0)
        p5 = self.shift_point(2.0, 4.0, 1.0)
        p6 = self.shift_point(1.0, 4.0, 1.0)
        p7 = self.shift_point(1.0, 2.0, 1.0)
        p8 = self.shift_point(0.0, 2.0, 1.0)
        p9 = self.shift_point(0.0, 1.0, 1.0)
        p10 = self.shift_point(1.0, 1.0, 1.0)
        p11 = self.shift_point(1.0, 0.0, 1.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p4),
            Edge(p4, p5),
            Edge(p5, p6),
            Edge(p6, p7),
            Edge(p7, p8),
            Edge(p8, p9),
            Edge(p9, p10),
            Edge(p10, p11),
            Edge(p11, p0),
        ])

    def left_face(self):
        p0 = self.shift_point(0.0, 1.0, 1.0)
        p1 = self.shift_point(0.0, 2.0, 1.0)
        p2 = self.shift_point(0.0, 2.0, 0.0)
        p3 = self.shift_point(0.0, 1.0, 0.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def right_face(self):
        p0 = self.shift_point(3.0, 1.0, 0.0)
        p1 = self.shift_point(3.0, 2.0, 0.0)
        p2 = self.shift_point(3.0, 2.0, 1.0)
        p3 = self.shift_point(3.0, 1.0, 1.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def top_face(self):
        p0 = self.shift_point(1.0, 0.0, 0.0)
        p1 = self.shift_point(2.0, 0.0, 0.0)
        p2 = self.shift_point(2.0, 0.0, 1.0)
        p3 = self.shift_point(1.0, 0.0, 1.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def bottom_face(self):
        p0 = self.shift_point(1.0, 4.0, 1.0)
        p1 = self.shift_point(2.0, 4.0, 1.0)
        p2 = self.shift_point(2.0, 4.0, 0.0)
        p3 = self.shift_point(1.0, 4.0, 0.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def left_top_face(self):  # самий низ
        p0 = self.shift_point(0.0, 1.0, 0.0)
        p1 = self.shift_point(1.0, 1.0, 0.0)
        p2 = self.shift_point(1.0, 1.0, 1.0)
        p3 = self.shift_point(0.0, 1.0, 1.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def right_top_face(self):  # самий низ
        p0 = self.shift_point(2.0, 1.0, 0.0)
        p1 = self.shift_point(3.0, 1.0, 0.0)
        p2 = self.shift_point(3.0, 1.0, 1.0)
        p3 = self.shift_point(2.0, 1.0, 1.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def left_bottom_face(self):  # самий низ
        p0 = self.shift_point(0.0, 2.0, 1.0)
        p1 = self.shift_point(1.0, 2.0, 1.0)
        p2 = self.shift_point(1.0, 2.0, 0.0)
        p3 = self.shift_point(0.0, 2.0, 0.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def right_bottom_face(self):  # самий низ
        p0 = self.shift_point(2.0, 2.0, 1.0)
        p1 = self.shift_point(3.0, 2.0, 1.0)
        p2 = self.shift_point(3.0, 2.0, 0.0)
        p3 = self.shift_point(2.0, 2.0, 0.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def top_left_face(self):  # самий низ
        p0 = self.shift_point(1.0, 0.0, 0.0)
        p1 = self.shift_point(1.0, 0.0, 1.0)
        p2 = self.shift_point(1.0, 1.0, 1.0)
        p3 = self.shift_point(1.0, 1.0, 0.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def top_right_face(self):  # самий низ
        p0 = self.shift_point(2.0, 1.0, 0.0)
        p1 = self.shift_point(2.0, 1.0, 1.0)
        p2 = self.shift_point(2.0, 0.0, 1.0)
        p3 = self.shift_point(2.0, 0.0, 0.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def bottom_left_face(self):  # самий низ
        p0 = self.shift_point(1.0, 2.0, 0.0)
        p1 = self.shift_point(1.0, 2.0, 1.0)
        p2 = self.shift_point(1.0, 4.0, 1.0)
        p3 = self.shift_point(1.0, 4.0, 0.0)

        return Face([
            Edge(p0, p1),
            Edge(p1, p2),
            Edge(p2, p3),
            Edge(p3, p0),
        ])

    def bottom_right_face(self):  # самий низ
        p0 = self.shift_point(2.0, 4.0, 0.0)
        p1 = self.shift_point(2.0, 4.0, 1.0)
        p2 = self.shift_point(2.0, 2.0, 1.0)
        p3 = self.shift_point(2.0, 2.0, 0.0)

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

        self.init_faces()

    def init_faces(self):
        self.set_faces([
            self.top_face(),
            self.bottom_face(),
            self.back_face(),
            self.front_face(),
            self.left_face(),
            self.right_face(),
            self.left_top_face(),
            self.right_top_face(),
            self.left_bottom_face(),
            self.right_bottom_face(),
            self.top_left_face(),
            self.top_right_face(),
            self.bottom_left_face(),
            self.bottom_right_face(),
        ])