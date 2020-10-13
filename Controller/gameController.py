import pygame as pg
import constants as c
import random as rand
from View.gameView import GameView
from Controller.pauseController import PauseController
from BlockStuff.block import Block
from BlockStuff.blockType import BlockType as bt
from BlockStuff.square import Square
from copy import deepcopy
from numpy import rot90, array

class GameController:
    def __init__ (self, gd):
        # input -> GameData class

        self.gd = gd
        self.gv = GameView()
        self.signal = gd.get_signal()

    # Main game loop
    def game_loop (self):
        # Game init
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
                new_grid[row][col-1] = Square(self.gd.curr_block.get_color(), bt.BLOCK)
            else: # direction == "right"
                self.gd.curr_block.curr_pos[i] = (row, col+1)
                new_grid[row][col+1] = Square(self.gd.curr_block.get_color(), bt.BLOCK)

    # Soft drop AKA "Down movement"
    def soft_drop (self):
        new_grid = self.gd.grid
        self.block_erase(self.gd.curr_block)
        for i in range(self.gd.curr_block.num_squares):
            row = self.gd.curr_block.curr_pos[i][0]
            col = self.gd.curr_block.curr_pos[i][1]
            self.gd.curr_block.curr_pos[i] = (row+1, col)
            new_grid[row+1][col] = Square(self.gd.curr_block.get_color(), bt.BLOCK)

    # Hard drop. Part of ghost block functionality. Drops block until it
    # collides with either the bottom or another block.
    def hard_drop (self, block):
        # input:
        # block -> Block Class
        new_grid = self.gd.grid
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
    def rotateOLD (self, direction):
        # input:
        # direction -> str

        # O-block doesn't need to rotate
        if self.gd.curr_block.rotation_states == None:
            return self.gd.grid
        # I-block, S-block, Z-block, L-block, J-block, T-block rotates 4 ways
        else:
            new_grid = self.gd.get_grid()
            curr_state = self.gd.curr_block.get_curr_state()
            next_state = curr_state
            diff = []
            if direction == "clockwise":
                if curr_state == 3:
                    next_state = 0
                else:
                    next_state += 1
            else: # direction == "counter clockwise"
                if curr_state == 0:
                    next_state = 3
                else:
                    next_state -= 1
            curr_points = self.gd.curr_block.get_rotation_states()[curr_state]
            next_points = self.gd.curr_block.get_rotation_states()[next_state]
            # Find the difference to transition from current to next state
            if direction == "clockwise":
                diff = self.find_diff(direction, curr_points, next_points)
            else: # direction == "counter clockwise"
                diff = self.find_diff(direction, next_points, curr_points)
            # Check collision before committing rotation
            leftmost = min(self.gd.curr_block.curr_pos,key=lambda x:x[1])[1]
            rightmost = max(self.gd.curr_block.curr_pos,key=lambda x:x[1])[1]

            # Wall kick if:
            # I-block, current state is 1 or 3, and near either wall
            # Current state is 1 and against left wall
            # Current state is 3 and against right wall
            if self.gd.curr_block.template == 'I':
                if ((curr_state == 1 or curr_state == 3) and leftmost <= 1 and
                not self.block_collision_h("right")):
                    self.wall_kick_i("left", diff, curr_state)
                elif ((curr_state == 1 or curr_state == 3) and rightmost >= 8 and
                not self.block_collision_h("left")):
                    self.wall_kick_i("right", diff, curr_state)
            else:
                if (curr_state == 1 and leftmost == 0 and
                not self.block_collision_h("right")):
                    self.wall_kick("left", diff)
                elif (curr_state == 3 and rightmost == 9 and
                not self.block_collision_h("left")):
                    self.wall_kick("right", diff)

            if not self.block_collision_r(diff):
                # Rotation
                self.block_erase(self.gd.curr_block)
                for i in range(self.gd.curr_block.num_squares):
                    row = self.gd.curr_block.curr_pos[i][0]
                    col = self.gd.curr_block.curr_pos[i][1]
                    next_row = row + diff[i][0]
                    next_col = col + diff[i][1]
                    self.gd.curr_block.curr_pos[i] = (next_row, next_col)
                    new_grid[next_row][next_col] = Square(self.gd.curr_block.get_color(), bt.BLOCK)
                self.gd.curr_block.set_curr_state(next_state)

    def rotate (self, direction):
        if self.gd.curr_block.template == "I" or self.gd.curr_block.template == "pX":
            return
        # Record everything before the rotation
        num_squares = self.gd.curr_block.num_squares
        temp = [[-1] * num_squares for i in range(num_squares)]
        curr_points = []
        next_points = [-1] * num_squares
        curr_state = self.gd.curr_block.get_curr_state()
        diff = []
        leftmost = min(self.gd.curr_block.curr_pos,key=lambda x:x[1])[1]
        rightmost = max(self.gd.curr_block.curr_pos,key=lambda x:x[1])[1]
        new_grid = self.gd.get_grid()

        for num, (row, col) in enumerate(self.gd.curr_block.shape):
            temp[row][col] = num
            curr_points.append((row, col))

        print(array(temp))

        # Rotate the shape
        if direction == "clockwise":
            if curr_state == 3:
                self.gd.curr_block.set_curr_state(0)
            else:
                self.gd.curr_block.set_curr_state(curr_state + 1)
            temp = rot90(temp, 3)
        else:
            if curr_state == 0:
                self.gd.curr_block.set_curr_state(3)
            else:
                self.gd.curr_block.set_curr_state(curr_state - 1)
            temp = rot90(temp)
        print(temp)
        # Get the position of the points after rotation
        for i, row in enumerate(temp):
            for j, num in enumerate(row):
                if num > -1:
                    next_points[num] = (i, j)
        if direction == "clockwise":
            diff = self.find_diff(direction, curr_points, next_points)
        else:
            diff = self.find_diff(direction, next_points, curr_points)

        if not self.block_collision_r(diff):
            # Rotation
            self.block_erase(self.gd.curr_block)
            for i in range(self.gd.curr_block.num_squares):
                row = self.gd.curr_block.curr_pos[i][0]
                col = self.gd.curr_block.curr_pos[i][1]
                next_row = row + diff[i][0]
                next_col = col + diff[i][1]
                self.gd.curr_block.curr_pos[i] = (next_row, next_col)
                new_grid[next_row][next_col] = Square(self.gd.curr_block.get_color(), bt.BLOCK)
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
            #self.gd.set_curr_block(Block(rand.choice(block_list), bt.BLOCK).clone())
            self.gd.set_curr_block(Block('pU', bt.BLOCK).clone())
        else:
            self.gd.set_curr_block(Block(self.gd.next_block.template, bt.BLOCK).clone())
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
            for i in range(4):
                row = curr_block.curr_pos[i][0]
                col = curr_block.curr_pos[i][1]
                self.gd.grid[row][col] = Square(curr_block.get_color(), bt.BLOCK)

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
        # input:
        # wall -> str
        # diff, curr_state -> int

        if wall == "left":
            self.move("right")
            if self.block_collision_r(diff):
                self.move("left")
        else:
            self.move("left")
            if self.block_collision_r(diff):
                self.move("right")

    # I-block is a unique case for wall kicking
    def wall_kick_i (self, wall, diff, curr_state):
        # input:
        # wall -> str
        # diff, curr_state -> int
        if wall == "left":
            if curr_state == 3:
                self.wall_kick(wall, diff)
            else:
                self.move("right")
                self.move("right")
                if self.block_collision_r(diff):
                    self.move("left")
                    self.move("left")
        else:
            if curr_state == 1:
                self.wall_kick(wall, diff)
            else:
                self.move("left")
                self.move("left")
                if self.block_collision_r(diff):
                    self.move("right")
                    self.move("right")

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
        self.gd.grid.insert(0, [Square(c.GREY, bt.EMPTY)] * c.COLUMN_COUNT)

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
                if event.key == pg.K_LEFT and not self.block_collision_h("left"):
                    self.move("left")
                    self.ghost_block_generate()
                # Move right (key press)
                elif event.key == pg.K_RIGHT and not self.block_collision_h("right"):
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
            pos = self.gd.curr_block.curr_pos
            row = pos[i][0]
            col = pos[i][1]
            if side == "left":
                if (col == 0 or ((row,col-1) not in pos
                and temp_grid[row][col-1].get_type() == bt.BLOCK)):
                    return True
            else: # if side == "right"
                if (col == 9 or ((row,col+1) not in pos
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
                block.dropped = True
                return True
        return False

    # Check block collision before rotation
    def block_collision_r (self, diff):
        if self.gd.signal == "tetris":
            col_limit = 9
        elif self.gd.signal == "pentris":
            col_limit = 11
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

    # If the block can't be loaded without overlapping a block, then game over.
    def block_overlap (self):
        temp_grid = self.gd.get_grid()
        for pos in self.gd.curr_block.start_pos:
            if (temp_grid[pos[0]][pos[1]].get_type() == bt.BLOCK):
                print("Game Over!")
                return True
            temp_grid[pos[0]][pos[1]] = Square(self.gd.curr_block.get_color(), bt.BLOCK)
        return False

    """Miscellaneous"""
    # Erase block from grid to avoid confusion when making changes
    def block_erase (self, block):
        new_grid = self.gd.grid
        for i in range(self.gd.curr_block.num_squares):
            row = block.curr_pos[i][0]
            col = block.curr_pos[i][1]
            if block.get_type() == bt.GHOST:
                if new_grid[row][col].get_type() != bt.BLOCK:
                    new_grid[row][col] = Square(c.GREY, bt.EMPTY)
            else:
                new_grid[row][col] = Square(c.GREY, bt.EMPTY)
        return new_grid

    # Difference in positions of squares to get from a,b,c,d to a',b',c',d'.
    # Used for rotate method.
    def find_diff (self, direction, curr_points, next_points):
        result = []
        for i in range(self.gd.curr_block.num_squares):
            curr_row = curr_points[i][0]
            curr_col = curr_points[i][1]
            next_row = next_points[i][0]
            next_col = next_points[i][1]
            if direction == "clockwise":
                result.append((next_row - curr_row, next_col - curr_col))
            else:
                result.append((curr_row - next_row, curr_col - next_col))
        return result
