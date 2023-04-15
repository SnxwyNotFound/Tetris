# Game mechanics
import blocks


def rotate_clockwise(shape):
    rows = len(shape)
    columns = len(shape[0])
    rotated_item = []
    new_list = []
    for i in range(columns):
        for index in range(len(shape)):
            new_list.append(shape[index][i])
        rotated_item.append(new_list)
        new_list = []
    p = []
    for i in rotated_item:
        row = ""
        for o in i:
            row += o
        p.append(row)
    return p


def rotate_counter_clockwise(shape):
    rows = len(shape)
    columns = len(shape[0])
    rotated_item = []
    new_list = []
    for i in range(columns - 1, -1, -1):
        for index in range(len(shape) - 1, -1, -1):
            new_list.append(shape[index][i])
        rotated_item.append(new_list)
        new_list = []
    p = []
    for i in rotated_item:
        row = ""
        for o in i:
            row+=o
        p.append(row)
    return p

print(rotate_clockwise(blocks.L))

def spawn_item(item):
    if item == blocks.I:
        spawn("row 22", "column 5,6")