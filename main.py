from math import radians, cos, sin
from typing import Optional

from entity.cross import Cross
from entity.cube import Cube
from entity.point3d import Point3D
from game.camera import Camera
from game.environment import Environment
from game.game import Game
from game.screen import Screen
from utils.color import RED, BLACK, Color, BLUE


class DownwardCross(Cross):

    def __init__(
            self,
            cords: Point3D,
            scale: float,
            visible_lines_color: Optional[Color] = None,
            invisible_lines_color: Optional[Color] = None
    ):
        self.__start_cords = Point3D(cords.x, cords.y, cords.z)
        super().__init__(cords, scale, visible_lines_color, invisible_lines_color)

    def move(self):
        self.cords.y += 0.05
        if self.cords.y >= 4.0:
            self.cords.y = self.__start_cords.y
        self.init_faces()


class LeftwardCross(Cross):

    def __init__(
            self,
            cords: Point3D,
            scale: float,
            visible_lines_color: Optional[Color] = None,
            invisible_lines_color: Optional[Color] = None
    ):
        self.__start_cords = Point3D(cords.x, cords.y, cords.z)
        super().__init__(cords, scale, visible_lines_color, invisible_lines_color)

    def move(self):
        self.cords.x -= 0.05
        if self.cords.x <= -4.0:
            self.cords.x = self.__start_cords.x
        self.init_faces()


class LeftDownwardCross(Cross):

    def __init__(
            self,
            cords: Point3D,
            scale: float,
            visible_lines_color: Optional[Color] = None,
            invisible_lines_color: Optional[Color] = None,
    ):
        self.__start_scale = scale
        self.__start_cords = Point3D(cords.x, cords.y, cords.z)
        super().__init__(cords, scale, visible_lines_color, invisible_lines_color)

    def move(self):
        self.scale -= 0.005
        self.cords.x -= 0.05
        self.cords.y += 0.05
        if self.cords.x <= -4.0 or self.cords.y >= 4.0:
            self.cords.x = self.__start_cords.x
            self.cords.y = self.__start_cords.y
            self.scale = self.__start_scale
        self.init_faces()


class EllipseCross(Cross):

    def __init__(
            self,
            cords: Point3D,
            scale: float,
            a: float,
            b: float,
            visible_lines_color: Optional[Color] = None,
            invisible_lines_color: Optional[Color] = None
    ):
        self.__center_cords = Point3D(cords.x, cords.y, cords.z)
        self.a = a
        self.b = b
        self.angle_degrees = 0
        self.__increase = 0.005
        super().__init__(cords, scale, visible_lines_color, invisible_lines_color)

    def _move_elliptical(self):
        if self.angle_degrees > 360:
            self.angle_degrees = 0
            self.__increase *= -1

        # Перетворення кута з градусів в радіани
        angle_radians = radians(self.angle_degrees)

        # Обчислення нових координат за формулами еліпса
        x = self.__center_cords.x + self.a * cos(angle_radians)
        y = self.__center_cords.y + self.b * sin(angle_radians)

        self.angle_degrees += 5

        self.scale += self.__increase

        return x, y

    def move(self):
        self.cords.x, self.cords.y = self._move_elliptical()
        self.init_faces()


def get_static_crosses():
    static_crosses = []

    for i in range(7):
        static_crosses.extend([
            Cross(Point3D(-8.8, -5.0 + i * 1.3, 5.0), 0.05),
            Cross(Point3D(-8.5, -5.0 + i * 1.3, 5.0), 0.1),
            Cross(Point3D(-8.0, -5.0 + i * 1.3, 5.0), 0.15),
            Cross(Point3D(-7.3, -5.0 + i * 1.3, 5.0), 0.2),
            Cross(Point3D(-6.4, -5.0 + i * 1.3, 5.0), 0.25),
            Cross(Point3D(-5.3, -5.0 + i * 1.3, 5.0), 0.3)
        ])

    static_crosses.append(Cross(Point3D(0, -4.0, 5.0), 0.05, RED, BLUE))
    static_crosses.append(Cross(Point3D(-0.15, -4.0 - 0.15, 5.0), 0.15, RED, BLUE))
    static_crosses.append(Cross(Point3D(-0.6, -4.0 - 0.6, 5.0), 0.45, RED, BLUE))

    return static_crosses


def get_dynamic_crosses():
    return (
        DownwardCross(Point3D(-4.0, -5.0, 5.0), 0.3, RED, BLUE),
        LeftwardCross(Point3D(5.0, 4.0, 5.0), 0.3, RED, BLUE),
        LeftDownwardCross(Point3D(5.0, -5.0, 5.0), 1, RED, BLUE),
        EllipseCross(Point3D(2.5, -2.0, 5.0), 0.3, 3, 2, RED, BLUE)
    )


def run():
    screen = Screen(1768, 1000)
    camera = Camera(3, screen)
    environment = Environment(BLACK)

    game = Game(
        screen,
        camera,
        environment
    )

    # for i in get_static_crosses():
    #     game.add_entity(i)
    #
    # for i in get_dynamic_crosses():
    #     game.add_entity(i)

    game.add_entity(Cube(Point3D(-1.75, -1, 1.0), 0.05, RED, BLUE))

    game.run()


if __name__ == "__main__":
    run()
