# convert sorted array to height-balanced BST.

def bst_base(nums, start, end):
  if (start > end):
    return None
  if (start == end):
    return TreeNode(nums[start])
  else:
    mid = (int)((start + end) / 2)
    root = TreeNode(nums[mid])
    if start < mid:
      root.left = bst_base(nums, start, mid-1)
    if mid < end:
      root.right = bst_base(nums, mid+1, end)
    return root
