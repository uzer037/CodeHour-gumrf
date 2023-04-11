# Example file showing a basic pygame "game loop"
import pygame
import time
from classes.EventSystem.EventSystem import *
from pygame.math import *
from classes.GUI import GUI

class Game:
    def __init__(self):
        self.running = True
        pygame.init()
        self.clock = pygame.time.Clock()
        self.GUI = GUI(pygame.display.set_mode((1280, 720)))

        # input
        self.mouseLastPos = Vector2(0,0)
        self.mousePos = Vector2(0,0)
        self.mouseDelta = Vector2(0,0)

        #clock
        self.lastTime = 0;
        self.time = time.time();
        self.deltaTime = self.time;


    def exit(self):
        print('Exited safley')
        self.running = False

    def handleInput(self, event):
        if event.key == pygame.K_ESCAPE:
            print('Exiting via Esc key...')
            self.exit()

    def loop(self):
        # update clock
        self.lastTime = self.time;
        self.clock.tick()
        self.time = time.time();
        self.deltaTime = self.time - self.lastTime;

        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                self.handleInput(event)
            if event.type == pygame.MOUSEMOTION:
                self.mouseLastPos = self.mousePos
                self.mousePos = Vector2(pygame.mouse.get_pos())
                self.mouseDelta = self.mousePos - self.mouseLastPos
                ## pass mouse event to GUI component
                self.GUI.onMouseDrag({
                    "mouse_pos":    self.mousePos,
                    "mouse_delta":  self.mouseDelta,
                    "delta_time":   self.deltaTime,
                    "used": False
                })

        # render
        self.GUI.update({
            "delta_time": self.deltaTime
        })
        self.GUI.redraw()
    

if __name__ == "__main__":
    game = Game()
    while game.running:
        game.loop()