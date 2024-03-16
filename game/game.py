from typing import List

from entity.entity import Entity
from game.camera import Camera
from game.environment import Environment
from game.screen import Screen


class Game:
    def __init__(
            self,
            screen: Screen,
            camera: Camera,
            environment: Environment
    ):
        self._screen = screen
        self._camera = camera
        self._environment = environment
        self._entities: List[Entity] = []

    def add_entity(self, entity):
        self._entities.append(entity)

    def run(self):
        while self._screen.run:
            self._screen.events()

            self._camera.render_environment(
                self._environment
            )

            for i in range(len(self._entities)):
                self._camera.render_3d_entity(self._entities, i)

            self._screen.update()
