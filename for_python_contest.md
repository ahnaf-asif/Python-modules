**List:** 

```python
lst0 = ["a","b","c",1,30.55] 
lst1 = list() 
lst2 = [] 
lst3 = [0]*n 
lst4 = [[0]*m]*n # n*m size matrix 
lst5 = [[[0]*k]*m]*n #n*m*k size matrix
for i in lst1: 
	# like for(auto i: v)

```

**Stack:**

```Python
class stack:
	def __init__(self):
		self.__lst = list()
		self.__size = 0
	def push(self,number):
		self.__lst.append(number)
		self.__size+=1
		return
	def pop(self):
		if(self.__size >= 1):
			self.__lst.pop()
			self.__size-=1
	def size(self):
		return self.__size
	def top(self):
		if(self.size() > 0):
			return self.__lst[self.__size-1]
		else:
			print("Stack has no data\n")
			sys.exit(-1)
	def clear(self):
		self.__lst.clear()
		__size = 0
	def empty(self):
		if(__size==0):
			return 1
		else:
			return 0

def main():
	asif = stack()
	asif.push(12)
	asif.push(234)
	asif.push(5)
	asif.push(234232334234)
	print(asif.size())
	print(asif.top())
	asif.pop()
	print(asif.top())
	asif.clear()
main()
```

**Priority Queue:**

```Python
from queue import PriorityQueue 
#make sure this line is in the top of your code 

class priority_queue:
	def __init__(self):
		self.__q = PriorityQueue()
		self.__size = 0
	def size(self):
		return self.__size
	def front(self):
		x = self.__q.get()
		self.__q.put(x)
		return x[0]
	def insert(self,x):
		self.__q.put((x,x))
		self.__size+=1
	def empty(self):
		if(self.__size == 0):
			return 1
		else:
			return 0
	def clear(self):
		self.__q.clear()
		self.__size = 0
	def pop(self):
		if(self.__size > 0):
			x = self.__q.get()
			self.__size-=1;
			del x
			return
		else:
			print("Queue has no data")
			sys.exit(-1)
def main():
	asif = priority_queue()
	asif.insert(5)
	asif.insert(4)
	asif.insert(5)
	asif.insert(7)
	asif.insert(1)

	print(asif.front())
	asif.pop()
	print(asif.front())
	print(asif.size())

main()
```

**Dictionary:**

```python
mp = dict()

mp.clear()
mp.update({"asif":122})

print(mp["asif"])
mp["asif"]-=1;
print(mp["asif"])
for i in mp:
	print(i) # i is the  key, mp[i] will be the mapped value
```

**SET:**

```Python
st = set()

#adding data 
st.add(12)
st.add(13)
st.add(14)
st.add(15)
st.add(12)

st.remove(12) #removing 12
print(st)
for i in st:
	print(i)
	#i is the element
st2 = {12,13,141,4}

st3 = st|st2 # set Union , or operation
st3 = st&st2 # and operation, set intersection

print(st3)
len(st)
st.clear()
```

**Dictionary:**

```Python
import collections 

deq = collections.deque()

deq.append(12) # append right
deq.append(14)
deq.appendleft(33) # append left
deq.pop() #pop right
deq.popleft() # pop left

print(deq)
print(type(deq))
```

**Queue:**

```Python
import queue
q = queue.Queue(maxsize=1e5)

q.put(12)
q.put(143) 
q.put(5454) 
q.put(666) 
q.put(5) 
q.put(44444) 

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
```

**Builtin Functions and other hacks:**

```python
#integet array input
ara = input().split()
for i in range(len(ara)):
	ara[i] = int(ara[i])
	
#template
import math
import sys
import random

sys.stdin = open("in.txt","r")
sys.stdout = open("out.txt","w")
lst = list()
random.shuffle(list) # random shuffle hoye gese 
import random
for x in range(10):
    print (random.randint(1,101))
    #random number generating 
#taking graph input
import random 
import math 
import sys
vector = []
n,m = map(int,input().split())
for i in range(n):
	vector.append([])
#sys.exit()
for i in range(m):
	a,b = map(int,input().split())
	vector[a].append(b)
print(vector)

abs(a) #absolute value of a float number. abs(5.55) = 5
math.ceil(a) #ceiling of a float number, ceil(5.55) = 6
math.floor(a) #floor of a float number, floor(5.55) = 5
math.log(a) # e based log of a
math.log10(a) #10 based log of a
max(a,b,c,d) #maximum value of a,b,c,d. you can use as many numbers as you can
min(a,b,c) #minimum value of a,b,c, you can use as many numbers as you can 
math.sqrt(a) #sqrt of a. sqrt(25) = 5.00

#these angles must be in radian
math.sin(a)
math.cos(a)
math.tan(a)
math.asin(a) #sin inverse
math.acos(a) #cos inverse
math.atan(a) #tan inverse
math.degrees(r) #convert degree from radian
math.radian(d) #converts radians from degrees
#we can shorten module names
import math as m
now , we will use m.sqrt(), not math.sqrt()
```

**2d array:**

```python
#here is an example of 2d array with size n*m
#initializing the "matrix" array first. 

matrix = []
n = 2
m = 3

for i in range(0,n):
    matrix.append([])
    for j in range(0,m):
        matrix[i].append(0)

#initialization completed
#Now we will take the input and append the matrix just like this:
ara = list()
for i in range(0,n):
	ara = list(map(int,input().split()))
	for j in range(0,m):
		matrix[i][j] = ara[j]

print(matrix) # just printing it to make sure everything works fine there
```

**Compare Functions for sorting:**

```python
from functools import cmp_to_key

nums = [28, 50, 17, 12, 121]
nums.sort(key=cmp_to_key(lambda x, y: 1 if x < y else -1))
print(nums) # print nums in descending order

nums.sort(key=cmp_to_key(lambda x, y: 1 if x > y else -1))
print(nums) #print nums in ascending order 



###### using alada compare functions : 
from functools import cmp_to_key

def func(a,b):
	if(a > b):
		return 1
	else:
		return -1


nums = [28, 50, 17, 12, 121]
nums.sort(key=cmp_to_key(lambda x,y: func(x,y)))

print(nums)

####### will print the arary as ascending order. 

from functools import cmp_to_key

def func(a,b):
	if(a < b):
		return 1
	else:
		return -1


nums = [28, 50, 17, 12, 121]
nums.sort(key=cmp_to_key(lambda x,y: func(x,y)))

print(nums)

####### this code will sort the array as descending order 
```



