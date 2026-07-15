class solution:
    @staticmethod
    def findgcd(a,b):
        if b == 0:
            return a
        return solution.findgcd(b,a%b)
    
    @staticmethod
    def gcdOfStrings(str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
           return ""
        prefix = solution.findgcd(max(len(str1), len(str2)), min(len(str1),len(str2)))
        candidate = str1[:prefix]
        if (str1 == candidate * (len(str1)//prefix)) and (str2 == candidate * (len(str2)//prefix)):
            return candidate
        else:
            return ""

#%%
chars = ["a","a","b","b","c","c","c"]
counter_group = 0
next_ = 1
new = []
for i in range(len(chars)):
    if chars[next_] == chars[i]:
        counter_group+=1
    else:
        if counter_group == 1:
            new.append(chars[i-1])
        else:
            new.append(counter_group)
            new.append(chars[i-1])
print(len(new)) 
# %%
