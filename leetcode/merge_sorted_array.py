# Given two sorted integer arrays nums1, nums2
# merge into nums1.
# assume nums1 has enough space.

def merge(nums1, m, nums2, n):
  curr = m + n - 1
  i = m - 1
  j = n - 1
  while (i >= 0) and (j >= 0):
    if nums1[i] > nums2[j]:
      nums1[curr] = nums1[i]
      i -= 1
    else:
      nums1[curr] = nums2[j]
      j -= 1
    curr -= 1
  while (j >= 0):
    nums1[curr] = nums2[j]
    curr -= 1
    j -= 1
