import math
from typing import Optional

import numpy as np

from entity.edge import Edge
from entity.entity import Entity
from entity.face import Face
from entity.point3d import Point3D
from utils.color import Color


class Sphere(Entity):
    def generate_sphere_vertices(self, num_vertices):
        vertices = []
        for i in range(num_vertices):
            theta = 2 * np.pi * i / num_vertices
            for j in range(num_vertices):
                phi = np.pi * j / (num_vertices - 1)
                x = np.sin(phi) * np.cos(theta)
                y = np.sin(phi) * np.sin(theta)
                z = np.cos(phi)
                vertices.append((x, y, z))
        return vertices

    def generate_sphere_polygons(self, num_vertices):
        polygons = []
        for i in range(num_vertices):
            for j in range(num_vertices - 1):
                v1 = i * num_vertices + j
                v2 = (i + 1) % num_vertices * num_vertices + j
                v3 = (i + 1) % num_vertices * num_vertices + (j + 1)
                v4 = i * num_vertices + (j + 1)
                polygons.append((v1, v2, v3, v4))
        return polygons

    def __init__(
            self,
            cords: Point3D,
            scale: float,
            lines_color: Optional[Color] = None
    ):
        super().__init__(
            cords,
            scale,
            lines_color
        )

        faces = []

        sphere_vertices = self.generate_sphere_vertices(12)
        sphere_polygons = self.generate_sphere_polygons(12)

        for polygon in sphere_polygons:
            p0 = self.shift_point(sphere_vertices[polygon[3]][0], sphere_vertices[polygon[3]][1],
                                  sphere_vertices[polygon[3]][2])
            p1 = self.shift_point(sphere_vertices[polygon[2]][0], sphere_vertices[polygon[2]][1],
                                  sphere_vertices[polygon[2]][2])
            p2 = self.shift_point(sphere_vertices[polygon[1]][0], sphere_vertices[polygon[1]][1],
                                  sphere_vertices[polygon[1]][2])
            p3 = self.shift_point(sphere_vertices[polygon[0]][0], sphere_vertices[polygon[0]][1], sphere_vertices[polygon[0]][2])




            faces.append(
                Face([
                    Edge(p0, p1),
                    Edge(p1, p2),
                    Edge(p2, p3),
                    Edge(p3, p0)
                ])
            )

        self.set_faces(faces)
