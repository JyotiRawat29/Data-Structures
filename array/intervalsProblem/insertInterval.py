"""
57. Insert Interval
Solved
Medium
Topics
premium lock iconCompanies
Hint

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

"""

#%%
#def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[List[int]]:
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval =[4,8]
result = []
i = 0
n = len(intervals)

# Step 1: Add all intervals before newInterval
while i < n and intervals[i][1] < newInterval[0]:
    result.append(intervals[i])
    i += 1
    print(result)

# Step 2: Merge overlapping intervals with newInterval
while i < n and intervals[i][0] <= newInterval[1]:
    newInterval[0] = min(newInterval[0], intervals[i][0])
    newInterval[1] = max(newInterval[1], intervals[i][1])
    i += 1
result.append(newInterval)

# Step 3: Add remaining intervals
while i < n:
    result.append(intervals[i])
    i += 1

print(result) 
# %%
chars = ["a","a","b","b","c","c","c"]
read = 1
write = 0
for i in range(1,len(chars)):
    if  chars[i]==chars[i-1]:
        read+=1 # r2
    else:
        if read == 1:
            chars[write] = chars[i-1]
            write +=1
        else:
            chars[write]=chars[i-1] #a2b2
            for c in str(read):
                write += 1 
                chars[write]= c
                print(write)
                print(chars)
            read = 1
            write+=1 #w3
if i== len(chars)-1:
    if read == 1:
        chars[write] = chars[i]
        write +=1
    else:
        chars[write]=chars[i] #a2b2
        for c in str(read):
            write += 1 
            chars[write]= c

print(len(chars[:write]))

# %%
