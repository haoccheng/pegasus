# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

def unique_bst(n):
  trees = []
  for i in range(n+1):
    row = [0] * (n+1)
    trees.append(row)
  for i in range(1, n+1):
    trees[i][i] = 1
  for j in range(2, n+1):
    for i in range(j-1, 0, -1):
      count = 0
      for root in range(i, j+1):
        if root == i:
          count += trees[root+1][j]
        elif root == j:
          count += trees[i][root-1]
        else:
          count += (trees[i][root-1] * trees[root+1][j])
      trees[i][j] = count
  return trees[1][-1]

print unique_bst(4)
