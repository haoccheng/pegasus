# Given #rows, generate the first nrows of Pascal triangle.
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# ..

def generate(num_rows):
  if num_rows == 0:
    return [1]
  elif num_rows == 1:
    return [1, 1]
  elif num_rows > 1:
    last = [1, 1]
    for i in range(1, num_rows):
      row = []
      row.append(1)
      x = 0
      y = 1
      while (y <= len(last) -1):
        row.append(last[x] + last[y])
        x += 1
        y += 1
      row.append(1)
      last = row
    return last

print generate(2)
print generate(5)

