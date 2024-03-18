from entity.cross import Cross
from entity.cube import Cube
from entity.point3d import Point3D
from entity.surface import Surface
from game.camera import Camera
from game.environment import Environment
from game.game import Game
from game.screen import Screen
from utils.color import RED, BLACK


class DownwardCross(Cross):
    def move(self):
        self.cords.y += 0.02
        self.init_faces()


def get_static_crosses():
    static_crosses = []

    for i in range(40):
        static_crosses.append(
            Cross(Point3D(-8.8, -5.0 + i * 0.25, 5.0), 0.05, RED)
        )
    for i in range(20):
        static_crosses.append(
            Cross(Point3D(-8.5, -5.0 + i * 0.5, 5.0), 0.1, RED)
        )
    for i in range(14):
        static_crosses.append(
            Cross(Point3D(-8.0, -5.0 + i * 0.7, 5.0), 0.15, RED)
        )
    for i in range(11):
        static_crosses.append(
            Cross(Point3D(-7.3, -5.0 + i * 0.9, 5.0), 0.2, RED)
        )
    for i in range(8):
        static_crosses.append(
            Cross(Point3D(-6.4, -5.0 + i * 1.3, 5.0), 0.25, RED)
        )
    for i in range(8):
        static_crosses.append(
            Cross(Point3D(-5.3, -5.0 + i * 1.3, 5.0), 0.3, RED)
        )

    return static_crosses


def run():
    screen = Screen(1768, 1000)
    camera = Camera(3, screen)
    environment = Environment(BLACK)

    game = Game(
        screen,
        camera,
        environment
    )

    for i in get_static_crosses():
        game.add_entity(i)

    game.add_entity(
        DownwardCross(Point3D(0, 0.0, 5.0), 0.3, RED)
    )

    game.run()


if __name__ == "__main__":
    run()
