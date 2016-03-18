# Given a pyramid of numbers, walk down to bottom.
# find the path whose sum is the maximum.
#                          55
#                        94 48
#                       95 30 96
#                     77 71 26 67

def maxtriangle(triangle):
  scores = [triangle[0][0]]
  for i in range(1, len(triangle)):
    new_scores = [0] * len(triangle[i])
    for j in range(len(triangle[i])):
      if j == 0:
        new_scores[j] = scores[j] + triangle[i][j]
      elif j == len(triangle[i])-1:
        new_scores[j] = scores[-1] + triangle[i][j]
      else:
        new_scores[j] = max(scores[j-1], scores[j]) + triangle[i][j]
    scores = new_scores
  return max(new_scores)

print maxtriangle([[55], [94, 48], [95, 30, 96], [77, 71, 26, 67]])
