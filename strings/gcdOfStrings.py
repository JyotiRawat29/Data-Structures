"""
1071. Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
gdf(6,3) = 3

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
gdf(6,4) =2

Example 3:

Input: str1 = "ABABABAB", str2 = "ABAB"
Output: "ABAB"
gdf(8,4) =4

Example 4:

Input: str1 = "ABABABAB", str2 = "ABAB"
Output: "ABAB"
gdf(8,4) =4

Example 5:

Input: str1 = "AAAAAB", str2 = "AAA"
Output: ""
gdf(6,3) = 3
Example 5:​​​​​​​
Input: str1 = "LEET", str2 = "CODE"
Output: ""
gdf(4,4) =1

Example 2 and Example 3 are crucial to understand what is asked here.
At first it might look that we need to find the repeated common pattern(prefix) in both strings which can be repeated itself n number of times to get
the longer string.
Howver, the question asks the greatest/longest pattern or prefix that repeats itself and gives the longer string and is present in the shorter string.
In example two, AB is the prefix that is common in both and repeated 3 and 2 times respectively to give both strings. However,
ABAB|AB = 6
ABAB = 4
gdf(6,4) = 2
If you repeat ABAB again it gives ABAB|ABAB which is not equal to ABABAB. HEnce the largest common prefix is AB.
However in example 3:
ABAB|ABAB
ABAB
gdf(8,4) = 4
Repeating ABAB 2 times gives the longer string. AB is also the common prefix but the longest common prefix is ABAB.
Hence we need to find out the gcd (greatest common divisor/factor) of both lengths to find the commmon longest prefix.
Approach,
Find the larger and smaller string.
Find gdf of 2 = prefix.
Check if the substring containg prefix chars of both is equal, if prefix repeating themselves m and n times resulting into the both strings.

#small_str = min(str1, str2) #1
        #large_str = max(str1,str2) #2
        #The above method compares string lexigraphically and not length wise

Know your return staments carefully. Focus on the cases that you need und if and rest can go into else.
"""

    def gcdOfStrings(str1: str, str2: str) -> str:
        if len(str1)> len(str2):
            large_str = str1
            small_str = str2
        else:
            large_str = str2
            small_str = str1
        for i in range(len(large_str),0,-1):
               if len(small_str)%i == 0 and len(large_str)%i ==0:
                   prefix = i
                   print("prefix",prefix)
                   break
               else:
                   continue
        q1 = int(len(small_str)/prefix)
        q2 = int(len(large_str)/prefix)
        if (small_str[:prefix] ==large_str[:prefix]) and(large_str == q2 * large_str[:prefix]) and (small_str == q1 * small_str[:prefix]):
            return small_str[:prefix]
        else:
            return ""
    """
    Optimized solution.
    combining both strings from Left to right and right to left should result in same combined long string. Only then it has common prefix.
    """
    
    def gcdOfStrings(str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
           return ""
        for i in range(max(len(str1), len(str2)), 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                prefix = str1[:i] # converting the number into string here reduced our number of lines of code
                print(f"Checking prefix: {prefix}")
                break
        if str1 == prefix * (len(str1) // len(prefix)) and str2 == prefix * (len(str2) // len(prefix)):
             return prefix
    


if __name__ == "__main__":
    str1 = "ABCABC"
    str2 = "ABC"
    print(gcdOfStrings(str1, str2))  

"""
Super Optimized solution
We have used Eucledian method instead of brute force approach to find greatest common factor between two numbers.
Eucledian's Time complexity is O(log(n)), which is better than O(n)). With O(n)
, time complexity inccreases linearly with the size of n and when the input is in billions number it would be impractical to manage.
As with log(n) grows slowly almost flat in compared to O(n).
Searching billion records linearly is impossisble but can be done instantly with log(n) Databases(Btrees) instantly in real time.

"""

class Solution:
    def findgcd(self,a,b):
        print("a",a)
        print("b",b)
        if b == 0:
            return a
        return self.findgcd(b,a%b)
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
           return ""
        prefix = self.findgcd(max(len(str1), len(str2)), min(len(str1),len(str2)))
        candidate = str1[:prefix]
        print(candidate)
        if (str1 == candidate * (len(str1)//prefix)) and (str2 == candidate * (len(str2)//prefix)):
            return candidate
        else:
            return ""
