# Given a 2d map of 1 (land) and 0 (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# Assume all 4 edges of grid are all surrounded by water.

# 11110
# 11010
# 11000
# 00000   answer:1
#======================
# 11000
# 11000
# 00100
# 00011   answer:3

def bfs(grid, x, y, index):
  if grid[x][y] == '1':
    curr = [(x,y)]
    label = str(1+index)
    while len(curr) > 0:
      (x,y) = curr.pop(0)
      grid[x][y] = label
      if (x-1) >= 0 and grid[x-1][y] == '1':
        grid[x-1][y] = label
        curr.append((x-1,y))
      if (x+1) <= len(grid)-1 and grid[x+1][y] == '1':
        grid[x+1][y] = label
        curr.append((x+1,y))
      if (y-1) >= 0 and grid[x][y-1] == '1':
        grid[x][y-1] = label
        curr.append((x,y-1))
      if (y+1) <= len(grid[x])-1 and grid[x][y+1] == '1':
        grid[x][y+1] = label
        curr.append((x,y+1))

def number_islands(grid):
  index = 0
  for x in range(len(grid)):
    for y in range(len(grid[x])):
      if grid[x][y] == '1':
        index += 1
        bfs(grid, x, y, index)
  return index

x = ['11110', '11010', '11000', '00000']
x = [list(e) for e in x]
print number_islands(x)

