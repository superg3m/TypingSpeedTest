import pygame
from pygame.locals import *
import sys
import time
import pyjokes
from pygame.transform import scale


class Main:

    def __init__(self):
        self.w = 750
        self.H
        self.reset
        self.active = False
        self.inputText = ''
        selfWord = ''
        self.timeStart = 0
        self.totalTime = 0
        self.accuracy = '0%'
        self.resualt = 'Time:0 Accuracy:0 WPM:0'
        self.WPM = 0
        self.end = False
        self.HEAD_C = (255, 213, 102)
        self.Text_C = (240, 240, 240)
        self.RESULT_C = (255, 70, 70)

        pygame.init()
        self.open_img = pygame.image.load('images/background.jpg')
        self.open_img = pygame.transform.scale(scale(self.bg, (750, 500)))

        self.screen = pygame.display.set_mode((self.w/2, y))
