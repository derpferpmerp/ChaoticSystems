import random

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

from utils import alpha_shape, stitch_boundaries

plt.style.use("dark_background")

def chooseFunction(*pos):
    return random.choice(pos)

def f1(x,y):
    X = x - y
    Y = x + y
    return [X/2, Y/2]
    
def f2(x,y):
    X = 2 - x - y
    Y = x - y
    return [X/2, Y/2]

XL = np.linspace(-10, 10, 200)
YL = np.linspace(-10, 10, 200)
points = []

with tqdm(total=len(XL)*len(YL), unit="points") as pbar:
    for x in XL:
        for y in YL:
            point = [x, y]
            for i in range(100):
                pt = chooseFunction(f1(*point), f2(*point))
                point = pt
            points.append(point)
            pbar.update(1)

points = np.array(points)
px, py = [ points[:, 0], points[:, 1] ]

edges = alpha_shape(points, alpha=0.01, only_outer=True)
boundsLIST = stitch_boundaries(edges)
pointThresh = 25

#plt.plot(points[:, 0], points[:, 1], '.')

for i, bounds in tqdm(list(enumerate(boundsLIST)), unit="bounds"):
    if len(bounds) <= pointThresh: continue
    bounds_lst = []
    for indx, none in bounds:
        bounds_lst.append(list(np.asarray(points[indx])))
    bx, by = [[], []]
    for x, y in bounds_lst:
        bx.append(x)
        by.append(y)
    fig, ax = plt.subplots(1,1,figsize=(13.5,10))
    ax.plot(bx, by)

plt.savefig(f"generated/dragon.png")
