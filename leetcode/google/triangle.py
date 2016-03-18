# Given an integer array, find if there are elements that can make legal triangle.

# sort the inputs.
# find a sequence of a/b/c such that a <= b <= c and a + b > c.
# This would naturally qualify another two constraints, a + c > b and b + c > a.

def triangle(input):
  input = sorted(input)
  output = []
  for i in range(len(input)):
    vi = input[i]
    for j in range(i+1, len(input)):
      vj = input[j]
      start = j + 1
      end = len(input) - 1
      while (start <= end):
        if start == end:
          if vi + vj > input[start]:
            output.append((vi, vj, input[start]))
          break
        elif start + 1 == end:
          if vi + vj > input[start]:
            output.append((vi, vj, input[start]))
          if vi + vj > input[end]:
            output.append((vi, vj, input[end]))
          break
        else:
          middle = (start + end) / 2
          if vi + vj <= input[middle]:
            end = middle - 1
          else:
            output += [(vi, vj, e) for e in input[start:middle+1]]
            start = middle + 1
  print output

triangle([1,1,1])
triangle([1,1,1,2,3,4,5,6,7])
