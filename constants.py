FPS = 60
# Grid block dimensions
SQUARE_SIZE = 30
SQUARE_MARGIN = 5
SQUARE = SQUARE_SIZE + SQUARE_MARGIN
COLUMN_COUNT = 10
ROW_COUNT = 20
# Keep the HEADER and SIDE_SCREEN ints, especially when dividing by 2
HEADER = 50
SIDE_SCREEN = 400
WIDTH = (SQUARE * COLUMN_COUNT + SQUARE_MARGIN) + SIDE_SCREEN
HEIGHT = (SQUARE * ROW_COUNT + SQUARE_MARGIN) + HEADER

# RGB
BLACK   = (0, 0, 0)
GREY    = (47,79,79)
WHITE   = (255, 255, 255)
YELLOW  = (255, 255, 0)
CYAN    = (0, 255, 255)
ORANGE  = (255, 165, 0)
BLUE    = (0, 0, 255)
PURPLE  = (128, 0, 128)
GREEN   = (0, 255, 0)
RED     = (255, 0, 0)

# INSTRUCTIONS
INSTRUCTIONS = ["Move Left:                 Left Arrow",
                "Move Right:                Right Arrow",
                "Rotate Clockwise:          X",
                "Rotate Counter-Clockwise:  Z",
                "Hold:                      C",
                "Soft Drop:                 Down Arrow",
                "Hard Drop:                 Spacebar",
                "Pause/Unpause:             P",
                "Close Game:                ESC"]

# BLOCKS {template : (starting position, color)}
BLOCKS = {
            'O':([(0,4),(0,5),(1,4),(1,5)], YELLOW),
            'I':([(0,3),(0,4),(0,5),(0,6)], CYAN),
            'L':([(0,5),(1,3),(1,4),(1,5)], ORANGE),
            'J':([(0,3),(1,3),(1,4),(1,5)], BLUE),
            'T':([(0,4),(1,3),(1,4),(1,5)], PURPLE),
            'S':([(0,4),(0,5),(1,3),(1,4)], GREEN),
            'Z':([(0,3),(0,4),(1,4),(1,5)], RED)
        }

SHAPES = {
            'O':[(1,1),(1,2),(2,1),(2,2)],
            'I':[(1,0),(1,1),(1,2),(1,3)],
            'L':[(0,2),(1,0),(1,1),(1,2)],
            'J':[(0,0),(1,0),(1,1),(1,2)],
            'T':[(0,1),(1,0),(1,1),(1,2)],
            'S':[(0,1),(0,2),(1,0),(1,1)],
            'Z':[(0,0),(0,1),(1,1),(1,2)]
           }
# ROTATION {template : [pos0, pos1, pos2, pos3]}
ROTATION = {
            'O':None,
            'I':[[(1,0),(1,1),(1,2),(1,3)],
                 [(0,2),(1,2),(2,2),(3,2)],
                 [(2,3),(2,2),(2,1),(2,0)],
                 [(3,1),(2,1),(1,1),(0,1)]],
            'L':[[(0,2),(1,0),(1,1),(1,2)],
                 [(2,2),(0,1),(1,1),(2,1)],
                 [(2,0),(1,2),(1,1),(1,0)],
                 [(0,0),(2,1),(1,1),(0,1)]],
            'J':[[(0,0),(1,0),(1,1),(1,2)],
                 [(0,2),(0,1),(1,1),(2,1)],
                 [(2,2),(1,2),(1,1),(1,0)],
                 [(2,0),(2,1),(1,1),(0,1)]],
            'T':[[(0,1),(1,0),(1,1),(1,2)],
                 [(1,2),(0,1),(1,1),(2,1)],
                 [(2,1),(1,2),(1,1),(1,0)],
                 [(1,0),(2,1),(1,1),(0,1)]],
            'S':[[(0,1),(0,2),(1,0),(1,1)],
                 [(1,1),(0,1),(2,2),(1,2)],
                 [(1,1),(1,2),(2,0),(2,1)],
                 [(1,0),(0,0),(2,1),(1,1)]],
            'Z':[[(0,0),(0,1),(1,1),(1,2)],
                 [(0,2),(1,1),(1,2),(2,1)],
                 [(1,0),(1,1),(2,1),(2,2)],
                 [(0,1),(1,0),(1,1),(2,0)]]
           }
