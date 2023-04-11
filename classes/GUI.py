import pygame
from easing_functions import *

from classes.Draggable import Draggable
from classes.SnapRegion import SnapRegion
from classes.TextRenderer import TextRenderer
from classes.GuiObject import *

TRANSPARENT_COLOR = (255,5,255)
class GUI:
    def __init__(self, screen : pygame.Surface):
        self.screen = screen
        self.TRANSPARENT_COLOR = (255, 5, 255,0)
        self.draggable = []
        self.snapRegions = []
        self.init()
        self.selected = None
        self.redraw()

    def init(self):
        self.draggable = [
            Draggable((0,0),(100,100)),
            Draggable((50,0),(100,100)),
            Draggable((150,150),(100,25)),
            TextRenderer((640, 300), (100, 100), 'Hello, World!')
        ]

        self.snapRegions = [
            SnapRegion((100, 100), (99, 99)),
            SnapRegion((100, 200), (99, 99)),
            SnapRegion((100, 300), (99, 99))
        ]
        for snap in self.snapRegions:
            snap.snapFunc = BounceEaseInOut(start=0, end=1)
            snap.speed = 10

    def onMouseDrag(self, event):
        if pygame.mouse.get_pressed(3)[0]:
            if self.selected == None:
                for obj in self.draggable:
                    if obj.isInRect(event["mouse_pos"]) and issubclass(type(obj), Draggable):
                        self.selected = obj

            if self.selected != None:
                if not event['used']:
                    self.selected.onDrag(event)
                    event['used'] = True
        else:
            self.selected = None

    def update(self, event):
        for obj in self.draggable:
            if obj != self.selected: # snapping to grid
                if issubclass(type(obj), Draggable):
                    if obj.snapTarget is None:
                        attractor = None
                        delta = 0
                        for snap in self.snapRegions:
                            if isOverlapping((obj.pos, obj.sca), (snap.pos, snap.sca)):
                                n_delta = (obj.pos - snap.pos).length() + (obj.sca - snap.sca).length() // 2
                                if snap.target is None and (attractor is None or delta > n_delta):
                                    attractor = snap
                                    delta = n_delta
                        if attractor != None:
                            attractor.snap(obj)

        for snap in self.snapRegions:
            if snap.target is not None:
                if snap.target == self.selected:
                    snap.unsnap()
                else:
                    if not snap.targetLocked:
                        delta = snap.getCenter() - snap.target.getCenter()
                        if delta.length() > 1:
                            snap.target.shift( delta * snap.snapFunc(event['delta_time']) * snap.speed)
                        else:
                            snap.target.move(delta + snap.target.pos)
                            snap.targetLocked = True

        #obj.pos = obj.pos + (round(obj.pos / 100) * 100 - obj.pos) * event['delta_time'] * 20

    def redraw(self):
        # clearing screen
        self.screen.fill((0,0,0))
        colOff = 0
        for obj in self.snapRegions:
            obj.render(self.screen)
        for obj in self.draggable:
            obj.render(self.screen, {'selected':self.selected})
        pygame.display.update()
