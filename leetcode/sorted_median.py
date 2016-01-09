# two sorted arrays nums1, nums2 of size m/n.
# find the median of the two sorted arrays.
# runtime complexity O(log(m+n)).

def median(nums1, nums2):
  length = len(nums1) + len(nums2)
  if length % 2 == 1: # odd
    return kth(nums1, nums2, length/2)
  else:
    return (kth(nums1, nums2, length/2) + kth(nums1, nums2, length/2-1)) / 2.0

def kth(nums1, nums2, k):
  if len(nums1) == 0:
    return nums2[k]
  if len(nums2) == 0:
    return nums1[k]
  i1 = (int)(len(nums1) / 2)
  i2 = (int)(len(nums2) / 2)
  v1 = nums1[i1]
  v2 = nums2[i2]
  if i1 + i2 < k:
    if v1 > v2:
      return kth(nums1, nums2[i2+1:], k-i2-1)
    else:
      return kth(nums1[i1+1:], nums2, k-i1-1)
  else:
    if v1 > v2:
      return kth(nums1[:i1], nums2, k)
    else:
      return kth(nums1, nums2[:i2], k)

print median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11])
print median([1, 3, 5, 7, 9], [2, 4, 6, 8, 10, 11])
