"""
191. Number of 1 Bits
Easy
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).
"""
#%%
n = 11
bin_num = str(bin(n))
count = 0
for dig in bin_num:
    if dig == '1':
        count+=1
count
# %%
