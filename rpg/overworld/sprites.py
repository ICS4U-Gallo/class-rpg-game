import pygame as pg
from config import *
from pathfinder import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, pathfinding):
        self.groups = game.playersprite
        super().__init__(self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE - 2, TILESIZE - 2))
        #PLAYER ASSETS HERE
        self.image.fill(RED)
        self.rect = self.image.get_rect(center = (544, 192))
        # player movement
        self.path = []
        self.pos = self.rect.center
        self.direction = pg.math.Vector2(0,0) # end position
        # find direction
        self.collision_rects = []
        self.speed = 2 # 4 is probably the highest this can go
        self.pathfinding = pathfinding
        self.moving = False
    
    def get_coord(self) -> Tuple:
        col = self.rect.centerx // TILESIZE
        row = self.rect.centery // TILESIZE
        return(col, row)
        
    def set_path(self, path): #this is called in Pathfinder to move the character and get the pathfinder coodinates
        self.path = path
        self.create_collision_rects()
        self.get_direction() 
    
    def create_collision_rects(self):
        if self.path:
            self.collision_rects = []
            for point in self.path:
                x = (point[0] * TILESIZE) + TILESIZE/2
                y = (point[1] * TILESIZE) + TILESIZE/2
                rect = pg.Rect((x - 2, y - 2),(4, 4)) # make this bigger if the player flies off
                self.collision_rects.append(rect)
    
    def get_direction(self):
        if self.collision_rects:
            start = pg.math.Vector2(self.pos)
            end = pg.math.Vector2(self.collision_rects[0].center)
            self.direction = (end-start).normalize()
        else:
            self.direction = pg.math.Vector2(0, 0)
            self.path = []
     
    def check_collisions(self):
        if self.collision_rects:
            for rect in self.collision_rects:
                if rect.collidepoint(self.pos):
                    del self.collision_rects[0]
                    self.get_direction()
                    self.moving = False
                else:
                    self.moving = True
        else:
            self.pathfinding.empty_path()

    def update(self):
        self.pos += self.direction * self.speed
        self.check_collisions()
        self.rect.center = self.pos


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.wallsprites 
        super().__init__(self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        # WALL ASSESTS HERE
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE  

class Floor(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.floorsprites
        super().__init__(self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.image.fill((10, 10, 10), self.rect.inflate(-1, -1))
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
