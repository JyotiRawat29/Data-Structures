"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

Solution:
Solution looks at first glance that first array needs to be sorted, than duplication needs to be removed and later binning. The maximium counter of the
bins is the solution to the problem.
For sorting: Binary sort (o(n^2)) T.C.
Removing duplication: O(n^2) : [nums[i] for i in range(len(nums)) if i==0 or nums[i]!=nums[i-1]] T.C = O(n^2) hence we use set(list) and it returns us a set not list.
A set is a collection of unordered elements and hence no indexing, no indexing that means no information of neighbours. The elements are stored using the hash of element itself.
Hence they cannot be indexed or searched as traditional list. It is a data structure used for fast lookup.
Binning: Having an empty dict, starting chain counter at every non consecutive number.

However, as you progress, the realization comes that with sets this can be easily solved and there is no need of sorting.
The heart of this problems lies in the guradline that says, checking the element in the set if it is the first element of chain by subtracting 1,
the lookup takes O(n) and no element needs to be iterarated again. Atmost 2. Check if the element is first element and if so, start the counter.

"""

nums_set = set(nums)
max_len = 0
for num in nums_set:
     if num-1 not in nums_set:
          length = 1
          while num +length in nums_set:
                length += 1
          max_len = max(max_len,length)
print(max_len)


