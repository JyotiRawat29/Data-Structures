"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest without duplicate characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""
max_counter = 0
for i in range(len(s)):
  hashkey = set ()
  counter = 0
  for j in range(i,len(s)):
    if s[j] in hashkey:
      break
    hashkey.add(s[j])
    counter+=1
  max_counter = max(max_counter, counter)
return max_counter

#Since in the bruteforce we are creating hashkey inside the loop and hence O(n^2).It is fine for bruteforce but need consistent variable handling.
#t.c. = O(n^2) and sc. O(min(n, charset)) for the set.

#Hence we use sliding window approach, here you dont need to rest the hashkey but change the length of window dynamically.

max_counter = 0
hashkey = {}
slow = 0

for fast in range(len(s)):
  if s[fast] in hashkey and hashkey[s[fast]]>= slow:
    slow += hashkey[s[fast]]
  hashkey[s[fast]] = fast
  max_counter = max(max_counter, (fast-slow+1))

return max_counter

  

  
  

