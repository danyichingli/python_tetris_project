import pygame as pg
import sys
import constants as c
from keyboardListener import KeyboardListener

class Controller:
    def __init__ (self, grid, block):
        self.grid = grid
        self.block = block

    # Left movement
    def move_left(self):
        # Erase the block's current position, fill in new position to left
        new_grid = self.grid
        for i in range(4):
            row = self.block.pos[i][0]
            col = self.block.pos[i][1]
            self.block.pos[i] = (row, col-1)
            new_grid[row][col] = 0
            new_grid[row][col-1] = self.block.val
        return new_grid
    # Right movement
    def move_right(self):
        # Erase the block's current position, fill in new position to right
        # ***If I used range(4), I'd be erasing the left side of the block in
        # its new position.
        new_grid = self.grid
        for i in range(3,-1,-1):
            row = self.block.pos[i][0]
            col = self.block.pos[i][1]
            self.block.pos[i] = (row, col+1)
            new_grid[row][col] = 0
            new_grid[row][col+1] = self.block.val
        return new_grid

    # TODO: Drop
    def drop_block (self):
        new_grid = self.grid
        curr_pos = self.block.pos
        # Leftmost column limit for block
        leftmost = min(self.block.pos, key=lambda x:x[1])[1]
        # Rightmost column limit for block
        rightmost = max(self.block.pos, key=lambda x:x[1])[1]
        # Bottom of row of the block
        upper_lim = max(self.block.pos, key=lambda x:x[0])[0]
        # First row down on the grid that's not filled with 0's
        lower_lim = 0
        # Last row on the grid
        bottom = c.ROW_COUNT-1
        # Distance from block to collision
        dist = 0
        for grid_row in range(upper_lim+1, bottom+1):
            row = new_grid[grid_row]
            margin = row[leftmost:rightmost+1]
            # If the block can drop straight to the bottom
            if grid_row == bottom and all(i == 0 for i in margin):
                dist = self.drop_dist(upper_lim, bottom)
            else:
                # If there's above the bottom
                if not all(j == 0 for j in margin):
                    # If it falls onto a flat surface
                    if 0 not in margin:
                        lower_lim = grid_row - 1
                        dist = self.drop_dist(upper_lim, lower_lim)
                        break
                    # If there's an opening
                    else:
                        grid_row_limit = {col:row[col]
                                        for col in range(leftmost, rightmost+1)}
                        min_dist = bottom
                        for k in range(4):
                            block_row = self.block.pos[k][0]
                            block_col = self.block.pos[k][1]
                            if grid_row_limit[block_col] == 0:
                                temp_dist = self.drop_dist(block_row, grid_row)
                                if temp_dist < min_dist:
                                    min_dist = temp_dist
                            else:
                                temp_dist = self.drop_dist(block_row, grid_row-1)
                                if temp_dist < min_dist:
                                    min_dist = temp_dist
                        dist = min_dist
                        break
        for i in range(4):
            row = self.block.pos[i][0]
            col = self.block.pos[i][1]
            self.block.pos[i] = (row+dist, col)
            new_grid[row][col] = 0
            new_grid[row+dist][col] = self.block.val
        return new_grid

    # TODO: Rotate
    # Rotate block counter or clockwise. If it collides, then don't rotate.
    def rotate_block ():
        return

    def event_listener (self):
        event = KeyboardListener().listener()
        if event == "quit":
            pg.quit()
        elif event == "left" and self.wall_collision("left"):
            return self.move_left()
        elif event == "right" and self.wall_collision("right"):
            return self.move_right()
        elif event == "down":
            self.block.dropped = True
            return self.drop_block()
        return self.grid

    # Check collision between blocks. This should signal game over if True.
    def wall_collision (self, side):
        if side == "left":
            leftmost = min(self.block.pos, key=lambda x:x[1])[1]
            if leftmost <= 0:
                return False
        else:
            rightmost = max(self.block.pos, key=lambda x:x[1])[1]
            if rightmost >= 9:
                return False
        return True

    def block_collision (self):
        temp_grid = self.grid
        for i in range(4):
            row = self.block.pos[i][0]
            col = self.block.pos[i][1]
            if temp_grid[row+1][col] > 0:
                return True
        return False

    def drop_dist (self, row1, row2):
        # row1 = lowest row for block pos
        # row2 = highest row on grid that has a row filled in

        return row2 - row1
