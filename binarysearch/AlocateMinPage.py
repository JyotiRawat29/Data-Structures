"""
#GFG Problem
Allocate Minimum Pages

Given an array arr[] of integers, where each element arr[i] represents the number of pages in the i-th book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:
Each student receives atleast one book.
Each student is assigned a contiguous sequence of books.
No book is assigned to more than one student.
All books must be allocated.
The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum. If it is not possible to allocate books to all students, return -1;
Examples:

Input: arr[] = [12, 34, 67, 90], k = 2
Output: 113
Explanation: Allocation can be done in following ways:
=> [12] and [34, 67, 90] Maximum Pages = 191
=> [12, 34] and [67, 90] Maximum Pages = 157
=> [12, 34, 67] and [90] Maximum Pages = 113.
The third combination has the minimum pages assigned to a student which is 113.
Input: arr[] = [15, 17, 20], k = 5
Output: -1
Explanation: Since there are more students than total books, it's impossible to allocate a book to each student.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i], k ≤ 104
"""

"""
Its a minimum of maximum finding problem.

"""
arr,k = [12, 34, 67, 90], 2
low = max(arr)
high = sum(arr)
ans = -1

def checkTrue(mid,arr,k):
    running_pages = 0
    num_studs = 1
    for i in range(len(arr)):
        if arr[i]+running_pages>mid:
            running_pages = arr[i]
            num_studs+=1
            if num_studs>k:
                return False
        else:
            running_pages+=arr[i]
    return True

if len(arr)<k:
    print("-1")
else:
    while(low<=high):
        mid = (low+high)//2
        if checkTrue(mid,arr,k):
            #print(mid)
            ans = mid
            high = mid-1
        else:
            low = mid+1
print(ans)

#GFG

class Solution:
    def checkTrue(self,mid,arr,k):
        num_student=1
        running_pages = 0
        for i in range(len(arr)):
            if arr[i]>mid:
                return False
            if running_pages+arr[i]>mid:
                running_pages= arr[i]
                num_student +=1
                if num_student >k:
                    return False
            else:
                running_pages+=arr[i]
        return True
        
    def findPages(self, arr, k):
        # code here
        low = max(arr)
        high = sum(arr)
        ans = -1
        if len(arr)<k:
            return ans
        else:
            while(low<=high):
                mid = (low+high)//2
                #print("mid is", mid)
                if self.checkTrue(mid,arr,k):
                    ans = mid
                    high = mid-1
                else:
                    low = mid+1
            return ans

