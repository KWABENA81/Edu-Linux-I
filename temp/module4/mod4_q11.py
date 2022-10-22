from numpy import random

nums = random.randint(199, size=(3, 3))
print('Original: \n', nums)
c = 1
nums_sorted = nums[nums[:, c - 1].argsort()]
print('\nSorted @ col ', c, ': \n', nums_sorted)
c += 1
nums_sorted = nums[nums[:, c - 1].argsort()]
print('\nSorted @ col ', c, ': \n', nums_sorted)
c += 1
nums_sorted = nums[nums[:, c - 1].argsort()]
print('\nSorted @ col ', c, ': \n', nums_sorted)


# Solution:
# Original:
#  [[ 46 114  15]
#  [184 102 124]
#  [ 62 106 147]]
#
# Sorted @ col  1 :
#  [[ 46 114  15]
#  [ 62 106 147]
#  [184 102 124]]
#
# Sorted @ col  2 :
#  [[184 102 124]
#  [ 62 106 147]
#  [ 46 114  15]]
#
# Sorted @ col  3 :
#  [[ 46 114  15]
#  [184 102 124]
#  [ 62 106 147]]
#
# Process finished with exit code 0