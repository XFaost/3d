import copy
from math import tan, sqrt, cos, sin
from typing import Optional, List

import numpy
import pygame
from pygame import Surface

from entity.edge import Edge
from entity.entity import Entity
from entity.face import Face
from entity.point2d import Point2D
from entity.point3d import Point3D
from game.environment import Environment
from game.screen import Screen
from utils.color import RED, Color, BLUE, WHITE


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

    def draw_line(self, a: Point2D, b: Point2D, color: Color = RED):
        a_screen_cords = self._screen.point_to_screen_cords(a).get()
        b_screen_cords = self._screen.point_to_screen_cords(b).get()

        pygame.draw.line(
            self._screen.get(),
            color.get(),
            a_screen_cords,
            b_screen_cords,
            1
        )

    def point_inside_face(self, face: Face, point: Point2D):
        cnt = 0

        for edge in face.edges:
            if not edge.a_2d or not edge.b_2d:
                raise Exception()
            (x1, y1), (x2, y2) = edge.a_2d.get(), edge.b_2d.get()

            try:
                r = ((point.y - y1) / (y2 - y1)) * (x2 - x1)
            except ZeroDivisionError:
                r = 0

            if (point.y < y1) != (point.y < y2) and point.x < x1 + r:
                cnt += 1

        return cnt % 2 == 1

    def get_pixel_color(self, x: int, y: int):
        try:
            color = self._screen.screen.get_at((x, y))[:3]
        except IndexError:
            raise
        return Color(*color)

    def draw_face(self, face: Face, color: Color, point: Optional[Point2D] = None):
        # print('==============')
        if not point:
            x = (face.edges[0].a_2d.x + face.edges[1].a_2d.x + face.edges[1].b_2d.x) / 3
            y = (face.edges[0].a_2d.y + face.edges[1].a_2d.y + face.edges[1].b_2d.y) / 3
            point = Point2D(x, y)

        # for edge in face.edges:
        #     print(self._screen.point_to_screen_cords(edge.a_2d).get(), end=',')
        # print('\n')
        # print(self._screen.point_to_screen_cords(point).get())

        a = Point2D(0, point.y)
        b = Point2D(0, point.y)

        left_edge = None
        right_edge = None

        for edge in face.edges:
            # print('edge',
            #       self._screen.point_to_screen_cords(edge.a_2d).get(), ',',
            #       self._screen.point_to_screen_cords(edge.b_2d).get()
            #       )
            if all([
                any([
                    edge.a_2d.x <= point.x,
                    edge.b_2d.x <= point.x
                ]),
                edge.a_2d.y <= point.y,
                edge.b_2d.y >= point.y,
            ]):
                left_edge = edge
            elif all([
                any([
                    edge.a_2d.x >= point.x,
                    edge.b_2d.x >= point.x
                ]),
                edge.a_2d.y >= point.y,
                edge.b_2d.y <= point.y,
            ]):
                right_edge = edge

        if not left_edge or not right_edge:
            raise Exception('point is not valid')

        # print(
        #     self._screen.point_to_screen_cords(left_edge.a_2d).get(), ',',
        #     self._screen.point_to_screen_cords(left_edge.b_2d).get(), ',',
        #     self._screen.point_to_screen_cords(right_edge.a_2d).get(), ',',
        #     self._screen.point_to_screen_cords(right_edge.b_2d).get()
        # )

        x1 = abs(left_edge.a_2d.x - left_edge.b_2d.x)
        x2 = abs(a.y - left_edge.a_2d.y)
        x3 = abs(left_edge.b_2d.y - left_edge.a_2d.y)
        try:
            len_left = ((x1) * (x2)) / (x3)
        except ZeroDivisionError:
            len_left = 0

        if left_edge.a_2d.x <= point.x:
            a.x = left_edge.a_2d.x + len_left
        else:
            a.x = left_edge.a_2d.x - len_left

        x1 = abs(right_edge.a_2d.y - b.y)
        x2 = abs(right_edge.b_2d.x - right_edge.a_2d.x)
        x3 = abs(right_edge.a_2d.y - right_edge.b_2d.y)
        try:
            len_right = (x1 * x2) / x3
        except ZeroDivisionError:
            len_right = 0

        if right_edge.a_2d.x <= right_edge.b_2d.x:
            b.x = right_edge.a_2d.x + len_right
        else:
            b.x = right_edge.b_2d.x + len_right

        # print(
        #     self._screen.point_to_screen_cords(a).get(), ',',
        #     self._screen.point_to_screen_cords(b).get(),
        # )
        self.draw_line(a, b, color)

        next_screen_cords = self._screen.point_to_screen_cords(a)
        next_screen_cords.y -= 1
        while next_screen_cords.x < self._screen.width and next_screen_cords.y < self._screen.height:

            next_point = self._screen.screen_cords_to_point(next_screen_cords)
            if next_point.x > b.x:
                break
            if (
                    self.point_inside_face(face, next_point)
                    and self.get_pixel_color(next_screen_cords.x, next_screen_cords.y) != color
            ):
                self.draw_face(face, color, next_point)
                break

            next_screen_cords.x += 1

        next_screen_cords = self._screen.point_to_screen_cords(a)
        next_screen_cords.y += 1
        while next_screen_cords.x < self._screen.width and next_screen_cords.y < self._screen.height:

            next_point = self._screen.screen_cords_to_point(next_screen_cords)
            if next_point.x > b.x:
                break
            if (
                    self.point_inside_face(face, next_point)
                    and self.get_pixel_color(next_screen_cords.x, next_screen_cords.y) != color
            ):
                self.draw_face(face, color, next_point)
                break

            next_screen_cords.x += 1

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
        faces_with_dot_product = []

        for face in entity.faces:
            normal = self.get_face_normal(face)

            dot_product = normal.x * (face.edges[0].a.x - self._position.x) + normal.y * (
                        face.edges[0].a.y - self._position.y) + normal.z * (face.edges[0].a.z - self._position.z)
            if dot_product < 0:
                faces_with_dot_product.append({
                    'face': face,
                    'dot_product': dot_product
                })

        faces_with_dot_product = sorted(faces_with_dot_product, key=lambda d: d['dot_product'], reverse=True)

        for face_with_dot_product in faces_with_dot_product:
            face = face_with_dot_product['face']

            normal = self.get_face_normal(face)
            dot_product = normal.x * (face.edges[0].a.x - self._position.x) + normal.y * (
                    face.edges[0].a.y - self._position.y) + normal.z * (face.edges[0].a.z - self._position.z)
            if dot_product < 0.0:
                for edge in face.edges:
                    point_a_translated = self._multiply_matrix_vector(edge.a, self._mat_proj)
                    point_b_translated = self._multiply_matrix_vector(edge.b, self._mat_proj)

                    edge.a_2d = Point2D(point_a_translated.x, point_a_translated.y)
                    edge.b_2d = Point2D(point_b_translated.x, point_b_translated.y)

                self.draw_face(face, RED)

                for edge in face.edges:
                    self.draw_line(edge.a_2d, edge.b_2d, WHITE)
