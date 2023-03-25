# Game mechanics
import blocks


def rotate_clockwise(shape):
    return [[shape[y][x]
             for y in range(len(shape))]
            for x in range(len(shape[0]) - 1, -1, -1)]
def place_block(shape)


def spawn_item(item):
    if item == blocks.I:
        spawn("row 22", "column 5,6")
