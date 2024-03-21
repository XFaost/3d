import copy
from math import tan, sqrt, cos, sin

import numpy
import pygame

from entity.entity import Entity
from entity.face import Face
from entity.point2d import Point2D
from entity.point3d import Point3D
from game.environment import Environment
from game.screen import Screen
from utils.color import RED, Color, BLUE


class Camera:
    def __init__(self, perspective_amount: float, screen: Screen):
        self.perspective_amount = perspective_amount
        self._screen = screen
        self._position = Point3D(0, 0, 0)

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

    def init_mat_rot(self, f_theta: float):
        mat_rot_z = numpy.zeros((4, 4))
        mat_rot_x = numpy.zeros((4, 4))

        # Rotation Z
        mat_rot_z[0][0] = cos(f_theta)
        mat_rot_z[0][1] = sin(f_theta)
        mat_rot_z[1][0] = -sin(f_theta)
        mat_rot_z[1][1] = cos(f_theta)
        mat_rot_z[2][2] = 1
        mat_rot_z[3][3] = 1

        # Rotation X
        mat_rot_x[0][0] = 1
        mat_rot_x[1][1] = cos(f_theta * 0.5)
        mat_rot_x[1][2] = sin(f_theta * 0.5)
        mat_rot_x[2][1] = -sin(f_theta * 0.5)
        mat_rot_x[2][2] = cos(f_theta * 0.5)
        mat_rot_x[3][3] = 1

        return mat_rot_z, mat_rot_x

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

    def point_from_3d_to_2d(self, point: Point3D, f_theta: float):
        fix_point = Point3D(point.x, point.y, point.z)
        mat_rot_z, mat_rot_x = self.init_mat_rot(f_theta)

        point_rotated_z = self._multiply_matrix_vector(fix_point, mat_rot_z)
        point_rotated_zx = self._multiply_matrix_vector(point_rotated_z, mat_rot_x)

        point_rotated_zx.z += 3.0

        point_projected = self._multiply_matrix_vector(point_rotated_zx, self._mat_proj)

        result = point_projected
        return Point2D(result.x, result.y)

    def render_environment(
            self,
            environment: Environment
    ):
        self._screen.fill(environment.bg_color)

    def get_face_normal(self, face: Face):
        line1 = Point3D(
            face.edges[0].b.x - face.edges[0].a.x,
            face.edges[0].b.y - face.edges[0].a.y,
            face.edges[0].b.z - face.edges[0].a.z,
        )
        line2 = Point3D(
            face.edges[-1].a.x - face.edges[-1].b.x,
            face.edges[-1].a.y - face.edges[-1].b.y,
            face.edges[-1].a.z - face.edges[-1].b.z,
        )
        normal = Point3D(
            line1.y * line2.z - line1.z * line2.y,
            line1.z * line2.x - line1.x * line2.z,
            line1.x * line2.y - line1.y * line2.x
        )

        # It's normally normal to normalise the normal
        l = sqrt(normal.x * normal.x + normal.y * normal.y + normal.z * normal.z)
        if l != 0:
            normal.x /= l
            normal.y /= l
            normal.z /= l

        return normal

    def render_3d_entity(
            self,
            entity: Entity
    ):
        temp_entity = copy.deepcopy(entity)
        mat_rot_z, mat_rot_x = self.init_mat_rot(entity.f_theta)

        for face in temp_entity.faces:
            for edge in face.edges:
                point_rotated_a_z = self._multiply_matrix_vector(edge.a, mat_rot_z)
                point_rotated_b_z = self._multiply_matrix_vector(edge.b, mat_rot_z)
                point_rotated_a_zx = self._multiply_matrix_vector(point_rotated_a_z, mat_rot_x)
                point_rotated_b_zx = self._multiply_matrix_vector(point_rotated_b_z, mat_rot_x)

                point_rotated_a_zx.z += 3.0
                point_rotated_b_zx.z += 3.0

                edge.a = point_rotated_a_zx
                edge.b = point_rotated_b_zx

        for face in temp_entity.faces:
            normal = self.get_face_normal(face)
            dot_product = normal.x * (face.edges[0].a.x - self._position.x) + normal.y * (
                    face.edges[0].a.y - self._position.y) + normal.z * (face.edges[0].a.z - self._position.z)
            if dot_product < 0.0:
                for edge in face.edges:
                    point_a_translated = self._multiply_matrix_vector(edge.a, self._mat_proj)
                    point_b_translated = self._multiply_matrix_vector(edge.b, self._mat_proj)

                    a_screen_cords = self._screen.point_to_screen_cords(Point2D(point_a_translated.x, point_a_translated.y)).get()
                    b_screen_cords = self._screen.point_to_screen_cords(Point2D(point_b_translated.x, point_b_translated.y)).get()

                    pygame.draw.line(
                        self._screen.get(),
                        RED.get(),
                        a_screen_cords,
                        b_screen_cords,
                        1
                    )

        entity.f_theta += 1.0 * 0.01
