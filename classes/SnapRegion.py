from classes.GuiObject import *
import pygame


class SnapRegion(GuiObject):
    def __init__(self, pos, sca, snapFunc = lambda x:x):
        self.target = None
        self.targetLocked = False
        self.snapFunction = snapFunc
        super().__init__(pos,sca)

    def snap(self, obj):
        self.target = obj
        obj.snapTarget = self
        self.targetLocked = False

    def unsnap(self):
        self.target.snapTarget = None
        self.target = None
        self.targetLocked = False

    def render(self, screen : pygame.Surface, event=None):
        if self.target == None:
            pygame.draw.rect(screen, (25, 100, 25), pygame.Rect(self.pos[0], self.pos[1], self.sca[0], self.sca[1]))
        else:
            pygame.draw.rect(screen, (50, 155, 50), pygame.Rect(self.pos[0], self.pos[1], self.sca[0], self.sca[1]))