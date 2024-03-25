from typing import List, Optional

from entity.face import Face
from entity.point3d import Point3D
from utils.color import Color, random_color


class Entity:
    def __init__(
            self,
            cords: Point3D,
            scale: float,
            visible_lines_color: Optional[Color] = None,
            invisible_lines_color: Optional[Color] = None
    ):
        self.cords = cords
        self.scale = scale
        self.faces: List[Face] = []
        self.visible_lines_color = visible_lines_color if visible_lines_color else random_color()
        self.invisible_lines_color = invisible_lines_color if invisible_lines_color else random_color()
        self.f_theta = 0.0

    def set_faces(self, faces: List[Face]):
        self.faces = faces

    def shift_point(self, shift_x: float, shift_y: float, shift_z: float):
        return Point3D(
            self.cords.x + (shift_x * self.scale),
            self.cords.y + (shift_y * self.scale),
            self.cords.z + (shift_z * self.scale)
        )

    def move(self):
        pass
