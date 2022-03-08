from scipy.integrate import odeint as integrate
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

class System(object):
    def __init__(self, derive, state0=[]):
        self.derive = derive
        self.state0 = [1.0, 1.0, 1.0] if state0 == [] else state0
        self.states = False

    def calculateSystem(self, list_t):
        self.states = integrate(
            self.derive,
            self.state0,
            list_t,
        )

    def graph(self, outfile="lode.png", dimensions=3, alpha=False, hideAxis=True, scaleAxes=False):
        if type(self.states) == bool:
            raise ArithmeticError("Must Have Calculated System Beforehand... Run With System.calculateSystem(T)")
        if dimensions == 3:
            fig = plt.figure()
            ax = plt.axes(projection='3d')
            items = [self.states[:, 0], self.states[:, 1], self.states[:, 2]]
            maxes = [max(X) for X in items]
            mins = [min(X) for X in items]
            MAX = max(maxes)
            MIN = min(mins)
            ax.plot(
                self.states[:, 0],
                self.states[:, 1],
                self.states[:, 2],
            )
            if scaleAxes:
                ax.set_xlim(MIN, MAX)
                ax.set_ylim(MIN, MAX)
                ax.set_zlim(MIN, MAX)

            if hideAxis:
                fig.set_facecolor('black')
                ax.set_facecolor('black')
                ax.grid(False)
                ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
                ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
                ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        elif dimensions == 2:
            fig = plt.figure()
            ax = plt.axes()
            items = [self.states[:, 0], self.states[:, 1]]
            ax.plot(*items)
            
            maxes = [max(X) for X in items]
            mins = [min(X) for X in items]
            MAX = max(maxes)
            MIN = min(mins)
            if scaleAxes:
                ax.set_xlim(MIN, MAX)
                ax.set_ylim(MIN, MAX)
            fig.set_facecolor('black')
            ax.set_facecolor('black')
            ax.grid(False)
        
        plt.draw()
        plt.savefig(f"generated/{outfile}", bbox_inches="tight")
