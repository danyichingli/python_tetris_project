FPS = 60
# Grid block dimensions
SQUARE_SIZE = 30
SQUARE_MARGIN = 5
SQUARE = SQUARE_SIZE + SQUARE_MARGIN
COLUMN_COUNT = 10
ROW_COUNT = 20
WIDTH = SQUARE * COLUMN_COUNT + SQUARE_MARGIN
HEIGHT = SQUARE * ROW_COUNT + SQUARE_MARGIN

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

# BLOCKS {template : (starting position, color)}
BLOCKS = {
            'O':([(0,4),(0,5),(1,4),(1,5)], YELLOW),
            'I':([(0,3),(0,4),(0,5),(0,6)], CYAN),
            'L':([(0,3),(1,3),(1,4),(1,5)], ORANGE),
            'J':([(0,5),(1,3),(1,4),(1,5)], BLUE),
            'T':([(0,4),(1,3),(1,4),(1,5)], PURPLE),
            'S':([(0,4),(0,5),(1,3),(1,4)], RED),
            'Z':([(0,3),(0,4),(1,4),(1,5)], GREEN)
        }
