# parse CSV file.
# name|address|phone|job
# -> json format {name:.., address:.., phone:.., job:..}

# "hello " world "hello" -> hello world hello
# "hello"""
# If start with ", for the subsequent consecutive double quote "", it would be converted to ".
# what is escape mean? """

def parse_csv(line):
  # name, address, phone, job.
  prev = ''
  quote = False
  items = []
  i = 0
  while (i < len(line)):
    if quote == False:
      if line[i] == ',':
        items.append(prev)
        prev = ''
      elif line[i] == '"':
        quote = True
      else:
        prev += line[i]
      i += 1
    else:
      if line[i] == '"':
        if (i + 1 <= len(line) - 1):
          if line[i+1] == '"':
            prev += '"'
            i += 2
          else:
            quote = False
            i += 1
        else:
          quote = False
          i += 1
      else:
        prev += line[i]
        i += 1
  items.append(prev)
  return items

print parse_csv('hello world,hello world,,,')
print parse_csv('hello "world,hello world",,,')
print parse_csv('hello "world,""hello world""",,,')
print parse_csv('hello "world," "hello world""",,,')

