import random

import numpy as np


def Random2D(_sizeX: int, _sizeY: int, _seed: float):
    if _sizeX <= 0 or _sizeY <= 0:
        raise ValueError("Dimensions must be positive")

    grid = np.zeros((_sizeX, _sizeY), dtype=float)

    random.seed(_seed)
    for x in range(_sizeX):
        for y in range(_sizeY):
            grid[x, y] = random.random()
    return grid


def Random3D(_sizeX: int, _sizeY: int, _sizeZ: int, _seed: float):
    if _sizeX <= 0 or _sizeY <= 0 or _sizeZ <= 0:
        raise ValueError("Dimensions must be positive")

    grid = np.zeros((_sizeX, _sizeY, _sizeZ), dtype=float)

    random.seed(_seed)
    for x in range(_sizeX):
        for y in range(_sizeY):
            for z in range(_sizeZ):
                grid[x, y, z] = random.random()
    return grid
