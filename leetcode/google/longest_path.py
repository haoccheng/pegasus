# longest path in binary tree.
# path can start/end at any arbitrary node.
#
# at any node, find the left subtree depth and right subtree depth.
# Basically this forms a path.

def longest_path(root):
  choice = 0
  lst = root.left
  lst_depth = 0
  rst = root.right
  rst_depth = 0
  if lst is not None:
    (lst_choice, lst_depth) = longest_path(lst)
    choice = max(choice, lst_choice)
  if rst is not None:
    (rst_choice, rst_depth) = longest_path(rst)
    choice = max(choice, rst_choice)
  choice = max(choice, lst_depth + rst_depth + 1)
  depth = max(lst_depth, rst_depth) + 1
  return (choice, depth)


