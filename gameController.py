import pygame as pg
import sys
import constants as c
from windowView import Window
from gameData import GameData

class Controller:
    def __init__ (self):
        self.gd = GameData()
        self.window = Window()

    """Game Execution"""
    def game_init (self):
        self.window.pygame_init()
        self.gd.grid_generate()
        self.block_load()

    def game_loop (self):
        self.game_init()
        while True:
            # Pygame loop speed
            self.gd.clock.tick(c.FPS)
            self.window.screen.fill(c.BLACK)

            # Update
            self.get_events()

            # Draw
            self.window.draw(self.gd)
            pg.display.flip()
        pg.quit()

    """Manual Changes"""
    # Left movement
    def move_left (self):
        # Erase the block's current position, fill in new position to left
        new_grid = self.gd.grid
        for i in range(4):
            row = self.gd.curr_block.curr_pos[i][0]
            col = self.gd.curr_block.curr_pos[i][1]
            self.gd.curr_block.curr_pos[i] = (row, col-1)
            new_grid[row][col] = c.GREY
            new_grid[row][col-1] = self.gd.curr_block.color
        return new_grid

    # Right movement
    def move_right (self):
        # Erase the block's current position, fill in new position to right
        # ***If I used range(4), I'd be erasing the left side of the block in
        # its new position.
        new_grid = self.gd.grid
        for i in range(3,-1,-1):
            row = self.gd.curr_block.curr_pos[i][0]
            col = self.gd.curr_block.curr_pos[i][1]
            self.gd.curr_block.curr_pos[i] = (row, col+1)
            new_grid[row][col] = c.GREY
            new_grid[row][col+1] = self.gd.curr_block.color
        return new_grid

    # Soft drop AKA "Down movement"
    def soft_drop (self):
        new_grid = self.gd.grid
        for i in range(3,-1,-1):
            row = self.gd.curr_block.curr_pos[i][0]
            col = self.gd.curr_block.curr_pos[i][1]
            self.gd.curr_block.curr_pos[i] = (row+1, col)
            new_grid[row][col] = c.GREY
            new_grid[row+1][col] = self.gd.curr_block.color
        return new_grid

    def hard_drop (self):
        new_grid = self.gd.grid
        curr_pos = self.gd.curr_block.curr_pos
        # Leftmost column limit for block
        leftmost = min(self.gd.curr_block.curr_pos, key=lambda x:x[1])[1]
        # Rightmost column limit for block
        rightmost = max(self.gd.curr_block.curr_pos, key=lambda x:x[1])[1]
        # Bottom of row of the block
        upper_lim = max(self.gd.curr_block.curr_pos, key=lambda x:x[0])[0]
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
            if grid_row == bottom and all(i == c.GREY for i in margin):
                dist = self.drop_dist(upper_lim, bottom)
            else:
                # If there's above the bottom
                if not all(j == c.GREY for j in margin):
                    # If it falls onto a flat surface
                    if c.GREY not in margin:
                        lower_lim = grid_row - 1
                        dist = self.drop_dist(upper_lim, lower_lim)
                        break
                    # If there's an opening
                    else:
                        grid_row_limit = {col:row[col]
                                        for col in range(leftmost, rightmost+1)}
                        min_dist = bottom
                        for k in range(4):
                            block_row = self.gd.curr_block.curr_pos[k][0]
                            block_col = self.gd.curr_block.curr_pos[k][1]
                            if grid_row_limit[block_col] == c.GREY:
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
            row = self.gd.curr_block.curr_pos[i][0]
            col = self.gd.curr_block.curr_pos[i][1]
            self.gd.curr_block.curr_pos[i] = (row+dist, col)
            new_grid[row][col] = c.GREY
            new_grid[row+dist][col] = self.gd.curr_block.color
        return new_grid

    # Follows super rotation system. If it collides, then don't rotate.
    def rotate_block (self):
        # O-block doesn't rotate
        # I-block, S-block, Z-block, L-block, J-block, T-block rotates 4 ways
        # Check collision before committing rotation
        if self.gd.curr_block.template == 'O':
            return self.gd.grid
        else:
            return

    """Automatic Changes"""
    # Load block into game where the top-left part of block is placed at (0,4)
    def block_load (self):
        self.gd.block_generate()

        # Check if we can still load block without overlapping
        if self.block_overlap():
            pg.quit()

    def block_fall (self):
        if self.gd.level_time / 1000 > 5:
            self.gd.level_time = 0
            if self.gd.level_time > 0.12:
                self.gd.level_time -= 0.005
        if self.gd.fall_time / 1000 > self.gd.fall_speed:
            fall_time = 0


    # Scoring based on original Nintendo scoring system
    def scoring (self, lines):
        n = self.gd.get_level()
        if lines == 1:
            self.gd.set_score(40 * (n + 1))
        elif lines == 2:
            self.gd.set_score(100 * (n + 1))
        elif lines == 3:
            self.gd.set_score(300 * (n + 1))
        elif lines == 4:
            self.gd.set_score(1200 * (n + 1))

    # Check if row(s) on grid is filled up.
    def check_line_clear (self):
        clear_counter = 0
        for i, row in enumerate(self.gd.grid):
            if all(color != c.GREY for color in row):
                self.remove_line(i)
                clear_counter += 1
        self.scoring(clear_counter)

    def remove_line (self, row_index):
        del self.gd.grid[row_index]
        self.gd.grid.insert(c.GREY, [c.GREY] * c.COLUMN_COUNT)

    def event_listener (self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and self.wall_collision("left"):
                    return self.move_left()
                elif event.key == pg.K_RIGHT and self.wall_collision("right"):
                    return self.move_right()
                elif event.key == pg.K_DOWN:
                    #self.gd.curr_block.dropped = True
                    return self.soft_drop()
                elif event.key == pg.K_ESCAPE:
                    pg.quit()
        return self.gd.grid

    def get_events (self):
        self.gd.set_grid(self.event_listener())
        if self.gd.curr_block.dropped:
            self.check_line_clear()
            self.block_load()

    """Conditions"""
    # Check collision between blocks. This should signal game over if True.
    def wall_collision (self, side):
        if side == "left":
            leftmost = min(self.gd.curr_block.curr_pos, key=lambda x:x[1])[1]
            if leftmost <= 0:
                return False
        else:
            rightmost = max(self.gd.curr_block.curr_pos, key=lambda x:x[1])[1]
            if rightmost >= 9:
                return False
        return True

    def block_collision (self):
        temp_grid = self.gd.grid
        for i in range(4):
            row = self.gd.curr_block.curr_pos[i][0]
            col = self.gd.curr_block.curr_pos[i][1]
            if temp_grid[row+1][col] != c.GREY:
                return True
        return False

    # If the block can't be loaded without overlapping a block, then game over.
    def block_overlap (self):
        for pos in self.gd.curr_block.start_pos:
            if self.gd.grid[pos[0]][pos[1]] != c.GREY:
                print("Game Over!")
                return True
            self.gd.grid[pos[0]][pos[1]] = self.gd.curr_block.color
        return False

    def drop_dist (self, row1, row2):
        # row1 = lowest row for block pos
        # row2 = highest row on grid that has a row filled in

        return row2 - row1
