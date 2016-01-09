# Given an arrya S of N integers, find 3 integers such that the sum is closest to a given number.
# Return the sum of 3 integers.
# {-2 2 1 -4}, target=1, return=2.

def sum3(nums, target):
  best_diff = None
  best_value = None
  nums = sorted(nums)
  for i in range(len(nums)):
    for j in range(i+1, len(nums)-1):
      if best_diff == 0:
        break
      if best_diff is not None:
        ma = target - nums[i] - nums[j] - nums[j+1]
        mb = target - nums[i] - nums[j] - nums[-1]
        print nums[i], nums[j], nums, ma, mb, best_diff
        if (mb > 0) and (mb > best_diff):
            continue
        elif (ma < 0) and (-ma > best_diff):
            continue
      r = target - nums[i] - nums[j]
      start = j+1
      end = len(nums) - 1
      while (start <= end):
        if (start == end):
          diff = abs(r - nums[start])
          best_diff = diff if (best_diff is None) or (best_diff > diff) else best_diff
          best_value = nums[i] + nums[j] + nums[start]
          break
        elif (start + 1 == end):
          diff = min(abs(r - nums[start]), abs(r - nums[end]))
          if abs(r - nums[start]) < abs(r - nums[end]):
            best_value = nums[i] + nums[j] + nums[start]
          else:
            best_value = nums[i] + nums[j] + nums[end]
          best_diff = diff if (best_diff is None) or (best_diff > diff) else best_diff
          break
        mid = (int)((start + end) / 2)
        if nums[mid] < r:
          start = mid
        else:
          end = mid
  return best_value

print sum3([1,2,4,8,16,32,64,128], 82)
#print sum3([0,0,0], 1)
#print sum3([-1, 2, 1, -4], 1)
#print sum3([1, 4, 10, 20], 5)
#print sum3([-43,57,-71,47,3,30,-85,6,60,-59,0,-46,-40,-73,53,68,-82,-54,88,73,20,-89,-22,39,55,-26,95,-87,-57,-86,28,-37,43,-27,-24,-88,-35,82,-3,39,-85,-46,37,45,-24,35,-49,-27,-96,89,87,-62,85,-44,64,78,14,59,-55,-10,0,98,50,-75,11,97,-72,85,-68,-76,44,-12,76,76,8,-75,-64,-57,29,-24,27,-3,-45,-87,48,10,-13,17,94,-85,11,-42,-98,89,97,-66,66,88,-89,90,-68,-62,-21,2,37,-15,-13,-24,-23,3,-58,-9,-71,0,37,-28,22,52,-34,24,-8,-20,29,-98,55,4,36,-3,-9,98,-26,17,82,23,56,54,53,51,-50,0,-15,-50,84,-90,90,72,-46,-96,-56,-76,-32,-8,-69,-32,-41,-56,69,-40,-25,-44,49,-62,36,-55,41,36,-60,90,37,13,87,66,-40,40,-35,-11,31,-45,-62,92,96,8,-4,-50,87,-17,-64,95,-89,68,-51,-40,-85,15,50,-15,0,-67,-55,45,11,-80,-45,-10,-8,90,-23,-41,80,19,29,7], 255)
