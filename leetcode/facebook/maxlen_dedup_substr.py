# maximum length substring with no duplicate letters.

def max_substr(input):
  candidate = None
  start = 0
  end = 0
  hit = {}
  while (end < len(input)):
    c = input[end]
    if c not in hit:
      end += 1
    else:
      prev = hit[c]
      if prev < start:
        end += 1
      else:
        start = prev+1
        end += 1
    hit[c] = end-1
    if candidate is None:
      candidate = (end - start, start, end)
    elif (end-start) > candidate[0]:
      candidate = (end - start, start, end)
  print candidate
  print input[candidate[1]:candidate[2]]

#max_substr('abcedax')  
#max_substr('abxcedaxcedf') 
max_substr('abxcedaxcedfg') 
