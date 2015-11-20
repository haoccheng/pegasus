# Implement a function that finds the edit distance of two input strings.
# 3 edit operations.
# insert, delete, substitution.

# saturday : sunday -> 3
# saturday : sturday -> 1
# sturday : surday -> 1
# surday : sunday -> 1

# Dynamic programming.
# Table format to keep some sort of states/scores/memory.
# How to initialize/kick start some cells in the table.
# What is the iterative direction to fill the rest of the cells.

def build_scores(input1, input2):
  scores = []
  for i in range(len(input1)+1):
    row = []
    for j in range(len(input2)+1):
      row.append(None)
    scores.append(row)
  return scores

def init_scores(scores):
  for i in range(len(scores)):
    scores[i][0] = i
  for i in range(len(scores[0])):
    scores[0][i] = i

def iterate_scores(scores, input1, input2):
  for i in range(1, len(scores)):
    for j in range(1, len(scores[i])):
      # 
      s1 = 0
      if (input1[i-1] == input2[j-1]): # match; and choose to match.
        s1 = scores[i-1][j-1]
      else: # mismatch; choose to substitute.
        s1 = scores[i-1][j-1] + 1
      s2 = scores[i-1][j] + 1 # choose to delete/addition.
      s3 = scores[i][j-1] + 1
      scores[i][j] = min([s1, s2, s3])

def print_scores(scores):
  print '==================='
  for i in range(len(scores)):
    print scores[i]

def edit(input1, input2):
  scores = build_scores(input1, input2)
  init_scores(scores)
  iterate_scores(scores, input1, input2)
  print_scores(scores)

edit('saturday', 'sunday')
edit('saturday', 'sturday')
edit('sturday', 'surday')
edit('surday', 'sunday')
