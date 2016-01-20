# Given n (1..n) to create unique structure BST

def generate_base(numbers):
  result = []
  if len(numbers) == 0:
    result.append(None)
  elif len(numbers) == 1:
    result.append(TreeNode(numbers[0]))
  else:
    for i in range(len(numbers)):
      numbers_left = numbers[:i]
      numbers_right = numbers[i+1:]
      left = generate_base(numbers_left)
      right = generate_base(numbers_right)
      for l in left:
        for r in right:
          root = TreeNode(numbers[i])
          root.left = l
          root.right = r
          result.append(root)
  return result

def generate(n):
  return generate_base(range(1, n+1))
