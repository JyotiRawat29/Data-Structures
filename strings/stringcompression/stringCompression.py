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
"""
"I use two pointers: one scans the array, 
the other writes compressed results. For each run of identical
characters, I write the character and its count if greater than one. 
At the end, I flush the last run. This gives me O(N) time and 
O(1) space, which is optimal since the problem requires 
in‑place compression.”
"""

#%%