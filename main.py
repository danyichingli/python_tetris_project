from tetris import Tetris

def main ():
    tetris = Tetris()
    tetris.run()
    # clock =  pg.time.Clock()
    # done = False
    # # Window size based on grid
    # grid_block = GRID_BLOCK_SIZE + GRID_BLOCK_MARGIN
    # width = grid_block * COLUMN_COUNT + GRID_BLOCK_MARGIN
    # height = grid_block * ROW_COUNT + GRID_BLOCK_MARGIN
    # screen = pg.display.set_mode((width, height))
    # block_queue = gd.block_queue([None, None])
    # grid = new_grid()
    #
    # #testing
    # grid = gd.block_load(grid)
    #
    # # Block queue
    # curr_block = block_queue[0]
    # next_block = block_queue[1]
    # block = Block(curr_block)
    #
    # while not done:
    #     # Pygame loop speed
    #     clock.tick(FPS)
    #
    #     screen.fill(BLACK)
    #
    #     # Block movement, record position
    #     val = kl.listener(grid, block.get_x(), block.get_y())
    #     block.set_x(val[1])
    #     block.set_y(val[2])
    #     new_board(screen, COLUMN_COUNT, ROW_COUNT, grid, block.get_color())
    #
    #     # Events
    #     for event in pg.event.get():
    #
    #         # Quit
    #         if event.type == pg.QUIT:
    #             done = True
    #     pg.display.flip()
    # pg.quit()
main()
