from utils import hidePlotBounds
from matplotlib import pyplot as plt
from math import floor, exp, cos
import numpy as np
from numpy import pi as PI

class Configuration(object):
	def __init__(self, nu, epsilon, r, x_0, y_0, points=1000, outfile="generated/zaslavskii.png", graph=True):
		self.nu = nu
		self.eps = epsilon
		self.r = r
		self.x_0 = x_0
		self.y_0 = y_0
		self.points = points
		self.pointList = []
		self.outfile = outfile
		self.graph = graph
	
	def display(self):
		return self.nu, self.eps, self.r, self.x_0, self.y_0

	def update(self, x, y):
		self.x_0 = x
		self.y_0 = y
		self.points -= 1
		self.pointList.append( (self.x_0, self.y_0) )

def mod_1(num):
	return num % 1

PRESET = Configuration(
	nu=0.2,
	epsilon=1.3,
	r=2,
	x_0=-1,
	y_0=-1,
	points=6220
)


def zas(config:Configuration):
	for i in range(config.points):
		nu, eps, r, x_0, y_0 = config.display()
		u_1 = eps * cos(2 * PI * x_0)
		mu = (1 - exp(-r))/r
		x_n1 = x_0 + nu * (1 + mu * y_0)
		x_n1 +=  nu * mu * u_1
		x_n1 = mod_1(x_n1)
		
		y_n1 = exp(-r)*(y_0 + u_1)
		config.update(x_n1, y_n1)
	if config.graph:
		graphZas(config)
	return config.pointList
	
def graphZas(config):
	points = config.pointList
	outfile = config.outfile
	plt.style.use("dark_background")
	fig, ax = plt.subplots(1, 1, figsize=(10,10))
	hidePlotBounds(ax)
	tk_x, tk_y = list(zip(*points))
	ax.scatter(tk_x, tk_y)
	plt.draw()
	plt.show()
	#plt.savefig(outfile)

zas(PRESET)