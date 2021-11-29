from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
from config import TILESIZE
from typing import Tuple, List

# Pathfinding is very resource hungry, so try not to use it over long distances
class Pathfinder:
    def __init__(self,matrix: List):
        self.matrix = matrix
        self.grid = Grid(matrix = matrix)
        # pathfinding
        self.path = []

    def create_path(self, pos: Tuple, game) -> None: 
        self.pos = pos
        self.player = game.player
        #start
        start_x, start_y = self.player.get_coord()
        start = self.grid.node(start_x, start_y)
        #end
        end_x, end_y = self.pos[0] // TILESIZE, self.pos[1] // TILESIZE
        end = self.grid.node(end_x, end_y)
        # path
        finder = AStarFinder(diagonal_movement = DiagonalMovement.always) # we want diagonal movement
        self.path,_ = finder.find_path(start, end, self.grid)
        self.player.set_path(self.path)
        self.grid.cleanup()
    
    def empty_path(self): # clears the path list
        self.path = [] # not necessary but cleans up the code
