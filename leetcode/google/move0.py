# move all 0s to right end of the array.

def move0(input):
  start = 0
  end = len(input) - 1
  while (start < end):
    while (start < end and input[end] == 0):
      end -= 1
    while (start < end and input[start] != 0):
      start += 1
    if start < end:
      if input[start] == 0 and input[end] != 0:
        input[start] = input[end]
        input[end] = 0
        start += 1
        end -= 1
  print input

move0([1, 2, 0, 3, 0, 4])
move0([0, 1, 2, 0, 3, 0, 4])
move0([0] * 4)
move0([1] * 4)
