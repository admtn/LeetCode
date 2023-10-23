from collections import deque

# queue popleft() vs pop()
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)

q.popleft() #pop the first element that enters the queue
print(q)

q.pop() #pop the last element that enters the queue (basically a stack pop operation)
print(q)


# multiple variables in for loop
arr = [[1,2,3],[4,5,6],[7,8,9]]
for i,j,k in arr:
    print(i,j,k)

arr2 = [[1,2],[3,4]]
for i,k in arr2:
    print(i," ",k)

# appending tuple to a queue
from collections import deque
q = deque()
q.append((1,2)) # appending a tuple to a queue
q.append(3,4) # this is not how you append a tuple, this doesn't work