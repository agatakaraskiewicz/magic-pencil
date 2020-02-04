# it prints lists elements in some different order than it is given

# as a result it prints a small heart

# it's cute :)

grid = [['.', '.', '.', '.', '.', '.'],
       ['.', 'O', 'O', '.', '.', '.'],
       ['O', 'O', 'O', 'O', '.', '.'],
       ['O', 'O', 'O', 'O', 'O', '.'],
       ['.', 'O', 'O', 'O', 'O', 'O'],
       ['O', 'O', 'O', 'O', 'O', '.'],
       ['O', 'O', 'O', 'O', '.', '.'],
       ['.', 'O', 'O', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '.']]


for column in range(0, len(grid[0])):
    for row in range (0, len(grid)):
        print (grid[row][column], end = '')
        row += 1
    print ()