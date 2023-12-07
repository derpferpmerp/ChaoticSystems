from utils import hidePlotBounds
from matplotlib import pyplot as plt

class Configuration(object):
	def __init__(self, alpha, beta, gamma, delta, x_0, y_0, points=100, outfile="tinker.png", graph=True):
		self.alpha = alpha
		self.beta = beta
		self.gamma = gamma
		self.delta = delta
		self.x_0 = x_0
		self.y_0 = y_0
		self.points = points
		self.pointList = []
		self.outfile = outfile
		self.graph = graph
	
	def display(self):
		return self.alpha, self.beta, self.gamma, self.delta, self.x_0, self.y_0

	def update(self, x, y):
		self.x_0 = x
		self.y_0 = y
		self.points -= 1
		self.pointList.append( (self.x_0, self.y_0) )

PRESET_1 = Configuration(
	alpha=0.9,
	beta=-0.6013,
	gamma=2,
	delta=0.5,
	x_0=-0.72,
	y_0=-0.64,
	points=1000
)

def tinker(config:Configuration):
	for i in range(config.points):
		alpha, beta, gamma, delta, x_0, y_0 = config.display()
		x_n1 = x_0*x_0 - y_0*y_0 + alpha*x_0 + beta*y_0
		y_n1 = 2*x_0*y_0 + gamma * x_0 + delta * y_0
		config.update(x_n1, y_n1)
	if config.graph:
		graphTinker(config)
	return config.pointList
	
def graphTinker(config):
	points = config.pointList
	outfile = config.outfile
	plt.style.use("dark_background")
	fig, ax = plt.subplots(1, 1, figsize=(7,7))
	hidePlotBounds(ax)
	tk_x, tk_y= list(zip(*points))
	ax.scatter(tk_x, tk_y)
	plt.draw()
	plt.show()
	#plt.savefig(outfile)

tinker(PRESET_1)