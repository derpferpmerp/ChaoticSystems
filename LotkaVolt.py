from lode import System
import numpy as np



class LotkaVolterra(System):
	def __init__(self, alpha=2/3, beta=4/3, gamma=1, delta=1, state0=[0.9, 0.9]):
		self.alpha = alpha
		self.beta = beta
		self.gamma = gamma
		self.delta = delta
		self.state0 = state0

	def derive(self, state, t):
		x, y = state
		return (
			(self.alpha*x)-(self.beta*x*y),
			(self.delta*x*y)-(self.gamma*y)
		)



SYSTEM = LotkaVolterra(state0=[10,10])
T = np.arange(0.0, 30.0, 0.01)
STATESL = lambda beta: [[alpha,beta,beta,alpha-1] for alpha in np.arange(1.2,2,0.1)]
STATESLL = []
LABELS = []
for beta in [0.4]:
	for STATE in STATESL(beta):
		SYSTEM.alpha = STATE[0]
		SYSTEM.beta = STATE[1]
		SYSTEM.gamma = STATE[2]
		SYSTEM.delta = STATE[3]
		STATESLL.append(SYSTEM.calculateSystem(T))
		LABELS.append(f"$\\alpha={round(10*STATE[0])/10},\\beta={round(10*STATE[1])/10}$")
	SYSTEM.graph(outfile="lotka.png", dimensions=2, hideAxis=False, states=STATESLL, LABELS=LABELS)
