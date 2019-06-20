# Python-modules

I will try to include all the possible shortcuts and other stuff here. 

**Arithmetic operations:**

`+ , - , *, /` are literally addition,subtraction, multiplication,division. and `a**b` means `a^b` (a to the power b) and `a//b` means the integer division of `a/b`


**string input:** `s = input()`

**int input:** `a = int(input())`

**float input:** `a = float(input())`
 
2 or 3 integer inputs __inline__ :

```python
a,b,c = map(int,input().split())
a,b,c = map(float,input().split())
```
**Conditional Logic:**

```python
if(statement):
	#this is inside if() condition
	#this is also inside if() condition
	#this is also inside if() condition
elif(another_statement):
	#this is inside elif() condition
	#this is inside elif() condition
else:
	#this is inside the else condition
	#do whatever you want to do.. 

#now we will see some conditional operators 

#conditional and operators
a = 3
b = 3
if(a == b and a+b == 6):
	print("Hello")
# it will print "Hello"

#conditional or operator

a = 4
b = 2
if(a+b == 6 or a==b):
	print("Hello")
#it will print "Hello"

```


**Loops:**


```python
#for loop...
for i in range(x,y):
	#do whatever you want
	# i will iterate from x to y-1
	# all lines indented here will be inside the for loop
# while loop

i = 0
while(i <= 10):
	print(i) # It will print from 0 to 10. So try to undarstand what's happening
```


**Different methods to work with Array/Lists:**

```python
#### array input-output showing

#method number 1(easy)
ara = list(map(int,input().split()))
print(len(ara)) # array ibdexes from 0 to len-1
print(ara) # printing the full array
print(ara[some_index]) #printing a particular index 
ara[some_index] = some_value # changing value at some index... same as C/C++

#method number 2(you have to know the size of the array before taking the input):
ara = []
length = int(input()) #taking the length of input
for i in range(length): # simply loop over the length and insert the values one by one
	ara.append(int(input()))

print(ara) # printing the full array
print(ara[some_index]) #printing a particular index 
ara[some_index] = some_value # changing value at some index... same as C/C++

# Removing a particular "value" from an array or string
ara.remove(value) # just like this

# taking the substring from an array or string

#suppose...
ara = [2, 3, 5, 1, 4, 3]
ara2 = ara[1:4]
#here ara2 = [3,4,5,4] . because we just took from 1th index to 4th index.
#array indexing starts from 0
#we can do it in another approach

ara = [2, 3, 5, 1, 4, 3]
ara2 = list()
for i in range(1,5):
	ara2.append(ara[i])
print(ara2) #here ara2 has the sbstring from 1th index to 4th index

```

**String:**

```python

a = input() #taken the input of a string
print(len(a)) #length of string a

b = input() #another string input
print(len(b)) #printing the length of a 

c = a+b #adding the string. if a = "Hello" and b = "world" then c = "Helloworld"
d = a*3 #if a = "Hello" then d = "HelloHelloHello"

s = a[2:5] #taken a substring of a from 2th index to 5th index

```

**2D array:**
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

**Functions:**

```python
#I'll write some simple functions here. make sure you understand everything here:
#it is the main structure of a function-->
def function_name(parameters):
	#do whatever you want
	#do something else if you nedd to
	#do something again..
	#keep doing, keep working
	return something #if you don't want to return, simply don't return something. It'll be fine 

#function ended
#simple addition function 

def add(a,b):
	c = a+b
	return c

x = 5
y = 4

z = add(x,y)
print(z) # here z will show 9, sum of 5 and 4

# you can also write recursive functions like that 
def factorial(a):
	if(a == 1):
		return 1
	return a*factorial(a-1)


print(factorial(5)) #it will show 120 because 1*2*3*4*5 = 120

```
