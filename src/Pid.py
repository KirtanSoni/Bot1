import math

from util.vec import Vec3
from util.Quaternion import Quat
"""Incomplete"""

class PID:
    __init__(self,K1 : float, K2 : float , K3 : float):
        self.k1=k1
        self.k2=K2
        self.k3=K3 
        self.integr=0
        self.lastval=0
    def intergrator(self,controlled_var)->float:
        
    
    def proportional(self,controlled_var)->float:

        
    
    
    def contr_Output(self,controlled_var)->float:
        x = self.k1*proportional(controlled_var) - self.k3 * derivative(controlled_var) + self.k2*intergrator(controlled_var)
        return x
    