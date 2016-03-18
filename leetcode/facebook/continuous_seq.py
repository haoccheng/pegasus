# given a sequence, target, if there is continuous sequence in sequence whose sum to total.
# need to positive sequence.

def continuous(input, target):
  start = 0
  end = 0
  cumsum = input[start]
  while (True):
    if cumsum == target:
      return True
    elif cumsum < target:
      end += 1
      if end <= len(input)-1:
        cumsum += input[end]
      else:
        break
    else:
      cumsum -= input[start]
      start += 1
  return False

print continuous([1, 2, 3, 4, 5], 9)
print continuous([1, 2, 3, 4, 5], 10)
print continuous([1, 2, 3, 4, 5], 12)
print continuous([1, 2, 3, 4, 5], 13)

