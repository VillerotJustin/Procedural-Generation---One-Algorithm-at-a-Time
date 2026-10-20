# TODO Algorithme de Shamos et Hoey
import math
import random
from enum import Enum

import numpy as np

InterpolationMethod = Enum(
    "InterpolationMethod", [("LINEAR", 0), ("SINUS", 1), ("CUBIC", 2), ("PERSO", 3)]
)


def personal_interpolation(_a: float, _b: float, _t: float):
    return _a + (_b - _a) * _t


def linear_interpolation(_a: float, _b: float, _t: float):
    return (1.0 - _t) * _a + _t * _b


def cosine_interpolation(_a: float, _b: float, _t: float):
    c: float = (1 - math.cos(_t * math.pi)) * 0.5
    return (1.0 - c) * _a + c * _b


# cubic interpolation of point t between b & c with a & d needed
def cubic_interpolation(_a: float, _b: float, _c: float, _d: float, _t: float):
    # Polynomes coeficients calculation
    c0: float = _b
    c1: float = -0.5 * _a + 0.5 * _c
    c2: float = _a - 2.5 * _b + 2 * _c - 0.5 * _d
    c3: float = -0.5 * _a + 1.5 * _b - 1.5 * _c + 0.5 * _d

    return (c3 * _t * _t * _t) + (c2 * _t * _t) + (c1 * _t) + c0


# Create _curve_length and height _curve_height
# this is only graphical the curve is between -1 and 1
#
# scale is the number of step in the curve
#
# (opt) _seed for the random otherwhise its random
def Perlin1D(
    _curve_length: int,
    _curve_height: int,
    scale: int,
    method: InterpolationMethod,
    _seed: float = random.random(),
):
    if _curve_length <= 1 or _curve_height <= 1 or scale < 2:
        raise ValueError("Dimensions must be positive")

    render_curvegrid = np.ones((_curve_length, _curve_height), dtype=int)
    random.seed(_seed)

    vector_grid = np.zeros((scale), dtype=float)

    # Grid definition
    for x in range(scale):
        vector_grid[x] = 2 * random.random() - 1

    # Interpolations

    for x in range(_curve_length):
        position = x * (scale - 1) / (_curve_length - 1)

        left: int = int(position)
        right: int = min(left + 1, (scale - 1))
        t = position - left

        y: float = -1
        match method:
            case InterpolationMethod.LINEAR:
                y = linear_interpolation(vector_grid[left], vector_grid[right], t)
            case InterpolationMethod.SINUS:
                y = cosine_interpolation(vector_grid[left], vector_grid[right], t)
            case InterpolationMethod.CUBIC:
                p_left: int = max(0, left - 1)
                f_right: int = min(right + 1, (scale - 1))
                y = cubic_interpolation(
                    vector_grid[p_left],
                    vector_grid[left],
                    vector_grid[right],
                    vector_grid[f_right],
                    t,
                )
            case InterpolationMethod.PERSO:
                y = personal_interpolation(vector_grid[left], vector_grid[right], t)

        render_y: int = (int)((_curve_height - 1) * ((y + 1) / 2))
        render_y = max(0, min(render_y, _curve_height - 1))

        render_curvegrid[x, render_y] = 0

    return render_curvegrid


def Perlin2D(_sizeX: int, _sizeY: int, _seed: float):
    if _sizeX <= 0 or _sizeY <= 0:
        raise ValueError("Dimensions must be positive")

    grid = np.zeros((_sizeX, _sizeY), dtype=float)
    random.seed(_seed)

    vector_grid = np.array((_sizeX, _sizeY))

    # Grid definition
    for x in range(_sizeX):
        for y in range(_sizeY):
            random_vector = [random.random(), random.random()]
            random_vector_magnitude = math.sqrt(
                random_vector[0] * random_vector[0]
                + random_vector[1] * random_vector[1]
            )
            random_vector_normalised = [
                random_vector[0] / random_vector_magnitude
                + random_vector[1] / random_vector_magnitude
            ]
            vector_grid[x, y] = random_vector_normalised

    # Interpolations

    return grid


def Perlin3D(_sizeX: int, _sizeY: int, _sizeZ: int, _seed: float):
    if _sizeX <= 0 or _sizeY <= 0 or _sizeZ <= 0:
        raise ValueError("Dimensions must be positive")

    grid = np.zeros((_sizeX, _sizeY, _sizeZ), dtype=float)
    random.seed(_seed)

    vector_grid = np.array((_sizeX, _sizeY, _sizeZ))

    # Grid definition
    for x in range(_sizeX):
        for y in range(_sizeY):
            for z in range(_sizeZ):
                random_vector = [random.random(), random.random(), random.random()]
                random_vector_magnitude = math.sqrt(
                    random_vector[0] * random_vector[0]
                    + random_vector[1] * random_vector[1]
                    + random_vector[2] * random_vector[2]
                )
                random_vector_normalised = [
                    random_vector[0] / random_vector_magnitude
                    + random_vector[1] / random_vector_magnitude
                    + random_vector[2] / random_vector_magnitude
                ]
                vector_grid[x, y, z] = random_vector_normalised

    # Interpolations

    return grid
