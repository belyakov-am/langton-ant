import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors, axes
import numpy as np
from collections import Counter
import pathlib
from textwrap import wrap

size = 300
cube_side = 2
cube = np.zeros((cube_side + 1, cube_side + 1), dtype=int)
field = np.zeros((size + 1, size + 1), dtype=int)
cmap = mpl.colors.ListedColormap(['#FFFFFF', '#53D4FF', '#D47EFF'])
index_cube = np.arange(cube_side + 1)
index_size = np.arange(size + 1)

route = 'D:\\Documents\\PycharmProjects\\ant\\'
folder = 'data\\' + str(cube_side + 1) + 'x' + str(cube_side + 1) + '\\'

with open(route + 'data_3x3.txt', 'r') as f:
    lines = Counter(f.readlines())
f.close()

most_common_lines = lines.most_common(3)
now_line = 1
pointer = 0
stop_step = ''
x = ''
y = ''
color = ''
count_iter = 0


for item in most_common_lines:
    count_iter += 1
    pathlib.Path(route + folder + str(count_iter) + '\\').mkdir(exist_ok=True, parents=True)
    frequency = str(item[1])
    line = item[0].strip('\n')
    pointer = 0

    for i in range(cube_side + 1):
        for j in range(cube_side + 1):
            cube[i][j] = int(line[pointer])
            field[int(size / 2) - int(cube_side / 2) + i][int(size / 2) - int(cube_side / 2) + j] = int(line[pointer])
            pointer += 1

    pointer += 1
    line = line[pointer:]
    splited_line = line.split()
    x_ind = 0
    y_ind = 1
    color_ind = 2
    count_exits_from_cube = 0
    x = splited_line[x_ind]
    while x != 'hw':
        if x == 'stop':
            stop_step = splited_line[y_ind]
            break

        if x == 'n':
            count_exits_from_cube += 1
            x_ind += 1
            y_ind += 1
            color_ind += 1
            x = splited_line[x_ind]
            fig, ax = plt.subplots()
            plt.imshow(field, interpolation='nearest', cmap=cmap)
            title = str(count_exits_from_cube) + ' exit from cube'
            plt.title(title)
            ax.set_xticks(index_size + 0.5)
            ax.set_yticks(index_size + 0.5)
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.grid(color='black', linestyle='-', linewidth=0.002)
            filename = 'exit_cube_' + str(count_exits_from_cube)
            fig.savefig(route + folder + str(count_iter) + '\\' + filename, dpi=1100)
            plt.close(fig)

        y = splited_line[y_ind]
        color = splited_line[color_ind]
        field[int(x)][int(y)] = int(color)
        x_ind += 3
        y_ind += 3
        color_ind += 3
        x = splited_line[x_ind]

    if x == 'hw':
        x_coord = splited_line[x_ind + 1]
        y_coord = splited_line[x_ind + 2]
        step = splited_line[x_ind + 3]
        moment_of_hw = splited_line[x_ind + 4]
        if splited_line[x_ind + 5] == 'o':
            pos = 'out'
            horiz_dist = splited_line[x_ind + 6]
            vert_dist = splited_line[x_ind + 7]
        else:
            pos = 'in'
        title = 'Highway was found. Moment of highway is ' + str(moment_of_hw)
        if pos == 'out':
            title += '. Highway started out of square. Horizontal distance from nearest cube side is ' + \
                     str(horiz_dist) + ', vertical distance is ' + str(vert_dist)
        else:
            title += '. Highway was found in square'
        title += '. The frequency of this pattern is ' + str(frequency)

    else:
        title = 'Ant went out of boundaries on step ' + stop_step + '. Highway was not found.'

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    title1 = ax1.set_title('\n'.join(wrap(title, 70)))
    fig1.tight_layout()
    title1.set_y(1.05)
    fig1.subplots_adjust(top=0.8)
    plt.imshow(cube, interpolation='nearest', cmap=cmap)
    # plt.title(title, fontsize=8)
    ax1.set_xticks(index_cube + 0.5)
    ax1.set_yticks(index_cube + 0.5)
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    ax1.grid(color='black', linestyle='-', linewidth=1.5)
    filename1 = 'cube' + str(now_line)
    fig1.savefig(route + folder + str(count_iter) + '\\' + filename1, dpi=300)
    plt.close(fig1)

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    title2 = ax2.set_title('\n'.join(wrap(title, 70)))
    fig2.tight_layout()
    title2.set_y(1.05)
    fig2.subplots_adjust(top=0.8)
    plt.imshow(field, interpolation='nearest', cmap=cmap)
    # plt.title(title, fontsize=8)
    ax2.set_xticks(index_size + 0.5)
    ax2.set_yticks(index_size + 0.5)
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    ax2.grid(color='black', linestyle='-', linewidth=0.002)
    filename2 = 'hw' + str(now_line)
    fig2.savefig(route + folder + str(count_iter) + '\\' + filename2, dpi=1100)
    plt.close(fig2)
    now_line += 1
