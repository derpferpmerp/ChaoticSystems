from math import floor
from matplotlib import pyplot as plt
import numpy as np

chaos = lambda x: 4*x*(1-x)
X_0 = 0.45

def constructMult(eq, npoints, x_0):
	alpha = x_0
	l = [x_0]
	for x in range(npoints):
		alpha = eq(alpha)
		l.append(alpha)
	return l

def constructPoints(eq, npoints, x_0):
	rmult = constructMult(eq, npoints, x_0)
	return list(enumerate(rmult))

def line(x1, y1, x2, y2):
	return lambda x: (y2-y1)/(x2-x1) * (x-x1) + y1

def segmentsFromPoints(points):
	L_X, L_Y = [[],[]]
	for x,y in points:
		L_X.append(x)
		L_Y.append(y)
	
	L_LINES = []
	
	for x in range(len(points)-1):
		y = [x, x+1]
		cpoint = (x_1, y_1), (x_2, y_2) = [
			points[y[0]],
			points[y[1]]
		]
		cline = line(x_1, y_1, x_2, y_2)
		L_LINES.append(cline)
	print(len(L_LINES))
	return lambda x: L_LINES[floor(x)](x)

points = constructPoints(chaos, 10, X_0)
lines = segmentsFromPoints(points)
rx = np.linspace(0, 9, 1000)
ry = list(map(lambda x: lines(x), rx))
plt.plot(rx, ry)

print(len(points))
LPX, LPY = [[],[]]
for x,y in points:
	LPX.append(x)
	LPY.append(y)

plt.scatter(LPX, LPY)
plt.savefig("utterchaos.png")