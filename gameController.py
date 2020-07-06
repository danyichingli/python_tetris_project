import pygame as pg
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
        #pg.mixer.init(44100, -16,2,2048)

    def game_loop (self):
        self.game_init()
        clock = self.gd.clock
        while True:
            # Pygame loop speed
            time = clock.tick(c.FPS)
            self.gd.fall_time += time

            # Update
            self.window.screen.fill(c.BLACK)
            self.update()

            # Draw
            self.window.draw(self.gd)
            pg.display.flip()
        pg.quit()

    """Manual Changes"""
    # Left movement
    def move_left (self):
        # Erase the block's current position, fill in new position to left
        new_grid = self.gd.get_grid()
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
        new_grid = self.gd.get_grid()
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
        while not self.block_collision_v():
            for i in range(3,-1,-1):
                row = self.gd.curr_block.curr_pos[i][0]
                col = self.gd.curr_block.curr_pos[i][1]
                self.gd.curr_block.curr_pos[i] = (row+1, col)
                new_grid[row][col] = c.GREY
                new_grid[row+1][col] = self.gd.curr_block.color
        self.gd.curr_block.dropped = True
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
        if self.gd.fall_time / 1000 > self.gd.fall_speed:
            self.gd.fall_time = 0
            if not self.block_collision_v():
                return self.soft_drop()
        return self.gd.grid


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
        self.gd.grid.insert(0, [c.GREY] * c.COLUMN_COUNT)

    def event_listener (self):
        # Soft drop (key hold)
        if pg.key.get_pressed()[pg.K_DOWN] and not self.block_collision_v():
            return self.soft_drop()
        for event in pg.event.get():
            # Close window
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN:
                # Move left (key press)
                if event.key == pg.K_LEFT and not self.block_collision_h("left"):
                    return self.move_left()
                # Move right (key press)
                elif event.key == pg.K_RIGHT and not self.block_collision_h("right"):
                    return self.move_right()
                # Hard drop (key press)
                elif event.key == pg.K_SPACE and not self.block_collision_v():
                    return self.hard_drop()
                # Close window (key press)
                elif event.key == pg.K_ESCAPE:
                    pg.quit()
        return self.block_fall()

    def update (self):
        self.event_listener()
        if self.gd.curr_block.dropped:
            self.check_line_clear()
            self.block_load()

    """Conditions"""
    # Check block collision horizontally
    def block_collision_h (self, side):
        temp_grid = self.gd.get_grid()
        if side == "left":
            for i in range(4):
                pos = self.gd.curr_block.curr_pos
                row = pos[i][0]
                col = pos[i][1]
                if (col == 0 or
                        ((row,col-1) not in pos and temp_grid[row][col-1] != c.GREY)):
                    return True
        else:
            for i in range(4):
                pos = self.gd.curr_block.curr_pos
                row = pos[i][0]
                col = pos[i][1]
                if (col == 9 or
                        ((row,col+1) not in pos and temp_grid[row][col+1] != c.GREY)):
                    return True
        return False

    # Check block collision verically
    def block_collision_v (self):
        temp_grid = self.gd.get_grid()
        for i in range(4):
            pos = self.gd.curr_block.curr_pos
            row = pos[i][0]
            col = pos[i][1]
            # Only focus on the positions with row that's downmost
            if (row == 19 or
                    ((row+1,col) not in pos and temp_grid[row+1][col] != c.GREY)):
                self.gd.curr_block.dropped = True
                return True
        return False

    # If the block can't be loaded without overlapping a block, then game over.
    def block_overlap (self):
        temp_grid = self.gd.get_grid()
        for pos in self.gd.curr_block.start_pos:
            if temp_grid[pos[0]][pos[1]] != c.GREY:
                print("Game Over!")
                return True
            temp_grid[pos[0]][pos[1]] = self.gd.curr_block.color
        return False

    """Miscellaneous"""
    def play_sound (self, sound):
        return
