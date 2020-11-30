from typing import List
import random

"""
FloodFill with a Triangle Grid
All public functions operate without side effects
"""


class TriFloodFill():

    class State():
        def __init__(self, width: int, height: int, colors: int,
                     board: List[List[int]]):
            self.width = width
            self.height = height
            self.colors = colors
            self.board = board

        def isOutOfBounds(self, x: int, y: int) -> bool:
            # TODO: Implement based on rotating the triangle grid 45 degrees
            # and not just on the 2D array bounds
            return x < 0 or x >= self.height or y < 0 or y >= self.width

        def __str__(self) -> str:
            out = '[%d width, %d height]<%d colors> %s' % \
                (self.width, self.height, self.colors, self.board)

            board_out = ''
            for row in range(len(self.board)):
                board_out += ' ' * (len(self.board)-1-row)
                tiles = row*2 + 1
                for i in range(tiles):
                    if i % 2 == 0:
                        # board_out += '[%d,%d]' % (i//2, row)
                        board_out += str(self.board[i//2][row])
                    else:
                        # board_out += '[%d,%d]' % (row, i//2)
                        board_out += str(self.board[row][i//2])
                board_out += '\n'

            return board_out

    class Move():
        def __init__(self, x: int, y: int, color: int):
            self.x = x
            self.y = y
            self.color = color

    # Returns an initial randomized state based on the 2D map representation
    # at https://twitter.com/ZenoRogue/status/1081254363216138240
    #
    # The value of state.board[i][j] is the number of the color stored there
    @staticmethod
    def init(width: int = 5, height: int = 5, colors: int = 3) -> State:
        return TriFloodFill().State(
            width, height, colors,
            [[random.randint(0, colors-1) for i in range(width)]
             for j in range(height)]
        )

    @staticmethod
    def step(state: State, move: Move) -> State:
        cur_color = state.board[move.x][move.y]
        # Setting a tile to its own color is illegal
        assert(cur_color != move.color)
        # Setting an out-of-bounds tile is illegal
        assert(not state.isOutOfBounds(move.x, move.y))

        # Avoid side effects by copying the board
        new_board = [row[:] for row in state.board]
        new_state = TriFloodFill().State(
            state.width, state.height, state.colors,
            new_board
        )

        # Flood-Fill the new board from this tile
        return TriFloodFill._floodFill(
            new_state, move.x, move.y, cur_color, move.color
        )

    # Destructively flood-fills from the given point in the given state
    def _floodFill(state: State, x: int, y: int, prevColor: int, newColor: int) -> State:
        # Base Case
        if(state.isOutOfBounds(x, y)
           or state.board[x][y] != prevColor
           or state.board[x][y] == newColor):
            return

        # Color this tile
        state.board[x][y] = newColor

        # And recurse on neighbors
        TriFloodFill._floodFill(state, y, x, prevColor, newColor)
        TriFloodFill._floodFill(state, y, x-1, prevColor, newColor)
        TriFloodFill._floodFill(state, y+1, x, prevColor, newColor)

        return state


print('initial state')
state1 = TriFloodFill.init()
print(state1)
fill_color = 0 if state1.board[0][0] == 1 else 1
print('filling (0,0) with %d' % fill_color)
state2 = TriFloodFill.step(state1, TriFloodFill().Move(0, 0, fill_color))
print(state2)
