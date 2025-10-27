#%%
x = 10
y = x
if x < 0:
    print (False)
else:
    new_num = 0
    while(x>=10):
        r = x%10
        x = int(x/10)
        print(r)
        new_num= (r+new_num)*10
    new_num +=x
    print(new_num)
    if (new_num == y):
        print (True)
    else:
        print (False)

# %%
