# Each house has a certain amount of money.
# If two adjacent hourses were broken into, it will trigger the alarm.
# Determine the maximum amount of money that can rob without trigger tha alarm.

def rob(nums):
  if len(nums) == 0:
    return 0
  yes = nums[0]
  no = 0
  for i in range(1, len(nums)):
    yes1 = no + nums[i]
    no1 = max(yes, no)
    yes = yes1
    no = no1
  return max(yes, no)

print rob([1, 2, 3])
print rob([2, 1, 1, 2])
