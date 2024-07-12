import pygame
from math import cos, sin

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800,800
pygame.display.set_caption("3D Renderer")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

vertices = [
    (0,  0, -1),  # Vertex 1
    (1,  0,  0),
    (0,  1,  0),
    (-1,  0, 0),
    (0, -1,  0),
    (0,  0,  1)
]

edges = [
    (0, 1), (0, 2), # Edge 1
    (0, 3), (0, 4),
    (1, 2), (1, 5),
    (2, 3), (2, 5),
    (3, 4), (3, 5),
    (4, 1), (4, 5)
]

# Octahedron as an example

scale = 100
cube_pos = [WIDTH / 2, HEIGHT / 2]  # Center x and y
angle_x = 0
angle_y = 0

clock = pygame.time.Clock()
while True:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(WHITE)

    projected_points = []
    for vertex in vertices:
        # Rotate around X-axis
        rotated_x = [vertex[0], vertex[1] * cos(angle_x) - vertex[2] * sin(angle_x), vertex[1] * sin(angle_x) + vertex[2] * cos(angle_x)]
        # Rotate around Y-axis
        rotated_y = [rotated_x[0] * cos(angle_y) + rotated_x[2] * sin(angle_y), rotated_x[1], -rotated_x[0] * sin(angle_y) + rotated_x[2] * cos(angle_y)]
        # Project onto 2D screen
        projected_2d = [(rotated_y[0] * scale) + cube_pos[0], (rotated_y[1] * scale) + cube_pos[1]]
        projected_points.append(projected_2d)


    # Draw edges
    for edge in edges:
        pygame.draw.line(screen, BLACK, projected_points[edge[0]], projected_points[edge[1]])
    
    angle_x += 0.01
    angle_y += 0.01

    pygame.display.update()
