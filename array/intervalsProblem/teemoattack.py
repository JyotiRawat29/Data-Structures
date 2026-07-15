#%%
def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        start = timeSeries[0]
        end = timeSeries[0]+duration-1
        temp = [start,end]
        count = end -start+1
        for i in timeSeries:
            timeinterval = i+duration-1
            end = timeinterval
            start = i
            if end > temp[0]:
                diff = end -temp[1]
                count +=diff
            else:
                diff = end -start
                count += diff
            temp[0] = start
            temp[1]= end
        return count
                    

#optimize solution
def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
    if duration == 0 or not timeSeries:
        return 0
    
    total = 0
    for i in range(len(timeSeries) - 1):
        # Add either full duration or the gap between attacks
        total += min(duration, timeSeries[i+1] - timeSeries[i])
    
    # Add duration for the last attack (always full)
    total += duration
    return total

#The key is if the next attack starts before the current attack ends, 
#we only add the time until the next attack starts. i.e. the gap between the two attacks.
#Otherwise, we add  the full duration of the current attack.
#Finally, we always add the full duration for the last attack 
# since there are no subsequent attacks to consider.

#%%
intervals = [[1,3],[2,6],[8,10],[2,4]]
intervals.sort(key=lambda x: x[0])
# %%
