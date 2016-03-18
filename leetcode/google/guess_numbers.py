# Given an array [4,2,1,3,5]
# it produces a new array [0,1,2,1,0] each cell represents how many numbers on the left of this position 
# are larger than this particular number.
# Question, given the new array, how to reverse engineering derive the original array.
# assume all numbers in the range 1-n.

def rr(input):
  answer = [-1] * len(input)
  curr = len(input)
  while (True):
    pivot = None
    for i in range(len(input)-1, -1, -1):
      if answer[i] == -1 and input[i] == 0:
        pivot = i
        break
    if pivot == None:
      break
    answer[pivot] = curr
    curr -= 1
    for i in range(pivot+1, len(input)):
      input[i] -= 1
  print answer

rr([0, 1, 2, 1, 0])
rr([0, 0, 0, 2, 1])
rr([0, 1, 2, 3, 4])
rr([0, 0, 0, 0, 0])
