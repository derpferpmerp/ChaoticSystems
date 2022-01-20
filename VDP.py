from lode import System
import numpy as np

class VDP(System):
	def __init__(self, mu=0.1, state0=[1.0,1.0]):
		self.mu = mu
		self.state0 = state0

	def derive(self, state, list_t):
		x, y = state
		return (
			self.mu * (x - 1/3 * x * x * x - y),
			1/self.mu * x
		)

SYSTEM = VDP()
SYSTEM.calculateSystem(np.arange(0.0, 100.0, 0.01))
SYSTEM.graph(outfile="VDP.png", dimensions=2)