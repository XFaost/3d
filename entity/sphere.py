import math
from typing import Optional

from entity.edge import Edge
from entity.entity import Entity
from entity.face import Face
from entity.point3d import Point3D
from utils.color import Color


class Sphere(Entity):
    def generate_sphere_vertices(self, num_vertices):
        vertices = []
        for i in range(num_vertices):
            theta = 2 * math.pi * i / num_vertices
            for j in range(num_vertices):
                phi = math.pi * j / (num_vertices - 1)
                x = math.sin(phi) * math.cos(theta)
                y = math.sin(phi) * math.sin(theta)
                z = math.cos(phi)
                vertices.append((x, y, z))
        return vertices

    def generate_sphere_polygons(self, num_vertices):
        polygons = []
        for i in range(num_vertices):
            for j in range(num_vertices - 1):
                vertices = (
                    i * num_vertices + (j + 1),
                    (i + 1) % num_vertices * num_vertices + (j + 1),
                    (i + 1) % num_vertices * num_vertices + j,
                    i * num_vertices + j
                )
                polygons.append(vertices)
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
            points = []
            for i in range(len(polygon)):
                points.append(
                    self.shift_point(
                        sphere_vertices[polygon[i]][0],
                        sphere_vertices[polygon[i]][1],
                        sphere_vertices[polygon[i]][2]
                    )
                )

            edges = []
            for i in range(len(points) - 1):
                if points[i] != points[i + 1]:
                    edges.append(
                        Edge(points[i], points[i + 1])
                    )
            if points[-1] != points[0]:
                edges.append(
                    Edge(points[-1], points[0])
                )

            faces.append(
                Face(edges)
            )

        self.set_faces(faces)
