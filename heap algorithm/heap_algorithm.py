import heapq
num = [1,2,3,4,7,8,9,10,14,16]
heapq.heapify(num)
print("The three largest integers from a given list of numbers : ",heapq.nlargest(3, num))



print("The three smallest integers from a given list of numbers: ",heapq.nsmallest(3, num)) 


print ("The popped and smallest element is : ",heapq.heappop(num)) 

print ("The created heap is : ",list(num)) 

