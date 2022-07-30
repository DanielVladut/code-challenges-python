# given a grid of tlles defined by width x height
# and a pawn located at a given starting position inside the grid [pxo, py0]
# and a series of the following types of movements:
#   - portal movement [p1, p2] : moves the pawn p1 tiles on x axix and p2 tiles on y axis
#       - where a positive value moves right/down and a negative value moves left/up
#   - tile by tile movements descrbed by a string of the following chars:
#      - D = down, U = up, R = right, L = left
# and the "out of grid" movement rule by which if a move in the movement series positions the pawn
# outside of the grid, then the movement is ignored and the next movement is taken.
# determine the final position of the pawn after all given movements are executed 

def move_pawn(initial_pos, width, height, portals, tile_by_tile_moves):
    current_pos = initial_pos
    for next_move in portals:
        ccurrent_pos = compute_next_pos(current_pos, next_move, width, height)
    for tile_move in tile_by_tile_moves:
        next_move = [0, 0]
        match tile_move:
            case 'R':
                next_move[0] = current_pos[0] + 1
            case 'L':
                next_move[0] = current_pos[0] - 1
            case 'U':
                next_move[1] = current_pos[1] - 1
            case 'D':
                next_move[1] = current_pos[1] + 1
        current_pos = compute_next_pos(current_pos, next_move, width, height)

    return current_pos


def compute_next_pos(current_pos, move, width, height):
    next_pos = [current_pos[0] + move[0], current_pos[1] + move[1]]
    if (is_in_grid(next_pos, width, height)):
        return next_pos
    return current_pos


def is_in_grid(pos, width, height):
    return 0 < pos[0] < width and 0 < pos[1] < height; 

def test_move_pawnd():
    assert move_pawn([0,0], 5, 5, [[1,1], [-1,-1], [6,6]], "RDUL") == [0,0]
   