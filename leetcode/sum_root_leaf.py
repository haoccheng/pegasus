# root-to-leaf form integer; each node value 0-9 only.
# sum all paths.

def sum_numbers_base(root, path):
  if (root.left is None) and (root.right is None):
    v = [str(e) for e in path]
    return int(''.join(v) + str(root.val))
  else:
    count = 0
    path.append(root.val)
    if root.left is not None:
      count += sum_numbers_base(root.left, path)
    if root.right is not None:
      count += sum_numbers_base(root.right, path)
    path.pop()
    return count

def sum_numbers(root):
  if root is None:
    return 0
  else:
    path = []
    return sum_numbers_base(root, path)

