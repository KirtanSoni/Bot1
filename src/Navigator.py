import math

from util.vec import Vec3
from util.Quaternion import Quat

class node:
    def __init__(self , pos : 'Vec3' , action , r : float = 50):
        self.pos = pos 
        self.action = action
        self.Next = None 
        self.r = r


class Navigator:
    def __init__(self,Vec3):
        self.head = node(Vec3,1)
        self.tar = self.head 

    
    def addNode(self,loc,action):
        self.tar =self.tar.Next
        self.tar = node(loc,action)

    
        