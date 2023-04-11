import pygame.math
from classes.GuiObject import *


class Draggable (GuiObject):
    def __init__(self, pos, sca):
        super().__init__(pos,sca)
        self.snapTarget = None

    def onDrag(self, event):
        self.pos += event['mouse_delta']

    def render(self, screen : pygame.Surface, event=None):
        if event['selected'] == self:
            thick = 5  # border thickness
            pygame.draw.rect(screen, (236, 183, 28),
                             pygame.Rect(self.pos[0] - thick, self.pos[1] - thick, self.sca[0] + thick * 2,
                                         self.sca[1] + thick * 2))
        pygame.draw.rect(screen, (155, 0, 0),
                         pygame.Rect(self.pos[0], self.pos[1], self.sca[0], self.sca[1]))