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


def Perlin2D(
    _sizeX: int, _sizeY: int, _scale: int, _method: InterpolationMethod, _seed: float
):
    if _sizeX <= 0 or _sizeY <= 0:
        raise ValueError("Dimensions must be positive")

    grid = np.zeros((_sizeX, _sizeY), dtype=float)
    random.seed(_seed)

    vector_grid = np.zeros((_sizeX, _sizeY), dtype=float)

    # Grid definition
    for x in range(_scale):
        for y in range(_scale):
            vector_grid[x, y] = random.random()

    # Interpolations
    for x in range(_sizeX):
        for y in range(_sizeY):
            position_x = x * (_scale - 1) / (_sizeX - 1)
            position_y = y * (_scale - 1) / (_sizeY - 1)

            x_min: int = int(position_x)
            x_max: int = x_min + 1
            y_min: int = int(position_y)
            y_max: int = y_min + 1
            t_x = position_x - x_min
            t_y = position_y - y_min

            height: float = -1
            match _method:
                case InterpolationMethod.LINEAR:
                    f = linear_interpolation(
                        vector_grid[x_min, y_min], vector_grid[x_max, y_min], t_x
                    )
                    g = linear_interpolation(
                        vector_grid[x_min, y_max], vector_grid[x_max, y_max], t_x
                    )
                    height = linear_interpolation(g, f, t_y)
                case InterpolationMethod.SINUS:
                    f = cosine_interpolation(
                        vector_grid[x_min, y_min], vector_grid[x_max, y_min], t_x
                    )
                    g = cosine_interpolation(
                        vector_grid[x_min, y_max], vector_grid[x_max, y_max], t_x
                    )
                    height = cosine_interpolation(g, f, t_y)
                case InterpolationMethod.CUBIC:
                    x_min_min: int = max(0, x_min - 1)
                    x_max_max: int = min(x_max + 1, (_scale - 1))
                    y_min_min: int = max(0, y_min - 1)
                    y_max_max: int = min(y_max + 1, (_scale - 1))
                    d = cubic_interpolation(
                        vector_grid[x_min_min, y_min_min],
                        vector_grid[x_min, y_min_min],
                        vector_grid[x_max, y_min_min],
                        vector_grid[x_max, y_min_min],
                        t_x,
                    )
                    e = cubic_interpolation(
                        vector_grid[x_min_min, y_min],
                        vector_grid[x_min, y_min],
                        vector_grid[x_max, y_min],
                        vector_grid[x_max, y_min],
                        t_x,
                    )
                    f = cubic_interpolation(
                        vector_grid[x_min_min, y_max],
                        vector_grid[x_min, y_max],
                        vector_grid[x_max, y_max],
                        vector_grid[x_max, y_max],
                        t_x,
                    )
                    g = cubic_interpolation(
                        vector_grid[x_min_min, y_max_max],
                        vector_grid[x_min, y_max_max],
                        vector_grid[x_max, y_max_max],
                        vector_grid[x_max, y_max_max],
                        t_x,
                    )
                    height = g = cubic_interpolation(
                        d,
                        e,
                        f,
                        g,
                        t_y,
                    )
                case InterpolationMethod.PERSO:
                    f = personal_interpolation(
                        vector_grid[x_min, y_min], vector_grid[x_max, y_min], t_x
                    )
                    g = personal_interpolation(
                        vector_grid[x_max, y_max], vector_grid[x_max, y_max], t_x
                    )
                    height = personal_interpolation(f, g, t_y)

            grid[x, y] = height
    return grid


def Perlin3D(
    _sizeX: int,
    _sizeY: int,
    _sizeZ: int,
    _scale: int,
    _method: InterpolationMethod,
    _seed: float,
):
    if _sizeX <= 0 or _sizeY <= 0 or _sizeZ <= 0:
        raise ValueError("Dimensions must be positive")

    grid = np.zeros((_sizeX, _sizeY, _sizeZ), dtype=float)
    random.seed(_seed)

    vector_grid = np.zeros((_sizeX, _sizeY, _sizeZ), dtype=float)

    # Grid definition
    for x in range(_sizeX):
        for y in range(_sizeY):
            for z in range(_sizeZ):
                vector_grid[x, y, z] = random.random()

    # Interpolations
    for x in range(_sizeX):
        for y in range(_sizeY):
            for z in range(_sizeZ):
                position_x = x * (_scale - 1) / (_sizeX - 1)
                position_y = y * (_scale - 1) / (_sizeY - 1)
                position_z = z * (_scale - 1) / (_sizeZ - 1)

                x_min: int = int(position_x)
                y_min: int = int(position_y)
                z_min: int = int(position_z)
                t_x = position_x - x_min
                t_y = position_y - y_min
                t_z = position_z - z_min

                a = vector_grid[x_min, y_min, z_min]
                b = vector_grid[x_min + 1, y_min, z_min]
                c = vector_grid[x_min, y_min, z_min]
                d = vector_grid[x_min + 1, y_min, z_min]
                e = vector_grid[x_min, y_min, z_min]
                f = vector_grid[x_min, y_min, z_min]
                g = vector_grid[x_min, y_min, z_min]
                h = vector_grid[x_min, y_min, z_min]

                height: float = -1
                match _method:
                    case InterpolationMethod.LINEAR:
                        # Bottom faces
                        i = linear_interpolation(a, b, t_x)
                        j = linear_interpolation(c, d, t_x)
                        k = linear_interpolation(i, j, t_y)

                        # Top faces
                        l = linear_interpolation(e, f, t_x)
                        m = linear_interpolation(g, h, t_x)
                        n = linear_interpolation(l, m, t_y)
                        height = linear_interpolation(k, n, t_z)
                    case InterpolationMethod.SINUS:
                        # Bottom faces
                        i = cosine_interpolation(a, b, t_x)
                        j = cosine_interpolation(c, d, t_x)
                        k = cosine_interpolation(i, j, t_y)

                        # Top faces
                        l = cosine_interpolation(e, f, t_x)
                        m = cosine_interpolation(g, h, t_x)
                        n = cosine_interpolation(l, m, t_y)
                        height = cosine_interpolation(k, n, t_z)
                    case InterpolationMethod.CUBIC:
                        print("Method Not Implemented")
                        return grid
                    case InterpolationMethod.PERSO:
                        # Bottom faces
                        i = personal_interpolation(a, b, t_x)
                        j = personal_interpolation(c, d, t_x)
                        k = personal_interpolation(i, j, t_y)

                        # Top faces
                        l = personal_interpolation(e, f, t_x)
                        m = personal_interpolation(g, h, t_x)
                        n = personal_interpolation(l, m, t_y)
                        height = personal_interpolation(k, n, t_z)

                grid[x, y, z] = height
    return grid
