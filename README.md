# Data-Structures
I have implemented data structures like arrays, Linked List, Queues, stacks etc in Python.
List of DS implemented:
  Arrays
  Linked List
  Queues
  Stacks
  Trees
Apart from it some concepts like Recursion and Big O notation are also explained.

Sliding window technique:: Concept is add the first value of the next sequence and subtract the last value of the preceeding sequence ORR slice the arrays by giving initial index and last index of the sequence by using dynamic i and j variables (i = 0 j = len(sequence)-1)

def sliding_average(J,p):

 n = len(J)
 max_avg = min_avg = sum(J[:p])//p
 print(f'max_avg, {max_avg}')
 for i in range(len(J)-p+1): #sliding window
   subarr = J[i:i+p]  #array slicing
   print(f'subarr,{subarr}')
   temp_sum = sum(subarr)//p
   if temp_sum<min_avg:
     min_avg = temp_sum
   if temp_sum>max_avg:
     max_avg = temp_sum
 
 return min_avg, max_avg
