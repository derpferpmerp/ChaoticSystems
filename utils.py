from matplotlib import pyplot as plt
from scipy.integrate import quad as integrate
import numpy  as np
from numpy import pi as PI
from math import tan, sin, exp
from numpy import log as loge

def cot(x):
	return 1/tan(x)

def csc(x):
	return 1/sin(x)


def hidePlotBounds(ax):
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.spines['bottom'].set_visible(False)
	ax.spines['left'].set_visible(False)

	ax.set_xticklabels([])
	ax.set_yticklabels([])

	ax.set_xticks([])
	ax.set_yticks([])

	ax.axes.get_xaxis().set_visible(False)
	ax.axes.get_yaxis().set_visible(False)

def lambertW(x):
	func_TOP = lambda t: ((1-t*cot(t))**2 + t**2)
	func_BOT = lambda t: x + t*csc(t)*exp(-t*cot(t))
	FUNC = lambda t: (func_TOP(t) / func_BOT(t))
	integral = integrate(FUNC, 0, PI - pow(10,-2))
	return (x/PI) * integral[0]

def smartLambert(x):
	a = abs(x)
	ln = loge(a)
	if a > 1 or a < 1:
		return -1 * lambertW(-ln)/ln
	else:
		return 1