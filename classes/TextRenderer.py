import operator

from classes.GuiObject import *
from classes.Draggable import Draggable
import pygame


class TextRenderer(GuiObject):
    def __init__(self, pos, sca, text=""):
        super().__init__(pos, sca)
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.color = (0,255,0)
        self.bgcolor = (self.color[0], self.color[1] - 50 if self.color[1] > 50 else self.color[1] + 50, self.color[2])
        print(self.bgcolor)
        self.textObj = self.font.render('Sampe Text', True, self.color, self.bgcolor)
        self.setText(text)

    def setText(self, text=""):
        self.text = text
        self.textObj = self.font.render(self.text, True, self.color, self.bgcolor)
        self.textRect = self.textObj.get_rect()
        sca = self.font.size(self.text)
        self.sca = pygame.Vector2(sca[0],sca[1])

    def render(self, screen : pygame.Surface, event):
        self.textObj.set_colorkey(self.bgcolor)
        self.textRect.center = (self.pos[0] + self.sca[0] // 2, self.pos[1] + self.sca[1] // 2)
        screen.blit(self.textObj, self.textRect)