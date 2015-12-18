# Given an absolute path, simplify.
# /home/ -> /home
# /a/./b/../../c/ -> /c

def simplify_path(path):
  items = path.split('/')
  items = [e.strip() for e in items if len(e.strip()) > 0]
  print items
  stack = []
  for e in items:
    if e == '.':
      continue
    elif e == '..':
      if len(stack) > 0:
        stack.pop()
    else:
      stack.append(e)
  return '/' + '/'.join(stack)

print simplify_path('/home/')
print simplify_path('/a/./b/../../c/')
print simplify_path('/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///')
