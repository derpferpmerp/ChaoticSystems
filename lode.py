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
        return self.states

    def graph(self, outfile="lode.png", dimensions=3, alpha=False, hideAxis=True, scaleAxes=False, fixedAxis=False, states=None, LABELS=None):
        if type(self.states) == bool:
            raise ArithmeticError("Must Have Calculated System Beforehand... Run With System.calculateSystem(T)")
        if states is None: states = [self.states]
        if dimensions == 3:
            fig = plt.figure()
            ax = plt.axes(projection='3d')
            MAXES = []
            MINS = []
            for i, stateobj in enumerate(states):
                items = [stateobj[:, 0], stateobj[:, 1], stateobj[:, 2]]
                maxes = [max(X) for X in items]
                mins = [min(X) for X in items]
                MAXES.append(max(maxes))
                MINS.append(min(mins))
                if LABELS is not None: ax.plot(*items,label=LABELS[i])
                else: ax.plot(*items)
            MIN = min(MINS)
            MAX = max(MAXES)
            if scaleAxes:
                ax.set_xlim(MIN, MAX)
                ax.set_ylim(MIN, MAX)
                ax.set_zlim(MIN, MAX)
            elif fixedAxis != False:
                ax.set_xlim(fixedAxis[0][0], fixedAxis[0][1])
                ax.set_ylim(fixedAxis[1][0], fixedAxis[1][1])
                ax.set_ylim(fixedAxis[2][0], fixedAxis[2][1])

            if hideAxis:
                fig.set_facecolor('black')
                ax.set_facecolor('black')
                ax.grid(False)
                ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
                ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
                ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        elif dimensions == 2:
            #if not hideAxis: plt.style.use("dark_background")
            fig = plt.figure()
            ax = plt.axes()
            MAXES = []
            MINS = []
            for i,stateobj in enumerate(states):
                items = [stateobj[:, 0], stateobj[:, 1]]
                if LABELS is not None:
                    ax.plot(*items,label=LABELS[i])
                else:
                    ax.plot(*items)
                
                maxes = [max(X) for X in items]
                mins = [min(X) for X in items]
                MAXES.append(max(maxes))
                MINS.append(min(mins))
            if scaleAxes:
                ax.set_xlim(MIN, MAX)
                ax.set_ylim(MIN, MAX)
            elif fixedAxis != False:
                ax.set_xlim(fixedAxis[0][0], fixedAxis[0][1])
                ax.set_ylim(fixedAxis[1][0], fixedAxis[1][1])
            if hideAxis:
                fig.set_facecolor('black')
                ax.set_facecolor('black')
                ax.grid(False)
        if LABELS is not None: ax.legend(loc='best',prop={'size': 8.5})
                
        plt.savefig(f"generated/{outfile}", bbox_inches="tight", dpi=300)
