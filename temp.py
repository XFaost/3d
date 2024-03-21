import math

import matplotlib.pyplot as plt
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
def generate_sphere_vertices():
    vertices = []
    num_vertices = 13
    for i in range(num_vertices):
        theta = np.pi * i / (num_vertices - 1)
        for j in range(num_vertices*2):
            if j < num_vertices:
                phi = np.pi * j / (num_vertices - 1)
                x = round(np.sin(phi) * np.cos(theta), 4)
                y = round(np.sin(phi) * np.sin(theta), 4)
                z = round(np.cos(phi), 4)
            else:
                phi = np.pi * (j-1) / (num_vertices - 1)
                x = round(np.sin(phi) * np.cos(theta), 4)/2 * -1
                y = round(np.sin(phi) * np.sin(theta), 4)/2 * -1
                z = round(np.cos(phi), 4)/2
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


sphere_vertices = generate_sphere_vertices()
sphere_polygons = generate_sphere_polygons(int(math.sqrt(len(sphere_vertices))))

draw_sphere_frame(sphere_vertices, sphere_polygons)
