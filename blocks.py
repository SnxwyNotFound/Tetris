import random

# Green Block (S) - 2 Rotations
S = [
    '.00',
    '00.']

# Red Block (Z) - 2 Rotations
Z = [
    '00.',
    '.00']

# Cyan Block (I) - 2 Rotations
I = ['0',
     '0',
     '0',
     '0']

# Yellow Block (O) - No Rotation Needed
O = ['00'
     '00']

# Blue Block (J) - 4 Rotations
J = ['0..',
     '000']

# Orange Block (L) - 4 Rotations
L = [
    '..0',
    '000', ]

# Purple Block (T) - 4 Rotations
T = ['.0.',
     '000', ]

# List Of Shapes
list_shapes = [S, Z, I, O, J, L, T]
# Colors of The Shapes
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class Shape():
    def __init__(self, shape):
        global list_shapes, shape_colors
        self.shape = shape
        self.color = shape_colors[list_shapes.index(shape)]
        self.rotation = 0  # number from 0-3

def get_shape():
    global list_shapes, shape_colors
    return Shape(random.choice(list_shapes))

##### roations in game mechanics
# def rotate_shape(shape, rotation):
#     new_shape = []
#     #Somehow have to make the shapes rotate and return
#     new_shape.append(shape[rotation])
#     new_shape

test_shape = get_shape()
print(test_shape.shape)
