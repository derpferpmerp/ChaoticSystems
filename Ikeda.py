from math import cos, sin

import matplotlib.pyplot as plt
import numpy as np
import scipy.spatial as spatial
from tqdm import tqdm
from matplotlib import cm
from utils import hidePlotBounds, colorline
from numpy import pi as PI, arctan

plt.style.use("dark_background")

class Ikeda(object):
    def __init__(self, u=0.918, iterations=100, points=700, outfile="generated/ikeda.png"):
        self.ikeda_param = u
        self.iterations = iterations
        self.n_points = points
        self.X_GRID = np.zeros((points, points))
        self.outfile = outfile
        
    def ikeda(self, x, y):
        t = 0.4 - 6 / (1 + x*x + y*y)
        return (
            1 + self.ikeda_param * (x * cos(t) - y * sin(t)),
            self.ikeda_param * (x * sin(t) + y * cos(t))
        )
        
    def solve_ikeda(self, x, y):
        X = np.zeros((self.iterations, 2))
        for i in range(self.iterations):
            X[i] = np.array((x, y))
            xi, yi= self.ikeda(x, y)
            x=xi
            y=yi
        return X
    
    def sigmoid(self, z:np.ndarray, a=1.1):
        z = np.interp(z, (z.min(), z.max()), (-a, a))
        b = -1.0#7.0
        sig = 1.0/(a * (1.0 + np.exp(b * z))) + 0.5 * ((a-1)/a)
        return sig
    
    def tanfit(self, z:np.ndarray, a=PI, bound=(-6,1.5)):
        z = np.interp(z, (z.min(), z.max()), bound)
        item = arctan(a * z)/PI
        item = item + 1/2
        return item
    
    def generate(self, graph=True, **kwargs):
        x = 10 * np.random.randn(self.n_points, 1)
        y = 10 * np.random.randn(self.n_points, 1)
        
        P_OUT = []
        for x_i, y_i in tqdm(zip(x, y), total=len(x)):
            X = x_i[0] # change_x(x_i)
            Y = y_i[0] # change_y(y_i)
            XL = self.solve_ikeda(X, Y)
            P_OUT.append([ XL[:, 0], XL[:, 1] ])
        if graph: self.graph_ikeda(P_OUT, **kwargs)
        else: return P_OUT
        
    def graph_ikeda(self, points, method="plot", interp="tan", size=(10,10)):
        fig, ax = plt.subplots(1, 1, figsize=size)
        for xG, yG in tqdm(points, unit="points"):
            if method == "plot":
                NPOINTS = len(xG)
                ALPHA = np.array([float(i)/(NPOINTS-1) for i in range(NPOINTS-1)])
                if interp == "tan":
                    ALPHA = self.tanfit(ALPHA)
                elif interp == "sig":
                    ALPHA = self.sigmoid(ALPHA)
                
                for i in range(NPOINTS-1):
                    ax.plot(
                        xG[i:i+2],
                        yG[i:i+2],
                        alpha=ALPHA[i],
                        color="white"
                    )
            else:
                ax.scatter(xG, yG)
        
        hidePlotBounds(ax)
        plt.savefig(
            self.outfile,
            bbox_inches="tight"
        )

SYSTEM = Ikeda()
SYSTEM.generate(
    size=(25,25),
    interp="tan",
    method="plot"
)
