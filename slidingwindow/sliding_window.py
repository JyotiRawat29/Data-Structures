#It is a better strategy to save the values in the memory, rather then have more run time. Here the concept is utilising the values than indices. The window has the sum of the k values always, and 
#after every counter, we want to know which element needs to be remove which element needs to be added in the window for getting the sum of next round of k elements. In start the window has sum
#of initital k elements and than after one counter we remove the 1st element(0th index) and add the next kth element(0th+k-1) to maintain the conscutive sum of kth element.
arr =[98,-5,2,3,5,-4,70]
k = 2
if len(arr)<k:
    print("0")
max_sum = sum([arr[l] for l in range(k)])
curr_sum = max_sum
for i in range(len(arr)-k):
    curr_sum = curr_sum - arr[i]+arr[i+k-1]
    max_sum = max(curr_sum,max_sum)

max_sum
