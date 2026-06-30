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

"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
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
