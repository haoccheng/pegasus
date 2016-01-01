# Given a set of distinct integers, generate all possible subsets.

def subsets(nums):
  nums = sorted(nums)
  ret = []
  bit = [0] * len(nums)
  bit[0] = 1
  ret.append([])
  while (1 in bit):
    row = []
    for i in range(len(bit)):
      if bit[i] == 1:
        row.append(nums[i])
    ret.append(row)
    carry = 1
    for i in range(len(bit)):
      if carry == 0:
        break
      else:
        if bit[i] == 0:
          bit[i] = 1
          carry = 0
        else:
          bit[i] = 0
          carry = 1
  return ret

print subsets([1,2])
