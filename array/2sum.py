map= {}
for i in range(len(nums)):
  diff = abs(nums[i] - target)
   if diff in map:
    return i, map[i]
  map[nums[i]] = diff
