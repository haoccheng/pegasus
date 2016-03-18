# Given array of integers, and a target.
# find two numbers such that the sum is close to target.

def closest(input, target):
  input = sorted(input)
  candidate = None
  candidate_best = None
  for i in range(len(input)):
    xi = input[i]

    start = i + 1
    end = len(input) - 1
    while (start <= end):
      if start == end:
        diff = abs(target - xi - input[start])
        if candidate_best is None:
          candidate_best = diff
          candidate = (xi, input[start])
        else:
          if diff < candidate_best:
            candidate_best = diff
            candidate = (xi, input[start])
        break
      elif start + 1 == end:
        d1 = abs(target - xi - input[start])
        d2 = abs(target - xi - input[end])
        if d1 < d2:
          candidate_best = d1
          candidate = (xi, input[start])
        else:
          candidate_best = d2
          candidate = (xi, input[end])
        break
      else:
        middle = (start + end) / 2
        diff = target - xi - input[middle]
        if candidate_best is None:
          candidate_best = abs(diff)
          candidate = (xi, input[middle])
        else:
          if abs(diff) < candidate_best:
            candidate_best = abs(diff)
            candidate = (xi, input[middle])
        if diff == 0:
          break
        elif diff > 0:
          start = middle + 1
        else:
          end = middle - 1
  return (candidate, candidate_best)

input = [1, 3, 5, 7, 9]
target = 20
print closest(input, target)
input = [1, 3, 5, 7, 9, 11]
target = 20
print closest(input, target)
input = [1, 3, 5, 7, 9, 11, 14]
target = 21
print closest(input, target)
