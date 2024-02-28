import pygame as pg

class Pantalla:
    def __init__(self, width, height):
        pg.init()
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption('Subnetting')
        self.clock = pg.time.Clock()

    def update_screen(self):
        pg.display.flip()
        self.clock.tick(60)