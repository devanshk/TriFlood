from TriFloodFill import TriFloodFill


class TriFloodFillView():
    pass


state1 = TriFloodFill.init()
print(state1)
state2 = TriFloodFill.step(state1, TriFloodFill().Move(0, 0, 1))
print(state2)
