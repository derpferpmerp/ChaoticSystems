import math
import numpy as np
from numpy import pi as PI, cos, sin, sqrt, tan
from lode import System
from matplotlib import pyplot as plt

class BlackHole(System):
    def __init__(self, a=0.94, M=10.0, t_0=None, r_0=None, theta_0=None, phi_0=None):
        # State: [ Time, Radius, Theta, Phi ]
        # M: Mass Of Black Hole
        # A: Spin Paramater
        if t_0 is None: self.t_0 = 10.0
        else: self.t_0 = t_0
        
        if r_0 is None: self.r_0 = 1.0
        else: self.r_0 = r_0
        
        if theta_0 is None: self.theta_0 = PI/8
        else: self.theta_0 = theta_0
        
        if phi_0 is None: self.phi_0 = 0
        else: self.phi_0 = phi_0
        
        self.a = a
        self.M = M
        self.mu = -1 # 0 for Massless, -1 for Mass
        self.state0 = [ self.t_0, self.r_0, self.theta_0, self.phi_0 ]
        
    def sigma(self, r, theta):
        return pow(r, 2) + pow(self.a, 2) * pow(cos(theta), 2)
    
    def delta(self, r):
        return pow(r, 2) - 2 * self.M * r + pow( self.a, 2 )
    
    def vecRoot(self, item):
        if item == 0: return 0
        mult = np.sign(item)
        SQUARE = np.sqrt(abs(item))
        return SQUARE * mult
    
    def calcE(self, r, theta, phi):
        sigma = self.sigma(r, theta)
        delta = self.delta(r)
        p1mult1 = ( sigma - 2 * r ) / ( sigma * delta )
        p1mult2 = sigma * r * r
        p1mult2 += sigma * delta * pow(theta, 2)
        p1mult2 -= delta * self.mu

        p1 = p1mult1 * p1mult2
        
        p2 = delta * phi * phi * pow(sin(theta), 2)
        beta = p1 + p2
        if math.isnan(beta) or math.isinf(beta) or not math.isfinite(beta) or beta < 0:
            return 0
        return sqrt(beta)
    
    def calcL_Z(self, r, theta, phi, E):
        sigma = self.sigma(r, theta)
        delta = self.delta(r)
        p_top_mult1 = sigma * delta * phi
        p_top_mult1 -= 2 * self.a * r * E
        
        p_top_mult2 = pow(sin(theta), 2)
        
        p_top = p_top_mult1 * p_top_mult2
        
        p_bottom = sigma - 2 * r
        
        return p_top / p_bottom
    
    def calcQ(self, E, L_Z, sigma, theta):
        p_theta = sigma * theta
        Q = pow( L_Z * pow( sin(theta), -1 ) , 2 )
        Q -= pow( self.a, 2 ) * ( pow(E, 2) + self.mu )
        Q *= pow( cos(theta), 2 )
        Q += pow( p_theta, 2 )
        return Q
             
    def derive(self, state, list_t):
        time, radius, theta, phi = state
        E = self.calcE(radius, theta, phi)
        L_Z = self.calcL_Z(radius, theta, phi, E)
        sigma = self.sigma(radius, theta)
        delta = self.delta(radius)
        Q = self.calcQ(E, L_Z, sigma, theta)
        
        dTime = 2 * radius * E * ( pow(radius, 2) + pow(self.a, 2) )
        dTime -= 2 * self.a * radius * L_Z
        dTime /= sigma * delta
        dTime += E
        
        dRp2 = ( delta / sigma ) * ( self.mu + E * time - L_Z * phi - sigma * theta * theta)
        dRadius = sqrt( dRp2 )
        
        dTp2 = Q + ( pow(E,2) + self.mu ) * pow( self.a * cos(theta), 2) - pow( L_Z / tan(theta) , 2 )
        dTp2 *= pow( sigma, -2 )
        dTheta = sqrt( dTp2 )
        
        dPhi = 2 * self.a * radius * E
        dPhi += (sigma - 2 * radius) * L_Z * pow( sin(theta), -2 )
        dPhi /= sigma * delta
        
        return (
            dTime,
            dRadius,
            dTheta,
            dPhi
        )

    def sigmoid(self, z:np.ndarray, a=1.1):
        z = np.interp(z, (z.min(), z.max()), (-1.1, 1.1))
        sig = 1.0/(a * (1.0 + np.exp(7.0 * z))) + 0.5 * ((a-1)/a)
        return sig 

    def sinRegress(self, z:np.ndarray, A=3.0, B=9.509, C=18.9):
        z = np.interp(z, (z.min(), z.max()), (-3, 2.94))
        return ( sin(A * z) + A * z + B ) / C
    
    def render(self, times, gradient=False):
        self.calculateSystem(times)
        STATES = np.nan_to_num(self.states, copy=True)
        time = STATES[:, 0]
        L = []
        alpha = []
        for i in range(len(STATES)):
            time, radius, theta, phi = STATES[i]
            x = radius * sin(theta) * cos(phi)
            y = radius * sin(theta) * sin(phi)
            z = radius * cos(theta)
            L.append([ x, y, z ])
            alpha.append(time)
        alpha = np.array(alpha)
        Z = self.sigmoid(alpha) if gradient else np.ones_like(alpha)
        
            
        self.states = np.array(L)
        self.graph(outfile="BlackHole.png", dimensions=3, hideAxis=False, scaleAxes=True)


if __name__ == "__main__":
    SYSTEM = BlackHole()
    SYSTEM.render(np.arange(0.0, 100.0, 0.01), gradient=True)

