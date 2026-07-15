#%%
"""
392
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false



"""
def isSubsequence(s: str, t: str) -> bool:
    s1 = 0
    t1 = 0
    while(s1<len(s) and t1 < len(t)):
        if s[s1]==t[t1]:
            s1+=1
        t1+=1
    return s1 == len(s)

if __name__ == "__main__":
    s = "aaaaaa"
    t = "bbaaaa"
    print(isSubsequence(s,t))

#cannot use str.index() because it will give
#error if the element is not present in the 
#string (can be resolved using continue) and if there are duplicates in the 
# string then it will give the index of 
# first occurrence of the element

# %%
