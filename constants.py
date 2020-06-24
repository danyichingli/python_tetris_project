FPS = 15
# Grid block dimensions
GRID_BLOCK_SIZE = 30
GRID_BLOCK_MARGIN = 5
GRID_BLOCK = GRID_BLOCK_SIZE + GRID_BLOCK_MARGIN
COLUMN_COUNT = 10
ROW_COUNT = 20
WIDTH = GRID_BLOCK * COLUMN_COUNT + GRID_BLOCK_MARGIN
HEIGHT = GRID_BLOCK * ROW_COUNT + GRID_BLOCK_MARGIN

# RGB
BLACK   = (0, 0, 0)
GREY    = (47,79,79)
WHITE   = (255, 255, 255)
YELLOW  = (255, 255, 0)
CYAN    = (0, 255, 255)
ORANGE  = (255, 0, 165)
BLUE    = (0, 0, 255)
PURPLE  = (128, 0, 128)
GREEN   = (0, 255, 0)
RED     = (255, 0, 0)

# Tetris blocks
# O_SHAPE = [[1,1],
#            [1,1]]
# I_SHAPE = [[1,1,1,1]]
# L_SHAPE = [[1,0,0],
#            [1,1,1]]
# J_SHAPE = [[0,0,1],
#            [1,1,1]]
# T_SHAPE = [[1,1,1],
#            [0,1,0]]
# S_SHAPE = [[1,1,0],
#            [0,1,1]]
# Z_SHAPE = [[0,1,1],
#            [1,1,0]]
O_SHAPE = [(0,4),(0,5),(1,4),(1,5)]
I_SHAPE = [(0,3),(0,4),(0,5),(0,6)]
L_SHAPE = [(0,5),(1,3),(1,4),(1,5)]
J_SHAPE = [(0,3),(1,3),(1,4),(1,5)]
T_SHAPE = [(0,4),(1,3),(1,4),(1,5)]
S_SHAPE = [(0,4),(0,5),(1,3),(1,4)]
Z_SHAPE = [(0,3),(0,4),(1,4),(1,5)]
templates = {'O': (O_SHAPE, YELLOW, 1),
             'I': (I_SHAPE, CYAN, 2),
             'L': (L_SHAPE, ORANGE, 3),
             'J': (J_SHAPE, BLUE, 4),
             'T': (T_SHAPE, PURPLE, 5),
             'S': (S_SHAPE, GREEN, 6),
             'Z': (Z_SHAPE, RED, 7)    }
