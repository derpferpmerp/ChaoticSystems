from utils import hidePlotBounds
from matplotlib import pyplot as plt

def henon(x_n, y_n, alpha=1.4, beta=0.3, points=100, pointList=[], graph=True, outfile="henon.png"):
	for i in range(points):
		x_n1 = 1 - alpha * x_n * x_n + y_n
		y_n1 = beta * x_n
		pointList.append((x_n1, y_n1))
		x_n = x_n1
		y_n = y_n1
	if graph: graphHenon(pointList, outfile=outfile)
	return pointList

def graphHenon(points, outfile="henon.png"):
	plt.style.use("dark_background")
	fig, ax = plt.subplots(1, 1, figsize=(20,20))
	hr_x, hr_y = list(zip(*points))
	hidePlotBounds(ax)
	ax.scatter(hr_x, hr_y)
	plt.draw()
	plt.savefig(outfile)