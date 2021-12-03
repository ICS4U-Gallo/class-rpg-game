from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
from config import TILESIZE
from typing import Tuple, List


class Pathfinder:
    def __init__(self,matrix: List, target):
        self.matrix = matrix
        self.grid = Grid(matrix = matrix)
        # pathfinding
        self.path = []
        self.target = target

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
        finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
        self.path,_ = finder.find_path(start, end, self.grid)
        self.target.set_path(self.path)
        self.grid.cleanup()
    
    def empty_path(self):
        self.path = []
