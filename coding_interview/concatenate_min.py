# Big numbers can be formed if numbers in an array are concatenated together.
# Find minimum of concatenated number of a given array.
# {3, 32, 321} -> 321323

def compare(inputs, available, ni, nj):
  maxi = '0'
  maxj = '0'
  for i in range(len(inputs)):
    if (available[i] == 0) or (i == ni):
      continue
    if maxi < inputs[i][0]:
      maxi = inputs[i][0]
  for i in range(len(inputs)):
    if (available[i] == 0) or (i == nj):
      continue
    if maxj < inputs[i][0]:
      maxj = inputs[i][0]
  # compare ni and nj position values.
  for i in range(min(len(inputs[ni]), len(inputs[nj]))):
    if inputs[ni][i] > inputs[nj][i]: # ni > nj
      return True
    elif inputs[ni][i] < inputs[nj][i]: # ni < nj
      return False
  if (len(inputs[ni]) == len(inputs[nj])):
    if maxi > maxj: # If match, then compare the next possible value.
      return True
    else:
      return False
  else:
    if len(inputs[ni]) > len(inputs[nj]):
      maxi = inputs[ni][len(inputs[nj])]
    else:
      maxj = inputs[nj][len(inputs[ni])]
    if maxi > maxj:
      return True
    else:
      return False

def concat_min(inputs):
  available = [1] * len(inputs)
  r = ''
  while (True):
    ni = None
    for i in range(len(inputs)):
      if available[i] == 1:
        ni = i
        break
    if ni is None:
      break
    for i in range(len(inputs)):
      if (available[i] == 1) and (i != ni):
        cmp = compare(inputs, available, ni, i)
        if cmp == True:
          ni = i
    r = r + inputs[ni]
    available[ni] = 0
  return r

def test():
  print concat_min(['3', '32', '321'])

test()

