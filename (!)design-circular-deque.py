class MyCircularDeque(object):

    def __init__(self, k):
        self.__start = 0
        self.__size = 0
        self.__buffer = [0] * k
        

    def insertFront(self, value):
        if self.isFull():
            return False
        self.__start = (self.__start-1) % len(self.__buffer)
        self.__buffer[self.__start] = value
        self.__size += 1
        return True
        

    def insertLast(self, value):
        if self.isFull():
            return False
        self.__buffer[(self.__start+self.__size) % len(self.__buffer)] = value
        self.__size += 1
        return True
        

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.__start = (self.__start+1) % len(self.__buffer)
        self.__size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.__size -= 1
        return True
        

    def getFront(self):
        return -1 if self.isEmpty() else self.__buffer[self.__start]
        

    def getRear(self):
        return -1 if self.isEmpty() else self.__buffer[(self.__start+self.__size-1) % len(self.__buffer)]
        

    def isEmpty(self):
        return self.__size == 0
        

    def isFull(self):
        return self.__size == len(self.__buffer)
