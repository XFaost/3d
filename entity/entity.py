from typing import List

from entity.face import Face
from entity.point3d import Point3D


class Entity:
    def __init__(self, cords: Point3D, scale: float):
        self.cords = cords
        self.scale = scale
        self.faces: List[Face] = []

    def set_faces(self, faces: List[Face]):
        self.faces = faces

    def shift_point(self, shift_x: float, shift_y: float, shift_z: float):
        return Point3D(
            self.cords.x + (shift_x * self.scale),
            self.cords.y + (shift_y * self.scale),
            self.cords.z + (shift_z * self.scale)
        )
