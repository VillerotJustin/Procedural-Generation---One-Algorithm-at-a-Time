import math
import random

import numpy as np
from PIL import Image


# _scale = one cell per k size part
def Voronoi2D(_sizeX: int, _sizeY: int, _scale: int, _seed: float):
    if _sizeX <= 0 or _sizeY <= 0:
        raise ValueError("Dimensions must be positive")

    random_scale = 1 / (_scale * _scale)

    grid = np.zeros((_sizeX, _sizeY), dtype=float)
    point_list = []
    random.seed(_seed)
    # Scatter Points
    for x in range(_sizeX):
        for y in range(_sizeY):
            if random.random() < random_scale:
                point_list.append([x, y])

    # Find Nearest Seed
    big_max_distance: float = 0
    for x in range(_sizeX):
        for y in range(_sizeY):
            min_distance: float = math.inf
            for point in point_list:
                distance = math.fabs(
                    (point[0] - x) * (point[0] - x) + (point[1] - y) * (point[1] - y)
                )
                min_distance = min(min_distance, distance)

            min_distance = math.sqrt(min_distance)
            big_max_distance = max(big_max_distance, min_distance)
            grid[x, y] = min_distance

    # Convert distance into grayscale
    for x in range(_sizeX):
        for y in range(_sizeY):
            grayscale: float = grid[x, y] / big_max_distance
            grid[x, y] = grayscale

    return grid


print("Enter background length (int):")
Xsize = (int)(input())
print("Enter background height (int):")
Ysize = (int)(input())
print("Enter background file name:")
file_name = input()
print(
    "Enter a scale (int) ! there is around one cell per scale square so make scalle smaller than your image size:"
)
scale = (int)(input())
print("Enter a seed (float):")
seed = (float)(input())

img = Image.new("RGBA", (Xsize, Ysize), (0, 0, 0, 0))
px = img.load()

if px is not None:
    grid = Voronoi2D(Xsize, Ysize, scale, seed)

    for y in range(Ysize):
        for x in range(Xsize):
            grayscale_gradient = grid[x, y]
            gray = int(255 * grayscale_gradient)
            px[x, y] = (gray, gray, gray, 255)

    out = f"{file_name}.png"
    img.save(out)

    print("\nDone.")
