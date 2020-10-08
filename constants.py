FPS = 60
# Grid block dimensions
SQUARE_SIZE = 30
SQUARE_MARGIN = 5
SQUARE = SQUARE_SIZE + SQUARE_MARGIN
ROW_COUNT = 20

# Tetris
COLUMN_COUNT = 10

# Pentris
COLUMN_COUNT_PENTRIS = 12

# Keep the HEADER and SIDE_SCREEN ints, especially when dividing by 2
HEADER = 50
SIDE_SCREEN = 400
HEIGHT = (SQUARE * ROW_COUNT + SQUARE_MARGIN) + HEADER

# Tetris
WIDTH = (SQUARE * COLUMN_COUNT + SQUARE_MARGIN) + SIDE_SCREEN
# Pentris
WIDTH_PENTRIS = (SQUARE * COLUMN_COUNT_PENTRIS + SQUARE_MARGIN) + SIDE_SCREEN

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
"""Tetris Blocks"""
# BLOCKS {template : (starting position, color)}
BLOCKS = {
            'O':([(0,4),(0,5),(1,4),(1,5)], YELLOW),
            'I':([(0,3),(0,4),(0,5),(0,6)], CYAN),
            'L':([(0,5),(1,3),(1,4),(1,5)], ORANGE),
            'J':([(0,3),(1,3),(1,4),(1,5)], BLUE),
            'T':([(0,4),(1,3),(1,4),(1,5)], PURPLE),
            'S':([(0,4),(0,5),(1,3),(1,4)], GREEN),
            'Z':([(0,3),(0,4),(1,4),(1,5)], RED),
            # Grey as placeholder. Gotta figure out the colors. Ugh.
            'pF':([(0,5),(1,4),(1,5),(1,6),(2,6)], GREY),
            'p7':([(0,5),(1,4),(1,5),(1,6),(2,4)], GREY),
            'pI':([(0,4),(0,5),(0,6),(0,7),(0,8)], CYAN),
            'pL':([(0,4),(0,5),(0,6),(0,7),(1,4)], ORANGE),
            'pJ':([(0,4),(0,5),(0,6),(0,7),(1,7)], BLUE),
            'pP':([(0,4),(0,5),(0,6),(1,5),(1,6)], GREY),
            'pQ':([(0,4),(0,5),(0,6),(1,4),(1,5)], GREY),
            'pN':([(0,4),(0,5),(0,6),(1,6),(1,7)], GREY),
            'p4':([(0,5),(0,6),(0,7),(1,4),(1,5)], GREY),
            'pV':([(0,4),(0,5),(0,6),(1,4),(2,4)], GREY),
            'pT':([(0,5),(1,5),(2,4),(2,5),(2,6)], PURPLE),
            'pU':([(0,4),(0,6),(1,4),(1,5),(1,6)], GREY),
            'pW':([(0,5),(0,6),(1,4),(1,5),(2,4)], GREY),
            'pX':([(0,5),(1,4),(1,5),(1,6),(2,5)], GREY),
            'pB':([(0,4),(0,5),(0,6),(0,7),(1,5)], GREY),
            'pD':([(0,4),(0,5),(0,6),(0,7),(1,6)], GREY),
            'pZ':([(0,6),(1,4),(1,5),(1,6),(2,4)], RED),
            'pS':([(0,4),(1,4),(1,5),(1,6),(2,6)], GREEN),
        }

SHAPES = {
            'O':[(1,1),(1,2),(2,1),(2,2)],
            'I':[(1,0),(1,1),(1,2),(1,3)],
            'L':[(0,2),(1,0),(1,1),(1,2)],
            'J':[(0,0),(1,0),(1,1),(1,2)],
            'T':[(0,1),(1,0),(1,1),(1,2)],
            'S':[(0,1),(0,2),(1,0),(1,1)],
            'Z':[(0,0),(0,1),(1,1),(1,2)],
            'pF':[(1,2),(2,1),(2,2),(2,3),(3,3)],
            'p7':[(1,2),(2,1),(2,2),(2,3),(3,1)],
            'pI':[(2,0),(2,1),(2,2),(2,3),(2,4)],
            'pL':[(2,1),(2,2),(2,3),(2,4),(3,1)],
            'pJ':[(2,0),(2,1),(2,2),(2,3),(3,3)],
            'pP':[(2,1),(2,2),(2,3),(3,2),(3,3)],
            'pQ':[(2,1),(2,2),(2,3),(3,1),(3,2)],
            'pN':[(2,0),(2,1),(2,2),(3,2),(3,3)],
            'p4':[(2,2),(2,3),(2,4),(2,1),(2,2)],
            'pV':[(2,2),(2,3),(2,4),(3,2),(4,2)],
            'pT':[(2,1),(2,2),(2,3),(3,2),(4,2)],
            'pU':[(2,1),(2,2),(2,3),(3,1),(3,3)],
            'pW':[(1,2),(1,3),(2,1),(2,2),(3,1)],
            'pX':[(1,2),(2,1),(2,2),(2,3),(3,2)],
            'pB':[(2,0),(2,1),(2,2),(2,3),(3,1)],
            'pD':[(2,1),(2,2),(2,3),(2,4),(3,3)],
            'pZ':[(1,3),(2,1),(2,2),(2,3),(3,1)],
            'pS':[(1,1),(2,1),(2,2),(2,3),(3,3)],
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
                 [(0,1),(1,0),(1,1),(2,0)]],
            'pF':[[(1,2),(2,1),(2,2),(2,3),(3,3)],
                  [(2,3),(1,2),(2,2),(3,2),(1,3)],
                  [(3,2),(2,3),(2,2),(1,2),(1,1)],
                  [(2,1),(3,2),(2,2),(2,1),(3,1)]],
            'p7':[[(1,2),(2,1),(2,2),(2,3),(3,1)],
                  [(2,3),(1,2),(2,2),(3,2),(1,1)],
                  [(3,2),(2,3),(2,2),(1,2),(1,3)],
                  [(2,1),(3,2),(2,2),(2,1),(3,3)]],
            'pI':[[(2,0),(2,1),(2,2),(2,3),(2,4)],
                  [(0,2),(1,2),(2,2),(3,2),(4,2)]],
            'pL':[[(2,1),(2,2),(2,3),(2,4),(3,1)],
            'pJ':[[(2,0),(2,1),(2,2),(2,3),(3,3)],
            'pP':[[(2,1),(2,2),(2,3),(3,2),(3,3)],
            'pQ':[[(2,1),(2,2),(2,3),(3,1),(3,2)],
            'pN':[[(2,0),(2,1),(2,2),(3,2),(3,3)],
            'p4':[[(2,2),(2,3),(2,4),(2,1),(2,2)],
            'pV':[[(2,2),(2,3),(2,4),(3,2),(4,2)],
            'pT':[[(2,1),(2,2),(2,3),(3,2),(4,2)],
            'pU':[[(2,1),(2,2),(2,3),(3,1),(3,3)],
            'pW':[[(1,2),(1,3),(2,1),(2,2),(3,1)],
            'pX':None,
            'pB':[[(2,0),(2,1),(2,2),(2,3),(3,1)],
            'pD':[[(2,1),(2,2),(2,3),(2,4),(3,3)],
            'pZ':[[(1,3),(2,1),(2,2),(2,3),(3,1)],
                  [(1,1),(3,2),(2,2),(1,2),(3,3)]],
            'pS':[[(1,1),(2,1),(2,2),(2,3),(3,3)],
                  [(1,3),(1,2),(2,2),(3,2),(3,1)]],
           }
