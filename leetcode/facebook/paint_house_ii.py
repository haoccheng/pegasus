# There are a row of n houses, each house can be painted with one of the k colors. 
# The cost of painting each house with a certain color is different. You have to 
# paint all the houses such that no two adjacent houses have the same color.

def paint(costs):
  # mine is O(nkk)
  # desired is O(nk). Interesting, only the top two paints of last house is relevant.d 
