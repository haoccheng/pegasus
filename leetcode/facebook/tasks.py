# A list of tasks, each is described by a letter.
# The same letter tasks should be separate at least by some minimum interval, K.
# Compute the minimum time to complete the tasks.
# tasks=AAA, K=2, answer=5 (A A A)
# tasks=AABBCC, K=3, answer=6 (ABCABC)

from collections import defaultdict

def lineup(input):
  counts = defaultdict(int)
  for c in input:
    counts[c] += 1

  cc = dict(counts)
  print cc


