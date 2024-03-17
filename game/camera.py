from math import tan
from typing import List

import numpy
import pygame

from entity.entity import Entity
from entity.point2d import Point2D
from entity.point3d import Point3D
from game.environment import Environment
from game.screen import Screen
from utils.color import RED, BLUE


class Camera:
    def __init__(self, perspective_amount: float, screen: Screen):
        self.perspective_amount = perspective_amount
        self._screen = screen

        self._init_mat_proj()

    def _multiply_matrix_vector(self, point: Point3D, m: numpy.ndarray):
        x = point.x * m[0][0] + point.y * m[1][0] + point.z * m[2][0] + m[3][0]
        y = point.x * m[0][1] + point.y * m[1][1] + point.z * m[2][1] + m[3][1]
        z = point.x * m[0][2] + point.y * m[1][2] + point.z * m[2][2] + m[3][2]

        w = point.x * m[0][3] + point.y * m[1][3] + point.z * m[2][3] + m[3][3]

        if w != 0.0:
            x /= w
            y /= w
            z /= w

        return Point3D(float(x), float(y), float(z))

    def _init_mat_proj(self):
        self._mat_proj = numpy.zeros((4, 4))

        f_near = 0.1
        f_far = 1000.0
        f_fov = 90.0
        f_aspect_ratio = self._screen.height / self._screen.width
        f_fov_rad = 1.0 / tan(f_fov * 0.5 / 180.0 * 3.14159)

        self._mat_proj[0][0] = f_aspect_ratio * f_fov_rad
        self._mat_proj[1][1] = f_fov_rad
        self._mat_proj[2][2] = f_far / (f_far - f_near)
        self._mat_proj[3][2] = (-f_far * f_near) / (f_far - f_near)
        self._mat_proj[2][3] = 1.0
        self._mat_proj[3][3] = 0.0

    def point_from_3d_to_2d(self, point: Point3D):
        # в pygame y та z розвернуті, тому додаю мінус
        fix_point = Point3D(point.x, -point.y, -point.z)
        point_projected = self._multiply_matrix_vector(fix_point, self._mat_proj)

        result = point_projected
        return Point2D(result.x, result.y)

    def render_line(
            self,
            a: Point3D,
            b: Point3D,
            entities: List[Entity],
            entity_index: int
    ):
        a_2d = self.point_from_3d_to_2d(a)
        b_2d = self.point_from_3d_to_2d(b)

        a_screen_cords = self._screen.point_to_screen_cords(a_2d).get()
        b_screen_cords = self._screen.point_to_screen_cords(b_2d).get()

        pygame.draw.line(
            self._screen.get(),
            RED.get(),
            a_screen_cords,
            b_screen_cords,
            1
        )

    def render_environment(
            self,
            environment: Environment
    ):
        self._screen.fill(environment.bg_color)

    def render_3d_entity(
            self,
            entities: List[Entity],
            index: int
    ):
        for face in entities[index].faces:
            for edge in face.edges:
                self.render_line(
                    edge.a,
                    edge.b,
                    entities,
                    index
                )
