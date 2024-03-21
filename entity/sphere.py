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
            theta = math.pi * i / (num_vertices - 1)
            for j in range(num_vertices * 2):
                if j < num_vertices:
                    phi = math.pi * j / (num_vertices - 1)
                    x = math.sin(phi) * math.cos(theta)
                    y = math.sin(phi) * math.sin(theta)
                    z = math.cos(phi)
                    vertices.append((x, y, z))

        for i in range(num_vertices):
            theta = math.pi * i / (num_vertices - 1)
            for j in range(num_vertices * 2):
                if j >= num_vertices:
                    phi = math.pi * (j - 1) / (num_vertices - 1)
                    x = math.sin(phi) * math.cos(theta) / 2 * -1
                    y = math.sin(phi) * math.sin(theta) / 2 * -1
                    z = math.cos(phi) / 2
                    vertices.append((x, y, z))

        return vertices

    def generate_sphere_polygons(self, num_vertices):
        polygons = []
        for i in range(num_vertices - 1):
            for j in range(num_vertices - 1):
                v1 = i * num_vertices + j
                v2 = (i + 1) % num_vertices * num_vertices + j
                v3 = (i + 1) % num_vertices * num_vertices + (j + 1)
                v4 = i * num_vertices + (j + 1)
                polygons.append((v1, v2, v3, v4))

                v1 = i * num_vertices + j + num_vertices ** 2
                v2 = (i + 1) % num_vertices * num_vertices + j + num_vertices ** 2
                v3 = (i + 1) % num_vertices * num_vertices + (j + 1) + num_vertices ** 2
                v4 = i * num_vertices + (j + 1) + num_vertices ** 2
                polygons.append((v1, v2, v3, v4))

        for i in (0, num_vertices - 1):
            for j in range(num_vertices - 1):
                v1 = i * num_vertices + j
                v2 = i * num_vertices + (j + 1) + num_vertices ** 2 + ((num_vertices -2) - 2 * j)
                v3 = i * num_vertices + j + num_vertices ** 2 + ((num_vertices -2) - 2 * j)
                v4 = i * num_vertices + (j + 1)

                if i == 0:
                    polygons.append((v4, v3, v2, v1))
                else:
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
