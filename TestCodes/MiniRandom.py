import random

import numpy as np
from PIL import Image


def Random2D(_sizeX: int, _sizeY: int, _seed: float):
    if _sizeX <= 0 or _sizeY <= 0:
        raise ValueError("Dimensions must be positive")

    grid = np.zeros((_sizeX, _sizeY), dtype=float)

    random.seed(_seed)
    for x in range(_sizeX):
        for y in range(_sizeY):
            grid[x, y] = random.random()
    return grid


print("Enter background length (int):")
Xsize = (int)(input())
print("Enter background height (int):")
Ysize = (int)(input())
print("Enter background file name:")
file_name = input()
print("Enter a seed (float):")
seed = (float)(input())

img = Image.new("RGBA", (Xsize, Ysize), (0, 0, 0, 0))
px = img.load()

if px is not None:
    grid = Random2D(Xsize, Ysize, seed)

    for y in range(Ysize):
        for x in range(Xsize):
            grayscale_gradient = grid[x, y]
            gray = int(255 * grayscale_gradient)
            px[x, y] = (gray, gray, gray, 255)

    out = f"{file_name}.png"
    img.save(out)

    print("\nDone.")
