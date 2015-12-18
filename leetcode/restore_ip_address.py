# given a string containing only digit, restore it to all possible valid IP addresses.
# 25525511135 -> 255.255.11.135, 255.255.111.35

def restore_ip_base(s, npart):
  if len(s) == 0:
    return None
  elif npart == 1:
    v = int(s)
    if (v >= 0) and (v <= 255) and (str(v) == s):
      return [s]
    else:
      return None
  else:
    ret = []
    for i in range(1, 4):
      s1 = s[:i]
      s2 = s[i:]
      if (len(s1) == i) and (len(s2) > 0):
        v = int(s1)
        if (v >= 0) and (v <= 255) and (str(v) == s1):
          rest = restore_ip_base(s2, npart-1)
          if rest is not None:
            for e in rest:
              ret.append(s1 + '.' + e)
    return ret

#def restore_ip_address(s):
#  xx
print restore_ip_base('25525511135', 4)
print restore_ip_base('0000', 4)
