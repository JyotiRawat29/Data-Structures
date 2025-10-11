#%%
s = "egg"
t = "bee"

h1 = {}
h2 = {}
if len(s) != len(t):
    print(False)
for char in s:
    h1[char] = h1.get(char,0)+1
for char in t:
    h2[char] = h2.get(char,0)+1
h3 = {} #map of both s and t
temp = ""
if list(h1.values()) == list(h2.values()):
    for i,j in enumerate(s):
        h3[j]=t[i]
    for k in s:
        temp +=h3[k]
        if temp == t:
            print(True)
else:
    False

# %%
#optimized solution
h3= {} # mapping s and t
h4 = {} # map of values of h3, to check from other side too. Isomers should comply from both sides of strings i.e. s to t and t to s
temp = ""
if len(s)!=len(t):
    print(False) 
if True:
    for (i,j) in enumerate(s):
        if j not in h3:
            h3[j]=t[i]
    for i in list(h3.values()):
        if i not in h4:
            h4[i]=h4.get(i,0)
        else:
            print(False) 
    for k in s:
        temp +=h3[k]
        if temp == t:
            print(True)
    print(False)
        


# %%
