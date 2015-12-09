# Given a number n, stands for n dices, print all probabilities of all possible sum of dice points.

# iteratively update matrix.

def init_dice_matrix(ndice):
  value_max = 6 * ndice
  dices = []
  for i in range(ndice):
    row = [0.0] * value_max
    dices.append(row)
  for i in range(6):
    dices[0][i] = 1.0 / 6.0
  return dices

def update_dice_matrix(dices, curr_ndice):
  value_min = 1 * curr_ndice - 1 # zero base.
  value_max = 6 * curr_ndice - 1
  curr_ndice = curr_ndice - 1
  for v in range(value_min, value_max+1):
    p = 0.0
    for curr_roll in range(1, 6+1):
      r = v - curr_roll
      if r >= 0:
        p = p + dices[curr_ndice-1][r] * dices[0][curr_roll-1]
    dices[curr_ndice][v] = p

def print_dice_matrix(dices):
  print '=================================================='
  for i in range(len(dices)):
    r = ['%.2f' % e for e in dices[i]]
    print r

def dice_sum(ndice):
  dices = init_dice_matrix(ndice)
  update_dice_matrix(dices, 2)
  print_dice_matrix(dices)

dice_sum(2)
