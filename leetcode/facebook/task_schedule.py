# task schedule
# tasks: AABABCD
# cool off time: 2
# output the task sequence; the sequence of tasks should be the same.

def schedule(tasks, cool):
  ret = ''
  hit = {}
  index = 0
  while (index < len(tasks)):
    task = tasks[index]
    if task not in hit:
      ret += task
      for key in hit.keys():
        hit[key] -= 1
        if hit[key] == 0:
          del hit[key]
      hit[task] = cool
      index += 1
    else:
      ret += ' '
      for key in hit.keys():
        hit[key] -= 1
        if hit[key] == 0:
          del hit[key]
  print ret

schedule('AABABCD', 2)
    
