# longest palindromic substring.

def lps(input):
  if len(input) == 0:
    return ''
  elif len(input) == 1:
    return input
  scores = []
  for i in range(len(input)):
    row = [-1] * len(input)
    scores.append(row)
  for i in range(len(input)):
    scores[i][i] = 1
  for j in range(1, len(input)):
    for i in range(0, j):
      if scores[i+1][j-1] > 0:
        if input[i] == input[j]:
          scores[i][j] = scores[i+1][j-1] + 1
  max_score = (0, 0)
  for i in range(len(input)):
    for j in range(i+1, len(input)):
      if scores[max_score[0]][max_score[1]] < scores[i][j]:
        max_score = (i, j)
  return input[max_score[0]:max_score[1]+1]

print lps('dcbabce')
print lps('ukxidnpsdfwieixhjnannbmtppviyppjgbsludrzdleeiydzawnfmiiztsjqqqnthwinsqnrhfjxtklvbozkaeetmblqbxbugxycrlzizthtuwxlmgfjokhqjyukrftvfwikxlptydybmmzdhworzlaeztwsjyqnshggxdsjrzazphugckgykzhqkdrleaueuajjdpgagwtueoyybzanrvrgevolwssvqimgzpkxehnunycmlnetfaflhusauopyizbcpntywntadciopanyjoamoyexaxulzrktneytynmheigspgyhkelxgwplizyszcwdixzgxzgxiawstbnpjezxinyowmqsysazgwxpthloegxvezsxcvorzquzdtfcvckjpewowazuaynfpxsxrihsfswrmuvluwbdazmcealapulnahgdxxycizeqelesvshkgpavihywwlhdfopmmbwegibxhluantulnccqieyrbjjqtlgkpfezpxmlwpyohdyftzgbeoioquxpnrwrgzlhtlgyfwxtqcgkzcuuwagmlvgiwrhnredtulxudrmepbunyamssrfwyvgabbcfzzjayccvvwxzbfgeglqmuogqmhkjebehtwnmxotjwjszvrvpfpafwomlyqsgnysydfdlbbltlwugtapwgfnsiqxcnmdlrxoodkhaaaiioqglgeyuxqefdxbqbgbltrxcnihfwnzevvtkkvtejtecqyhqwjnnwfrzptzhdnmvsjnnsnixovnotugpzuymkjplctzqbfkdbeinvtgdpcbvzrmxdqthgorpaimpsaenmnyuyoqjqqrtcwiejutafyqmfauufwripmpcoknzyphratopyuadgsfrsrqkfwkdlvuzyepsiolpxkbijqw')
