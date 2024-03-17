import pygame

from entity.point2d import Point2D
from utils.color import Color


class Screen:
    def __init__(self, width, height):
        pygame.init()
        self._width = width
        self._height = height
        self._center = 0.5 * width, 0.5 * height
        self._screen = pygame.display.set_mode((width, height))
        self._clock = pygame.time.Clock()
        self._fps = 60
        self._run = True

    @property
    def screen(self):
        return self._screen

    @property
    def center(self):
        return self._center

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._run = False

    def quit(self):
        pygame.quit()

    def update(self):
        pygame.display.update()
        self._clock.tick(self._fps)

    def fill(self, color: Color):
        self._screen.fill(color.get())

    @property
    def run(self):
        return self._run

    def get(self):
        return self._screen

    def point_to_screen_cords(self, point: Point2D):
        return Point2D((point.x + 1) * self.center[0], (point.y + 1) * self.center[1])

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
