import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors, axes
import pathlib
from textwrap import wrap

size = 300
cube_side = 10
str_size = str(cube_side + 1) + 'x' + str(cube_side + 1)
route = 'D:\\Documents\\PycharmProjects\\ant\\'
folder = 'data\\' + str_size + '\\'

with open('data_' + str_size + '.txt', 'r') as f:
    lines = f.readlines()
f.close()

moment_of_hw_x = [i for i in range(1, 20)]
moment_of_hw_y = []
x_dist = []
y_dist = []
n_bins = 17

for line in lines:
    line = line.strip('\n')
    line = line.replace(',', ' ').split()
    pos = len(line) - 1
    while line[pos] != 'hw':
        pos -= 1

    pos_hw = pos + 4
    if line[pos + 5] == 'o':
        pos_x_dist = pos + 6
        pos_y_dist = pos + 7
        x_dist.append(int(line[pos_x_dist]))
        y_dist.append(int(line[pos_y_dist]))
    moment_of_hw = int(line[pos_hw])
    moment_of_hw_y.append(moment_of_hw)

# plot stats for moments of hw
fig_hw, ax_hw = plt.subplots(tight_layout=True)
# ax_hw[0].hist(moment_of_hw_x, bins=n_bins)
ax_hw.hist(moment_of_hw_y, bins=n_bins)
plt.xticks(moment_of_hw_x)
plt.xlabel('Moments of highway')
plt.ylabel('Frequency')
title_hw = 'Histogram shows frequency of appearance of moments of highway. Cube side = ' + str(cube_side + 1) + '.'
title_hw = ax_hw.set_title('\n'.join(wrap(title_hw, 50)))
filename_hw = 'hist_moment_of_hw'
fig_hw.savefig(route + folder + filename_hw)
plt.close(fig_hw)

# plot stats for dist from cube
fig_dist, ax_dist = plt.subplots(tight_layout=True)
plt.hist2d(x_dist, y_dist, bins=10, cmap='Blues')
# plt.yticks([i for i in range(1, 7)])
cb = plt.colorbar()
cb.set_label('Counts')
plt.xlabel('x')
plt.ylabel('y')
title_dist = 'Histogram shows frequency of distances from cube. Cube side = ' + str(cube_side + 1) + '.'
title_dist = ax_dist.set_title('\n'.join(wrap(title_dist, 50)))
filename_dist = 'hist_dist_from_cube'
fig_dist.savefig(route + folder + filename_dist)
plt.close(fig_dist)
