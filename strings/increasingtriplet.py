#%%
#Bruteforce approach to find increasing triplet in an array
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        for num in range(len(nums)-2):
            for start in range(num + 1, len(nums)-1):
                end = start+1
                while(end != len(nums)):
                    if nums[num]<nums[start]:
                        while(end!=len(nums)):
                            if nums[start]<nums[end]:
                                return True
                            else:
                                end += 1
                    else:
                        start += 1
                        end = start + 1
        return False

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    s = Solution()
    print(s.increasingTriplet(nums))

#%%
"""
If we find 2 smallest numbers in the array, then we can check if there is any number greater than the second smallest number. 
If yes, then we have found an increasing triplet.
To build that concept, first try to build on finding smallest number in the array.
Then we can build on that to find second smallest number and 
then finding third greatest number in array.

In the question we just need to find if there is any increasing triplet in the array,
so we can just return True if we find any number greater than second smallest number, no need to 
find the actual triplet (hence saving time and space complexity)

"""
first = float('inf')
second = float('inf')
third = float('inf')

nums = [1,5,0,4,1,3]
for num in nums:
    if num <=first:
        third = second
        second = first
        first = num
    elif num <= second:
        third = second
        second = num
    elif num <= third:
        third = num

print(first, second, third)

# %%

first = float('inf')
second = float('inf')

for num in nums:
    if num <= first:
        first = num
    elif num <= second:
        second = num
    else:
        print("Found increasing triplet")
        #Here at any point in thr loop first < second
        #Both are already found hence we just to check if there is any number greater than second smallest number
        #which is num>second: else is covering that case becasue if num > second, it is also greater than first
        #hence we can just return True if we find any number greater than second smallest number, no need to 
        #find the actual triplet (hence saving time and space complexity)
        break
# %%
