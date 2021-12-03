import pygame as pg
from config import *
from sprites import *
from pathfinder import *
from cameramovement import *
from level import Level
from game_data import level_0
from typing import List

class Overworld:

    def __init__(self):
        pg.init()
        # pg.mixer.init()
        pg.display.set_caption("RPG_Game")
        self.clock = pg.time.Clock()
        self.abspos = (0, 0)
        self.new()

    def load_data(self):
        self.map_matrix = []
        self.mouseimage = pg.image.load("assets/cursor.png").convert_alpha()
        self.level = Level(level_0, self)

    def new(self):
        pg.mouse.set_visible(False)
        
        # creating sprite groups
        self.shadowsprites = pg.sprite.Group()
        self.enemysprites = pg.sprite.Group()
        self.wallsprites = pg.sprite.Group()
        self.playersprite = pg.sprite.GroupSingle()
        self.floorsprites = pg.sprite.Group()

        self.load_data()
        self.player = Player(self, (100, 100))
        self.enemy = Enemy(self, (300, 300))
        self.camera = Camera(self.map_matrix)
    
    def update(self):
        self.playersprite.update()
        self.enemysprites.update()
        self.wallsprites.update()
        self.shadowsprites.update()
        self.camera.update(self.player)
    
    def event_loop(self, events: List[pg.event.Event]) -> None:
        for event in events:
            self.mousepos = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN:
                if not(self.player.moving):
                    self.getabspos(self.mousepos, self.player)
                    self.player.pathfinder.create_path(self.abspos, self)

    def draw_active_cell(self, screen): # draws the tile that the user is hovering over
        mouse_pos = pg.mouse.get_pos()
        x = mouse_pos[0] // 32
        y = mouse_pos[1] // 32
        mouse = pg.Surface((TILESIZE, TILESIZE), pg.SRCALPHA)
        mouse.fill((30, 30, 30, 100))
        screen.blit(mouse, (x * TILESIZE, y * TILESIZE))

    def draw(self, screen: pg.Surface):
        screen.fill((30, 30, 30))
    
        for sprite in self.floorsprites:
            screen.blit(sprite.image, self.camera.apply(sprite))

        if not self.player.moving:
            self.draw_active_cell(screen)

        for sprite in self.wallsprites:
            screen.blit(sprite.image, self.camera.apply(sprite))
        
        for sprite in self.playersprite:
            screen.blit(sprite.image, self.camera.apply(sprite))

        for sprite in self.enemysprites:
            screen.blit(sprite.image, self.camera.apply(sprite))
            
        for sprite in self.shadowsprites:
            screen.blit(sprite.image, self.camera.apply(sprite))

        screen.blit(self.mouseimage, self.mousepos)

    def getabspos(self, cursorpos, target):
        x = target.rect.x - int(WIDTH / 2)
        y = target.rect.y - int(HEIGHT / 2)
        absposx = x + cursorpos[0]
        absposy = y + cursorpos[1]
        self.abspos = (absposx, absposy)

    def show_start_screen(self):
        pass