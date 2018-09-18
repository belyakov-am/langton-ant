import numpy as np
from random import randint

# 0 - up, 1 - left, 2 - down, 3 - right (counterclockwise)
# -------------------------------------------------------
# WRITING PATTERN
# for i in range(pos_x - int((cube_side / 2)), pos_x + int((cube_side / 2)) + 1):
#     for j in range(pos_x - int((cube_side / 2)), pos_x + int((cube_side / 2)) + 1):
#         write(field[i][j])
#
#
# if ant is out of square: write x, y, field[x][y]
# if highway: write 'hw', x, y, step, moment of hw
# if highway was found in square: write 'i'
# if highway was found out of square: write 'o', horizontal and vertical distance from nearest side of the cube
# if out of boundaries: write 'stop'
# if ant was out of square and came back into square: write 'n'
# -------------------------------------------------------
# cube_side only even number
# out_of_square - prev position

f = open('D:\\Documents\\PycharmProjects\\ant\\data_5x5.txt', 'w')

now_iter = 0
iter_number = 1000000
size = 300
field = np.zeros((size + 1, size + 1), dtype=int)
total_steps = 100000
cube_side = 4


def get_color(x, y, now_field):
    return now_field[x][y]


def move():
    global direction, pos_x, pos_y
    if direction == 0:
        pos_y += 1
    elif direction == 1:
        pos_x -= 1
    elif direction == 2:
        pos_y -= 1
    elif direction == 3:
        pos_x += 1


def make_step():
    global direction, pos_x, pos_y, field, out_of_square
    if get_color(pos_x, pos_y, field) == 0 or get_color(pos_x, pos_y, field) == 1:
        direction = (direction + 1) % 4
    elif get_color(pos_x, pos_y, field) == 2:
        direction = (direction - 1) % 4
    field[pos_x][pos_y] = (get_color(pos_x, pos_y, field) + 1) % 3
    out_of_square = check_if_out_of_square(pos_x, pos_y)
    move()


def check_step_1(x, y, now_field, now_direction):
    if now_direction == 1 and get_color(x, y, now_field) == 0 and get_color(x, y - 1, now_field) == 0 and \
            get_color(x + 1, y, now_field) == 0 and get_color(x + 1, y - 1, now_field) == 0 and \
            get_color(x, y + 1, now_field) == 1 and get_color(x - 1, y + 1, now_field) == 0 and \
            get_color(x - 1, y, now_field) == 0 and get_color(x + 1, y + 1, now_field) == 2 and \
            get_color(x + 2, y, now_field) == 2 and get_color(x - 2, y, now_field) == 0:
        return True
    else:
        return False


def check_step_2(x, y, now_field, now_direction):
    if now_direction == 2 and get_color(x, y, now_field) == 0 and get_color(x + 1, y, now_field) == 0 and \
            get_color(x + 1, y + 1, now_field) == 0 and get_color(x, y + 1, now_field) == 1 and \
            get_color(x, y + 2, now_field) == 1 and get_color(x - 1, y + 1, now_field) == 0 and \
            get_color(x - 1, y + 2, now_field) == 0 and get_color(x + 1, y + 2, now_field) == 2 and \
            get_color(x - 1, y, now_field) == 0 and get_color(x - 2, y, now_field) == 0 and \
            get_color(x - 3, y, now_field) == 0:
        return True
    else:
        return False


def check_step_3(x, y, now_field, now_direction):
    if now_direction == 3 and get_color(x, y, now_field) == 0 and get_color(x, y + 1, now_field) == 0 and \
            get_color(x - 1, y, now_field) == 1 and get_color(x - 1, y + 1, now_field) == 1 and \
            get_color(x - 1, y + 2, now_field) == 1 and get_color(x - 2, y + 1, now_field) == 0 and \
            get_color(x - 2, y + 2, now_field) == 0 and get_color(x, y + 2, now_field) == 2 and \
            get_color(x - 2, y, now_field) == 0 and get_color(x - 3, y, now_field) == 0 and \
            get_color(x - 4, y, now_field) == 0:
        return True
    else:
        return False


def check_step_4(x, y, now_field, now_direction):
    if now_direction == 0 and get_color(x, y, now_field) == 0 and get_color(x - 1, y, now_field) == 1 and \
            get_color(x, y - 1, now_field) == 1 and get_color(x - 1, y - 1, now_field) == 1 and \
            get_color(x - 1, y + 1, now_field) == 1 and get_color(x - 2, y, now_field) == 0 and \
            get_color(x - 2, y + 1, now_field) == 0 and get_color(x, y + 1, now_field) == 2 and \
            get_color(x - 2, y - 1, now_field) == 0 and get_color(x - 3, y - 1, now_field) == 0 and \
            get_color(x - 4, y - 1, now_field) == 0:
        return True
    else:
        return False


def check_step_5(x, y, now_field, now_direction):
    if now_direction == 1 and get_color(x, y, now_field) == 1 and get_color(x, y - 1, now_field) == 1 and \
            get_color(x + 1, y, now_field) == 1 and get_color(x + 1, y - 1, now_field) == 1 and \
            get_color(x, y + 1, now_field) == 1 and get_color(x - 1, y + 1, now_field) == 0 and \
            get_color(x - 1, y, now_field) == 0 and get_color(x + 1, y + 1, now_field) == 2 and \
            get_color(x - 1, y - 1, now_field) == 0 and get_color(x - 2, y - 1, now_field) == 0 \
            and get_color(x - 3, y - 1, now_field) == 0:
        return True
    else:
        return False


def check_step_6(x, y, now_field, now_direction):
    if now_direction == 2 and get_color(x, y, now_field) == 1 and get_color(x + 1, y, now_field) == 1 and \
            get_color(x + 1, y + 1, now_field) == 1 and get_color(x, y + 1, now_field) == 2 and \
            get_color(x, y + 2, now_field) == 1 and get_color(x - 1, y + 1, now_field) == 0 and \
            get_color(x - 1, y + 2, now_field) == 0 and get_color(x + 1, y + 2, now_field) == 2 and \
            get_color(x - 1, y, now_field) == 0 and get_color(x - 2, y, now_field) == 0 and \
            get_color(x - 3, y, now_field) == 0:
        return True
    else:
        return False


def check_step_7(x, y, now_field, now_direction):
    if now_direction == 3 and get_color(x, y, now_field) == 1 and get_color(x, y + 1, now_field) == 1 and \
            get_color(x - 1, y, now_field) == 2 and get_color(x - 1, y + 1, now_field) == 2 and \
            get_color(x - 1, y + 2, now_field) == 1 and get_color(x - 2, y + 1, now_field) == 0 and \
            get_color(x - 2, y + 2, now_field) == 0 and get_color(x, y + 2, now_field) == 2 and \
            get_color(x - 2, y, now_field) == 0 and get_color(x - 3, y, now_field) == 0 and \
            get_color(x - 4, y, now_field) == 0:
        return True
    else:
        return False


def check_step_8(x, y, now_field, now_direction):
    if now_direction == 0 and get_color(x, y, now_field) == 1 and get_color(x - 1, y, now_field) == 2 and \
            get_color(x, y - 1, now_field) == 2 and get_color(x - 1, y - 1, now_field) == 2 and \
            get_color(x - 1, y + 1, now_field) == 1 and get_color(x - 2, y, now_field) == 0 and \
            get_color(x - 2, y + 1, now_field) == 0 and get_color(x, y + 1, now_field) == 2 and \
            get_color(x - 2, y - 1, now_field) == 0 and get_color(x - 3, y - 1, now_field) == 0 \
            and get_color(x - 4, y - 1, now_field) == 0:
        return True
    else:
        return False


def check_step_9(x, y, now_field, now_direction):
    if now_direction == 1 and get_color(x, y, now_field) == 2 and get_color(x, y - 1, now_field) == 2 and \
            get_color(x + 1, y, now_field) == 2 and get_color(x + 1, y - 1, now_field) == 2 and \
            get_color(x, y + 1, now_field) == 1 and get_color(x - 1, y + 1, now_field) == 0 and \
            get_color(x - 1, y, now_field) == 0 and get_color(x + 1, y + 1, now_field) == 2 and \
            get_color(x - 1, y - 1, now_field) == 0 and get_color(x - 2, y - 1, now_field) == 0 and \
            get_color(x - 3, y - 1, now_field) == 0:
        return True
    else:
        return False


def check_step_10(x, y, now_field, now_direction):
    if now_direction == 0 and get_color(x, y, now_field) == 1 and get_color(x, y - 1, now_field) == 0 and \
            get_color(x, y - 2, now_field) == 2 and get_color(x + 1, y - 1, now_field) == 2 and \
            get_color(x + 1, y - 2, now_field) == 2 and get_color(x + 1, y, now_field) == 2 and \
            get_color(x - 1, y, now_field) == 0 and get_color(x - 1, y - 1, now_field) == 0 and \
            get_color(x - 1, y - 2, now_field) == 0 and get_color(x - 2, y - 2, now_field) == 0 and \
            get_color(x - 3, y - 2, now_field) == 0:
        return True
    else:
        return False


def check_step_11(x, y, now_field, now_direction):
    if now_direction == 1 and get_color(x, y, now_field) == 0 and get_color(x, y - 1, now_field) == 0 and \
            get_color(x + 1, y, now_field) == 2 and get_color(x + 1, y - 1, now_field) == 0 and \
            get_color(x + 1, y - 2, now_field) == 2 and get_color(x + 2, y, now_field) == 2 and \
            get_color(x + 2, y - 1, now_field) == 2 and get_color(x + 2, y - 2, now_field) == 2 and \
            get_color(x, y - 2, now_field) == 0 and get_color(x - 1, y - 2, now_field) == 0 and \
            get_color(x - 2, y - 2, now_field) == 0:
        return True
    else:
        return False


def check_step_12(x, y, now_field, now_direction):
    if now_direction == 2 and get_color(x, y, now_field) == 0 and get_color(x, y + 1, now_field) == 1 and \
            get_color(x + 1, y + 1, now_field) == 2 and get_color(x + 1, y, now_field) == 0 and \
            get_color(x + 1, y - 1, now_field) == 2 and get_color(x + 2, y + 1, now_field) == 2 and \
            get_color(x + 2, y, now_field) == 2 and get_color(x + 2, y - 1, now_field) == 2 and \
            get_color(x, y - 1, now_field) == 0 and get_color(x - 1, y - 1, now_field) == 0 and \
            get_color(x - 2, y - 1, now_field) == 0:
        return True
    else:
        return False


def check_step_13(x, y, now_field, now_direction):
    if now_direction == 3 and get_color(x, y, now_field) == 0 and get_color(x, y + 1, now_field) == 2 and \
            get_color(x, y - 1, now_field) == 2 and get_color(x - 1, y, now_field) == 1 and \
            get_color(x - 1, y + 1, now_field) == 1 and get_color(x + 1, y + 1, now_field) == 2 and \
            get_color(x + 1, y, now_field) == 2 and get_color(x + 1, y - 1, now_field) == 2 and \
            get_color(x - 1, y - 1, now_field) == 0 and get_color(x - 2, y - 1, now_field) == 0 and \
            get_color(x - 3, y - 1, now_field) == 0:
        return True
    else:
        return False


def check_step_14(x, y, now_field, now_direction):
    if now_direction == 0 and get_color(x, y, now_field) == 2 and get_color(x, y - 1, now_field) == 1 and \
            get_color(x, y - 2, now_field) == 2 and get_color(x - 1, y, now_field) == 1 and \
            get_color(x - 1, y - 1, now_field) == 1 and get_color(x + 1, y, now_field) == 2 and \
            get_color(x + 1, y - 1, now_field) == 2 and get_color(x + 1, y - 2, now_field) == 2 and \
            get_color(x - 1, y - 2, now_field) == 0 and get_color(x - 2, y - 2, now_field) == 0 and \
            get_color(x - 3, y - 2, now_field) == 0:
        return True
    else:
        return False


def check_step_15(x, y, now_field, now_direction):
    if now_direction == 3 and get_color(x, y, now_field) == 2 and get_color(x, y - 1, now_field) == 2 and \
            get_color(x, y - 2, now_field) == 2 and get_color(x - 1, y, now_field) == 0 and \
            get_color(x - 1, y - 1, now_field) == 1 and get_color(x - 1, y - 2, now_field) == 2 and \
            get_color(x - 2, y, now_field) == 1 and get_color(x - 2, y - 1, now_field) == 1 and \
            get_color(x - 2, y - 2, now_field) == 0 and get_color(x - 3, y - 2, now_field) == 0 and \
            get_color(x - 4, y - 2, now_field) == 0:
        return True
    else:
        return False


def check_step_16(x, y, now_field, now_direction):
    if now_direction == 2 and get_color(x, y, now_field) == 2 and get_color(x, y + 1, now_field) == 0 and \
            get_color(x, y - 1, now_field) == 2 and get_color(x - 1, y + 1, now_field) == 0 and \
            get_color(x - 1, y, now_field) == 1 and get_color(x - 1, y - 1, now_field) == 2 and \
            get_color(x - 2, y + 1, now_field) == 1 and get_color(x - 2, y, now_field) == 1 and \
            get_color(x - 2, y - 1, now_field) == 0 and get_color(x - 3, y - 1, now_field) == 0 and \
            get_color(x - 4, y - 1, now_field) == 0:
        return True
    else:
        return False


def check_step_17(x, y, now_field, now_direction):
    if now_direction == 1 and get_color(x, y, now_field) == 1 and get_color(x, y + 1, now_field) == 0 and \
            get_color(x, y - 1, now_field) == 2 and get_color(x + 1, y, now_field) == 0 and \
            get_color(x + 1, y + 1, now_field) == 0 and get_color(x + 1, y - 1, now_field) == 2 and \
            get_color(x - 1, y, now_field) == 1 and get_color(x - 1, y + 1, now_field) == 1 and \
            get_color(x - 1, y - 1, now_field) == 0 and get_color(x - 2, y - 1, now_field) == 0 and \
            get_color(x - 3, y - 1, now_field) == 0:
        return True
    else:
        return False


def check_step_18(x, y, now_field, now_direction):
    if now_direction == 2 and get_color(x, y, now_field) == 2 and get_color(x, y + 1, now_field) == 2 and \
            get_color(x, y + 2, now_field) == 0 and get_color(x + 1, y, now_field) == 2 and \
            get_color(x + 1, y + 1, now_field) == 0 and get_color(x + 1, y + 2, now_field) == 0 and \
            get_color(x - 1, y + 1, now_field) == 1 and get_color(x - 1, y + 2, now_field) == 1 and \
            get_color(x - 1, y, now_field) == 0 and get_color(x - 2, y, now_field) == 0 and \
            get_color(x - 3, y, now_field) == 0:
        return True
    else:
        return False


def check_line(x, y, now_field):
    global cube_side
    while abs(x) + 2 <= cube_side or abs(y) <= cube_side:
        for i in range(-2, 3):
            if get_color(x + i, y, now_field) != 0:
                return False
        x -= 1
        y -= 1
    return True


def check_highway(x, y, now_field, now_direction):
    global hw_found
    num = 0
    write_info = False
    if check_step_1(x, y, now_field, now_direction) and check_line(x - 1, y - 1, now_field):
        num = 1
        hw_found = True
        write_info = True
    elif check_step_2(x, y, now_field, now_direction) and check_line(x - 2, y - 1, now_field):
        num = 2
        hw_found = True
        write_info = True
    elif check_step_3(x, y, now_field, now_direction) and check_line(x - 3, y - 1, now_field):
        num = 3
        hw_found = True
        write_info = True
    elif check_step_4(x, y, now_field, now_direction) and check_line(x - 3, y - 2, now_field):
        num = 4
        hw_found = True
        write_info = True
    elif check_step_5(x, y, now_field, now_direction) and check_line(x - 2, y - 2, now_field):
        num = 5
        hw_found = True
        write_info = True
    elif check_step_6(x, y, now_field, now_direction) and check_line(x - 2, y - 1, now_field):
        num = 6
        hw_found = True
        write_info = True
    elif check_step_7(x, y, now_field, now_direction) and check_line(x - 3, y - 1, now_field):
        num = 7
        hw_found = True
        write_info = True
    elif check_step_8(x, y, now_field, now_direction) and check_line(x - 3, y - 2, now_field):
        num = 8
        hw_found = True
        write_info = True
    elif check_step_9(x, y, now_field, now_direction) and check_line(x - 2, y - 2, now_field):
        num = 9
        hw_found = True
        write_info = True
    elif check_step_10(x, y, now_field, now_direction) and check_line(x - 2, y - 3, now_field):
        num = 10
        hw_found = True
        write_info = True
    elif check_step_11(x, y, now_field, now_direction) and check_line(x - 1, y - 3, now_field):
        num = 11
        hw_found = True
        write_info = True
    elif check_step_12(x, y, now_field, now_direction) and check_line(x - 1, y - 2, now_field):
        num = 12
        hw_found = True
        write_info = True
    elif check_step_13(x, y, now_field, now_direction) and check_line(x - 2, y - 2, now_field):
        num = 13
        hw_found = True
        write_info = True
    elif check_step_14(x, y, now_field, now_direction) and check_line(x - 2, y - 3, now_field):
        num = 14
        hw_found = True
        write_info = True
    elif check_step_15(x, y, now_field, now_direction) and check_line(x - 3, y - 3, now_field):
        num = 15
        hw_found = True
        write_info = True
    elif check_step_16(x, y, now_field, now_direction) and check_line(x - 3, y - 2, now_field):
        num = 16
        hw_found = True
        write_info = True
    elif check_step_17(x, y, now_field, now_direction) and check_line(x - 2, y - 2, now_field):
        num = 17
        hw_found = True
        write_info = True
    elif check_step_18(x, y, now_field, now_direction) and check_line(x - 2, y - 1, now_field):
        num = 18
        hw_found = True
        write_info = True
    return write_info, num


def check_highway_left_down():
    global pos_x, pos_y, field, direction
    return check_highway(pos_x, pos_y, field, direction)


def check_highway_left_up():
    global pos_x, pos_y, field, direction
    now_field_rot90 = np.rot90(field, k=1)
    x_rot90 = int(size / 2) - pos_y + int(size / 2)
    y_rot90 = pos_x
    direction_rot90 = (direction + 1) % 4
    return check_highway(x_rot90, y_rot90, now_field_rot90, direction_rot90)


def check_highway_right_up():
    global pos_x, pos_y, field, count_steps
    now_field_rot180 = np.rot90(field, k=2)
    x_rot180 = int(size / 2) - pos_x + int(size / 2)
    y_rot180 = int(size / 2) - pos_y + int(size / 2)
    direction_rot180 = (direction - 2) % 4
    return check_highway(x_rot180, y_rot180, now_field_rot180, direction_rot180)


def check_highway_right_down():
    global pos_x, pos_y, field
    now_field_rot270 = np.rot90(field, k=3)
    x_rot270 = pos_y
    y_rot270 = int(size / 2) - pos_x + int(size / 2)
    direction_rot270 = (direction - 1) % 4
    return check_highway(x_rot270, y_rot270, now_field_rot270, direction_rot270)


def check_turn(x, y, now_dir):
    if now_dir == 0 and field[x][y] in [0, 1] and field[x - 1][y] in [0, 1] and y == y_top + 1 \
            and x_left < x <= x_right:
        return True
    elif now_dir == 0 and field[x][y] == 2 and field[x + 1][y] == 2 and y == y_top + 1 and x_left <= x < x_right:
        return True
    elif now_dir == 1 and field[x][y] in [0, 1] and field[x][y - 1] in [0, 1] and x == x_left - 1 \
            and y_bot < y <= y_top:
        return True
    elif now_dir == 1 and field[x][y] == 2 and field[x][y + 1] == 2 and x == x_left - 1 and y_bot <= y < y_top:
        return True
    elif now_dir == 2 and field[x][y] in [0, 1] and field[x + 1][y] in [0, 1] and y == y_bot - 1 \
            and x_left <= x < x_right:
        return True
    elif now_dir == 2 and field[x][y] == 2 and field[x - 1][y] == 2 and y == y_bot - 1 and x_left < x <= x_right:
        return True
    elif now_dir == 3 and field[x][y] in [0, 1] and field[x][y + 1] in [0, 1] and x == x_right + 1 \
            and y_bot <= y < y_top:
        return True
    elif now_dir == 3 and field[x][y] == 2 and field[x][y - 1] == 2 and x == x_right + 1 and y_bot < y <= y_top:
        return True
    elif now_dir == 1 and field[x][y] in [0, 1] and y == y_top + 1 and x_left <= x < x_right:
        return True
    elif now_dir == 3 and field[x][y] == 2 and y == y_top + 1 and x_left < x <= x_right:
        return True
    elif now_dir == 2 and field[x][y] in [0, 1] and x == x_left - 1 and y_bot <= y < y_top:
        return True
    elif now_dir == 0 and field[x][y] == 2 and x == x_left - 1 and y_bot < y <= y_top:
        return True
    elif now_dir == 3 and field[x][y] in [0, 1] and y == y_bot - 1 and x_left < x <= x_right:
        return True
    elif now_dir == 1 and field[x][y] == 2 and y == y_bot - 1 and x_left <= x < x_right:
        return True
    elif now_dir == 0 and field[x][y] in [0, 1] and x == x_right + 1 and y_bot < y <= y_top:
        return True
    elif now_dir == 2 and field[x][y] == 2 and x == x_right + 1 and y_bot <= y < y_top:
        return True
    else:
        return False


def check_boundaries(x, y):
    if x < 0 or x > size or y < 0 or y > size:
        return True
    else:
        return False


def check_if_out_of_square(x, y):
    if x < x_left or x > x_right or y < y_bot or y > y_top:
        return True
    else:
        return False


def get_dist(x, y):
    horiz_dist = abs(int(size / 2) - x) - int(cube_side / 2) - 1
    vert_dist = abs(int(size / 2) - y) - int(cube_side / 2) - 1
    if horiz_dist < 0:
        horiz_dist = 0
    if vert_dist < 0:
        vert_dist = 0
    return horiz_dist, vert_dist


def write_data(x, y, now_dir, out_of_sqr):
    global info_written
    if out_of_sqr and not check_if_out_of_square(x, y) and info_written:
        f.write('n ')
        info_written = False
    if check_if_out_of_square(x, y) and not check_turn(x, y, now_dir):
        f.write('%d' % x)
        f.write(' ')
        f.write('%d' % y)
        f.write(' ')
        color = (field[x][y] + 1) % 3
        f.write('%d' % color)
        f.write(' ')
        info_written = True


while now_iter != iter_number:
    count_steps = 0
    pos_x = int(size / 2)
    pos_y = int(size / 2)
    direction = 0

    hw_found = False
    out_of_square = False
    info_written = False
    x_left = pos_x - int(cube_side / 2)
    x_right = pos_x + int(cube_side / 2)
    y_top = pos_y + int(cube_side / 2)
    y_bot = pos_y - int(cube_side / 2)

    field = np.zeros((size + 1, size + 1), dtype=int)
    for i in range(pos_x - int((cube_side / 2)), pos_x + int((cube_side / 2)) + 1):
        for j in range(pos_x - int((cube_side / 2)), pos_x + int((cube_side / 2)) + 1):
            field[i][j] = randint(0, 2)
            f.write('%d' % field[i][j])
    f.write(',')

    while count_steps != total_steps:
        if hw_found:
            count_steps = total_steps
            if check_if_out_of_square(pos_x, pos_y):
                f.write(' o ')
                horizontal_dist, vertical_dist = get_dist(pos_x, pos_y)
                f.write('%d' % horizontal_dist)
                f.write(' ')
                f.write('%d' % vertical_dist)
            else:
                f.write(' i')
            break

        make_step()

        if check_boundaries(pos_x, pos_y):
            f.write(' ')
            f.write('stop ')
            f.write('%d' % count_steps)
            count_steps = total_steps
            break

        count_steps += 1

        write_data(pos_x, pos_y, direction, out_of_square)
        check1, num1 = check_highway_left_down()
        check2, num2 = check_highway_left_up()
        check3, num3 = check_highway_right_up()
        check4, num4 = check_highway_right_down()

        if hw_found and (check1 or check2 or check3 or check4):
            f.write('hw ')
            f.write('%d' % pos_x)
            f.write(' ')
            f.write('%d' % pos_y)
            f.write(' ')
            f.write('%d' % count_steps)
            f.write(' ')

            if check1:
                moment_of_hw = num1
            elif check2:
                moment_of_hw = num2
            elif check3:
                moment_of_hw = num3
            else:
                moment_of_hw = num4

            f.write('%d' % moment_of_hw)

            count_steps = total_steps
            if check_if_out_of_square(pos_x, pos_y):
                f.write(' o ')
                horizontal_dist, vertical_dist = get_dist(pos_x, pos_y)
                f.write('%d' % horizontal_dist)
                f.write(' ')
                f.write('%d' % vertical_dist)
            else:
                f.write(' i')

    f.write('\n')
    now_iter += 1

f.close()
