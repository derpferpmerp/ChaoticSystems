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
			list_t
		)

	def graph(self, outfile="lode.png", dimensions=3):
		if type(self.states) == bool:
			raise ArithmeticError("Must Have Calculated System Beforehand... Run With System.calculateSystem(T)")
		if dimensions == 3:
			fig = plt.figure()
			ax = plt.axes(projection='3d')

			ax.plot(
				self.states[:, 0],
				self.states[:, 1],
				self.states[:, 2]
			)

			fig.set_facecolor('black')
			ax.set_facecolor('black')
			ax.grid(False)
			ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
			ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
			ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
		elif dimensions == 2:
			fig = plt.figure()
			ax = plt.axes()
			ax.plot(self.states[:, 0], self.states[:, 1])
			fig.set_facecolor('black')
			ax.set_facecolor('black')
			ax.grid(False)
		
		plt.draw()
		plt.savefig(outfile)
