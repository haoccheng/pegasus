# Given a positive integer, return its corresponding title as in Excel sheet.
# 1->A
# 2->B
# ..
# 26 -> Z
# 27 -> AA
# 28 -> AB.

def excel_title(n):
  title = ''
  v = n
  while (v > 0):
    v = v - 1
    r1 = (int)(v / 26)
    r2 = v % 26
    title = chr(ord('A') + r2) + title
    v = r1
  return title

print excel_title(1)
print excel_title(26)
print excel_title(27)
print excel_title(28)

