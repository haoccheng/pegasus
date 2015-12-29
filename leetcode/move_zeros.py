# move all 0 to the end while maintaining relative order. do it in place.
# 0,1,0,3,12 -> 1,3,12,0,0

def move_zero(nums):
  x = 0
  y = 0
  while (x <= len(nums)-1):
    if nums[x] == 0:
      y = x + 1
      while (y <= len(nums)-1):
        if nums[y] != 0:
          break
        else:
          y += 1
      if y <= len(nums) - 1:
        nums[x] = nums[y]
        nums[y] = 0
        x += 1
      else:
        break
    else:
      x += 1

input = [0, 1, 0, 3, 12]
move_zero(input)
print input
