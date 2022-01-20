from lode import System
import numpy as np


class Rossler(System):
	def __init__(self, a=0.2, b=0.2, c=5.7, state0=[1.0, 1.0, 1.0]):
		self.a = a
		self.b = b
		self.c = c
		self.state0 = state0
	
	def derive(self, state, list_t):
		x, y, z = state
		return (
			-1 * ( y + z ),
			x + self.a * y,
			self.b + (z * (x - self.c))
		)
		
SYSTEM = Rossler()
T = np.arange(0.0, 400.0, 0.01)
SYSTEM.calculateSystem(T)
SYSTEM.graph(outfile="rossler.png")
