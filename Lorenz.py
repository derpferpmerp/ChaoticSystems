from lode import System
import numpy as np

class Lorenz(System):
	def __init__(self, rho=28.0, sigma=10.0, beta=8.0/3.0, state0=[1.0,1.0,1.0]):
		self.rho = rho
		self.sigma = sigma
		self.beta = beta
		self.state0 = state0

	def derive(self, state, t):
		x, y, z = state
		return (
			self.sigma * (y - x),
			x * (self.rho - z) - y,
			x * y - self.beta * z
		)

SYSTEM = Lorenz()
T = np.arange(0.0, 40.0, 0.01)
SYSTEM.calculateSystem(T)
SYSTEM.graph(outfile="lorenz.png")
