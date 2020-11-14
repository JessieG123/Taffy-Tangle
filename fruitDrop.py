import random
import checkForMatch
import drawTaffyOnGrid 
import fruits

def placement(grid):
    for i in range(9):
        for j in range(7):
            number = random.randrange(1, 7)
            grid[i][j] = number

rows, cols = (9, 7) #9 by 7 grid
grid = [[0 for i in range(cols)] for j in range(rows)]

placement(grid)
drawTaffyOnGrid.draw_fruits_on_grid(grid)

fruits.show_forever()