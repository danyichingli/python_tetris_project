import pygame as pg
import constants as c
import random as rand
from View.gameView import GameView
from Controller.pauseController import PauseController
from BlockStuff.block import Block
from BlockStuff.blockType import BlockType as bt
from BlockStuff.square import Square
from copy import deepcopy
from math import floor

class GameController:
    def __init__ (self, gd):
        # input -> GameData class

        self.gd = gd
        self.gv = GameView()
        self.signal = gd.get_signal()

    # Main game loop
    def game_loop (self):
        # Game init

        # Column count dependent on game type
        if self.signal == "tetris":
            self.gd.col_count = 10
        elif self.signal == "pentris":
            self.gd.col_count = 12

        if self.gd.new_game:
            self.gd.grid_generate()
            self.next_block_load()
            self.gd.new_game = False
        while self.signal == "tetris" or self.signal == "pentris":
            # Pygame loop speed
            time = self.gd.clock.tick(c.FPS)
            # Update
            self.gv.screen.fill(c.BLACK)
            self.update()
            self.gv.draw_tetris_UI(self.gd)
            self.gv.draw_grid(self.gd)
            # Draw
            pg.display.flip()
        return self.signal

    """Manual Changes"""
    # Left/Right movement
    def move (self, direction):
        # Erase the block's current position, fill in new position to left/right
        new_grid = self.gd.get_grid()
        self.block_erase(self.gd.curr_block)
        for i in range(self.gd.curr_block.num_squares):
            row = self.gd.curr_block.curr_pos[i][0]
            col = self.gd.curr_block.curr_pos[i][1]
            if direction == "left":
                self.gd.curr_block.curr_pos[i] = (row, col-1)
                new_grid[row][col-1] = Square(self.gd.curr_block.get_color(), bt.PLAYER)
            else: # direction == "right"
                self.gd.curr_block.curr_pos[i] = (row, col+1)
                new_grid[row][col+1] = Square(self.gd.curr_block.get_color(), bt.PLAYER)

    # Soft drop AKA "Down movement"
    def soft_drop (self):
        new_grid = self.gd.grid
        type = self.gd.curr_block.get_type()
        self.block_erase(self.gd.curr_block)
        for i in range(self.gd.curr_block.num_squares):
            row = self.gd.curr_block.curr_pos[i][0]
            col = self.gd.curr_block.curr_pos[i][1]
            self.gd.curr_block.curr_pos[i] = (row+1, col)
            new_grid[row+1][col] = Square(self.gd.curr_block.get_color(), type)

    # Hard drop. Part of ghost block functionality. Drops block until it
    # collides with either the bottom or another block.
    def hard_drop (self, block):
        # input:
        # block -> Block Class
        new_grid = self.gd.grid
        if block == self.gd.curr_block:
            block.set_type(bt.BLOCK)
        while not self.block_collision_v(block):
            self.block_erase(block)
            for i in range(self.gd.curr_block.num_squares):
                row = block.curr_pos[i][0]
                col = block.curr_pos[i][1]
                block.curr_pos[i] = (row+1, col)
        for i in range(block.num_squares):
            row = block.curr_pos[i][0]
            col = block.curr_pos[i][1]
            new_grid[row][col] = Square(block.get_color(), block.get_type())

    # Follows super rotation system. If it collides, then don't rotate.
    def rotate(self, direction):
        curr_template = self.gd.curr_block.template
        # We don't need to rotate these.
        if curr_template == "O" or curr_template == "pX":
            return

        # Some variables
        num_squares = self.gd.curr_block.num_squares
        new_grid = self.gd.get_grid()
        curr_points = self.gd.curr_block.shape
        next_points = [0] * num_squares
        shift = num_squares - 1
        col_limit = self.gd.col_count

        # Shift the block after rotating about the 'origin'
        # If the num of squares is even, we need to accomodate some blocks' centers
        if self.gd.curr_block.num_squares % 2 == 0:
            leftmost    = min(self.gd.curr_block.shape,key=lambda x:x[1])[1]
            rightmost   = max(self.gd.curr_block.shape,key=lambda x:x[1])[1]
            topmost     = min(self.gd.curr_block.shape,key=lambda x:x[0])[0]
            botmost     = max(self.gd.curr_block.shape,key=lambda x:x[0])[0]
            shift = max(rightmost - leftmost, botmost - topmost)
        # If it's odd, we'll easily have a center point to pivot
        else:
            shift = self.gd.curr_block.num_squares - 1

        # Rotate the block in an N x N matrix, N being the num of squares
        for i in range(num_squares):
            row = curr_points[i][0]
            col = curr_points[i][1]
            if direction == "clockwise":
                next_row = col
                next_col = (row * -1) + shift
            else:
                next_row = (col * -1) + shift
                next_col = row
            next_points[i] = (next_row, next_col)

        # Get difference of points from rotation and translate onto board
        diff = [(next_points[i][0] - curr_points[i][0],
        next_points[i][1] - curr_points[i][1]) for i in range(num_squares)]

        # Check wall kick before committing rotation
        leftmost    = min(self.gd.curr_block.curr_pos,key=lambda x:x[1])[1]
        rightmost   = max(self.gd.curr_block.curr_pos,key=lambda x:x[1])[1]
        if (leftmost == 0 and not self.block_collision_h("right")
        and self.block_collision_r(diff)):
            self.wall_kick("left", diff)
        elif (rightmost == col_limit-1 and not self.block_collision_h("left")
        and self.block_collision_r(diff)):
            self.wall_kick("right", diff)

        # Check block collision before committing rotation
        if not self.block_collision_r(diff):
            # Rotation
            self.block_erase(self.gd.curr_block)
            for i in range(self.gd.curr_block.num_squares):
                row = self.gd.curr_block.curr_pos[i][0]
                col = self.gd.curr_block.curr_pos[i][1]
                next_row = row + diff[i][0]
                next_col = col + diff[i][1]
                self.gd.curr_block.curr_pos[i] = (next_row, next_col)
                new_grid[next_row][next_col] = Square(self.gd.curr_block.get_color(), bt.PLAYER)
            # Update the shape that will be represented in the N x N matrix next time
            self.gd.curr_block.shape = next_points


    """Automatic Changes"""

    # Loads the next block. If it overlaps with a block type square then player
    # returns to menu.
    def next_block_load (self):
        self.next_block_generate()

        # Check if we can still load block without overlapping
        if self.block_overlap():
            self.signal = "main_menu"
            return

    # Generates the next block as current block and a new random block as next
    # block. If there is no next block, current block is generated as a new
    # random block.
    def next_block_generate (self):
        block_list = []
        if self.signal == "tetris":
            block_list = ['O', 'I', 'L', 'J', 'T', 'S', 'Z']
        elif self.signal == "pentris":
            block_list = ['pF','p7','pI','pL','pJ','pP','pQ','pN','p4',
                          'pV','pT','pU','pW','pX','pB','pD','pZ','pS']
        # Current block
        if not self.gd.curr_block:
            self.gd.set_curr_block(Block(rand.choice(block_list), bt.BLOCK).clone())
        else:
            self.gd.set_curr_block(Block(self.gd.next_block.template, bt.PLAYER).clone())
        self.ghost_block_generate()
        # Next block
        self.gd.set_next_block(Block(rand.choice(block_list), bt.BLOCK).clone())

    # Ghost block is generated as a clone of the current block with same
    # attributes except for its color and type. It will immediately hard drop to
    # act as a predictor for the current block's landing.
    def ghost_block_generate (self):
        curr_block = self.gd.curr_block
        if self.gd.ghost_block:
            self.block_erase(self.gd.ghost_block)
        self.gd.ghost_block = Block(curr_block.template, bt.GHOST).clone()
        self.gd.ghost_block.set_color(c.WHITE)
        self.gd.ghost_block.set_pos(deepcopy(curr_block.get_pos()))
        self.hard_drop(self.gd.ghost_block)
        if self.gd.ghost_block.get_pos() == curr_block.get_pos():
            for i in range(self.gd.curr_block.num_squares):
                row = curr_block.curr_pos[i][0]
                col = curr_block.curr_pos[i][1]
                self.gd.grid[row][col] = Square(curr_block.get_color(), bt.PLAYER)

    # Loads the hold block. If it overlaps with a block type square then player
    # returns to menu.
    def hold_block_load (self):
        self.hold_block_generate()

        # Check if we can still load block without overlapping
        if self.block_overlap():
            self.gd.running = False

    # Generates the hold block as current block and current block as hold block.
    # If there is no hold block, current block is still generated as current
    # block but current block is now next block.
    def hold_block_generate (self):
        # First time holding a block
        if self.gd.hold_block == None:
            self.gd.set_hold_block(Block(self.gd.curr_block.template, bt.BLOCK).clone())
            self.block_erase(self.gd.curr_block)
            self.next_block_generate()
        # Swap current block with hold block
        else:
            temp_hold_block = self.gd.get_hold_block()
            self.gd.set_hold_block(Block(self.gd.curr_block.template, bt.BLOCK).clone())
            self.block_erase(self.gd.curr_block)
            self.gd.set_curr_block(temp_hold_block)

    # Block fall speed increases after every 5 levels until level 20
    def block_fall (self):
        curr_level = self.gd.get_level()
        fall_level = self.gd.get_fall_level()
        fall_time = self.gd.get_fall_time()
        fall_delay = self.gd.get_fall_delay()

        self.gd.set_fall_time(fall_time + 10)
        if curr_level == fall_level and fall_level != 20:
            self.gd.set_fall_level(fall_level + 5)
            self.gd.set_fall_delay(fall_delay / 2)
        if not self.block_collision_v(self.gd.curr_block) and fall_time % fall_delay == 0:
            return self.soft_drop()
        return self.gd.grid

    # Allows a block leaning against a wall to rotate when it should not
    def wall_kick (self, wall, diff):
        counter = 0
        direction = ""
        undo = ""

        if wall == "left":
            direction = "right"
            undo = "left"
        else:
            direction = "left"
            undo = "right"

        for i in range(floor(self.gd.curr_block.num_squares / 2)):
            if not self.block_collision_wk(diff):
                break
            self.move(direction)
            counter += 1

        # Undo wall kick
        if self.block_collision_r(diff):
            for i in range(counter):
                self.move(undo)

    # Scoring based on original Nintendo scoring system
    def scoring (self, lines):
        # input:
        # lines -> int
        n = self.gd.get_level()
        if lines == 1:
            self.gd.set_score(40 * (n + 1))
        elif lines == 2:
            self.gd.set_score(100 * (n + 1))
        elif lines == 3:
            self.gd.set_score(300 * (n + 1))
        elif lines == 4:
            self.gd.set_score(1200 * (n + 1))

    # Check if row(s) on grid is filled up with block type squares
    def check_line_clear (self):
        clear_counter = 0
        for i, row in enumerate(self.gd.grid):
            if all(square.get_type() == bt.BLOCK for square in row):
                self.remove_line(i)
                clear_counter += 1
        self.scoring(clear_counter)
        self.gd.set_lines_cleared(self.gd.get_lines_cleared() + clear_counter)
        if self.gd.get_lines_cleared() >= 10:
            self.gd.set_level(self.gd.get_level() + 1)
            self.gd.set_lines_cleared(self.gd.get_lines_cleared() % 10)

    # Remove row of block squares and replace with an empty row at the top
    def remove_line (self, row_index):
        # input:
        # row_index -> int

        del self.gd.grid[row_index]
        self.gd.grid.insert(0, [Square(c.GREY, bt.EMPTY)] * self.gd.col_count)

    # Listen to events
    def game_event_listener (self):
        # Soft drop (key hold)
        if pg.key.get_pressed()[pg.K_DOWN] and not self.block_collision_v(self.gd.curr_block):
            self.soft_drop()
        for event in pg.event.get():
            # Close window
            if event.type == pg.QUIT:
                self.signal = "quit"
            elif event.type == pg.KEYDOWN:
                # Move left (key press)
                if event.key in [pg.K_LEFT, pg.K_a] and not self.block_collision_h("left"):
                    self.move("left")
                    self.ghost_block_generate()
                # Move right (key press)
                elif event.key in [pg.K_RIGHT, pg.K_d] and not self.block_collision_h("right"):
                    self.move("right")
                    self.ghost_block_generate()
                # Hard drop (key press)
                elif event.key == pg.K_SPACE and not self.block_collision_v(self.gd.curr_block):
                    self.hard_drop(self.gd.curr_block)
                # Rotate clockwise (key press)
                elif event.key == pg.K_x:
                    self.rotate("clockwise")
                    self.ghost_block_generate()
                # Rotate counter-clockwise (key press)
                elif event.key == pg.K_z:
                    self.rotate("counter clockwise")
                    self.ghost_block_generate()
                # Hold block (key press)
                elif event.key == pg.K_c:
                    self.hold_block_load()
                    self.ghost_block_generate()
                # Pause/Unpause (key press)
                elif event.key == pg.K_p:
                    self.signal = "pause"
                # Close window (key press)
                elif event.key == pg.K_ESCAPE:
                    self.signal = "quit"
        self.block_fall()

    # Update the game to keep it going. Most of the actions keep track of the
    # current block's changes. If it's dropped then check if there's any lines
    # to be cleared and then change the current block.
    def update (self):
        self.game_event_listener()
        if self.gd.curr_block.dropped:
            self.check_line_clear()
            self.next_block_load()

    """Conditions"""
    # Check block collision horizontally
    def block_collision_h (self, side):
        temp_grid = self.gd.get_grid()
        for i in range(self.gd.curr_block.num_squares):
            col_limit = self.gd.col_count - 1
            pos = self.gd.curr_block.curr_pos
            row = pos[i][0]
            col = pos[i][1]
            if side == "left":
                if (col == 0 or ((row,col-1) not in pos
                and temp_grid[row][col-1].get_type() == bt.BLOCK)):
                    return True
            else: # if side == "right"
                if (col == col_limit or ((row,col+1) not in pos
                and temp_grid[row][col+1].get_type() == bt.BLOCK)):
                    return True
        return False

    # Check block collision verically, associated with ghost block behavior
    def block_collision_v (self, block):
        temp_grid = self.gd.get_grid()
        for i in range(self.gd.curr_block.num_squares):
            pos = block.curr_pos
            row = pos[i][0]
            col = pos[i][1]
            if (row == 19 or ((row+1,col) not in pos
            and temp_grid[row+1][col].get_type() == bt.BLOCK)):
                self.gd.curr_block.set_type(bt.BLOCK)
                block.dropped = True
                return True
        return False

    # Check block collision before rotation
    def block_collision_r (self, diff):
        col_limit = self.gd.col_count - 1
        temp_grid = self.gd.get_grid()
        for i in range(self.gd.curr_block.num_squares):
            pos = self.gd.curr_block.curr_pos
            row = pos[i][0] + diff[i][0]
            col = pos[i][1] + diff[i][1]
            if row < 0 or row > 19 or col < 0 or col > col_limit:
                return True
            if (row,col) not in pos and temp_grid[row][col].get_type() == bt.BLOCK:
                return True
        return False

    def block_collision_wk(self, diff):
        col_limit = self.gd.col_count - 1
        for i in range(self.gd.curr_block.num_squares):
            pos = self.gd.curr_block.curr_pos
            row = pos[i][0] + diff[i][0]
            col = pos[i][1] + diff[i][1]
            if row < 0 or row > 19 or col < 0 or col > col_limit:
                return True
        return False

    # If the block can't be loaded without overlapping a block, then game over.
    def block_overlap (self):
        temp_grid = self.gd.get_grid()
        for pos in self.gd.curr_block.start_pos:
            if (temp_grid[pos[0]][pos[1]].get_type() == bt.PLAYER):
                print("Game Over!")
                return True
            temp_grid[pos[0]][pos[1]] = Square(self.gd.curr_block.get_color(), bt.PLAYER)
        return False

    """Miscellaneous"""
    # Erase block from grid to avoid confusion when making changes
    def block_erase (self, block):
        new_grid = self.gd.grid
        for i in range(self.gd.curr_block.num_squares):
            row = block.curr_pos[i][0]
            col = block.curr_pos[i][1]
            if block.get_type() == bt.GHOST:
                if (new_grid[row][col].get_type() != bt.BLOCK
                and new_grid[row][col].get_type() != bt.PLAYER):
                    new_grid[row][col] = Square(c.GREY, bt.EMPTY)
            else:
                new_grid[row][col] = Square(c.GREY, bt.EMPTY)
        return new_grid
