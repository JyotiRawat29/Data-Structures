"""
1768. Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

Constraints:

    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.
"""

#solution1
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x_counter=0
        y_counter=0
        i=0
        new = ""
        while(i<max(len(word1),len(word2))):
            if x_counter <len(word1):
                new = new+word1[i]
                x_counter+=1
            if y_counter <len(word2):
                new = new+word2[i]
                y_counter+=1
            i+=1
        
        return new

#solution2
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""
        counter = 0
        while(counter<min(len(word1), len(word2))):
            new +=word1[counter]
            new +=word2[counter]
            counter+=1
        if(len(word1)>len(word2)):
            new+=word1[counter:]
        elif(len(word2)>len(word1)):
            new+=word2[counter:]
        return new

#Solution3 (optimized solution)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for i in range(max(len(word1), len(word2))):
             if i < len(word1):
                 merged.append(word1[i])
             if i < len(word2):
                 merged.append(word2[i])
        return("".join(merged))
"""
In optmized solution list is used to append instead of string as here lengths of strings are changing and hence mutable data structure is 
best as the time complexity is O(n) in compare to concatenate the strings(O(n^2)).
"""

