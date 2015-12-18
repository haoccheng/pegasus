# Given #rows, generate the first nrows of Pascal triangle.
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# ..

def generate(num_rows):
  pascal = []
  if num_rows <= 0:
    return pascal
  pascal.append([1])
  if num_rows >= 2:
    pascal.append([1, 1])
  for i in range(2, num_rows):
    last = pascal[-1]
    row = []
    row.append(1)
    x = 0
    y = 1
    while (y <= len(last) -1):
      row.append(last[x] + last[y])
      x += 1
      y += 1
    row.append(1)
    pascal.append(row)
  return pascal

print generate(2)
print generate(5)

