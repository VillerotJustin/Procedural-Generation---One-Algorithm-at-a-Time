import random
import sys

from numpy.f2py.auxfuncs import throw_error

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(150000)
from PIL import Image

from Functions.Random import Random2D
from Functions.Voronoi import Voronoi2D

print("Enter background length (int):")
Xsize = (int)(input())
print("Enter background height (int):")
Ysize = (int)(input())
print("Enter background file name:")
file_name = input()
print("Enter a scale (int):")
scale = (int)(input())
print("Enter a random variance (float 0-0.5-1):")
variance = (float)(input())
print("Enter a seed (float):")
seed = (float)(input())

img = Image.new("RGBA", (Xsize, Ysize), (0, 0, 0, 0))
px = img.load()

if px is not None:
    grid = Voronoi2D(Xsize, Ysize, scale, seed)
    grid_RDM = Random2D(Xsize, Ysize, seed)
    for y in range(Ysize):
        for x in range(Xsize):
            grayscale_gradient = 255 * grid[x, y]
            random_variance = int(
                min(255, max(0, grayscale_gradient + grid_RDM[x, y] * (255 * variance)))
            )
            gray = random_variance
            px[x, y] = (gray, gray, gray, 255)

    out = f"{file_name}.png"
    img.save(out)

    print("\nDone.")
else:
    print("\nIssue Loading Image.")
