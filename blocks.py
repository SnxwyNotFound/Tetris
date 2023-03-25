import random

# Green Block (S) - 2 Rotations
S = [[
      '.00',
      '00.']]

# Red Block (Z) - 2 Rotations
Z = [[
      '00.',
      '.00']]

# Cyan Block (I) - 2 Rotations
I = [['0',
      '0',
      '0',
      '0']]

# Yellow Block (O) - No Rotation Needed
O = [['00'
      '00']]

# Blue Block (J) - 4 Rotations
J = [['0..',
      '000']]

# Orange Block (L) - 4 Rotations
L = [[
      '..0',
      '000',]]

# Purple Block (T) - 4 Rotations
T = [['.0.',
      '000',]]

# List Of Shapes
shapes = [S, Z, I, O, J, L, T]
# Colors of The Shapes
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


class Shape():
    def __init__(self, shapes):
        self.shapes = shapes
        self.color = shape_colors[shapes.index(shapes)]
        self.rotation = 0  # number from 0-3


def get_shape():
    global shapes, shape_colors

    return Shape(random.choice(shapes))


##### roations in game mechanics
