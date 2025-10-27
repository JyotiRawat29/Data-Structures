#%%
"""
Reverse bits of a given 32 bits signed integer.
Easy
This is not a good approach to build a string first and than iterate it.
It is time inefficient approach.
"""

n = 43261596
n_bits = ""
reverse_num = 0
while(n!=1):
    r = n % 2
    n = n //2
    n_bits = n_bits+str(r)
n_bits = n_bits+str(n)
n_bits+=str(0)*(32-len(n_bits))
for i,index in enumerate(range(len(n_bits)-1,-1,-1)):
    print(index)
    reverse_num+= (2**index)*int(n_bits[i])
    print(reverse_num)
print(reverse_num)

#%%
n = 43261596
bin(n)
x = ''
n = 43261596
y = str(bin(n))
for i in (range(len(y)-1, 1, -1)):
   x += y[i]
x+=str(0)*(32-len(bin(n))+2)
x
eval('0b'+ x)

#%%
"""
****Optimal Approach****

Use the bit operator, right bit operator and left bit operator.
<<: left bit operator 16 << 2 shift the binary digits of 2 towards left
16 :: 00010000 (Octal)
16 << 2 :: 01000000 :: 64 :: move all bits to left 2 bits, filled with 0
>> : right bit operator
64 :: 01000000 
64 >> 2 ::00010000 ::16 :: move all the bits to right 2 bits, filled with 0

"""

#%%
def reverseBits(n: int) -> int:
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)  # append LSB of n to res
        n >>= 1                     # drop LSB
    return res & 0xFFFFFFFF 

reverseBits(43261596) 
# %%
