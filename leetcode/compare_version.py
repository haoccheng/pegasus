# compare version string
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
# 0.1 < 1.1 < 1.2 < 13.37

def compare_version(version1, version2):
  v1 = version1.split('.')
  v1 = [e for e in v1 if e != '.']
  v1 = [int(e) for e in v1]
  
  v2 = version2.split('.')
  v2 = [e for e in v2 if e != '.']
  v2 = [int(e) for e in v2]

  for i in range(min(len(v1), len(v2))):
    if v1[i] == v2[i]:
      continue
    elif v1[i] > v2[i]:
      return +1
    else:
      return -1
  if len(v1) == len(v2):
    return 0
  elif len(v1) > len(v2):
    for i in range(min(len(v1), len(v2)), len(v1)):
      if v1[i] == 0:
        continue
      else:
        return +1
  else:
    for i in range(min(len(v1), len(v2)), len(v2)):
      if v2[i] == 0:
        continue
      else:
        return -1
  return 0

print compare_version('0.1', '1.1')
print compare_version('1.1', '1.2')
print compare_version('13.37', '1.2')
