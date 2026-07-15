"""

345. Reverse Vowels of a String


Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, 
more than once.
Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

"""

def reverseVowels(self, s: str) -> str:
        #vowels = ["a","e","i","o","u","A","E","I","O","U"]# lsit scans all elements hence T.C O(n)
        vowels = set("aeiouAEIOU")# look up of set is O(1)
        left = 0
        right = len(s)-1
        #s = list(s)
        while left<right:
            if s[left] not in vowels:
                left +=1
            elif s[right] not in vowels:
                right -=1
            else:
                s[left],s[right]= s[right], s[left]
                left +=1
                right-=1
        return "".join(s)
#here we need to convert string to list because
#string is immutable(no inplace modifications at all) in python and we cannot 
#swap the elements of string in python


#%%



# %%
