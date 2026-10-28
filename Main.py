import argparse
import json
import random
import sys
from pathlib import Path

from numpy.f2py.auxfuncs import throw_error

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(150000)
from PIL import Image

from Functions.Perlin import InterpolationMethod, Perlin1D, Perlin2D, Perlin3D
from Functions.Random import Random2D
from Functions.Voronoi import Voronoi2D

parser = argparse.ArgumentParser()
parser.add_argument("paths", nargs="+", help="Relative paths to JSON files")
args = parser.parse_args()

for relative_path in args.paths:
    path = Path(relative_path)

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    print(f"Processing {path}")

    Xsize: int = (int)(data["Xsize"])
    Ysize: int = (int)(data["Ysize"])

    img = Image.new("RGBA", (Xsize, Ysize), (0, 0, 0, 0))
    px = img.load()

    seed: float = (float)(data["seed"])

    if px is not None:
        match data["program"]:
            case "Voronoi2D":
                print("Voronoi Texture")
                grid = Voronoi2D(Xsize, Ysize, (int)(data["scale"]), seed)
                for y in range(Ysize):
                    for x in range(Xsize):
                        gray = int(255 * grid[x, y])
                        px[x, y] = (gray, gray, gray, 255)
            case "Random2D":
                print("Random Texture")
                grid = Random2D(Xsize, Ysize, seed)
                for y in range(Ysize):
                    for x in range(Xsize):
                        gray = int(255 * grid[x, y])
                        px[x, y] = (gray, gray, gray, 255)
            case "VoronoiRandom2D":
                print("Voronoi with random variance Texture")
                variance: float = (float)(data["variance"])
                grid = Voronoi2D(Xsize, Ysize, (int)(data["scale"]), seed)
                grid_random = Random2D(Xsize, Ysize, seed)
                for y in range(Ysize):
                    for x in range(Xsize):
                        grayscale_gradient = 255 * grid[x, y]
                        rndm_variance = grayscale_gradient + grid_random[x, y] * (
                            255 * variance
                        )
                        gray = int(min(255, max(0, rndm_variance)))
                        px[x, y] = (gray, gray, gray, 255)
            case "PerlinCurve":
                print("Perlin Curve")

                grid = Perlin1D(
                    Xsize,
                    Ysize,
                    (int)(data["scale"]),
                    (InterpolationMethod)((int)(data["method"])),
                    seed,
                )

                for y in range(Ysize):
                    for x in range(Xsize):
                        gray = int(255 * grid[x, y])
                        px[x, y] = (gray, gray, gray, 255)
            case "PerlinCurveTriple":
                print("Perlin Tripe")
                scale: int = (int)(data["scale"])

                Linear = Perlin1D(
                    Xsize,
                    Ysize,
                    scale,
                    (InterpolationMethod)(0),
                    seed,
                )

                Sine = Perlin1D(
                    Xsize,
                    Ysize,
                    scale,
                    (InterpolationMethod)(1),
                    seed,
                )

                Cubic = Perlin1D(
                    Xsize,
                    Ysize,
                    scale,
                    (InterpolationMethod)(2),
                    seed,
                )

                for y in range(Ysize):
                    for x in range(Xsize):
                        px[x, y] = (
                            255 - int(255 * Linear[x, y]),  # Red
                            255 - int(255 * Sine[x, y]),  # Green
                            255 - int(255 * Cubic[x, y]),  # Blue
                            255,
                        )

                        if px[x, y] == (0, 0, 0, 255) or px[x, y] == (
                            255,
                            255,
                            255,
                            255,
                        ):
                            if px[x, y] == (0, 0, 0, 255):
                                px[x, y] = (255, 255, 255, 255)
                            else:
                                px[x, y] = (0, 0, 0, 255)
            case "Perlin2D":
                print("Perlin 2D")

                grid = Perlin2D(
                    Xsize,
                    Ysize,
                    (int)(data["scale"]),
                    (InterpolationMethod)((int)(data["method"])),
                    seed,
                )

                for y in range(Ysize):
                    for x in range(Xsize):
                        gray = int(255 * grid[x, y])
                        px[x, y] = (gray, gray, gray, 255)
            case "Perlin3D":
                print("Perlin 3D")
                Zsize = (int)(data["Zsize"])
                grid = Perlin3D(
                    Xsize,
                    Ysize,
                    Zsize,
                    (int)(data["scale"]),
                    (InterpolationMethod)((int)(data["method"])),
                    seed,
                )

                for y in range(Ysize):
                    for x in range(Xsize):
                        gray = 0
                        for z in range(Zsize):
                            gray += (255 * grid[x, y, z]) / Zsize
                        gray = int(max(255, gray))
                        px[x, y] = (gray, gray, gray, 255)
            case _:
                print("Invalid Program")

        out = f"{data['file_name']}.png"
        img.save(out)

        print("\nDone.")
    else:
        print("\nIssue Loading Image.")
