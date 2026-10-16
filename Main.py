import random
import sys

from numpy.f2py.auxfuncs import throw_error

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(150000)
from PIL import Image

from VoronoiTexture import Voronoi2D

print("Enter background length (int):")
Xsize = (int)(input())
print("Enter background height (int):")
Ysize = (int)(input())
print("Enter background file name:")
file_name = input()
print("Enter a scale (int):")
scale = (int)(input())
print("Enter a seed (float):")
seed = (float)(input())

img = Image.new("RGBA", (Xsize, Ysize), (0, 0, 0, 0))
px = img.load()

grid = Voronoi2D(Xsize, Ysize, scale, seed)

for y in range(Ysize):
    for x in range(Xsize):
        grayscale_gradient = grid[x, y]
        gray = int(255 * grayscale_gradient)
        px[x, y] = (gray, gray, gray, 255)

out = f"{file_name}.png"
img.save(out)

print("\nDone.")
