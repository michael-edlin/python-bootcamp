# Challenge yourself and practice learning from outside resources
# by following this tutorial to build a maze generator:
# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e

import random
import matplotlib.pyplot as plt
import numpy as np

def initialize_grid(width, height):
    grid = np.zeros((height, width), dtype=bool)
    return grid

def carve_maze(grid, x, y):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 1 <= nx < grid.shape[1] - 1 and 1 <= ny < grid.shape[0] - 1:
            if not grid[ny][nx]:
                grid[y][x] = True
                grid[ny][nx] = True
                carve_maze(grid, nx, ny)

def display_maze(grid):
    plt.imshow(grid, cmap='binary')
    plt.axis('off')
    plt.show()

def main():
    width, height = 20, 20
    grid = initialize_grid(width, height)
    carve_maze(grid, 1, 1)
    display_maze(grid)

if __name__ == "__main__":
    main()
