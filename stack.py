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
			return self.__lst[len(self.__lst)-1]
		else:
			print("Stack has no data\n")
			sys.exit(-1)
		#done..
	#done..
#done..