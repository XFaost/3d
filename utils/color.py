import numpy as np


def random_color():
    return Color(*list(np.random.choice(range(256), size=3)))


class Color:
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue

    def get(self):
        return self._red, self._green, self._blue


BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
BLUE = Color(0, 0, 255)
