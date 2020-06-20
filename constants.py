FPS = 15
GRID_BLOCK_SIZE = 30
GRID_BLOCK_MARGIN = 5
COLUMN_COUNT = 10
ROW_COUNT = 20

# RGB
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
YELLOW  = (255, 255, 0)
CYAN    = (0, 255, 255)
ORANGE  = (255, 0, 165)
BLUE    = (0, 0, 255)
PURPLE  = (128, 0, 128)
GREEN   = (0, 255, 0)
RED     = (255, 0, 0)

# Tetris blocks
O_SHAPE = [[1,1],
           [1,1]]
I_SHAPE = [[1,1,1,1]]
L_SHAPE = [[1,0,0],
           [1,1,1]]
J_SHAPE = [[0,0,1],
           [1,1,1]]
T_SHAPE = [[1,1,1],
           [0,1,0]]
S_SHAPE = [[1,1,0],
           [0,1,1]]
Z_SHAPE = [[0,1,1],
           [1,1,0]]
templates = {'O': (O_SHAPE, YELLOW),
             'I': (I_SHAPE, CYAN),
             'L': (L_SHAPE, ORANGE),
             'J': (J_SHAPE, BLUE),
             'T': (T_SHAPE, PURPLE),
             'S': (S_SHAPE, GREEN),
             'Z': (Z_SHAPE, RED)    }
