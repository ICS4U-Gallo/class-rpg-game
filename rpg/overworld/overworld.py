import pygame
from config import *
from sprites import *
from cameramovement import *

class Overworld:
    def __init__(self):
        self.running = True
        self.new()
        self.load_data()
        self.abspos = (0, 0)
    
    def load_data(self):
        # This is just used to convert.txt file into proper format
        self.map_matrix = []
        with open('maps/map.txt', 'r' ) as f:
            for line in f:
                line_list = []
                for char in line:
                    if char != "\n":
                        line_list.append(char)
                self.map_matrix.append(line_list)
        
        self.mouseimage = pygame.image.load("assets/cursor.png")

    def event_loop(self, events:List[pygame.event.Event]) -> None:
        for event in events:
            self.mousepos = pygame.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN:
                if not self.player.moving:
                    self.getabspos(self.mousepos, self.player)
                    self.pathfinding.create_path(self.abspos, self)

    def new(self):
        pygame.mouse.set_visible(False)
        # initialize pathfinding, player
        self.pathfinding = Pathfinder(self.map_matrix)
        # creating sprite groups
        self.enemysprites = pygame.sprite.Group() # not actually in use right now
        self.wallsprites = pygame.sprite.Group()
        self.playersprite = pygame.sprite.GroupSingle()
        self.floorsprites = pygame.sprite.Group()
        self.player = Player(self, self.pathfinding)
        # Create wall objects based on .txt file
        for row_index, row_contents in enumerate(self.map_matrix):
            for col_index, cell in enumerate(row_contents):
                if cell == "0":
                    Wall(self, col_index, row_index)
                if cell == "1":
                    Floor(self, col_index, row_index)
        self.camera = Camera(self.map_matrix)
    
    def draw_active_cell(self) -> None: # draws the tile that the user is hovering over
        mouse_pos = pg.mouse.get_pos()
        x = mouse_pos[0] // 32
        y = mouse_pos[1] // 32
        pg.draw.rect(self.screen, (100, 100, 100), (x * TILESIZE, y * TILESIZE, TILESIZE - 1, TILESIZE - 1))

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill(BLACK)

        for sprite in self.floorsprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        if not self.player.moving:
            self.draw_active_cell()

        for sprite in self.wallsprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
    
        for sprite in self.playersprite:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        self.screen.blit(self.mouseimage, self.mousepos) # drawing cursor

    def getabspos(self, cursorpos: Tuple, target: Player) -> None:
        """
        This method gets the position of the cursor relative to the (0, 0) coordinate using the position of the player
        It gets the position of the player, then subtracts it by half the screen dimensions in order to get the coordinates 
        of the top-left corner, then adds the position of the mouse to the coordinates of the screen corner to get the 
        absolute location of the mouse click relative to (0, 0)
        """
        x = target.rect.x - int(WIDTH / 2)
        y = target.rect.y - int(HEIGHT / 2)
        absposx = x + cursorpos[0]
        absposy = y + cursorpos[1]
        self.abspos = (absposx, absposy)
        
    def update(self) -> None:
        self.playersprite.update()
        self.enemysprites.update()
        self.wallsprites.update()
        self.camera.update(self.player)
