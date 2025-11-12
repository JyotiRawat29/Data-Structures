#%%
from collections import defaultdict

grid = [ ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]
m = len(grid)
n = len(grid[0])
set1 = set()
grid1 = [[ (i*n)+j for j in range(n)] for i in range(m)]
print(grid1)
for i in range(m):
    for j in range(n):
        if grid[i][j] == "0":
            pass
        else:
            set1.add(grid1[i][j])
print(set1)
list1 = list(set1)
#%%
hm = defaultdict(list)
temp = list1[0]
for i in range(1,len(list1)):
    diff = list1[i] - temp
    y = temp + n
    if  diff == 1:
        hm[temp].append(list1[i])
    if y in set1:
        hm[temp].append(y)
    try:
        max(hm[temp])
        temp = max(hm[temp])
    except:
        temp = list1[i]

    #else:
    #    key = set1[i]
    #    hm[key] = key
# %%
