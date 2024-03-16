from typing import List

from entity.edge import Edge
from entity.point2d import Point2D


class Face:
    def __init__(self, edges: List[Edge]):
        self.edges = edges

    def point_inside(self, camera, point: Point2D):
        # TODO: camera typing
        cnt = 0

        for edge in self.edges:
            (x1, y1), (x2, y2) = camera.point_from_3d_to_2d(edge.a).get(), camera.point_from_3d_to_2d(edge.b).get()
            try:
                r = ((point.y - y1) / (y2 - y1)) * (x2 - x1)
            except ZeroDivisionError:
                r = 0
            if (point.y < y1) != (point.y < y2) and point.x < x1 + r:
                cnt += 1

        return cnt % 2 == 1
