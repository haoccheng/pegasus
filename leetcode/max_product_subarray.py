# https://leetcode.com/problems/maximum-product-subarray/
# [2,3,-2,4] -> [2,3] -> 6

def max_product(nums):
  if len(nums) == 0:
    return 0
  pos_products = [0] * len(nums)
  neg_products = [0] * len(nums)
  pos_products[0] = nums[0]
  neg_products[0] = nums[0]
  for i in range(1, len(nums)):
    o1 = nums[i]
    o2 = pos_products[i-1]*nums[i]
    o3 = neg_products[i-1]*nums[i]
    pos_products[i] = max(max(o1, o2), o3)
    neg_products[i] = min(min(o1, o2), o3)
  return max(pos_products)

print max_product([2, -5, -2, -4, 3])
