# check whether it is possible for an array to be the post-order traversal sequence of a binary search tree.
# All numbers in the array are unique.
# {5, 7, 6, 9, 11, 10, 8} is a probable post order traversal.
# {7, 4, 6, 5} is not

def check_post_order(input, min_value=None, max_value=None):
  if len(input) == 0:
    return True
  root = input[-1]
  if min_value is not None:
    if (root < min_value):
      return False
  if max_value is not None:
    if (root > max_value):
      return False
  # split by the root value.
  split_index = None
  for i in range(len(input)-2, -1, -1):
    if input[i] < root:
      split_index = i
      break
  left = input[0:split_index+1] if split_index is not None else []
  right = input[split_index+1:-1] if split_index is not None else input[:-1]

  left_check = check_post_order(left, min_value, root)
  right_check = check_post_order(right, root, max_value)
  if (left_check == False) or (right_check == False):
    return False
  return True

def test():
  input = [5, 7, 6, 9, 11, 10, 8]
  print check_post_order(input)
  input = [7, 4, 6, 5]
  print check_post_order(input)

test()

