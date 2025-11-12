from collections import defaultdict

"""
defaultdict(int)
defaultdict(list)
defaultdict(set)
defaultdict(str)
defaultdict(custom function)
defaultdict() is a hashmap(dict) of groups like int,list,set, str etc.
"""

x ={}
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
for word in words:
    x[word]=x.get(word,0)+1
x

x= defaultdict(int)
for word in words:
    x[word] += 1
x
# %%
groups = defaultdict(list)
pairs = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]
for key, value in pairs:
    groups[key].append(value)
print(groups)

# %%
groups = {}
pairs = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]
for key,value in pairs:
    if key not in groups:
        groups[key] =[]
    groups[key].append(value)
groups
# %%
