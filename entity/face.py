from typing import List

from entity.edge import Edge
from entity.point2d import Point2D


class Face:
    def __init__(self, edges: List[Edge]):
        self.edges = edges
