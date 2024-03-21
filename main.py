from entity.point3d import Point3D
from entity.right_triangular_prism import RightTriangularPrism
from entity.sphere import Sphere
from game.camera import Camera
from game.environment import Environment
from game.game import Game
from game.screen import Screen
from utils.color import RED, BLACK


def run():
    screen = Screen(1768, 1000)
    camera = Camera(3, screen)
    environment = Environment(BLACK)

    game = Game(
        screen,
        camera,
        environment
    )

    game.add_entity(
        Sphere(Point3D(0.0, 0.0, 0.0), 1, RED)
    )

    game.run()


if __name__ == "__main__":
    run()
