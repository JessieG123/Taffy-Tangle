import taffy

def index_j_to_x(j):
    x = (4 * j) - 12
    return x

def index_i_to_y(i):
    y = (-4 * i) + 16
    return y

def x_to_index_j(mouseX):
    j = int(((mouseX + 14) / 28) * 7)
    return j
def y_to_index_i(mouseY):
    i = int(((mouseY - 18) / 36) * -9)
    return i

def draw_fruits_on_grid(grid):
    for i in range(9):
        for j in range(7):
            x = index_j_to_x(j)
            y = index_i_to_y(i)
            if grid[i][j]==1:
                taffy.pic1(x, y)
            if grid[i][j]==2:
                taffy.pic2(x, y)
            if grid[i][j]==3:
                taffy.pic3(x, y)
            if grid[i][j]==4:
                taffy.pic4(x, y)
            if grid[i][j]==5:
                taffy.pic5(x, y)
            if grid[i][j]==6:
                taffy.pic6(x, y)