from lode import System
import numpy as np



class LotkaVolterra(System):
	def __init__(self, state0=[1/4, 1/2, 1/2]):
		self.state0=state0

	def derive(self, state, t):
		x1, x2, x3 = state
		return (
			1*x1*(1-((((1/32)*x1)+((24/32)*x2)+((24/32)*x3))/4)),
			1*x2*(1-((((1/(48*32))*x1)+((1/32)*x2)+((1/(48*32))*x3))/(20))),
			0.5*x3*(1-(((((1/48)/32)*x1)+(((1/48)/32)*x2)+((1/32)*x3))/(50)))
		)



SYSTEM = LotkaVolterra()
T = np.arange(0.0,10.0,0.01)
STATESL = [[z,z,z] for z in np.arange(0.5,4,0.5)]
STATESLL = []
LABELS = []
for i, STATE in enumerate(STATESL):
	SYSTEM.state0 = STATE
	STATESLL.append(SYSTEM.calculateSystem(T))
	LABELS.append(f"$x_i(0)={round(10*STATE[0])/10}$")
SYSTEM.graph(outfile="lotka3d.png", dimensions=3, hideAxis=False, states=STATESLL, LABELS=LABELS)

