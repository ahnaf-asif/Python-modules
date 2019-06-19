#used to make a stack. just like c++ 
class stack:
	def __init__(self):
		self.__lst = list()
		self.__size = 0
	#done...
	def push(self,number):
		self.__lst.append(number)
		self.__size+=1
		return
	#done..
	def pop(self):
		if(self.__size >= 1):
			self.__lst.pop()
			self.__size-=1
		#done..
	#done..
	def size(self):
		return self.__size
	#done..	
	def top(self):
		if(self.size() > 0):
			return self.__lst[self.__size-1]
		else:
			print("Stack has no data\n")
			sys.exit(-1)
		#done..
	#done..
	def clear(self):
		self.__lst.clear()
		__size = 0
	#done
	def empty(self):
		if(__size==0):
			return 1
		else:
			return 0
		#done
	#done
#done..
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

