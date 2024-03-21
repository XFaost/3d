import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def draw_sphere_frame(vertices, polygons):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for polygon in polygons:
        for i in range(len(polygon)):
            x = [vertices[polygon[i % len(polygon)]][0], vertices[polygon[(i + 1) % len(polygon)]][0]]
            y = [vertices[polygon[i % len(polygon)]][1], vertices[polygon[(i + 1) % len(polygon)]][1]]
            z = [vertices[polygon[i % len(polygon)]][2], vertices[polygon[(i + 1) % len(polygon)]][2]]
            ax.plot(x, y, z, color='black')
    plt.show()


# Генерація вершин сфери
def generate_sphere_vertices(num_vertices):
    vertices = []
    for i in range(num_vertices):
        theta = 2 * np.pi * i / num_vertices
        for j in range(num_vertices):
            phi = np.pi * j / (num_vertices - 1)
            x = np.sin(phi) * np.cos(theta)
            y = np.sin(phi) * np.sin(theta)
            z = np.cos(phi)
            vertices.append((x, y, z))
    return vertices


# Генерація полігонів для сфери
def generate_sphere_polygons(num_vertices):
    polygons = []
    for i in range(num_vertices):
        for j in range(num_vertices - 1):
            v1 = i * num_vertices + j
            v2 = (i + 1) % num_vertices * num_vertices + j
            v3 = (i + 1) % num_vertices * num_vertices + (j + 1)
            v4 = i * num_vertices + (j + 1)
            polygons.append((v1, v2, v3, v4))
    return polygons


num_vertices = 12  # кількість вершин кулі
sphere_vertices = generate_sphere_vertices(num_vertices)
sphere_polygons = generate_sphere_polygons(num_vertices)

draw_sphere_frame(sphere_vertices, sphere_polygons)
