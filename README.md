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
**Comditional Logic:**

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


