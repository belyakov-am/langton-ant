import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors, axes
from textwrap import wrap


def check_boundaries(x, y):
    if x < 0 or x > size or y < 0 or y > size:
        return True
    else:
        return False


def get_color(x, y, now_field):
    return now_field[x][y]


def move():
    global direction, pos_x, pos_y, count_steps, total_steps
    if direction == 0:
        pos_y += 1
    elif direction == 1:
        pos_x -= 1
    elif direction == 2:
        pos_y -= 1
    elif direction == 3:
        pos_x += 1


def make_step():
    global direction, pos_x, pos_y, field
    if get_color(pos_x, pos_y, field) == 0 or get_color(pos_x, pos_y, field) == 1:
        direction = (direction + 1) % 4
    elif get_color(pos_x, pos_y, field) == 2:
        direction = (direction - 1) % 4
    field[pos_x][pos_y] = (get_color(pos_x, pos_y, field) + 1) % 3
    move()


size = 100
cube_side = 2
total_steps = 1000
cube_pattern = '122101202'
cmap = mpl.colors.ListedColormap(['#FFFFFF', '#53D4FF', '#D47EFF'])
str_size = str(cube_side + 1) + 'x' + str(cube_side + 1)
route = 'D:\\Documents\\PycharmProjects\\ant\\'
folder = 'data\\' + str_size + '\\'
index_size = np.arange(size + 1)

count_steps = 0
pos_x = int(size / 2)
pos_y = int(size / 2)
direction = 0
field = np.zeros((size + 1, size + 1), dtype=int)
for i in range(cube_side + 1):
    for j in range(cube_side + 1):
        field_i = pos_x - int(cube_side / 2) + i
        field_j = pos_x - int(cube_side / 2) + j
        field[field_i][field_j] = cube_pattern[(cube_side + 1) * i + j]

while count_steps != total_steps:
    make_step()
    count_steps += 1
    if check_boundaries(pos_x, pos_y):
        count_steps = total_steps

title = ''
fig = plt.figure()
ax = fig.add_subplot(111)
title = ax.set_title('\n'.join(wrap(title, 70)))
fig.tight_layout()
title.set_y(1.05)
fig.subplots_adjust(top=0.8)
plt.imshow(field, interpolation='nearest', cmap=cmap)
ax.set_xticks(index_size + 0.5)
ax.set_yticks(index_size + 0.5)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(color='black', linestyle='-', linewidth=0.002)
filename = 'most_common_pattern_2'
fig.savefig(route + folder + filename, dpi=1100)
plt.close(fig)
