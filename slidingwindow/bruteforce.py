arr = [98,-5,2,3,5,-4,70]
k = 2
max_sum = -inf #(as elements can be negative)
n = len(arr)
for i in range(0,n-k+1):
    curr_sum = 0
    for j in(i+1,i+k-1):
        curr_sum = arr[i]+arr[j]
    max_sum = max(curr_sum,max_sum)
max_sum
