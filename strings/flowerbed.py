#class Solution:
#    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
#%%
flowerbed =[1,0,0,0,0,1]
count = 0
n = 2
i = 0
while(i<len(flowerbed)):
    print(i)
    if flowerbed[i] == 0:
        left_empty = (i==0 or flowerbed[i-1]==0)
        right_empty = (i== len(flowerbed)-1 or flowerbed[i+1]==0)
        if left_empty and right_empty:
            count += 1
            i+=2
            continue
                
    i = i+1
print(count >= n )
# %%
#optimized approach

#Flowers can only be planted in gaps of zeros.
#In a run of k consecutive zeros:
#If it’s between two 1s (like 1 0 0 0 1), then you can plant (k-1)//2 flowers.
#If it’s at the edge (like 0 0 0 1 or 1 0 0 0), then you can plant k//2 flowers.
#If the whole array is zeros (like [0,0,0,0]), then you can plant (k+1)//2.

def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
    count = 0
    i = 0
    length = len(flowerbed)
    
    while i < length:
        if flowerbed[i] == 0:
            j = i
            while j < length and flowerbed[j] == 0:
                j += 1
            run_length = j - i
            
            # Case 1: run at the edge
            if i == 0 or j == length:
                count += run_length // 2
            else:
                # Case 2: run between two 1s
                count += (run_length - 1) // 2
            
            if count >= n:
                return True
            i = j
        else:
            i += 1
    
    return count >= n

#%%
timeSeries =[1,4]
duration = 2
attack_timer = [i+duration for i in timeSeries]
print(attack_timer)

# %%
