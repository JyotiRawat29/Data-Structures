"""
443. String Compression
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.
Note: The characters in the array beyond the returned length do not matter and should be ignored.
Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
After modifying the input array in-place, the first 6 characters of chars should be ["a","2","b","2","c","3"].

Example 2:

Input: chars = ["a"]
Output: 1
Explanation: The only group is "a", which remains uncompressed since it is a single character.
After modifying the input array in-place, the first character of chars should be ["a"].

Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: 4
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
After modifying the input array in-place, the first 4 characters of chars should be ["a","b","1","2"].

Constraints:

    1 <= chars.length <= 2000
    chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""

class Solution:
    @staticmethod
    def compress(chars: list[str]) -> int:
        count = 1
        write = 0
        for i in range(1,len(chars)):
            if chars[i-1]==chars[i]:
                count +=1
            else:
                chars[write] = chars[i-1]
                write +=1
                if count!=1:
                    for c in str(count):
                        chars[write]=c
                        write+=1
                count = 1
        chars[write]=chars[-1]
        write +=1
        if count>1:
            for c in str(count):
                chars[write]=c
                write +=1
        return len(chars[:write])

#The approach is to have 2 pointers, one counts the number of consecutive characters
#and the other is the index pointer to write the compressed characters in the original array.
#The count is reset to 1 when a new character is encountered.
#The result should be in strings format so we convert the count to string and
# write each character of the count in the original array (for c in str(count)): print(c), gives the
# individual characters of the count (12--> "1", "2").
#The last flush is done after the loop to account 
#for the last character group. As the loop ends when the last character is reached,
# we need to write the last character and its count (if greater than 1) to the original array. 
#The function returns the length of the compressed array.

