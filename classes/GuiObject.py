import pygame
from pygame.math import *

def isOverlapping(A,B):
    # check if 2 AABB's overlap
    # 2 AABB overlaps <=> both projections overlaps
    if isinstance(A,list) or isinstance(B,tuple) or isinstance(A,Vector2):
        return A[0][0] <= B[0][0] + B[1][0] and A[0][0] + A[1][0] >= B[0][0] and \
                A[0][1] <= B[0][1] + B[1][1] and A[0][1] + A[1][1] >= B[0][1]
    else:
        return False

class GuiObject:
    def __init__(self, pos, sca):
        self.TRANSPARENT_COLOR = (255,5,255,0)
        self.pos = Vector2(pos)
        self.sca = Vector2(sca)
        self.parent = None
        self.child = []

    def setParent(self, parent):
        self.parent = parent
        self.parent.child.append(self)

    def clearParent(self):
        self.parent.child.remove(self)
        self.parent = None

    def move(self, pos):
        delta = pos - self.pos
        for c in self.child:
            c.shift(delta)
        self.pos = pos
    def getCenter(self):
        return self.pos + self.sca // 2
    def isInRect(self, point):
        return self.pos[0] <= point[0] < self.pos[0] + self.sca[0] and self.pos[1] <= point[1] < self.pos[1] + self.sca[1]

    def shift(self, off):
        self.move(self.pos + off)

    def render(self, screen : pygame.Surface, event=None):
        pass