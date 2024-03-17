from entity.cross import Cross
from entity.cube import Cube
from entity.point3d import Point3D
from entity.surface import Surface
from game.camera import Camera
from game.environment import Environment
from game.game import Game
from game.screen import Screen
from utils.color import RED, BLACK


def run():
    screen = Screen(1768, 1000)
    camera = Camera(3, screen)
    environment = Environment(BLACK)

    cross_left = Cross(Point3D(-5.0, -1.0, -5.0), 0.5, RED)
    cross_center0 = Cross(Point3D(0.0, -3.0, -5.0), 0.5, RED)
    cross_center1 = Cross(Point3D(0.0, 1.0, -7.0), 0.5, RED)
    cross_right = Cross(Point3D(5.0, -1.0, -5.0), 0.5, RED)

    surface0 = Surface(Point3D(1.0, 0.0, 0.0), 0.5, RED)
    surface1 = Surface(Point3D(0.0, 0.0, -1.0), 1.0, RED)

    cube = Cube(Point3D(0.0, 0.0, 3.0), 1, RED)

    game = Game(
        screen,
        camera,
        environment
    )

    # game.add_entity(cross_left)
    # game.add_entity(cross_center0)
    # game.add_entity(cross_center1)
    # game.add_entity(cross_right)
    # game.add_entity(surface0)
    # game.add_entity(surface1)
    game.add_entity(cube)

    game.run()


if __name__ == "__main__":
    run()
